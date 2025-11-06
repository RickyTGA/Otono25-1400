### maybe pip install geopy
# distancia_casa.py
# Programa en español que pide dónde naciste y dónde vives ahora,
# obtiene coordenadas mediante geocoding y calcula la distancia en km.

###from geopy.geocoders import Nominatim
###from geopy.exc import GeocoderServiceError
import math
import sys
import re
import time

def parse_coords(text):
    """
    Intenta detectar si el usuario introdujo 'lat, lon' directamente.
    Devuelve (lat, lon) como floats o None.
    Acepta formatos como: "40.4168, -3.7038" o "40.4168 -3.7038".
    """
    m = re.match(r'\s*([+-]?\d+(?:\.\d+)?)\s*[,\s]\s*([+-]?\d+(?:\.\d+)?)\s*$', text)
    if not m:
        return None
    try:
        lat = float(m.group(1))
        lon = float(m.group(2))
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return (lat, lon)
    except ValueError:
        return None
    return None

def geocode_place(geolocator, text, retries=3, delay=1.0):
    """
    Convierte un texto (ciudad, dirección...) en (lat, lon).
    Reintenta en caso de fallos transitorios.
    """
    # permitir que el usuario ponga ya coordenadas
    coords = parse_coords(text)
    if coords:
        return coords

    for attempt in range(retries):
        try:
            # exactly_one=True: toma la mejor coincidencia
            loc = geolocator.geocode(text, exactly_one=True, timeout=10)
            if loc:
                return (loc.latitude, loc.longitude)
            else:
                return None
        except GeocoderServiceError as e:
            # reintentar en caso de error temporal
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            else:
                raise
    return None

def haversine_km(lat1, lon1, lat2, lon2):
    """
    Calcula distancia en km entre dos puntos (grados decimales)
    usando la fórmula de Haversine.
    """
    # convertir a radianes (hacer paso a paso para reducir errores)
    r = 6371.0088  # radio medio de la Tierra en km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0) ** 2
    # Protección para errores por redondeo
    a = min(1.0, max(0.0, a))
    c = 2 * math.asin(math.sqrt(a))
    return r * c

def pedir_entrada(prompt):
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario.")
        sys.exit(1)

def main():
    print("=== Calculador de distancia a tu casa (en km) ===\n")
    geolocator = Nominatim(user_agent="calculador_distancia_app_v1")

    nac_text = pedir_entrada("¿Dónde naciste? (ciudad/dirección o 'lat, lon'): ")
    if not nac_text:
        print("No se proporcionó la ubicación de nacimiento. Saliendo.")
        return

    vive_text = pedir_entrada("¿Dónde vives ahora? (ciudad/dirección o 'lat, lon'): ")
    if not vive_text:
        print("No se proporcionó la ubicación actual. Saliendo.")
        return

    print("\nBuscando coordenadas... (si tarda, espera un momento)")
    try:
        coords_nac = geocode_place(geolocator, nac_text)
    except Exception as e:
        print(f"Error al geocodificar nacimiento: {e}")
        return

    if not coords_nac:
        print("No se pudo encontrar la ubicación de nacimiento. Intenta con un nombre más específico o introduce 'lat, lon'.")
        return

    try:
        coords_vive = geocode_place(geolocator, vive_text)
    except Exception as e:
        print(f"Error al geocodificar ubicación actual: {e}")
        return

    if not coords_vive:
        print("No se pudo encontrar la ubicación actual. Intenta con un nombre más específico o introduce 'lat, lon'.")
        return

    lat1, lon1 = coords_nac
    lat2, lon2 = coords_vive

    distancia = haversine_km(lat1, lon1, lat2, lon2)

    print("\nResultados:")
    print(f"  Nacimiento: {nac_text} -> lat={lat1:.6f}, lon={lon1:.6f}")
    print(f"  Actual:     {vive_text} -> lat={lat2:.6f}, lon={lon2:.6f}")
    print(f"\nDistancia aproximada (gran círculo): {distancia:.2f} km")

    # si quieres información extra: redondeo y direcciones
    if distancia < 1:
        print("Nota: la distancia es menor a 1 km (posiblemente estás muy cerca de tu lugar de nacimiento).")

if __name__ == "__main__":
    main()
