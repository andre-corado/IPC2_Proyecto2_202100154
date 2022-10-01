class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, objeto):
        if self.primero is None:
            self.primero = Nodo(dato=objeto)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=objeto)

    def get(self, id):
        if self.primero is None:
            return None
        else:
            actual = self.primero
            while actual:
                if actual.id == id:
                    return actual
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
            self.tiempoDeEsperaAcumulado += self.primero.dato.tiempoDedato
            self.len += 1
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(dato=objeto)
            self.len += 1
            self.tiempoDeEsperaAcumulado += actual.siguiente.dato.tiempoDedato

    def pop(self, tiempoTranscurrido):
        if self.primero is not None:
            primerNodo = self.primero
            self.primero = self.primero.siguiente
            primerNodo.siguiente = None
            self.tiempoDeEsperaAcumulado -= primerNodo.dato.tiempoDedato
            if self.primero:
                self.actualizarTiemposdeEspera(tiempoTranscurrido)
            self.len -= 1
            return primerNodo
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
            print(f'\nNombre: {dato.nombre}\t\t\tCantidad de Shucos:{str(dato.cantidadShucos)}')
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
