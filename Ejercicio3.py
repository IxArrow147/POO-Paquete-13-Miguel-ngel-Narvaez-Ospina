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