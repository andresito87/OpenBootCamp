# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# Color
# Ruedas
# Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# Velocidad
# Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.


import json


class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, velocidad, cilindrada):
        super().__init__("amarillo", 4, 5)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


vehiculo = Vehiculo("rojo", 4, 3)
vehiculoStr = json.dumps(vehiculo.__dict__)
print(vehiculoStr)
coche = Coche(100, 1.4)
cocheStr = json.dumps(coche.__dict__)
print(cocheStr)
