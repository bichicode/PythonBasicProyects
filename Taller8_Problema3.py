"""Taller 8
Problema 3
Bianca
Crear una lista que contenga nombre de clientes que compraron en el mes de enero y
nombre de clientes que compraron en el mes de febrero. Los nombres pueden estar
repetidos. Una vez capturados los nombres convertir la lista en un conjunto.
El programa debe tener las siguientes opciones:
a. Agregar elemento. El programa debe permitir adicionar nuevos nombres de
clientes en cualquiera de los dos conjuntos.
b. Eliminar elemento. El programa debe permitir eliminar nombres de clientes en
cualquiera de los dos conjuntos.
c. Unión de conjuntos. Crear un nuevo conjunto que sea el resultado de la unión del
conjunto de clientes que compraron enero con el conjunto de clientes que
compraron en febrero. """

# --------------------------------------- Funciones -------------------------------------------------


def menu(cenero, cfebrero):

    clientesenero = set(cenero)
    clientesfebrero = set(cfebrero)

    while True:

        op = int(input("\nMenu\n1 Agregar Elemento\n2 Eliminar Elemento\n3 Unir Conjuntos\n4 Salir\n>> "))

        if op == 1:

            nlista = int(input("A cual mes desea agregar un cliente\n1 Enero\n2 Febrero\n>>"))
            elemento = input("Nombre del cliente: ")

            if nlista == 1:
                clientesenero.add(elemento)
                print(clientesenero)

            elif nlista == 2:
                clientesfebrero.add(elemento)
                print(clientesfebrero)

        elif op == 2:

            nlista = int(input("A cual mes desea eliminar un cliente\n1 Enero\n2 Febrero\n>>"))
            elemento = input("Nombre del cliente: ")

            if nlista == 1:
                clientesenero.discard(elemento)
                print(clientesenero)

            elif nlista == 2:
                clientesfebrero.discard(elemento)
                print(clientesfebrero)

        elif op == 3:
            clientes = clientesenero.union(clientesfebrero)
            print(clientes)

        elif op == 4:
            print("Fin del programa")
            break

    return

# ------------------------------------------------------------------------------------------------


print("\nPrograma de Compradores")

enero = []
febrero = []

c_enero = int(input("Cantidad de Compradores en Enero: "))

for comprador in range(c_enero):
    enero.append(input("Ingrese el comprador: "))

c_febrero = int(input("Cantidad de Compradores en Febrero: "))

for comprador in range(c_febrero):
    febrero.append(input("Ingrese el comprador: "))

c_enero = set(enero)
c_febrero = set(febrero)

menu(c_enero, c_febrero)
