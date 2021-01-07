#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extensión del Software ShopiSell: Inventario
#       Los artículos deberán tener la siguiente estructura de array: [referencia, nombre, precio]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import csv



def addItem(reference, name, price):
    data = getItems()

    data.append([reference, name, price])

    writeItems(data)

def delItem(id):
    data = getItems()

    data.pop(id)

    writeItems(data)

def findItem(id):
    data = getItems()
    if id > len(data) or id < 0:
        return None
    else:
        return data[id]

def findItemByReference(referencia):
    pass

def getItems():
    data = []
    with open('storage/inventario.csv') as csvarchivo:
        entrada = csv.DictReader(csvarchivo)
        for reg in entrada:
            data.append([reg['referencia'] ,reg['nombre'], reg['precio']])
        csvarchivo.close()
    return data

def writeItems(data):
    try:
        archivo = open('storage/inventario.csv', 'w')
        header = ['referencia', 'nombre', 'precio']
        salida = csv.DictWriter(archivo, fieldnames=header)
        salida.writeheader()
        for item in data:
            salida.writerow({ 'referencia':item[0],
                              'nombre':item[1],
                              'precio':item[2]})

    finally:
        archivo.close()