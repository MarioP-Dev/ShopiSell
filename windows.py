import tkinter as tk
from tkinter import Menu

def openClientes():
    window = tk.Tk()
    window.title("Clientes")
    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label='Agregar cliente')
    menu.add_cascade(label='Gestionar', menu=new_item)
    window.config(menu=menu)