# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.


file = open('text.txt', 'w')
file.write('Hola, me llamo Andrés\n')
file.write('me gusta programar\n')
file.write('en Python')
file.close()

file = open('text.txt', 'r')
info = file.readlines()
file.close()


print(info)