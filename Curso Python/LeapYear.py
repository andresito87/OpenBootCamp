# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

year = int(input("Dime un año "))


def showLeapYear(year):

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")


showLeapYear(year)
