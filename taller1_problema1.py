"""Taller 1
Problema 1

Bianca Gonzalez

Puntos ABC club

Elabore un programa que permita ingresar el número de partidos ganados, perdidos
y empatados, por el ABC club en el torneo apertura, se debe de mostrar su puntaje
total, teniendo en cuenta que por cada partido ganado obtendrá 3 puntos, empatado
1 punto y perdido O puntos.

"""

print("\n              - ABC  Club - \n- Sistema De Puntos Del Torneo Apertura -\n")
partidos_ganados=int(input("Introduzca la cantidad de partidos ganados: "))
partidos_perdidos=int(input("Introduzca la cantidad de partidos perdidos: "))
partidos_empatados=int(input("Introduzca la cantidad de partidos empatados: "))
puntaje_total= (partidos_ganados*3 + partidos_perdidos*0 + partidos_empatados*1)
print("El puntaje total es: ", puntaje_total)
