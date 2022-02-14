"""Se desea un programa que lea el nombre de tres países. El programa debe escribir el nombre
del país en cierre de mayúscula. Trabaje con una función que reciba parámetros arbitrarios."""


from tkinter import *

root = Tk()

root.title("Mayuscula @bichicode")

root.resizable(True, True)

root.iconbitmap("bichi.ico")

miFrame = Frame()

miFrame.pack()

# ----------------------------Variables-------------------------
cierre_mayuscula = StringVar()
Cont = 0

# ---------------------------Funciones---------------------------------


def obtener_datos():
    pais1 = str(caja1.get())
    pais2 = str(caja2.get())
    pais3 = str(caja3.get())

    mayuscula(pais1, pais2, pais3)

    return


def mayuscula(*paises):
    paisesmayuscula = ""

    for i in paises:
        paisesmayuscula = paisesmayuscula + i.upper() + " "

    return cierre_mayuscula.set(str(paisesmayuscula))


# -------------------------------------------------------------------

etiqueta1 = Label(miFrame, text="Programa de Mayusculas \n\n Favor ingresar tres paises")
etiqueta1.grid(row=2, column=1, padx=55, pady=20, columnspan=2)


etiquetac1 = Label(miFrame, text="1er Pais:")
etiquetac1.grid(row=5, column=1, padx=30, pady=20)

caja1 = Entry(miFrame, justify="right")
caja1.grid(row=5, column=2, padx=30, pady=20)


etiquetap2 = Label(miFrame, text="2do Pais:")
etiquetap2.grid(row=7, column=1, padx=30, pady=20)

caja2 = Entry(miFrame, justify="right")
caja2.grid(row=7, column=2, padx=30, pady=20)


etiquetap3 = Label(miFrame, text="3er Pais:")
etiquetap3.grid(row=9, column=1, padx=30, pady=20)

caja3 = Entry(miFrame, justify="right")
caja3.grid(row=9, column=2, padx=30, pady=20)

resp = Entry(miFrame, textvariable=cierre_mayuscula, justify="center", font="bold", width=30)
resp.grid(row=15, column=1, padx=30, pady=15, columnspan=2)


# -------------------------------------Botones----------------------------------------

boton1 = Button(miFrame, text="Aceptar", width=13, command=obtener_datos)
boton1.grid(row=13, column=2, padx=30, pady=20)

# ---------------------------------------------------------------------

miImagen = PhotoImage(file="../Taller5/pp.png")
firma = Label(miFrame, image=miImagen)
firma.grid(row=25, column=1, padx=10, pady=30, columnspan=2)


# ---------------------------------------------------------------------

root.mainloop()