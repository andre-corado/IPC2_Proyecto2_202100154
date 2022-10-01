from TDA import ListaEnlazada
import os


class DataBase:
    def __init__(self):
        self.empresas = ListaEnlazada()

    def agregarEmpresa(self, empresa):
        self.empresas.insertar(empresa)


def clearConsola():
    os.system('cls')


if __name__ == '__main__':
    DB = DataBase()
    menuPrin = ''
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
                    DB = DataBase()
                    print('El sistema se ha limpiado exitosamente.\nPresione Enter para regresar.')
                    input()
                # Carga de Archivo de Configuración del Sistema
                elif menuSec == '2':
                    print('El archivo ha sido cargado.\nPresione Enter para regresar al menú principal.')
                    input()
                # Carga de Archivo de Configuración Inicial para la Prueba
                elif menuSec == '3':
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
                            print("Empresa Creada")
                        # Crear Punto de Atención
                        elif menuTer == '2':
                            print("Punto de Atención Creado")
                        # Crear Escritorio
                        elif menuTer == '3':
                            print("Escritorio Creado")
                        # Crear Transacción
                        elif menuTer == '4':
                            print("Transacción Creada")
        # SELECCIÓN DE EMPRESA Y PUNTO DE ATENCIÓN
        elif menuPrin == '2':
            # Elegir Empresa
            # Elegir Punto de Atención
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
                    print('ESTADO PUNTO.\nPresione Enter para regresar.')
                    input()
                # Activar Escritorio
                elif menuSec == '2':
                    print('Escritorio Activado')
                # Desactivar Escritorio
                elif menuSec == '3':
                    print('Escritorio Desactivado')
                # Atender Cliente
                elif menuSec == '4':
                    print('Cliente atendido')
                # Solicitud de Atención
                elif menuSec == '5':
                    print('Será atendido pronto')
                # Simular Actividad del Punto de Atención
                elif menuSec == '6':
                    print('Atención Simulada')
