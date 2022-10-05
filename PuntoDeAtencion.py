from TDA import *


class PuntoDeAtencion:
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.numClientesLlegadosDeEspera = 0
        self.sumaTiempoEspera = 0
        self.numEscritorios = 0
        self.numEscritoriosActivos = 0
        self.numEscritoriosInactivos = 0
        self.numClientesEnEspera = 0
        self.cola = Cola()
        self.escritorios = ListaEnlazada()
        self.escritoriosActivos = Pila()
        self.tiempoPromedioEspera = 0
        self.tiempoMaximoEspera = 0
        self.tiempoMinimoEspera = 0
        self.tiempoPromedioAtencion = 0
        self.tiempoMaximoAtencion = 0
        self.tiempoMinimoAtencion = 0

    def agregarEscritorio(self, escritorio):
        self.escritorios.insertar(escritorio)
        self.numEscritorios += 1

    def agregarCliente(self, cliente):
        self.cola.push(cliente)
        # Verificar si hay servidor disponible y atender

    def atenderCliente(self):
        # Obtener tiempo transcurrido del tiempo min  de los clientes en los servidores

        # Actualizar los tiempos de Atención

        # Verificar si se puede atender a más de un cliente
        clientePorAtender = self.cola.pop(tiempoTranscurrido=0)
        self.actualizarDataEspera(clientePorAtender.tiempoDeEspera)

    def activarEscritorio(self):
        escritorio = None
        actual = self.escritorios.primero
        while actual:
            if not actual.dato.activo:
                escritorio = actual.dato
                break
            actual = actual.siguiente

        if escritorio:
            escritorio.activo = True
            self.escritoriosActivos.push(escritorio)
            self.numEscritoriosActivos += 1
            self.numEscritoriosInactivos = self.numEscritorios - self.numEscritoriosActivos
            print('El escritorio ' + escritorio.id + ' ha sido activado.')
            return True
        else:
            return False

    def activarEscritorioEspecifico(self, escritorio):
        if escritorio:
            escritorio.activo = True
            self.escritoriosActivos.push(escritorio)
            self.numEscritoriosActivos += 1
            self.numEscritoriosInactivos = self.numEscritorios - self.numEscritoriosActivos
            print('El escritorio ' + escritorio.id + ' ha sido activado.')
        else:
            print('No existe el escritorio.')

    def desactivarEscritorio(self):
        escritorio = self.escritoriosActivos.pop
        if escritorio:
            escritorio.activo = False
            self.numEscritoriosActivos -= 1
            self.numEscritoriosInactivos = self.numEscritorios - self.numEscritoriosActivos
            return True
        else:
            return False

    def actualizarDataEspera(self, tiempoEsperaCliente):
        if tiempoEsperaCliente < self.tiempoMinimoEspera:
            self.tiempoMinimoEspera = tiempoEsperaCliente
        elif tiempoEsperaCliente > self.tiempoMaximoEspera:
            self.tiempoMaximoEspera = tiempoEsperaCliente

        self.sumaTiempoEspera += tiempoEsperaCliente
        self.numClientesLlegadosDeEspera += 1
        self.tiempoPromedioEspera = self.sumaTiempoEspera / self.numClientesLlegadosDeEspera

    def getEscritorio(self, idEscritorio):
        escritorio = None
        actual = self.escritorios.primero
        while actual:
            if actual.dato.id == str(idEscritorio):
                escritorio = actual.dato
                break
            actual = actual.siguiente
        return escritorio

    def getEscritorios(self):
        if self.escritorios.primero is None:
            return None
        else:
            txt = ''
            actual = self.escritorios.primero
            while actual is not None:
                txt += str(actual.id) + '.\tId: ' + actual.dato.id + '\tIdentificación: ' + actual.dato.identificacion \
                       + '\n'
                actual = actual.siguiente
            return txt

    def printEstado(self):
        print("\n\t\t\t\t\t\tPUNTO DE ATENCIÓN:\t " + self.nombre + "\nId: " + self.id + "\t\tDirección: " +
              self.direccion + "\n\nEscritorios Activos: " + str(self.numEscritoriosActivos) +
              "\t\tEscritorios Inactivos: " + str(self.numEscritoriosInactivos) + "\nClientes en Espera: " +
              str(self.numClientesEnEspera) + "\n\nTiempo Prom. de Espera: " + str(self.tiempoPromedioEspera) +
              "\t\tTiempo Máx. de Espera: " + str(self.tiempoMaximoEspera) + "\t\tTiempo Mín. de Espera: " +
              str(self.tiempoMinimoEspera) + "\nTiempo Prom. de Atención: " + str(self.tiempoPromedioAtencion) +
              "\t\tTiempo Máx. de Atención: " + str(self.tiempoMaximoAtencion) + "\t\tTiempo Mín. de Atención: " +
              str(self.tiempoMinimoAtencion))
        print("__________________________________________________________________________\n"
              "\t\t\t\t\t\t\nESCRITORIOS ACTIVOS:")
        if self.numEscritoriosActivos == 0:
            print("Ningún escritorio activo aún.")
        else:
            if self.numEscritoriosActivos > 1:
                print("El número mayor fue el último en activarse.\n")
            i = 0
            actual = self.escritoriosActivos.primero
            while actual:
                i += 1
                actual.dato.printEstado(i)
                actual = actual.siguiente
