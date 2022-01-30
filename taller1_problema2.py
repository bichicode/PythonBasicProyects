"""Taller 1
Problema 2
Bianca Gonzalez

Perimetro y Superficie de un rectángulo
Construya un programa que dado como datos la base y la altura de un rectángulo,
calcule el perímetro y la superficie de este.
Superficie = Base * Altura

Perimetro = 2 *(Base * Altura)
"""

print("\n-Sistema De Cálculo de Perimetro y Superficie- \n")
base_rectangulo = float(input("Introduzca la base del rectángulo: "))
altura_rectangulo = float(input("Introduzca la altura del rectángulo: "))
perimetro_rectangulo= 2*base_rectangulo + 2*altura_rectangulo  #P = 2A + 2B
superficie_rectangulo= base_rectangulo * altura_rectangulo
print("El perimetro calculado es: %.2f"%perimetro_rectangulo + "cm")
print("La superficie calculada es: %.2f"%superficie_rectangulo + "cm2")

