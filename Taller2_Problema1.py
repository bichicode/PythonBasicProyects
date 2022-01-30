"""Taller2 Problema 1
Bianca González
Cree un programa que solicite al usuario ingresar una cadena y el programa de invertir la
cadena.
"""

print("\n-Programa de inversion de cadena")
invertida = ""
cadena = (input("Ingrese la cadena: "))
for letra in cadena:
    invertida = (letra+invertida)
    print("Cadena invertida: " + invertida)
