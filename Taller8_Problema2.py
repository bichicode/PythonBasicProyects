""" Escriba un programa en Python que utilice los siguientes conjuntos que contienen el
nombre de los empleados de dos departamentos de una empresa. El programa debe
obtener aquellos empleados que aparecen en ambos conjuntos.
VENTA = {Juan, José, Ramón, Pedro, Mario, Julio}
MERCADEO = {Kevin, Ana, Lucia, Pedro, José, Boris}"""

VENTA = {"Juan", "José", "Ramón", "Pedro", "Mario", "Julio"}
MERCADEO = {"Kevin", "Ana", "Lucia", "Pedro", "José", "Boris"}

print(VENTA | MERCADEO)