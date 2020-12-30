#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extensión del Software ShopiSell: Clientes
#       Esta extensión, proporciona al programa un sistema de control de clientes. Todos estos datos los almacena en un fichero 
#       denominado "clientes", localizable en la carpeta storage del programa.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import csv
import tkinter as tk


def addCliente(documento, nombre, telefono, email):
    data = getClientes()

    data.append([documento, nombre, telefono, email])

    writeClientes(data)

def delCliente(id):
    data = getClientes()

    data.pop(id)

    writeClientes(data)

def findCliente(id):
    data = getClientes()
    if id > len(data) or id < 0:
        return None
    else:
        return data[id]

def getClientes():
    data = []
    with open('storage/clientes.csv') as csvarchivo:
        entrada = csv.DictReader(csvarchivo)
        for reg in entrada:
            data.append([reg['documento'], reg['nombre'], reg['telefono'], reg['email']])
        csvarchivo.close()
    return data

def writeClientes(data):
    try:
        archivo = open('storage/clientes.csv', 'w')
        header = ['documento', 'nombre','telefono', 'email']
        salida = csv.DictWriter(archivo, fieldnames=header)
        salida.writeheader()
        for cliente in data:
            salida.writerow({ 'documento':cliente[0],
                              'nombre':cliente[1],
                              'telefono':cliente[2],
                              'email':cliente[3]})

    finally:
        archivo.close()


