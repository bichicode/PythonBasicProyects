"""
Taller 3 Problema 3
Bianca Gonzalez
Durante el semestre un estudiante debe realizar tres evaluaciones. Cada evaluación tiene
una calificación y la nota total que recibe el estudiante es la suma de las dos mejores
calificaciones.
Escribir un programa que lea las tres calificaciones y determine cual es la calificación total
que recibirá el estudiante.
"""
print("\n -Sistema de Calificaciones-\n")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

if (nota1 >= nota2) and (nota2 >= nota3):
    print("EL promedio es de: %.2f" % ((nota1+nota2)/2))
elif (nota1 >= nota2) and (nota3 >= nota2):
    print("EL promedio es de: %.2f" % ((nota1 + nota3) / 2))
else:
    print("EL promedio es de: %.2f" % ((nota2 + nota3) / 2))