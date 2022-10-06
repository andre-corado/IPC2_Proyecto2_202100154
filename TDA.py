class Nodo:
    def __init__(self, dato=None, siguiente=None, id=None):
        self.id = id
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.len = 0

    def insertar(self, objeto):
        self.len += 1
        if self.primero is None:
            self.primero = Nodo(dato=objeto, id=self.len)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=objeto, id=self.len)

    def get(self, id):
        if self.primero is None:
            return None
        else:
            actual = self.primero
            while actual:
                if actual.dato.id == id:
                    return actual.dato
                actual = actual.siguiente
            return None

    def getSlot(self, idSlot):
        if self.primero is None:
            return None
        else:
            actual = self.primero
            while actual:
                if actual.id == int(idSlot):
                    return actual.dato
                actual = actual.siguiente
            return None


class Pila:
    def __init__(self):
        self.primero = None

    def push(self, objeto):
        if self.primero is None:
            self.primero = Nodo(dato=objeto)
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(dato=objeto)

    def pop(self):
        if self.primero is None:
            return None
        else:
            if self.primero.siguiente is None:
                primero = self.primero.dato
                self.primero = None
                return primero
            actual = self.primero
            anterior = None
            while actual and actual.siguiente:
                anterior = actual
                actual = actual.siguiente
                anterior.siguiente = None
                return actual.dato

    def get(self, id):
        if self.primero is None:
            return None
        else:
            actual = self.primero
            while actual:
                if actual.dato.id == id:
                    return actual.dato
                actual = actual.siguiente
            return None


class Cola:
    def __init__(self):
        self.primero = None
        self.tiempoDeEsperaAcumulado = 0
        self.len = 0

    def push(self, objeto):
        if self.primero is None:
            self.primero = Nodo(dato=objeto)
            self.tiempoDeEsperaAcumulado += self.primero.dato.tiempoDeAtencion
            self.len += 1
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(dato=objeto)
            self.len += 1
            self.tiempoDeEsperaAcumulado += actual.siguiente.dato.tiempoDeAtencion

    def pop(self):
        if self.primero is not None:
            primerNodo = self.primero
            self.primero = self.primero.siguiente
            primerNodo.siguiente = None
            self.tiempoDeEsperaAcumulado -= primerNodo.dato.tiempoDeAtencion
            self.len -= 1
            return primerNodo.dato
        else:
            return None

    def print(self):
        if self.primero is None:
            print('No existen clientes aún.\nPresione Enter para regresar.')
            input()
            return
        j = 1
        actual = self.primero
        while actual:
            print('___________________________________________________________________________________')
            print('\n\n\t\t\tCliente NO. ' + str(j))
            dato = actual.dato
            print(f'\nNombre: {dato.nombre}\t\t\tTiempo en Espera:{str(dato.tiempoDeEspera)}')
            i = 1
            actual = actual.siguiente
        print('___________________________________________________________________________________')
        print('\n\nPresione Enter para regresar.')

    def actualizarTiemposdeEspera(self, tiempoTranscurrido):
        # Actualización de Tiempo de Espera
        actual = self.primero
        while actual:
            actual.dato.tiempoDeEspera += tiempoTranscurrido
            actual = actual.siguiente
