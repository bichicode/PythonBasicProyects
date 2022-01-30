"""Taller2 Problema 2
Bianca González
Cree un proqrama que pida una cadena y dos caracteres por teclado
sustituye la aparición del primer carácter en la cadena por el sequndo carácter."""

print("\n-Programa de Sustitucion del 1er caracter")
nueva = ""
cadena = (input("Ingrese la cadena: "))
caracteres = (input("Ingrese dos caracteres: "))
a = len(cadena)
nueva = caracteres[1] + cadena[1:a]
print("La nueva cadena es: " + nueva)