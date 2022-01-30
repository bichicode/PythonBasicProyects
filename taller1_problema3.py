"""Taller 1
Problema 3
velocidad correspondiente

Bianca Gonzalez

Dado el tiempo en segundos (t) y la distancia en metros (d) de un automóvil,
ingresados por teclado, calcule la velocidad correspondiente.
v=d/t"""

print("\n   -Sistema de Calculo de Velocidad Correspondiente de un automóvil-\n")
tiempo = float(input("Introduzca el tiempo en segundos: "))
distancia = float(input("Intrduzca la distancia en metros: "))
velocidad = distancia/tiempo
print("La velocidad correspondiente es: %.2f"%velocidad + "m/s")