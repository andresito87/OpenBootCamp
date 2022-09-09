#Enunciado:Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.#

import math

peso = float(input("Ingresa tu peso "))
estatura = float(input("Ingresa tu estatura "))
IMC = peso/estatura
print("Tu índice de masa corporal es donde es "+str(round(IMC, 2)))
