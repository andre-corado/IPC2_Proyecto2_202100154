import os
import webbrowser

from TDA import *


class PuntoDeAtencion:
    def __init__(self, id, nombre, direccion):
        self.primeraVez = True
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
        self.sumaTiempoAtencion = 0
        self.numClientesAtendidos = 0

    def agregarEscritorio(self, escritorio):
        self.escritorios.insertar(escritorio)
        self.numEscritorios += 1

    def agregarCliente(self, cliente):
        self.cola.push(cliente)

    def agregarClienteApp(self, cliente):
        escritorio = None
        actual = self.escritoriosActivos.primero
        while actual:
            if actual.dato.disponible:
                escritorio = actual.dato
            actual = actual.siguiente

        if escritorio:
            self.cola.push(cliente)
            self.pasarClienteAEscritorio(escritorio)
            escritorio.cliente.notificarEnApp(escritorio)
            self.actualizarDataEspera(escritorio.cliente.tiempoDeEspera)
        else:
            numCliente = self.cola.len
            tiempoAEsperar = self.cola.tiempoDeEsperaAcumulado
            esperaProm = self.tiempoPromedioEspera
            self.cola.push(cliente)
            cliente.ventanaEspera(numCliente, tiempoAEsperar, esperaProm)



    def getMinTiempoAtencion(self):
        if self.escritoriosActivos.primero:
            tiempoMin = None
            actual = self.escritoriosActivos.primero
            while actual:
                if actual.dato.cliente:
                    tiempoPendiente = actual.dato.tiempoPendiente
                    if tiempoMin is None:
                        tiempoMin = tiempoPendiente
                    if tiempoPendiente < tiempoMin:
                        tiempoMin = tiempoPendiente
                actual = actual.siguiente
            return tiempoMin
        else:
            return None

    def atenderCliente(self):
        # Obtener tiempo transcurrido del tiempo min  de los clientes en los servidores
        tiempo = self.getMinTiempoAtencion()
        if tiempo:
            actual = self.escritoriosActivos.primero
            self.cola.actualizarTiemposdeEspera(tiempo)
            while actual:
                escritorio = actual.dato
                if escritorio.cliente:
                    escritorio.tiempoPendiente -= tiempo
                    if escritorio.tiempoPendiente == 0:
                        self.sumaTiempoAtencion += escritorio.cliente.tiempoDeAtencion
                        print('El cliente ' + escritorio.cliente.nombre + ' ha sido atendido.')
                        escritorio.atenderCliente()
                        self.numClientesAtendidos += 1
                        self.actualizarDataAtencion(escritorio)
                        if self.cola.primero:
                            self.pasarClienteAEscritorio(escritorio)
                            if escritorio.cliente.generadoEnApp:
                                escritorio.cliente.notificarEnApp(escritorio)
                            self.actualizarDataEspera(escritorio.cliente.tiempoDeEspera)
                            print('Por favor ' + escritorio.cliente.nombre + ', pasar a escritorio Id: ' + escritorio.id)
                        else:
                            escritorio.disponible = True
                            print('No hay más clientes en cola para llamar.')
                actual = actual.siguiente
            if self.cola.primero:
                self.cola.actualizarTiemposdeEspera(tiempo)
            self.primeraVez = False
        else:
            print('No hay escritorios activos o clientes por atender.')

        # Actualizar los tiempos de Atención


    def activarEscritorio(self):
        escritorio = None
        actual = self.escritorios.primero
        while actual:
            if actual.dato.activo is False:
                escritorio = actual.dato
                break
            actual = actual.siguiente

        if escritorio is not None:
            self.activarEscritorioEspecifico(escritorio)
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
        escritorio = self.escritoriosActivos.pop()
        if escritorio:
            escritorio.activo = False
            escritorio.disponible = True
            escritorio.cliente = None
            escritorio.tiempoPendiente = None
            self.numEscritoriosActivos -= 1
            self.numEscritoriosInactivos = self.numEscritorios - self.numEscritoriosActivos
            print('Escritorio ID: ' + escritorio.id + ' ha sido desactivado.')
            return True
        else:
            return False

    def actualizarDataEspera(self, tiempoEsperaCliente):
        if self.tiempoMinimoEspera == 0:
            self.tiempoMinimoEspera = tiempoEsperaCliente
        if tiempoEsperaCliente < self.tiempoMinimoEspera:
            self.tiempoMinimoEspera = tiempoEsperaCliente
        elif tiempoEsperaCliente > self.tiempoMaximoEspera:
            self.tiempoMaximoEspera = tiempoEsperaCliente

        self.sumaTiempoEspera += tiempoEsperaCliente
        self.numClientesLlegadosDeEspera += 1
        self.tiempoPromedioEspera = self.sumaTiempoEspera / self.numClientesLlegadosDeEspera

    def actualizarDataAtencion(self, escritorio):
        if self.escritoriosActivos.primero:
            actual = self.escritoriosActivos.primero
            while actual:
                escritorio = actual.dato
                if self.tiempoMinimoAtencion == 0:
                    self.tiempoMinimoAtencion = escritorio.tiempoMinimoAtencion
                if escritorio.tiempoMinimoAtencion < self.tiempoMinimoAtencion:
                    self.tiempoMinimoAtencion = escritorio.tiempoMinimoAtencion
                elif escritorio.tiempoMaximoAtencion > self.tiempoMaximoAtencion:
                    self.tiempoMaximoAtencion = escritorio.tiempoMaximoAtencion

                self.tiempoPromedioAtencion = (self.sumaTiempoAtencion / self.numClientesAtendidos)
                actual = actual.siguiente

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

    def pasarClienteAEscritorio(self, escritorio):
        cliente = self.cola.pop()
        self.actualizarDataEspera(cliente.tiempoDeEspera)
        escritorio.asignarCliente(cliente)

    def pasarClientesAEscritorios(self):
        actual = self.escritoriosActivos.primero
        while actual:
            if actual.dato.activo:
                if self.cola.primero:
                    cliente = self.cola.pop()
                    actual.dato.asignarCliente(cliente)
            actual = actual.siguiente

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
            while actual is not None:
                i += 1
                actual.dato.printEstado(i)
                actual = actual.siguiente
        self.graficar()

    def graficar(self):
        actual = self.escritorios.primero
        graphviz = 'digraph Patron{ \n node[shape = box  fillcolor="#FFEDBB" style=filled]; \n subgraph Cluster_A{ \n label = "' + self.id + " - " + self.nombre + '"   \n fontcolor ="black" \n fontsize = 41 \n bgcolor ="#c6e2e9" \n'
        graphviz += 'edge[dir="none" style=invisible]'
        graphviz += 'node' + str(
            1) + '[label = "' + 'Escritorio más próximo fue el primero en activarse.' + '" fontcolor = "black" fontsize = 20 fillcolor = "#a7bed3" style = filled]; \n'

        noOrden = 2
        if actual is None:
            graphviz += 'node' + str(
                noOrden) + '[label = "' + 'No hay escritorios aún ' + '" fontcolor = "black" fontsize = 20 fillcolor = "#a7bed3" style = filled]; \n'

        while actual:
            escritorio = actual.dato
            graphviz += 'node' + str(noOrden) + '[label = "' + "Escritorio" + str(
                noOrden-1) + '\n________________________________________________________________\n' + '\nId: ' + escritorio.id + ' | Tiempo Pendiente: ' + str(
                escritorio.tiempoPendiente) + 'Mín Atención: ' + str(escritorio.tiempoMinimoAtencion) +'min | Máx Atención: ' + \
                        str(escritorio.tiempoMaximoAtencion) +'Promedio Atención: ' + str(escritorio.tiempoPromedioAtencion) + 'min' '" fontcolor = "black" fontsize = 20 fillcolor = "#a7bed3" style = filled]; \n'
            actual = actual.siguiente
            noOrden += 1
        m = 1
        a = 2
        for h in range(noOrden - 2):
            graphviz += 'node{}->node{} \n'.format(m, a)
            m += 1
            a += 1

        graphviz += '} \n}'

        document = 'ArchivoAuxiliarGraphViz' + '.txt'
        with open(document, 'w') as grafica:
            grafica.write(graphviz)

        item = 1
        nombre = 'grafica'
        if item == 1:
            jpg = 'OrdenAgregada_' + nombre + '.jpg'
            os.system("dot.exe -Tjpg " + document + " -o " + jpg)
            webbrowser.open(jpg)


