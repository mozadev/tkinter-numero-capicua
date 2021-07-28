import tkinter
from tkinter import messagebox


def calcular():
    n1 = txtnumero1.get()
    n2=int(n1)

    if (len(n1) == 0):
        messagebox.showinfo(message="Ingrese el primero Numero !!", title="Mensaje")
        txtnumero1.focus()

    else:

        if n2 >= 0:
            if str(n2) == str(n2)[::-1]:

                area.insert(1.0,"\nEl numero es capicua")
            else:
                area.insert(1.0,"\nEl numero es no es capicua")


        else:

            area.insert(1.0,"\nEl numero debe ser  positivo")

    sumDigit, extNum = 0, 0
    while n2 != 0:
        extNum = n2 % 10
        n2 //= 10
        sumDigit += extNum
    area.insert(1.0, "\nla suma de digitos es: "+str(sumDigit))



ventana = tkinter.Tk()  # instancia del formulario
ventana.title("Ventana Principal")
ventana.geometry("600x500")
# ventana.configure(background='green')
lblnumero1 = tkinter.Label(ventana, text='ingrese el  numero:')
lblnumero1.place(x=100, y=50)
txtnumero1 = tkinter.Entry(ventana, width=20)
txtnumero1.place(x=310, y=50)

boton = tkinter.Button(ventana, text="Determinar si es capicua", command=calcular)
boton.place(x=250, y=100)
area = tkinter.Text(ventana)
area.config(width=42, height=13)
area.place(x=100, y=150)

ventana.mainloop()  # ejec