#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extensión del Software ShopiSell: Clientes
#       Esta extensión, proporciona al programa un sistema de control de clientes, ver la cantidad de pedidos realizados
#       así como ver sus datos personales. Todos estos datos los almacena en un fichero denominado "clientes", localizable
#       en la carpeta storage del programa.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import tkinter as tk
from tkinter import Menu
import os.path as path
from ShopiSell import availableExtensions

def setUp():
    if not path.exists(path="../storage/clientes.json"):
        file = open('./storage/clientes.json', 'w')
        file.close()
    else:
        availableExtensions.append("clientes")


def run():
    main = tk.Tk()
    main.geometry('620x400')
    main.title("Clientes")
    menu = Menu(main)
    new_item = Menu(menu)
    new_item.add_command(label='Agregar cliente', command=addClientWindow)
    new_item.add_command(label='Buscar cliente')
    menu.add_cascade(label='Gestionar', menu=new_item)
    main.config(menu=menu)

def addClientWindow():
    addClient = tk.Tk()
    addClient.geometry('600x400')
    addClient.title("Agregar cliente")
    tk.Label(addClient, text="Agregar un nuevo cliente", font=("Arial Bold", 20)).grid(column=0, row=0)