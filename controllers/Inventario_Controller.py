#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extensión del Software ShopiSell: Inventario
#       
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import csv
import tkinter as tk



def addItem(name, price):
    data = getItems()

    data.append([name, price])

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

def getItems():
    data = []
    with open('storage/inventario.csv') as csvarchivo:
        entrada = csv.DictReader(csvarchivo)
        for reg in entrada:
            data.append([reg['nombre'], reg['precio']])
        csvarchivo.close()
    return data

def writeItems(data):
    try:
        archivo = open('storage/campos.csv', 'w')
        header = ['nombre', 'precio']
        salida = csv.DictWriter(archivo, fieldnames=header)
        salida.writeheader()
        for item in data:
            salida.writerow({ 'nombre':item[0],
                              'precio':item[1]})

    finally:
        archivo.close()

