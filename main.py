from tkinter import filedialog
from Empresa import Empresa
from Cliente import Cliente
from Transaccion import Transaccion
from PuntoDeAtencion import PuntoDeAtencion
from Escritorio import Escritorio
from TDA import *
from DataBase import DB
import os
import XML


def clearConsola():
    os.system('cls')


if __name__ == '__main__':
    menuPrin = ''
    empresaElegida = None
    puntoDeAtencionElegido = None
    while menuPrin != '4':
        clearConsola()
        menuPrin = menuSec = menuTer = ''
        while not (menuPrin == '1' or menuPrin == '2' or menuPrin == '3' or menuPrin == '4'):
            print('\t\t\tMENÚ PRINCIPAL\n1.\tConfiguración de Empresas\n2.\tSelección de empresa y punto de atención.\n'
                  '3.\tManejo de puntos de atención\n4.\tSalir\nElija una opción:\t')
            menuPrin = input()
        # Fin de ejecución de la Aplicación
        if menuPrin == '4':
            break
        # 1. CONFIGURACIÓN DE EMPRESAS
        elif menuPrin == '1':
            # Despliegue Menú Secundario
            while not (menuSec == '1' or menuSec == '2' or menuSec == '3' or menuSec == '4' or menuSec == '5'):
                clearConsola()
                print('1.\tLimpiar Sistema\n2.\tCargar archivo de configuración del sistema\n3.\tCargar archivo de '
                      'configuración inicial para la prueba\n4.\tAgregar Empresa/Escritorio/Transacción\n'
                      '5.\tRegresar al Menú Principal\nElija una opción:\t')
                menuSec = input()
                # Retorno a Menú Principal
                if menuSec == '5':
                    break
                # Limpieza del Sistema
                elif menuSec == '1':
                    DB.restart()
                    print('El sistema se ha limpiado exitosamente.\nPresione Enter para regresar.')
                    input()
                # Carga de Archivo de Configuración del Sistema
                elif menuSec == '2':
                    #ruta = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
                    #("XML files", "*.xml"), ("All files", "*.*")))
                    XML.cargarArchivoDeConfiguracionInicial('hola.xml')
                    print('El archivo ha sido cargado.\nPresione Enter para regresar al menú principal.')
                    input()
                # Carga de Archivo de Configuración Inicial para la Prueba
                elif menuSec == '3':
                    #ruta = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
                    #    ("XML files", "*.xml"), ("All files", "*.*")))
                    XML.cargarArchivoDeSimulacion('hola2.xml')
                    print('El archivo ha sido cargado.\nPresione Enter para regresar al menú principal.')
                    input()
                # Creación de Empresa/Escritorio/Transaccion
                elif menuSec == '4':
                    while not (menuTer == '1' or menuTer == '2' or menuTer == '3' or menuTer == '4' or menuTer == '5'):
                        clearConsola()
                        print('1.\tCrear Empresa\n2.\tCrear Punto de Atención\n3.\tCrear Escritorio de Servicio\n'
                              '4.\tCrear Transacción\n5.\tRegresar a Configuración de Empresas\nElija una opción:\t')
                        menuTer = input()
                        if menuTer == '5':
                            break
                        # Crear Empresa
                        elif menuTer == '1':
                            id = ''
                            while id == '':
                                clearConsola()
                                print('Ingrese el id de la Empresa:\n\t\t\t')
                                id = input()
                            nombre = ''
                            while nombre == '':
                                clearConsola()
                                print('Ingrese el nombre de la Empresa:\n\t\t\t')
                                nombre = input()
                            abrev = ''
                            while abrev == '':
                                clearConsola()
                                print('Ingrese la abreviatura de la Empresa:\n\t\t\t')
                                abrev = input()
                            empresa = Empresa(id, nombre, abrev)
                            DB.agregarEmpresa(empresa)
                            print("Empresa Creada")
                        # Crear Punto de Atención
                        elif menuTer == '2':
                            opcion = ''
                            clearConsola()
                            if DB.empresas.primero is None:
                                print('No existen empresas aún. Presione Enter para regresar.')
                                input()
                            else:
                                empresa = None
                                while empresa is None:
                                    try:
                                        print(DB.getEmpresas())
                                        print('Elija una empresa:\t\t')
                                        opcion = input()
                                        empresa = DB.empresas.getSlot(opcion)
                                    except:
                                        print('Debe de ingresar una opción válida.\nPresione Enter para intentar de '
                                              'nuevo.')
                                        input()
                                id = ''
                                while id == '':
                                    clearConsola()
                                    print('Ingrese el id del Punto de Atención:\n\t\t\t')
                                    id = input()
                                nombre = ''
                                while nombre == '':
                                    clearConsola()
                                    print('Ingrese el nombre del Punto de Atención:\n\t\t\t')
                                    nombre = input()
                                dir = ''
                                while dir == '':
                                    clearConsola()
                                    print('Ingrese la dirección del Punto de Atención:\n\t\t\t')
                                    dir = input()
                                puntodeatencion = PuntoDeAtencion(id, nombre, dir)
                                empresa.agregarPuntoDeAtencion(puntodeatencion)
                                print("Punto de Atención Creado")
                                input()
                        # Crear Escritorio
                        elif menuTer == '3':
                            opcion = ''
                            clearConsola()
                            if DB.empresas.primero is None:
                                print('No existen empresas aún. Presione Enter para regresar.')
                                input()
                            else:
                                empresa = None
                                while empresa is None:
                                    try:
                                        print(DB.getEmpresas())
                                        print('Elija una empresa:\t\t')
                                        opcion = input()
                                        empresa = DB.empresas.getSlot(opcion)
                                    except:
                                        print('Debe de ingresar una opción válida.\nPresione Enter para intentar de '
                                              'nuevo.')
                                        input()
                                opcion = ''
                                clearConsola()
                                if empresa.puntosDeAtencion.primero is None:
                                    print(
                                        'No existen puntos de atención aún en esta empresa. Presione Enter para regresar.')
                                    input()
                                else:
                                    puntodeatencion = None
                                    while puntodeatencion is None:
                                        try:
                                            print(empresa.getPuntosDeAtencion())
                                            print('Elija un punto de atención:\t\t')
                                            opcion = input()
                                            puntodeatencion = empresa.puntosDeAtencion.getSlot(opcion)
                                        except:
                                            print(
                                                'Debe de ingresar una opción válida.\nPresione Enter para intentar de '
                                                'nuevo.')
                                            input()
                                    id = ''
                                    while id == '':
                                        clearConsola()
                                        print('Ingrese el id del escritorio:\n\t\t\t')
                                        id = input()
                                    identificacion = ''
                                    while identificacion == '':
                                        clearConsola()
                                        print('Ingrese la identificación del escritorio:\n\t\t\t')
                                        identificacion = input()
                                    encargado = ''
                                    while encargado == '':
                                        clearConsola()
                                        print('Ingrese el encargado del escritorio:\n\t\t\t')
                                        encargado = input()
                                    escritorio = Escritorio(id, identificacion, encargado)
                                    puntodeatencion.agregarEscritorio(escritorio)
                                    print("Escritorio Creado")
                        # Crear Transacción
                        elif menuTer == '4':
                            opcion = ''
                            clearConsola()
                            if DB.empresas.primero is None:
                                print('No existen empresas aún. Presione Enter para regresar.')
                                input()
                            else:
                                empresa = None
                                while empresa is None:
                                    try:
                                        print(DB.getEmpresas())
                                        print('Elija una empresa:\t\t')
                                        opcion = input()
                                        empresa = DB.empresas.getSlot(opcion)
                                    except:
                                        print('Debe de ingresar una opción válida.\nPresione Enter para intentar de '
                                              'nuevo.')
                                        input()
                                id = ''
                                while id == '':
                                    clearConsola()
                                    print('Ingrese el id de la transacción:\n\t\t\t')
                                    id = input()

                                t = ''
                                while t == '':
                                    clearConsola()
                                    print('Ingrese el tiempo de la transacción:\n\t\t\t')
                                    t = input()
                                    try:
                                        t = int(t)
                                        if t <= 0:
                                            t = ''
                                    except:
                                        t = ''
                                        print('Debe de ingresar un número válido.\nPresione Enter para intentar de '
                                              'nuevo.')
                                        input()
                                transaccion = Transaccion(id, t)
                                empresa.agregarTransaccion(transaccion)
                            print("Transacción Creada")
        # SELECCIÓN DE EMPRESA Y PUNTO DE ATENCIÓN
        elif menuPrin == '2':
            if DB.empresas.primero is None:
                print('No existen empresas aún. Presione Enter para regresar.')
                input()
            else:
                clearConsola()
                empresa = None
                while empresa is None:
                    try:
                        print(DB.getEmpresas())
                        print('Elija una empresa:\t\t')
                        opcion = input()
                        empresa = DB.empresas.getSlot(opcion)
                    except:
                        print('Debe de ingresar una opción válida.\nPresione Enter para intentar de '
                              'nuevo.')
                        input()
                clearConsola()
                if empresa.puntosDeAtencion.primero is None:
                    print('No existen puntos de atención aún en esta empresa. Presione Enter para regresar.')
                    input()
                else:
                    puntodeatencion = None
                    while puntodeatencion is None:
                        try:
                            print(empresa.getPuntosDeAtencion())
                            print('Elija un punto de atención:\t\t')
                            opcion = input()
                            puntodeatencion = empresa.puntosDeAtencion.getSlot(opcion)
                        except:
                            print('Debe de ingresar una opción válida.\nPresione Enter para intentar de '
                                  'nuevo.')
                            input()
                    empresaElegida = empresa
                    puntoDeAtencionElegido = puntodeatencion
                    print('Se ha escogido el punto de atención exitosamente.')
                    print('Presione Enter para regresar al Menú principal.')
                    input()

        # MANEJO DE PUNTOS DE ATENCIÓN
        elif menuPrin == '3':
            # Despliegue Menú Secundario
            while not (menuSec == '1' or menuSec == '2' or menuSec == '3' or menuSec == '4'
                       or menuSec == '5' or menuSec == '6' or menuSec == '7'):
                clearConsola()
                print('1.\tVer estado del punto de atención\n2.\tActivar escritorio\n3.\tDesactivar Escritorio\n'
                      '4.\tAtender Cliente\n5.\tSolicitud de Atención\n6.\tSimular actividad del punto de atención\n'
                      '7.\tRegresar al Menú Principal\nElija una opción:\t')
                menuSec = input()
                # Retorno a Menú Principal
                if menuSec == '7':
                    break
                # Ver estado del punto de atención
                elif menuSec == '1':
                    if puntoDeAtencionElegido is None:
                        print("No se ha elegido algún punto de atención aún.")
                    else:
                        puntoDeAtencionElegido.printEstado()
                    print('\nPresione Enter para regresar.')
                    input()
                # Activar Escritorio
                elif menuSec == '2':
                    if empresaElegida is None:
                        print("No se ha elegido alguna empresa aún.")
                    else:
                        if puntoDeAtencionElegido is None:
                            print("No se ha elegido algún punto de atención aún.")
                        else:
                            if not puntoDeAtencionElegido.activarEscritorio():
                                print('No hay escritorios por activar.')
                    print('\nPresione Enter para regresar.')
                    input()
                # Desactivar Escritorio
                elif menuSec == '3':
                    if empresaElegida is None:
                        print("No se ha elegido alguna empresa aún.")
                    else:
                        if puntoDeAtencionElegido is None:
                            print("No se ha elegido algún punto de atención aún.")
                        else:
                            if not puntoDeAtencionElegido.desactivarEscritorio():
                                print('No hay escritorios por desactivar.')
                    print('\nPresione Enter para regresar.')
                    input()
                # Atender Cliente
                elif menuSec == '4':
                    if empresaElegida is None:
                        print("No se ha elegido alguna empresa aún.")
                    else:
                        if puntoDeAtencionElegido is None:
                            print("No se ha elegido algún punto de atención aún.")
                        else:
                            puntoDeAtencionElegido.atenderCliente()
                    print('\nPresione Enter para regresar.')
                    input()
                # Solicitud de Atención
                elif menuSec == '5':
                    if empresaElegida is None:
                        print("No se ha elegido alguna empresa aún.")
                    else:
                        if puntoDeAtencionElegido is None:
                            print("No se ha elegido algún punto de atención aún.")
                        else:
                            id = nombre = ''
                            while id == '':
                                clearConsola()
                                print('Ingrese su número de dpi:\n\t\t\t')
                                id = input()
                            while nombre == '':
                                clearConsola()
                                print('Ingrese su nombre:\n\t\t\t')
                                nombre = input()
                            clienteNuevo = Cliente(id, nombre, True)

                            if empresaElegida.transacciones.primero is None:
                                print('No existen transacciones aún en la empresa elegida. Presione Enter para regresar.')
                                input()
                            else:
                                continuar = False
                                while not continuar:
                                    clearConsola()
                                    trans = None
                                    while trans is None:
                                        try:
                                            print(DB.getTransacciones())
                                            print('Ingrese 0 para continuar')
                                            print('Elija una transacción:\t\t')
                                            opcion = input()
                                            if opcion == '0':
                                                continuar = True
                                                break
                                            trans = empresaElegida.transacciones.getSlot(opcion)
                                            print('Ingrese la cantidad deseada:')
                                            cantidad = int(input())
                                            clienteNuevo.agregarTransaccion(trans.tiempoAtencion, cantidad)
                                        except:
                                            print('Debe de ingresar una opción válida.\nPresione Enter para intentar de '
                                                  'nuevo.')
                                            input()
                                puntoDeAtencionElegido.agregarClienteApp(clienteNuevo)



                    print('\nPresione Enter para regresar.')
                    input()
                # Simular Actividad del Punto de Atención
                elif menuSec == '6':
                    print('Atención Simulada')
