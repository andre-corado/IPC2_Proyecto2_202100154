from TDA import ListaEnlazada
class Empresa:
    def __init__(self, id, nombre, abrev):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abrev
        self.puntosDeAtencion = ListaEnlazada()
        self.transacciones = ListaEnlazada()

    def agregarPuntoDeAtencion(self, puntoDeAtencion):
        self.puntosDeAtencion.insertar(puntoDeAtencion)

    def agregarTransaccion(self, transaccion):
        self.transacciones.insertar(transaccion)

    def getPuntosDeAtencion(self):
        if self.puntosDeAtencion.primero is None:
            return None
        else:
            txt = ''
            actual = self.puntosDeAtencion.primero
            while actual is not None:
                txt += str(actual.id) + '.\tId: ' + actual.dato.id + '\tNombre: ' + actual.dato.nombre + '\n'
                actual = actual.siguiente
            return txt

    def getPunto(self, idPunto):
        punto = None
        actual = self.puntosDeAtencion.primero
        while actual:
            if actual.dato.id == str(idPunto):
                punto = actual.dato
                break
            actual = actual.siguiente
        return punto

    def getTrans(self, idTrans):
        transaccion = None
        actual = self.transacciones.primero
        while actual:
            if actual.dato.id == str(idTrans):
                transaccion = actual.dato
                break
            actual = actual.siguiente
        return transaccion