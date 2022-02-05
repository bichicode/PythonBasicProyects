"""
Taller 3 Problema 2
Bianca Gonzalez
Crear un programa que le permita calcular el pago semanal a un obrero. Para este problema
se consideran los siguientes datos: horas trabajadas, tarifa por hora y descuentos. Si la
cantidad de horas trabajadas en la semana es mayor a 40, se le debe pagar las horas en
exceso con una bonificación de 50% adicional al pago normal. """

print("\n -Programa De Pago Semanal A Obrero\n")
horas = int(input("Introduzca la cantidad de horas trabajadas: "))
tarifa = float(input("Introduzca la tarifa por hora: "))
descuento = float(input("Introduzca el descuento total: "))
pago_ex = 0.00

if horas > 40:
    horas_ex = horas - 40
    horas = 40
    pago_ex = horas_ex * (tarifa + (tarifa * 0.5))

print("\nEl pago semanal es:  %.2f" % (horas * tarifa + pago_ex - descuento))
print("\nDesglose:\nPago por horas trabajadas %.2f" % (horas * tarifa), "\nPago por horas extra: %.2f" % pago_ex, "\nDescuentos: %.2f" % descuento)