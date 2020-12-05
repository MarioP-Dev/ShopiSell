#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Software que permite la gestión de clientes, ventas, finanzas de una tienda y marketing.
#       Modulos utilizados:
#           - JSON: Módulo utilizado para el almacenamiento de la información sustituyendo así a una base de datos, que sería lo comúnmente utilizado
#           - 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from windows import *

import tkinter as tk

window = tk.Tk()

window.geometry('650x400')
window.title("Dashboard | ShopiSell")

tk.Label(window, text="Bienvenido a ShoppiSell", font=("Arial Bold", 40)).grid(column=0, row=0)
tk.Label(window, text="Software TPV basado en Pythonm utilizando JSON files para operar", font=("Arial", 15)).grid(column=0, row=1)


tk.Button(window,text='Clientes', command=openClientes).grid(column=0,row=2)
tk.Button(window,text='Pedidos', command=openClientes).grid(column=0,row=3)
tk.Button(window,text='Finanzas', command=openClientes).grid(column=0,row=4)
tk.Button(window,text='Configuración', command=openClientes).grid(column=0,row=5)

window.mainloop()

