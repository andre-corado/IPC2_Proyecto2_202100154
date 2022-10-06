import xml.etree.ElementTree as ET
from Empresa import Empresa
from Cliente import Cliente
from Transaccion import Transaccion
from PuntoDeAtencion import PuntoDeAtencion
from Escritorio import Escritorio
from DataBase import DB


def cargarArchivoDeConfiguracionInicial(ruta):
    tree = ET.parse(ruta)
    listaEmpresas = tree.getroot()
    # Por cada empresa
    for empresa in listaEmpresas.findall('empresa'):
        idEmpresa = empresa.attrib['id']
        nombreEmpresa = empresa.find('nombre').text
        abrevEmpresa = empresa.find('abreviatura').text
        nuevaEmpresa = Empresa(idEmpresa, nombreEmpresa, abrevEmpresa)

        listaPA = empresa.find('listaPuntosAtencion')
        for PA in listaPA.findall('puntoAtencion'):
            idPA = PA.attrib['id']
            nombrePA = PA.find('nombre').text
            dirPA = PA.find('direccion').text
            nuevoPA = PuntoDeAtencion(idPA, nombrePA, dirPA)
            nuevaEmpresa.agregarPuntoDeAtencion(nuevoPA)

            listaEscritorios = PA.find('listaEscritorios')
            for escritorio in listaEscritorios.findall('escritorio'):
                idEscritorio = escritorio.attrib['id']
                identificacion = escritorio.find('identificacion').text
                encargado = escritorio.find('encargado').text
                nuevoEscritorio = Escritorio(idEscritorio, identificacion, encargado)
                nuevoPA.agregarEscritorio(nuevoEscritorio)

        listaTrans = empresa.find('listaTransacciones')
        for transTag in listaTrans.findall('transaccion'):
            idTrans = transTag.attrib['id']
            nombre = transTag.find('nombre').text
            tiempo = transTag.find('tiempoAtencion').text
            transaccion = Transaccion(idTrans, nombre, tiempo)
            nuevaEmpresa.agregarTransaccion(transaccion)

        DB.agregarEmpresa(nuevaEmpresa)


def cargarArchivoDeSimulacion(ruta):
    tree = ET.parse(ruta)
    listadoInicial = tree.getroot()
    for configInicial in tree.findall('configInicial'):
        idConfig = configInicial.attrib['id']
        idEmpresa = configInicial.attrib['idEmpresa']
        idPunto = configInicial.attrib['idPunto']

        empresa = DB.getEmpresa(idEmpresa)
        if empresa:
            punto = empresa.getPunto(idPunto)
            if punto:
                escritoriosActivos = configInicial.find('escritoriosActivos')
                for escritorioTag in escritoriosActivos.findall('escritorio'):
                    idEscritorio = escritorioTag.attrib['idEscritorio']
                    escritorio = punto.getEscritorio(idEscritorio)
                    if escritorio:
                        punto.activarEscritorioEspecifico(escritorio)
                    else:
                        print('ERROR EN CONFIGURACIÓN ID: ' + idConfig + '\nNo existe el escritorio con el id: '
                              + idEscritorio)
                listadoClientes = configInicial.find('listadoClientes')
                for clienteTag in listadoClientes.findall('cliente'):
                    dpi = clienteTag.attrib['dpi']
                    nombre = clienteTag.find('nombre').text
                    listadoTransacciones = clienteTag.find('listadoTransacciones')
                    cliente = Cliente(dpi, nombre)
                    for transaccionTag in listadoTransacciones.findall('transaccion'):
                        idTrans = transaccionTag.attrib['idTransaccion']
                        cantidad = int(transaccionTag.attrib['cantidad'])
                        transaccion = empresa.getTrans(idTrans)
                        if transaccion:
                            if cantidad > 0:
                                cliente.agregarTransaccion(transaccion.tiempoAtencion, cantidad)
                                print('La transacción id: ' + idTrans + ', ha sido añadida a ' + nombre)
                            else:
                                print('ERROR EN CONFIGURACIÓN ID: ' + idConfig + '\nEn cliente: ' + nombre +
                                      'La cantidad debe ser mayor a 0 en la Transacción id: ' + idTrans)
                        else:
                            print('ERROR EN CONFIGURACIÓN ID: ' + idConfig + '\nEn cliente: ' + nombre +
                                  'No existe la transacción id: ' + idTrans)
                    punto.agregarCliente(cliente)
                    print('El cliente ' + nombre + ' ha sido agregado a la cola en el punto de atención ' +
                          punto.nombre + '\n')
                punto.pasarClientesAEscritorios()

            else:
                print(
                    'ERROR EN CONFIGURACIÓN ID: ' + idConfig + '\nNo existe el punto de atención con el id: ' + idPunto)

        else:
            print('ERROR EN CONFIGURACIÓN ID: ' + idConfig + '\nNo existe la empresa con el id: ' + idEmpresa)
