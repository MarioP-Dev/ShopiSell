#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extensión del Software ShopiSell: Pedidos
#       
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Pedido:
    identificador = ''
    articulos = []
    total= 0;

    def __init__(self) -> None:
        pass

    """
    Función encargada añadir un artículo al pedido
    """
    def añadirArticulo(self, articulo):
        self.articulos.append(articulo)
        self.calcularTotal()

    """
    Función encargada eliminar un artículo del pedido
    """
    def añadirArticulo(self, articulo):
        self.articulos.remove(articulo)
        self.calcularTotal()
        
    """
    Función encargada de calcular el total del pedido
    """
    def calcularTotal(self):
        total = 0
        for item in self.articulos:
            total = total + item[1]
        self.total = total


    """
    Función encargada de inscribir el pedido en el JSON para cerrarlo
    """
    def placeOrder():
        pass
    