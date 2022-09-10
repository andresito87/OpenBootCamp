# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def showIsPassed(self):
        if self.nota >= 5:
            print(self.nombre, "con un ", self.nota, "si ha aprobado")
        else:
            print(self.nombre, "con un ", self.nota, "no ha aprobado")


alumno = Alumno("Andres", 4)
alumno.showIsPassed()
alumno2 = Alumno("Ana", 7)
alumno2.showIsPassed()
