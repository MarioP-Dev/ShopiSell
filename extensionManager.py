#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Módulo encargado de cargar y verificar los módulos presentes en ShopiSell.
#   Proporciona una lista con todas las extensiones disponibles.
#   Extensiones compatibles con esta versión: Clientes, finanzas e inventario
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from pathlib import Path
import importlib

def loadExtensions():
    extensions = []
    p = Path('extensions/')
    for child in p.iterdir():
        extensions.append(child)
    
    for module in extensions:
        print(module)


loadExtensions()