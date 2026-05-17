Profe aqui los agrego en codigo por si los necesitas de esa manera

"""
Ejercicio 1   Vehiculo y Bicicleta
Crea una clase abstracta Vehiculo con el atributo marca y un método abstracto describir_transporte().
Crea una subclase Bicicleta que herede de Vehiculo, agregue el atributo num_cambios e implemente describir_transporte()
imprimiendo la marca y el número de cambios. Instancia dos bicicletas de marcas distintas.
"""


from abc import ABC, abstractmethod

# Aqui creamos la Clase abstracta
class Vehiculo(ABC):

    def __init__(self, marca):
        self.marca = marca

    @abstractmethod
    def describir_transporte(self):
        pass


# Subclase que heredan a la clase madre
class Bicicleta(Vehiculo):

    def __init__(self, marca, num_cambios):
        super().__init__(marca)
        self.num_cambios = num_cambios

    def describir_transporte(self):
        print(f"\nLa bicicleta de marca {self.marca} tiene {self.num_cambios} cambios.")


# Algunos Objetos de prueba
bicicleta1 = Bicicleta("GW", 18)
bicicleta2 = Bicicleta("Trek", 21)

# Llamadas de los métodos
bicicleta1.describir_transporte()
bicicleta2.describir_transporte()




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




"""
Ejercicio 3   Paciente, Medicamento, Adulto e Infantil
Crea una clase Paciente (nombre, peso_kg, edad).
Crea una clase abstracta Medicamento con atributos nombre y dosis_base_mg, y métodos abstractos calcular_dosis(paciente) y advertencias().
Crea subclases MedicamentoAdulto (dosis = dosis_base x peso / 70) y MedicamentoInfantil (dosis = dosis_base x peso / 40, máximo 200 mg).
Prueba con un adulto de 75 kg y un niño de 25 kg.
"""
from abc import ABC, abstractmethod

# Clase Paciente
class Paciente:

    def __init__(self, nombre, peso_kg, edad):
        self.nombre = nombre
        self.peso_kg = peso_kg
        self.edad = edad


# Clase abstracta
class Medicamento(ABC):

    def __init__(self, nombre, dosis_base_mg):
        self.nombre = nombre
        self.dosis_base_mg = dosis_base_mg

    @abstractmethod
    def calcular_dosis(self, paciente):
        pass

    @abstractmethod
    def advertencias(self):
        pass


# Subclase Medicamento Adulto
class MedicamentoAdulto(Medicamento):

    def calcular_dosis(self, paciente):
        dosis = (self.dosis_base_mg * paciente.peso_kg) / 70
        return dosis

    def advertencias(self):
        print("Uso exclusivo para mayores a 18 anos.")


# Subclase MedicamentoInfantil
class MedicamentoInfantil(Medicamento):

    def calcular_dosis(self, paciente):
        dosis = (self.dosis_base_mg * paciente.peso_kg) / 40

        if dosis > 200:
            dosis = 200

        return dosis

    def advertencias(self):
        print("Mantener bajo supervision medica.")


# Pacientes de prueba
adulto = Paciente("Carlos", 75, 30)
nino = Paciente("Juan", 25, 8)

# Medicamentos
med_adulto = MedicamentoAdulto("Paracetamol", 500)
med_infantil = MedicamentoInfantil("Jarabe Infantil", 300)

# Cálculo de dosis llamado de metodos
print() #Un saltico de linea para que no este pegado
print("Dosis adulto:", med_adulto.calcular_dosis(adulto), "mg")
med_adulto.advertencias()

print()

print("Dosis infantil:", med_infantil.calcular_dosis(nino), "mg")
med_infantil.advertencias()







