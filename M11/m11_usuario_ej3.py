# --------------------------------------------------------------------------
#          CLASE CLIENTE QUE GESTIONA UNA CUENTA BANCARIA
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una clase `Cliente` que represente a un cliente
# de un banco. Cada cliente tendrá un nombre y su propia instancia de
# `CuentaBancaria`. La clase `Cliente` actuará como una interfaz para
# realizar operaciones en la cuenta de ese cliente.
#
# Instrucciones para el estudiante:
# 1. La clase `CuentaBancaria` del ejercicio anterior se proporciona como ayuda.
# 2. Completa el método `__init__` de la clase `Cliente`. Debe crear una
#    nueva instancia de `CuentaBancaria` y asignarla a un atributo.
# 3. Completa el método `hacer_deposito`. Este método debe llamar al método
#    `depositar` del objeto cuenta del cliente.
# 4. Completa el método `hacer_retiro`, que debe llamar al método `retirar`
#    de la cuenta.
# 5. Completa el método `ver_saldo`, que debe llamar a `consultar_saldo`
#    de la cuenta y devolver el resultado.
# --------------------------------------------------------------------------

# Clase del ejercicio anterior (necesaria para este ejercicio)
class CuentaBancaria:
    """
    Una clase para simular una cuenta bancaria simple.
    """

    def __init__(self, titular, saldo_inicial=0):
        """
        Inicializa una nueva cuenta bancaria.

        Args:
          titular (str): El nombre del titular de la cuenta.
          saldo_inicial (float, opcional): El saldo con el que empieza la cuenta. Por defecto es 0.
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """
        Añade una cantidad al saldo de la cuenta.
        """
        self.saldo += cantidad
        print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        """
        Retira una cantidad del saldo, si es posible.
        """
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Error: fondos insuficientes.")

    def consultar_saldo(self):
        """
        Devuelve el saldo actual de la cuenta.
        """
        return self.saldo


class Cliente:
    """
    Una clase para representar a un cliente del banco.
    """

    def __init__(self, nombre, saldo_inicial_cuenta=0):
        """
        Inicializa un nuevo cliente.

        Args:
          nombre (str): El nombre del cliente.
          saldo_inicial_cuenta (float, opcional): Saldo inicial para la cuenta del cliente.
        """
        # TODO: Paso 1. Almacena el nombre del cliente.
        self.nombre = nombre

        # TODO: Paso 2. Crea una instancia de CuentaBancaria para este cliente
        # y guárdala en un atributo, por ejemplo, `self.cuenta`.
        # Pasa el nombre del cliente como el titular de la cuenta.
        self.cuenta = CuentaBancaria(nombre, saldo_inicial_cuenta)

    def hacer_deposito(self, cantidad):
        """
        Deposita dinero en la cuenta del cliente.
        """
        # TODO: Paso 3. Llama al método `depositar` del objeto cuenta.
        print(f"Cliente {self.nombre} depositando {cantidad}...")
        self.cuenta.depositar(cantidad)

    def hacer_retiro(self, cantidad):
        """
        Retira dinero de la cuenta del cliente.
        """
        # TODO: Paso 4. Llama al método `retirar` del objeto cuenta.
        print(f"Cliente {self.nombre} retirando {cantidad}...")
        self.cuenta.retirar(cantidad)

    def ver_saldo(self):
        """
        Consulta el saldo de la cuenta del cliente.
        """
        # TODO: Paso 5. Llama al método `consultar_saldo` de la cuenta y devuelve el valor.
        return self.cuenta.consultar_saldo()


# --- Bloque para probar tu clase ---
if __name__ == "__main__":
    cliente1 = Cliente("Maria Rojas", 500)
    print(f"Saldo inicial de {cliente1.nombre}: {cliente1.ver_saldo()}")

    cliente1.hacer_deposito(250)
    cliente1.hacer_retiro(100)

    print(f"Saldo final de {cliente1.nombre}: {cliente1.ver_saldo()}")
# --- Fin del bloque de prueba ---
