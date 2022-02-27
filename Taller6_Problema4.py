"""Se desea un programa que nos ayude a obtener la suma de los gastos que realizamos la semana pasada.
El programa debe preguntar si tenemos otro gasto que contabilizar (S/N). El programa debe suministrar la siguiente
información:
•	La cantidad de gastos.
•	La suma de los gastos.
El usuario debe suministrar los montos de los gastos.
"""

# ---------------------------------Funciones----------------------------------------------------------------------------


def acumular():
    lista = []

    while True:
        lista.append(float(input("Ingrese el monto del gasto: ")))
        resp = input("Tiene otro gasto S/N ")

        if resp == 'N' or resp == 'n':
            break

    return lista


def sumaGastos(lista):
    return sum(lista)


def cantidadGastos(lista):
    return len(lista)


# ----------------------------------------------------------------------------------------------------------------------

print("\nPrograma de Gastos\n")

gastos = acumular()

total = sumaGastos(gastos)

cantidad = cantidadGastos(gastos)

print("\nTotal de gastos: %.2f" %total, "Cantidad de gastos: ", cantidad, "\nDetalle:\n", gastos)