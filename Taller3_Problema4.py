"""
Taller3 Problema 4
Bianca Gonzalez
Cree un programa que ayude a tomar la siguiente decisión para pagar una cuenta en un
restaurante: Si la cuenta es menor a $50 pago en efectivo. Sinó, si es de $50 hasta $100
pagaré con el celular(dinero electrónico). Pero si es mayor a 100 hasta $200, usaré la tarjeta
de débito. Caso contrario, pagaré con la tarjeta de crédito."""

print("\n -Sistema De Toma De Decisiones Pago De Cuenta-\n")
cuenta = float(input("Ingrese el total de la cuenta: "))
if cuenta <50:
    print("Pagar en efectivo")
elif (cuenta >= 50) and (cuenta <= 100):
    print("Pagar con el celular")
elif (cuenta >100) and (cuenta <=200):
    print("Pagar con tarjeta de débito")
else:
    print("Pagar con tarjeta de crédito")