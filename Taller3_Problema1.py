"""
Taller 3 Problema 1
Bianca Gonzalez

Cree un programa para calcular el valor total que una persona debe pagar por la compra de
llantas en un almacén que tiene la siguiente promoción: Si la cantidad de llantas comprada
es mayor a 4, el precio unitario tiene un descuento de 10%. El programa debe ingresar como
datos la cantidad de llantas y el precio inicial de cada llanta.
"""

print("\n -Empresa de Llantas- \n -Programa de Cotización- \n")
cantidad = int(input("Introduzca la cantidad de llantas a comprar: "))
precio_inicial = float(input("Introduzca el precio inicial de cada llanta: "))

if cantidad > 4:
    precio_unitario = precio_inicial - (precio_inicial * 0.1)
else:
    precio_unitario = precio_inicial

print("El precio unitario es: ", precio_unitario)
print("El total es: ", precio_unitario * cantidad)
