"""
Taller 4 Problema 3
Bianca Gonzalez
Se desea un programa que lea n números enteros. El programa debe suministrar el promedio
de la suma.
"""

print("\n-Programa que lee n numeros enteros\n")
n = int(input("Ingrese la cantidad de numeros a leer: "))
sum = 0
for i in range(n):
    entero = int(input("Ingrese un entero: "))
    sum += entero
print("\nEl promedio es %.2f" % (sum/n))
