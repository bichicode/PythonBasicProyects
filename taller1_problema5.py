"""Taller 1
Problema 5
Resultado de una expresion
Bianca Gonzalez

Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una
persona y que calcule su índice de masa corporal (imc).
Se recuerda que el imc se calcula con la fórmula imc = peso / altura 2"""

print("\n-Sistema de Calculo de imc-\n")
peso = float(input("Introduzca el peso en kilogramos (kg): "))
altura = float(input("Introduzca la altura en metros (m): "))
imc = peso / (altura**2)
print("imc = %.2f"%imc)
