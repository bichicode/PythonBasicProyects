"""Taller2 Problema 3
Bianca González
Cree un proqrama que le solicite al usuario una cadena y un carácter y el proqrama debe
escribir el carácter entre cada una de las letras de la cadena."""

print("\n-Programa de Inserción de Caracter-\n")
nueva = ""
cadena = (input("Ingrese la cadena: "))
caracter = (input("Ingrese un carácter: "))
for letra in cadena:
    nueva = (nueva + letra + caracter)
print("La nueva cadena es: " + nueva)