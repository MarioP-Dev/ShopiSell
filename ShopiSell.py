#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Módulo principal de Software ShopiSell
#       Librerías utilizados:
#           - JSON: Módulo utilizado para el almacenamiento de la información sustituyendo así a una base de datos, que sería lo comúnmente utilizado
#           - Tkinter: Generación de UI para el software
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os.path as path
import tempfile as temp
import tkinter as tk
import extensionManager

availableExtensions = []


main = tk.Tk()

main.geometry('620x400')
main.title("Dashboard | ShopiSell")

tk.Label(main, text="Bienvenido a ShoppiSell", font=("Arial Bold", 40)).grid(column=0, row=0)
tk.Label(main, text="Software TPV basado en Python utilizando JSON files para operar", font=("Arial", 15)).grid(column=0, row=1)

tk.Button(main,text='Pedidos', command=pedidos.run, font=("Arial", 15)).grid(column=0,row=3)
tk.Button(main,text='Clientes', command=clientes.run, font=("Arial", 15)).grid(column=0,row=2)
tk.Button(main,text='Finanzas', command=pedidos.run, font=("Arial", 15)).grid(column=0,row=4)
tk.Button(main,text='Inventario', command=inventario.run, font=("Arial", 15)).grid(column=0,row=5)
tk.Button(main,text='Configuración', command=config.run, font=("Arial", 15)).grid(column=0,row=6)

tk.Label(main, text="Puede descargar las extensiones en nuestro GitHub", font=("Arial", 8)).grid(column=0, row=7)


main.mainloop()

