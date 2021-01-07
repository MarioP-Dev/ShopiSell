#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Módulo principal de Software ShopiSell
#       Librerías utilizados:
#           - JSON: Módulo utilizado para el almacenamiento de la información sustituyendo así a una base de datos, que sería lo comúnmente utilizado
#           - Tkinter: Generación de UI para el software
#
#   https://www.python-course.eu/tkinter_entry_widgets.php
#   https://sodocumentation.net/es/tkinter/topic/6439/varias-ventanas--widgets-toplevel-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tkinter import *
from controllers import Inventario_Controller as inventario
from controllers import Clientes_Controller as clientes
from controllers import Pedidos_Contoller as pedidos

class app:
    def __init__(self):

        __author__ = 'Samuel Carballo Pacheco, Carlos González Fernández, Mario Pérez Fernández'
        __title__= 'ShopiSell'
        __date__ = '05/01/2021'
        __version__ = '0.0.1'
        __license__ = 'GNU GPLv3'




        self.main = Tk()

        self.main.geometry('620x400')
        self.main.title("Dashboard | ShopiSell")

        Label(self.main, text="Bienvenido a ShoppiSell", font=("Arial Bold", 40)).grid(column=0, row=0)
        Label(self.main, text="Software TPV basado en Python utilizando JSON files para operar", font=("Arial", 15)).grid(column=0, row=1)

        Button(self.main,text='Pedidos', command=self.opnPedidos, font=("Arial", 15)).grid(column=0,row=3)
        Button(self.main,text='Clientes', command=self.opnClientes, font=("Arial", 15)).grid(column=0,row=2)
        #Button(self.main,text='Finanzas', command=pedidos.run, font=("Arial", 15)).grid(column=0,row=4)
        #Button(self.main,text='Inventario', command=inventario.runWindowController, font=("Arial", 15)).grid(column=0,row=5)
        #Button(self.main,text='Configuración', command=config.run, font=("Arial", 15)).grid(column=0,row=6)
        Button(self.main,text='Acerca de', command=self.opnAcerca, font=("Arial", 15)).grid(column=0,row=7)

        self.main.mainloop()
    
    def opnPedidos(self):
        self.pedidosWnd = Toplevel(self.main)
        self.pedidosWnd.geometry('620x400')
        self.pedidosWnd.title("Pedidos | ShopiSell")

        menubar = Menu(self.pedidosWnd)
        self.pedidosWnd.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo")
        filemenu.add_command(label="Buscar", command=self.buscarPedido)
        filemenu.add_command(label="Guardar")
        filemenu.add_command(label="Cerrar")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.pedidosWnd.destroy)

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

    def buscarPedido(self):
        pass
        #pedidos.searchOrder(int(input("Referencia del pedido")))

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

    def reqData(self, msg):
        aux = Toplevel()
        Label(aux, text="Referencia").grid(row=1)

        e2 = Entry(aux)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)





app = app()



