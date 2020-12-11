#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extensión del Software ShopiSell: Pedidos
#       Esta extensión, proporciona al programa un sistema de control de pedidos, ver los pedidos realizados y generar nuevos
#       Todos estos datos los almacena en un fichero denominado "clientes", localizable en la carpeta storage del programa.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import tkinter as tk
from tkinter import Menu
import os.path as path
from ShopiSell import availableExtensions

def run():
    main = tk.Tk()
    main.geometry('620x400')
    main.title("Pedidos")
    menu = Menu(main)
    new_item = Menu(menu)
    new_item.add_command(label='Nuevo pedido', command=addClientWindow)
    new_item.add_command(label='Buscar pedido')
    menu.add_cascade(label='Gestionar', menu=new_item)
    main.config(menu=menu)

def addOrder():
    print("nUEVO PEDIDO")