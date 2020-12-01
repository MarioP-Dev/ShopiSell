#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Software que permite la gestión de clientes, ventas y finanzas de una tienda.
#       Modulos utilizados:
#           - JSON: Módulo utilizado para el almacenamiento de la información sustituyendo así a una base de datos, que sería lo comúnmente utilizado
#           - 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tkinter import *

from tkinter import messagebox

window = Tk()
window.geometry('650x400')
window.title("Dashboard | ShopiSell")

Label(window, text="Bienvenido a ShoppiSell", font=("Arial Bold", 40)).grid(column=0, row=0)
Label(window, text="Software TPV basado en Pythonm utilizando JSON files para operar", font=("Arial", 15)).grid(column=0, row=1)


def clicked():
    messagebox.showinfo('Message title', 'Message content')

Button(window,text='Clientes', command=clicked).grid(column=0,row=2)
Button(window,text='Pedidos', command=clicked).grid(column=0,row=3)
Button(window,text='Finanzas', command=clicked).grid(column=0,row=4)
Button(window,text='Configuración', command=clicked).grid(column=0,row=5)

window.mainloop()