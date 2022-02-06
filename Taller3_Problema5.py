"""Taller3 Problema 5
Bianca Gonzalez
Se requiere un programa para un restaurante el programa debe leer el tamaño de la pizza y el
número de ingredientes adicionales y debe mostrar el precio que debe pagar.
Tamaño Precio
1 5.00
2 9.00
3 20.00
Cada ingrediente adicional cuesta $1.50"""

print("\nRestaurante Pizzeria-\n")
print("-Programa de Precio a Pagar-\n")
tamano = int(input("Introduzca el tamaño de la pizza 1, 2 o 3: "))
ingredientes = int(input("Introduzca la cantidad de ingredientes: "))
if tamano == 1:
    total = 5 + (1.50 * ingredientes)
elif tamano == 2:
    total = 9 + (1.50 * ingredientes)
elif tamano == 3:
    total = 20 + (1.50 * ingredientes)
else:
    print("Error de datos favor introduzca un número valido")
    exit()
print("Precio a pagar: %.2f" % total)