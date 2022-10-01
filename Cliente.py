from TDA import ListaEnlazada
class Cliente:
    def __init__(self, transacciones, cui, nombre):
        self.transacciones = transacciones
        self.id = cui
        self.nombre = nombre
        self.transacciones = ListaEnlazada()
        self.tiempoDeEspera = 0
        self.tiempoDeAtencion = 0

    def agregarTransaccion(self, idTrans, cantidad):
        transaccion = self.transacciones.get(idTrans)
        if transaccion:
            tiempoTrans = transaccion.tiempoAtencion
            self.tiempoDeAtencion += (tiempoTrans * cantidad)
        else:
            print('No existe la transacción: ' + idTrans)
