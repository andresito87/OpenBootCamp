# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce


def myfunction(list):

    oddNumbers = filter(lambda x: x % 2 != 0, list)
    return reduce(lambda a, b: a+b, oddNumbers)


print(myfunction([1, 2, 3, 4, 5, 6]))
