#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Módulo principal de Software ShopiSell
#       Librerías utilizados:
#           - JSON: Módulo utilizado para el almacenamiento de la información sustituyendo así a una base de datos, que sería lo comúnmente utilizado
#           - Tkinter: Generación de UI para el software
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tkinter import *
from extensions import Inventario_Controller as inventario
from extensions import Clientes_Controller as clientes

class app:
    def __init__(self):

        __author__ = 'python para impacientes'
        __title__= 'ShopiSell'
        __date__ = '30/12/2020'
        __version__ = '0.0.1'
        __license__ = 'GNU GPLv3'




        self.main = Tk()

        self.main.geometry('620x400')
        self.main.title("Dashboard | ShopiSell")

        Label(self.main, text="Bienvenido a ShoppiSell", font=("Arial Bold", 40)).grid(column=0, row=0)
        Label(self.main, text="Software TPV basado en Python utilizando JSON files para operar", font=("Arial", 15)).grid(column=0, row=1)

        #Buttonself.(main,text='Pedidos', command=inventario.run, font=("Arial", 15)).grid(column=0,row=3)
        Button(self.main,text='Clientes', command=self.opnClientes, font=("Arial", 15)).grid(column=0,row=2)
        #Button(self.main,text='Finanzas', command=pedidos.run, font=("Arial", 15)).grid(column=0,row=4)
        #Button(self.main,text='Inventario', command=inventario.runWindowController, font=("Arial", 15)).grid(column=0,row=5)
        #Button(self.main,text='Configuración', command=config.run, font=("Arial", 15)).grid(column=0,row=6)
        Button(self.main,text='Acerca de', command=self.opnAcerca, font=("Arial", 15)).grid(column=0,row=7)

        self.main.mainloop()
    
    def opnClientes(self):
        self.clientesWnd = Toplevel(self.main)
        self.clientesWnd.geometry('620x400')
        self.clientesWnd.title("Clientes | ShopiSell")

        menubar = Menu(self.clientesWnd)
        self.clientesWnd.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo")
        filemenu.add_command(label="Abrir")
        filemenu.add_command(label="Guardar")
        filemenu.add_command(label="Cerrar")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.clientesWnd.destroy)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cortar")
        editmenu.add_command(label="Copiar")
        editmenu.add_command(label="Pegar")

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...")

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Editar", menu=editmenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)

    def opnAcerca(self):
        acerca = Toplevel()
        acerca.geometry("320x200")
        acerca.resizable(width=False, height=False)
        acerca.title("Acerca de")
        
        marco1 = Frame(acerca, relief=RAISED)
        marco1.pack(side=TOP, fill=BOTH, expand=True)
        boton1 = Button(marco1, text="Salir", command=acerca.destroy)
        boton1.pack(side=TOP, padx=10, pady=10)
        boton1.focus_set()

        acerca.transient(self.main)
        self.main.wait_window(acerca)
app = app()



