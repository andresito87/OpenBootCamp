# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.


from datetime import datetime

dateTime = datetime.now()

time = str(dateTime).split(" ")
hoursActual = int(str(time[1]).split(":")[0])
minutesActual = int(str(time[1]).split(":")[1])
print("Son las", hoursActual, ":", minutesActual)


def calculateRestTimeOfWork(hours, minutes):
    timeOfExit = 19
    minutesInAHour = 60
    if hours >= timeOfExit:
        print("Son las", hours, " es hora de irse a casa")
    else:
        hoursLeft = timeOfExit-hours
        minutesLeft = minutesInAHour-minutes
        print("Ánimo, ya sólo quedan", hoursLeft,
              "horas y", minutesLeft, "minutos para salir")


calculateRestTimeOfWork(hoursActual, minutesActual)
