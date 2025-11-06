# --------------------------------------------------------------------------
#          COPIAS SUPERFICIALES Y PROFUNDAS DE OBJETOS
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es entender la diferencia entre una copia superficial y una
# profunda al trabajar con objetos que contienen otros objetos (composición).
# Modificaremos la clase `Cliente` para que pueda crear copias de sí misma.
#
# Instrucciones para el estudiante:
# 1. Importa el módulo `copy`.
# 2. La clase `Cliente` ahora tiene dos nuevos métodos: `copia_superficial`
#    y `copia_profunda`.
# 3. En `copia_superficial`, usa `copy.copy(self)` para crear y devolver
#    una copia superficial del cliente.
# 4. En `copia_profunda`, usa `copy.deepcopy(self)` para crear y devolver
#    una copia profunda.
# 5. Analiza el bloque de prueba para ver cómo un cambio en la cuenta
#    bancaria de una copia superficial afecta al original, mientras que
#    en una copia profunda no lo hace.
# --------------------------------------------------------------------------

# ✅ Paso 1. Importa el módulo `copy`.
import copy


class CuentaBancaria:
    """Representa una cuenta bancaria simple con un titular y saldo."""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """Suma una cantidad positiva al saldo."""
        if cantidad > 0:
            self.saldo += cantidad

    def consultar_saldo(self):
        """Devuelve el saldo actual."""
        return self.saldo

    def __repr__(self):
        """Representación legible del objeto para depuración."""
        return f"CuentaBancaria(titular={self.titular!r}, saldo={self.saldo})"


class Cliente:
    """Un cliente que tiene una cuenta bancaria asociada."""

    def __init__(self, nombre, saldo_inicial_cuenta=0):
        self.nombre = nombre
        self.cuenta = CuentaBancaria(nombre, saldo_inicial_cuenta)

    # ✅ Paso 2. Implementa el método de copia superficial.
    def copia_superficial(self):
        """Devuelve una copia superficial del cliente."""
        return copy.copy(self)

    # ✅ Paso 3. Implementa el método de copia profunda.
    def copia_profunda(self):
        """Devuelve una copia profunda del cliente."""
        return copy.deepcopy(self)

    def __repr__(self):
        """Muestra información útil del cliente."""
        return f"Cliente(nombre={self.nombre!r}, cuenta={self.cuenta})"


# --- Bloque para probar tu clase ---
if __name__ == "__main__":    
    cliente_original = Cliente("Ana", 1000)
    print("Cliente original:", cliente_original)

    print("\n--- Probando Copia Superficial ---")
    cliente_superficial = cliente_original.copia_superficial()
    cliente_superficial.cuenta.depositar(500)

    print("Cliente superficial:", cliente_superficial)
    print(
        f"Saldo del original después de modificar la copia superficial: {cliente_original.cuenta.consultar_saldo()}"
    )
    print("🔍 Observa: ¡El saldo del original cambió! Ambos clientes comparten la misma cuenta.\n")

    print("--- Probando Copia Profunda ---")
    cliente_profundo = cliente_original.copia_profunda()
    cliente_profundo.cuenta.depositar(1000)

    print("Cliente profundo:", cliente_profundo)
    print(
        f"Saldo del original después de modificar la copia profunda: {cliente_original.cuenta.consultar_saldo()}"
    )
    print("✅ Observa: El saldo del original no cambió. La copia profunda tiene su propia cuenta.\n")
    
    print(id(cliente_original.cuenta))
    print(id(cliente_superficial.cuenta))
    print(id(cliente_profundo.cuenta))
