import tkinter as tk
from tkinter import Menu

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