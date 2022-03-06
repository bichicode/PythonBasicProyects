"""Taller8
Problema 5
Bianca
Se le solicita crear un programa que tenga información de los vendedores por región.
Se tendrán tres conjuntos: norte, centro y sur.
El programa debe permitir realizar las siguientes acciones al conjunto regional:
a. Presentar los nombres que son iguales en el conjunto norte y sur.
b. Presentar los nombres que son iguales en el conjunto norte y centro."""

print("\nPrograma de vendedores iguales")

norte = {"Maria", "Marta", "Juana", "Lucia", "Carlos"}
centro = {"Carlos", "Cris", "Pedro", "Maria"}
sur = {"Merida", "Lucia", "Tiana", "Maria"}

print("\nNombres iguales en el conjunto Norte y Sur: ", norte & sur)


print("\nNombres iguales en el conjunto Norte y Centro: ", norte & centro)

print("\nNorte", norte, "\nCentro", centro, "\nSur", sur)