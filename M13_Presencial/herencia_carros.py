import re

# 1. CLASE PADRE: Vehiculo (Herencia)
class Vehiculo:
    """Clase base que define la funcionalidad común de todos los vehículos."""
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        """Método común a todos los vehículos."""
        print(f"El {self.marca} {self.color} ha arrancado su motor.")

    # El Polimorfismo se define aquí (el comportamiento será diferente en cada hijo)
    def tocar_bocina(self):
        """Método polimórfico. Será sobrescrito por las clases hijas."""
        raise NotImplementedError("Cada vehículo debe saber cómo tocar su propia bocina.")

# ----------------------------------------------------------------------

# 2. CLASE HIJA 1: Coche (Herencia + Regex)
class Coche(Vehiculo):
    """Extiende Vehiculo y añade validación de placa con Regex."""
    def __init__(self, marca, color, placa):
        # Llama al constructor del padre (reutilización)
        super().__init__(marca, color)
        self.tipo = "Coche"
        self.placa = self._validar_placa(placa)
        

    def _validar_placa(self, placa):
        """Usa Regex para validar el formato de la placa (3 letras - 3 números)."""
        # Patrón Regex: ^[A-Z]{3}-\d{3}$
        # ^ : inicio de la cadena
        # [A-Z]{3} : exactamente 3 letras mayúsculas
        # - : un guion
        # \d{3} : exactamente 3 dígitos
        # $ : fin de la cadena
        patron_placa = r"^[A-Z]{3}-\d{3}$"

        if re.fullmatch(patron_placa, placa):
            print(f"Placa '{placa}' válida para el {self.tipo}.")
            return placa
        else:
            print(f"ERROR: Placa '{placa}' inválida. Usando 'SIN-PLACA'.")
            return "SIN-PLACA" # Valor por defecto si falla la validación

    # SOBREESCRITURA (Polimorfismo: "Muchas Formas" del método tocar_bocina)
    def tocar_bocina(self):
        print(f"¡El {self.tipo} {self.marca} dice: BEEP BEEP!")

# ----------------------------------------------------------------------

# 3. CLASE HIJA 2: Camion (Polimorfismo)
class Camion(Vehiculo):
    """Extiende Vehiculo y añade un comportamiento de bocina diferente."""
    def __init__(self, marca, color, capacidad):
        super().__init__(marca, color)
        self.capacidad = capacidad
        self.tipo = "Camión"

    # SOBREESCRITURA (Polimorfismo)
    def tocar_bocina(self):
        print(f"¡El {self.tipo} {self.marca} dice: HONK HOOONK! (Sonido de aire)")

# ----------------------------------------------------------------------
# 4. DEMOSTRACIÓN DE HERENCIA Y POLIMORFISMO

print("--- DEMOSTRACIÓN DE HERENCIA Y POLIMORFISMO ---")

# Creamos instancias (objetos) de las clases hijas
coche_taxi = Coche("Toyota", "Amarillo", "TXI-567")
camion_carga = Camion("Volvo", "Rojo", 10000)
coche_error = Coche("Ford", "Azul", "123-ABC") # Placa inválida para probar Regex

print("\n--- TEST DE REUTILIZACIÓN (HERENCIA) ---")
# Ambos objetos usan el método arrancar() del padre (Vehiculo)
coche_taxi.arrancar()
camion_carga.arrancar()

print("\n--- TEST DE FLEXIBILIDAD (POLIMORFISMO) ---")
# Creamos una 'flota' de objetos de diferentes tipos
flota_vehiculos = [coche_taxi, camion_carga, coche_error]

# Iteramos sobre la flota y llamamos al mismo método
for vehiculo in flota_vehiculos:
    # El código no necesita saber si es un Coche o un Camión
    # Simplemente llama a tocar_bocina(), y el objeto sabe cómo responder.
    vehiculo.tocar_bocina()

print("\n--- TEST DE VALIDACIÓN (REGEX) ---")
# La validación ya se hizo al crear los objetos:
print(f"Placa de 'coche_taxi': {coche_taxi.placa}")
print(f"Placa de 'coche_error': {coche_error.placa}")