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
        self.tiempoPromedioEspera = 0
        self.tiempoMaximoEspera = 0
        self.tiempoMinimoEspera = 0
        self.tiempoPromedioAtencion = 0
        self.tiempoMaximoAtencion= 0
        self.tiempoMinimoAtencion = 0

    def agregarEscritorio(self, escritorio):
        self.escritorios.insertar(escritorio)
        self.numEscritorios += 1

    def agregarCliente(self, cliente):
        self.cola.push(cliente)
        #Verificar si hay servidor disponible y atender

    def atenderCliente(self):
        # Obtener tiempo transcurrido del tiempo min  de los clientes en los servidores

        # Actualizar los tiempos de Atención

        #Verificar si se puede atender a más de un cliente
        clientePorAtender = self.cola.pop(tiempoTranscurrido=0)
        self.actualizarDataEspera(clientePorAtender.tiempoDeEspera)


    def activarEscritorio(self, idEscritorio):
        escritorio = self.escritorios.get(idEscritorio)
        if (escritorio is not None) and escritorio.activo is False:
            escritorio.estado = True
            self.numEscritoriosActivos += 1
            self.numEscritoriosInactivos = self.numEscritorios - self.numEscritoriosActivos
        else:
            print('No existe el escritorio o ya se encuentra activado.')

    def desactivarEscritorio(self, idEscritorio):
        escritorio = self.escritorios.get(idEscritorio)
        if (escritorio is not None) and escritorio.activo is True:
            escritorio.estado = False
            self.numEscritoriosActivos -= 1
            self.numEscritoriosInactivos = self.numEscritorios - self.numEscritoriosActivos

        else:
            print('No existe el escritorio o ya se encuentra desactivado.')

    def actualizarDataEspera(self, tiempoEsperaCliente):
        if tiempoEsperaCliente < self.tiempoMinimoEspera:
            self.tiempoMinimoEspera = tiempoEsperaCliente
        elif tiempoEsperaCliente > self.tiempoMaximoEspera:
            self.tiempoMaximoEspera = tiempoEsperaCliente

        self.sumaTiempoEspera += tiempoEsperaCliente
        self.numClientesLlegadosDeEspera += 1
        self.tiempoPromedioEspera = self.sumaTiempoEspera / self.numClientesLlegadosDeEspera


