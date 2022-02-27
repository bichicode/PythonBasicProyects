"""5.	En una universidad se tienen los puntajes al examen de ingreso presentado por los
estudiantes. Hay un total de 10 estudiantes que presentaron el examen. Los datos deben ser suministrados por el
usuario. El programa debe suministrar:

•	El promedio de los puntajes
•	El puntaje mayor obtenido
•	El puntaje mejor obtenido
"""
import statistics


def puntajes():
    notas = []

    for i in range(10):
        notas.append(float(input("Ingrese el puntaje: ")))

    return notas


def promedio(lista):
    return statistics.mean(lista)


def mayor(lista):
    return max(lista)


def menor(lista):
    return min(lista)


# ----------------------------------------------------------------------------------------------------------------------


print("\nPrograma de Calificaciones Universitario\n")

calificaciones = puntajes()

medio = promedio(calificaciones)

mejor = mayor(calificaciones)

peor = menor(calificaciones)

print("\nEl promedio de los puntajes es: %.2f" %medio,
      "\nEl puntaje mayor obtenido es: ", mejor,
      "\nEl puntaje menor obtenido es: ", peor,
      "\n\nDetalle\n", calificaciones)

