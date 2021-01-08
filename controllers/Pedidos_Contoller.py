#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extensión del Software ShopiSell: Pedidos
#       
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import csv

class Pedido:
    cliente = ''
    articulos = []
    importe = 0
    descuento = 0
    total= 0;

    def __init__(self) -> None:
        pass

    """
    Función encargada añadir un artículo al pedido
    """
    def añadirArticulo(self, articulo):
        self.articulos.append(articulo)
        self.actualizarLiquidaciones()

    """
    Función encargada eliminar un artículo del pedido
    """
    def eliminarArticulo(self, articulo):
        self.articulos.remove(articulo)
        self.actualizarLiquidaciones()
        
    """
    Función encargada de calcular el total del pedido
    """
    def actualizarLiquidaciones(self):
        importe = 0
        for item in self.articulos:
            importe = importe + item[2]
        self.importe = importe
        self.total = self.importe - self.descuento


    """
    Función encargada de inscribir el pedido en el JSON para cerrarlo
    """
    def placeOrder(self):
        data = getOrders()

        data.append([self.cliente, self.importe, self.descuento, self.total])

        writeOrders(data)


        


def getOrders():
    data = []
    with open('storage/pedidos.csv') as csvarchivo:
        entrada = csv.DictReader(csvarchivo)
        for reg in entrada:
            data.append([reg['cliente'], reg['importe'], reg['descuentos'], reg['total']])
        csvarchivo.close()
    return data

def writeOrders(data):
    try:
        archivo = open('storage/pedidos.csv', 'w')
        header = ['cliente', 'importe', 'descuentos', 'total']
        salida = csv.DictWriter(archivo, fieldnames=header)
        salida.writeheader()
        for item in data:
            salida.writerow({ 'cliente':item[0],
                              'importe':item[1],
                              'descuentos':item[2],
                              'total':item[3]})

    finally:
        archivo.close()

def searchOrder(id):
    orders = getOrders()
    return orders[id]