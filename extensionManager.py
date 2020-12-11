#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Módulo encargado de cargar y verificar los módulos presentes en ShopiSell.
#   Proporciona una lista con todas las extensiones disponibles.
#   Extensiones compatibles con esta versión: Clientes, finanzas e inventario
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from ShopiSell import availableExtensions

def installExtension(extension):
    if extension in availableExtensions:
        print("Existe la extension")
