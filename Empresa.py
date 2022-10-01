from TDA import ListaEnlazada
class Empresa:
    def __init__(self, id, nombre, abrev):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abrev
        self.puntosDeAtencion = ListaEnlazada()

    def agregarPuntoDeAtencion(self, puntoDeAtencion):
        self.puntosDeAtencion.insertar(puntoDeAtencion)
