from TDA import ListaEnlazada
class Cliente:
    def __init__(self, cui, nombre):
        self.id = cui
        self.nombre = nombre
        self.transacciones = ListaEnlazada()
        self.tiempoDeEspera = 0
        self.tiempoDeAtencion = 0

    def agregarTransaccion(self, tiempoTrans, cantidad):
        self.tiempoDeAtencion += (tiempoTrans * cantidad)

