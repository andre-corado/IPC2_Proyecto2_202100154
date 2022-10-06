from TDA import ListaEnlazada


class Cliente:
    def __init__(self, cui, nombre, app=False):
        self.id = cui
        self.nombre = nombre
        self.transacciones = ListaEnlazada()
        self.tiempoDeEspera = 0
        self.tiempoDeAtencion = 0
        self.generadoEnApp = app

    def agregarTransaccion(self, tiempoTrans, cantidad):
        self.tiempoDeAtencion += (tiempoTrans * cantidad)

    def notificarEnApp(self, escritorio):
        print(self.nombre + ' ha llegado su turno!\nPor favor dirigirse a escritorio Id: ' + escritorio.id)

    def ventanaEspera(self, numCliente, tiempoEspera, EsperaPromedio):
        print('Puesto en Fila: ' + str(numCliente) + "\nTiempo de Espera: " + str(tiempoEspera) +
              "\nTiempo de Espera Promedio: " + str(EsperaPromedio))
