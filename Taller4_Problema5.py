"""
Taller 4 Problema 5
Bianca González
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál
fue el mayor número ingresado.

"""
mayor = 0
while True:
    numero = int(input("Ingresar un numero: "))
    if numero > mayor:
        mayor = numero
    elif numero == 0:
        print("El numero mayor fue: ", mayor)
        break
    elif numero < 0:
        print("Error, el numero debe ser positivo, vuelva a")
