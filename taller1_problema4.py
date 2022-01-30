"""Taller 1
Problema 4
Resultado de una expresion

Bianca Gonzalez

Se desea un programa que dado dos números enteros A y B calcule el resultado de
una expresión.
Expresion =(A+B)23"""

print("\n-Sistema que Calcula el Resultado de la Expresion =(A+B)23 -\n")
A = float(input("Introduzca el valor de A: "))
B = float(input("Introduzca el valor de B: "))
expresion = (A+B)*23
print("(A+B)23 = %.2f"%expresion)