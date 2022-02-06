"""
Taller 4 Problema 4
Bianca Gonzalez
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
cortando el ingreso de datos cuando el usuario ingrese el monto 0.
Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo
monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el
total de $1000, se le debe aplicar un 10% de descuento.

"""
print("\n-Programa De Compras-\n")
subtotal = 0
while True:
    monto = float(input("Ingresar El Monto: "))
    if monto < 0:
        print("Vuelva A ")
    elif monto == 0:
        break
    else:
        subtotal += monto

if subtotal > 1000:
    subtotal = subtotal - (subtotal * 0.1)

print("El total es: %.2f" % subtotal, "$")
