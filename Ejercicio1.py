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