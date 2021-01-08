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
        data = pedidos.getOrders()

        searchBar = IntVar()

        def orderDetail(order):
            print(order)
            cliente, importe, descuentos, total = StringVar(), StringVar(), StringVar(), StringVar()
            cliente.set(order[0]), importe.set(order[1]), descuentos.set(order[2]), total.set(order[3])
            aux = Toplevel(self.pedidosWnd)
            aux.resizable(0, 0) 
            aux.title("Detalles del pedido | ShopiSell")
            Label(aux, text="Detalles del Pedido", font=("Verdana",24)).pack()
            Label(aux, text="Cliente").pack()
            Entry(aux, justify="center", textvariable=cliente, state="disabled", width=30).pack()

            Label(aux, text="Importe").pack()
            Entry(aux, justify="center", textvariable=importe, state="disabled", width=30).pack()

            Label(aux, text="Descuentos").pack()
            Entry(aux, justify="center", textvariable=descuentos, state="disabled", width=30).pack()

            Label(aux, text="Total").pack()
            Entry(aux, justify="center", textvariable=total, state="disabled", width=30).pack()
            Label(aux, text="").pack()  # Separador
            Button(aux, text="Salir", justify="center", command=aux.destroy, width=30).pack()

        def getData():
            if searchBar != "":
                orderDetail(pedidos.searchOrder(searchBar.get()))
            else:
                data = pedidos.getOrders()

        self.pedidosWnd = Toplevel(self.main)
        self.pedidosWnd.geometry('620x400')
        self.pedidosWnd.title("Pedidos | ShopiSell")

        menubar = Menu(self.pedidosWnd)
        self.pedidosWnd.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.pedidosWnd.destroy)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...", command=self.opnAcerca)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)

        searchWidget = Frame(self.pedidosWnd)
        searchWidget.pack()
        Label(searchWidget, text="Realizar búsqueda por referencia:").grid(pady=5, row=0, column=0)
        Entry(searchWidget, textvariable=searchBar, width=40).grid(padx=5, row=0, column=1)
        Button(searchWidget, text="Buscar",command=getData, width=15).grid(padx=10, pady=10, row=0, column=2, columnspan=2)

        result = Frame(self.pedidosWnd)
        result.pack()

        Label(result, text="-- Ref. Pedido --").grid(row=1, column=0)
        Label(result, text="-- Cliente --").grid( row=1, column=1)
        Label(result, text="-- Importe --").grid( row=1, column=2)
        Label(result, text="-- Descuentos --").grid( row=1, column=3)
        Label(result, text="-- Total --").grid( row=1, column=4)
        row = 2
        for pedido in data:
            Label(result, text=row-2).grid(row=row, column=0)
            Label(result, text=pedido[0]).grid(padx=1, row=row, column=1)
            Label(result, text=pedido[1]+"€").grid(padx=2, row=row, column=2)
            Label(result, text=pedido[2]+"€").grid(padx=2, row=row, column=3)
            Label(result, text=pedido[3]+"€").grid(padx=2, row=row, column=4)
            row = row+1

        self.pedidosWnd.mainloop()

    def buscarPedido(self):
        print("hola")
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





app = app()



