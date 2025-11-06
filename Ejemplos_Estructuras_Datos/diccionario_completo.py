# Crear un diccionario
estediccionario = {
    "limon": "amarillo",
    "naranja": "anaranjado", 
    "mandarina": "anaranjado",
    "manzana": "roja",
    "uva": "morada"
}

# Imprimir el diccionario completo
print("Diccionario completo:")
print(estediccionario)

# Imprimir la longitud del diccionario
print(f"\nEl diccionario tiene {len(estediccionario)} elementos")

# Acceder a elementos específicos
print("\n--- Accediendo a elementos ---")
print(f"El color del limón es: {estediccionario['limon']}")
print(f"El color de la naranja es: {estediccionario['naranja']}")

# Agregar elementos al diccionario
print("\n--- Agregando elementos ---")
estediccionario["platano"] = "amarillo"
estediccionario["fresa"] = "roja"
print(f"Después de agregar elementos: {estediccionario}")
print(f"Ahora tiene {len(estediccionario)} elementos")

# Quitar elementos del diccionario
print("\n--- Quitando elementos ---")
color_eliminado = estediccionario.pop("mandarina")
print(f"Se eliminó 'mandarina' con color '{color_eliminado}'")
print(f"Diccionario después de eliminar: {estediccionario}")

# Usar del para eliminar
del estediccionario["uva"]
print(f"Después de eliminar 'uva': {estediccionario}")

# Mostrar todas las claves (keys)
print("\n--- Claves del diccionario ---")
print(f"Claves: {list(estediccionario.keys())}")

# Mostrar todos los valores (values)
print(f"Valores: {list(estediccionario.values())}")

# Mostrar todos los pares clave-valor (items)
print(f"Pares clave-valor: {list(estediccionario.items())}")

# Iterar sobre el diccionario
print("\n--- Iterando sobre el diccionario ---")
for fruta, color in estediccionario.items():
    print(f"La {fruta} es de color {color}")

# Estado final
print(f"\n--- Estado final ---")
print(f"Diccionario final: {estediccionario}")
print(f"Longitud final: {len(estediccionario)} elementos")