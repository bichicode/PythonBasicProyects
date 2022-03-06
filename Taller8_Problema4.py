"""Taller 8
Problema 4
Bianca
Se le solicita crear un programa que tenga información de los vendedores por región.
Se tendrán tres conjuntos: norte, centro y sur.
Una vez se tengan los vendedores de cada región crear un conjunto que tenga la unión
de estos tres conjuntos y se nombrará regional.
El programa debe permitir realizar las siguientes acciones al conjunto regional:
a. Buscar si un nombre indicado por el usuario existe en el conjunto regional.
b. Adicionar un nuevo vendedor al conjunto regional.
c. Eliminar un vendedor al conjunto regional.
d. Mandar a imprimir los cuatro conjuntos."""

norte = []
centro = []
sur = []

c_norte = int(input("Cantidad de Vendedores en Norte: "))

for comprador in range(c_norte):
    norte.append(input("Ingrese el vendedor: "))

c_centro = int(input("Cantidad de Vendedores en Centro: "))

for comprador in range(c_centro):
    centro.append(input("Ingrese el vendedor: "))

c_sur = int(input("Cantidad de Vendedores en Sur: "))

for comprador in range(c_sur):
    sur.append(input("Ingrese el vendedor: "))

norte = set(norte)

centro = set(centro)

sur = set(sur)

regional = norte | centro | sur

while True:

    op = int(input("\nMenu\n1 Buscar Vendedor\n2 Agregar Vendedor\n3 Eliminar Vendedor\n4 Imprimir Conjuntos"
                   "\n5 Salir\n>> "))

    if op == 1:

        nvendedor = input("Nombre del vendedor: ")

        if nvendedor in regional:
            print("si se encontro")
        else:
            print("No se encontro")

    elif op == 2:

        nvendedor = input("Nombre del vendedor: ")

        regional.add(nvendedor)

        print(regional)

    elif op == 3:

        nvendedor = input("Nombre del vendedor: ")

        regional.discard(nvendedor)

        print(regional)

    elif op == 4:
        print(norte)
        print(centro)
        print(sur)
        print(regional)

    elif op == 5:
        print("Fin del programa")
        break
