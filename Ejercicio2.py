"""
Ejercicio 2   CuentaBancaria, Ahorros y Corriente
Crea una clase abstracta CuentaBancaria con los atributos titular y saldo, y dos métodos abstractos: cobrar_comision() y mostrar_info().
Crea dos subclases: CuentaAhorros (sin comisión, genera rendimiento del 2% sobre el saldo) y CuentaCorriente (cobra comisión fija de $8.000).
Cada subclase hereda e implementa ambos métodos. Instancia una cuenta de cada tipo y pruébalas.
"""

from abc import ABC, abstractmethod

# Aqui creamos la Clase abstracta
class CuentaBancaria(ABC):

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def cobrar_comision(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

#Las Clases
# Subclase CuentaAhorros
class CuentaAhorros(CuentaBancaria):

    def cobrar_comision(self):
        rendimiento = self.saldo * 0.02 #Como decia el ejercicio genera rendimiento del 2% sobre el saldo
        self.saldo += rendimiento

    def mostrar_info(self):
        print(f"Cuenta de Ahorros")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.saldo}")


# Subclase CuentaCorriente
class CuentaCorriente(CuentaBancaria):

    def cobrar_comision(self):
        self.saldo -= 8000 #Comision Fija

    def mostrar_info(self):
        print(f"Cuenta Corriente")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.saldo}")


# Objetos de prueba
cuenta1 = CuentaAhorros("Miguel", 500000)
cuenta2 = CuentaCorriente("Laura", 500000)
cuenta3 = CuentaAhorros("David", 750000)
cuenta4 = CuentaCorriente("Mael", 400000)

# Aplicar comisión o rendimiento
cuenta1.cobrar_comision()
cuenta2.cobrar_comision()
cuenta3.cobrar_comision()
cuenta4.cobrar_comision()
# Mostrar información
print() #Un saltico de linea para que no este pegado
cuenta1.mostrar_info()
print()
cuenta2.mostrar_info()
print()
cuenta3.mostrar_info()
print()
cuenta4.mostrar_info()