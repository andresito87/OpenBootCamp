# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.


import pickle


class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.encendido = False

    def arrancar(self):
        self.encendido = True

    def __str__(self):
        return f'El Vehiculo es de color {self.color}, tiene {self.ruedas} ruedas {self.puertas} y {"si" if self.encendido else "no"} está encendido'


vehiculo = Vehiculo("rojo", 4, 5)
file = open('file.bin', 'wb')
pickle.dump(vehiculo, file)
file.close()

file = open('file.bin', 'rb')
fileLoaded = pickle.load(file)
file.close()

print(fileLoaded)
