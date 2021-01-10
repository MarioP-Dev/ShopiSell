#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Módulo principal de Software ShopiSell
#       Librerías utilizados:
#           - CSV: Módulo utilizado para el almacenamiento de la información sustituyendo así a una base de datos, que sería lo comúnmente utilizado
#           - Tkinter: Generación de UI para el software
#
#   https://www.python-course.eu/tkinter_entry_widgets.php
#   https://sodocumentation.net/es/tkinter/topic/6439/varias-ventanas--widgets-toplevel-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tkinter import *
from tkinter import ttk
from controllers import Inventario_Controller as inventario
from controllers import Clientes_Controller as clientes
from controllers import Pedidos_Contoller as pedidos

class ShopiSell:
    def __init__(self, window):

        __author__ = 'Samuel Carballo Pacheco, Carlos González Fernández, Mario Pérez Fernández'
        __title__= 'ShopiSell'
        __date__ = '09/01/2020'
        __version__ = '0.0.1'
        __license__ = 'GNU GPLv3'




        self.main = window

        self.main.geometry('620x400') # Dimensiones de la ventana principal
        self.main.title("Dashboard | ShopiSell") # Nombre de la ventana principal

        Label(self.main, text="Bienvenido a ShoppiSell", font=("Arial Bold", 40)).grid(column=0, row=0)
        Label(self.main, text="Software TPV basado en Python utilizando JSON files para operar", font=("Arial", 15)).grid(column=0, row=1)

        Button(self.main,text='Pedidos', command=self.pedidosWnd, font=("Arial", 15)).grid(column=0,row=3)
        Button(self.main,text='Clientes', command=self.opnClientes, font=("Arial", 15)).grid(column=0,row=2)
        Button(self.main,text='Inventario', font=("Arial", 15)).grid(column=0,row=5)
        Button(self.main,text='Configuración', font=("Arial", 15)).grid(column=0,row=6)
        Button(self.main,text='Acerca de', command=self.opnAcerca, font=("Arial", 15)).grid(column=0,row=7)
        
    
    def pedidosWnd(self):

        def buscarPedido():
            
            aux = Toplevel()
            aux.title("Vista de pedido | ShopiSell")

            frame = LabelFrame(aux, text = 'Información del pedido')
            frame.grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = 20)
            # Input búsqueda
            Label(frame, text = 'Referencia del pedido: ').grid(row = 1, column = 0)
            cliente = Entry(frame, width=30)
            cliente.grid(row = 1, column = 1)

            Label(frame, text = 'Importe: ').grid(row = 2, column = 0)
            importe = Entry(frame)
            importe.grid(row = 2, column = 1)

            Label(frame, text = 'Descuentos: ').grid(row = 3, column = 0)
            descuentos = Entry(frame)
            descuentos.grid(row = 3, column = 1)

            Label(frame, text = 'Total: ').grid(row = 4, column = 0)
            total = Entry(frame)
            total.grid(row = 4, column = 1)

            data = pedidos.searchOrder(int(self.search.get()))
            cliente.insert(0, data[0])
            importe.insert(0, data[1])
            descuentos.insert(0, data[2])
            total.insert(0, data[3])

            ttk.Button(aux, text = 'Cerrar vista', command=aux.destroy).grid(row = 5, column = 2, sticky = W + E)

            aux.mainloop()

        def eliminarPedido():
            try:
               self.tree.item(self.tree.selection())['text']
            except IndexError as e:
                print("No ha seleccionado ningún pedido")
                return
            pedidos.deleteOrder(self.tree.item(self.tree.selection())['text'])
            
            getData()

        def getData():
            # Limpiando la tabla para actualizar
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            # Recibir datos en array
            records = pedidos.getOrders()
            # filling data
            idOrder = 0
            for order in records:
                self.tree.insert('', 0, text = idOrder, values = order[3])
                idOrder = idOrder+1
            #pedidos.searchOrder(int(input("Referencia del pedido")))

        def orderEdit():
            def save():
                pedidos.modifyOrder(self.tree.item(self.tree.selection())['text'], cliente.get(), importe.get(), descuentos.get(), total.get())
                getData()
                aux.destroy()

            try:
               self.tree.item(self.tree.selection())['text']
            except IndexError as e:
                print("No ha seleccionado ningún pedido")
                return e
            
            aux = Toplevel()
            aux.title("Gestión de pedido | ShopiSell")

            frame = LabelFrame(aux, text = 'Editar pedido')
            frame.grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = 20)
            # Input búsqueda
            Label(frame, text = 'Referencia del producto: ').grid(row = 1, column = 0)
            cliente = Entry(frame, width=30)
            cliente.grid(row = 1, column = 1)

            Label(frame, text = 'Importe: ').grid(row = 2, column = 0)
            importe = Entry(frame)
            importe.grid(row = 2, column = 1)

            Label(frame, text = 'Descuentos: ').grid(row = 3, column = 0)
            descuentos = Entry(frame)
            descuentos.grid(row = 3, column = 1)

            Label(frame, text = 'Total: ').grid(row = 4, column = 0)
            total = Entry(frame)
            total.grid(row = 4, column = 1)

            data = pedidos.searchOrder(self.tree.item(self.tree.selection())['text'])
            cliente.insert(0, data[0])
            importe.insert(0, data[1])
            descuentos.insert(0, data[2])
            total.insert(0, data[3])

            ttk.Button(aux, text = 'Guardar', command=save).grid(row = 5, column = 2, sticky = W + E)

            aux.mainloop()

        def orderCreate():
            order = pedidos.Pedido()
            aux = Toplevel()
            aux.title("Crear pedido | ShopiSell")
            
            def actualizarCampos():
                importe.delete(0, 'end')
                total.delete(0, 'end')
                dto.delete(0, 'end')
                importe.insert(0, order.importe)
                total.insert(0, order.total)
                dto.insert(0, order.descuento)

            def getOrderProducts(order):
                records = tree.get_children()
                for element in records:
                    tree.delete(element)
                records = order.articulos
                for articulo in records:
                    tree.insert('', 0, text = articulo[1], values = articulo[2])
                

            def addProduct():
                order.añadirArticulo([ref.get(), nombre.get(), int(precio.get())])
                getOrderProducts(order)
                order.actualizarLiquidaciones()
                actualizarCampos()
                ref.delete(0, 'end'), nombre.delete(0, 'end'), precio.delete(0, 'end')
            frame = LabelFrame(aux, text = 'Cliente')
            frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
            Label(frame, text = 'nombre del cliente: ').grid(row = 0, column = 0)
            cliente = Entry(frame, width= 30)
            cliente.focus()
            cliente.grid(row = 0, column = 1)

            def applyDiscount():
                order.descuento = int(dto.get())
                order.actualizarLiquidaciones()
                actualizarCampos()
            descuento = LabelFrame(aux, text = 'Descuento')
            descuento.grid(row = 1, column = 0, columnspan = 3)
            dto = ttk.Entry(descuento, width=15)
            dto.grid(row = 0, column = 0)
            dto.insert(0, order.descuento)
            ttk.Button(descuento, text = 'Aplicar', command=applyDiscount ).grid(row = 0, column = 1)

            tree = ttk.Treeview(aux, height = 10, columns = 3)
            tree.grid(row = 4, column = 0, columnspan = 4)
            tree.heading('#0', text = 'Producto', anchor = CENTER)
            tree.heading('#1', text = 'Precio', anchor = CENTER)
            getOrderProducts(order)

            frame2 = LabelFrame(aux, text = 'Añadir producto')
            frame2.grid(row = 5, column = 1, sticky = W + E)

            Label(frame2, text = 'Ref:').grid(row = 0, column = 0)
            ref = ttk.Entry(frame2)
            ref.grid(row = 0, column = 1)
            Label(frame2, text = 'Nombre:').grid(row = 1, column = 0)
            nombre = ttk.Entry(frame2)
            nombre.grid(row = 1, column = 1)
            Label(frame2, text = 'Precio:').grid(row = 2, column = 0)
            precio = ttk.Entry(frame2)
            precio.grid(row = 2, column = 1)
            ttk.Button(frame2, text = 'Añadir', command=addProduct ).grid(row = 5, column = 3)

            liquidaciones = LabelFrame(aux, text = 'Liquidaciones')
            liquidaciones.grid(row = 5, column = 2, sticky = W + E)
            Label(liquidaciones, text = 'Importe').grid(row = 0, column = 0)
            importe = ttk.Entry(liquidaciones)
            importe.grid(row = 0, column = 1)
            Label(liquidaciones, text = 'Total').grid(row = 1, column = 0)
            total = ttk.Entry(liquidaciones)
            total.grid(row = 1, column = 1)
            total.insert(0, order.total)

            def cerrarPedido():
                order.cliente = cliente.get()
                order.placeOrder()
                getData()
                aux.destroy()

            Button(aux, text = 'Crear pedido', command=cerrarPedido, width=30).grid(row = 7, column = 0, columnspan = 3, pady = 20)



        aux = Toplevel(self.main)
        aux.resizable(0, 0) 
        aux.title("Pedidos | ShopiSell")
        # Contenedor
        frame = LabelFrame(aux, text = 'Buscar pedido')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Input búsqueda
        Label(frame, text = 'Referencia del producto: ').grid(row = 1, column = 0)
        self.search = Entry(frame)
        self.search.focus()
        self.search.grid(row = 1, column = 1)

        # Botón buscar
        ttk.Button(frame, text = 'Buscar', command=buscarPedido).grid(row = 3, columnspan = 2, sticky = W + E)

        # Tabla pedidos
        self.tree = ttk.Treeview(aux, height = 10, columns = 3)
        self.tree.grid(row = 4, column = 0, columnspan = 4)
        self.tree.heading('#0', text = 'ID de pedido', anchor = CENTER)
        self.tree.heading('#1', text = 'Total', anchor = CENTER)

        # Botones de acción
        ttk.Button(aux, text = 'Eliminar seleccionado', command=eliminarPedido).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(aux, text = 'Editar seleccionado', command=orderEdit ).grid(row = 5, column = 1, sticky = W + E)
        ttk.Button(aux, text = 'Crear pedido', command=orderCreate ).grid(row = 5, column = 2, sticky = W + E)

        getData()

        

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



if __name__ == '__main__':
    window = Tk()
    application = ShopiSell(window)
    window.mainloop()