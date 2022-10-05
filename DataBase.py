from TDA import ListaEnlazada


class DataBase:
    def __init__(self):
        self.empresas = ListaEnlazada()

    def agregarEmpresa(self, empresa):
        self.empresas.insertar(empresa)

    def getEmpresas(self):
        if self.empresas.primero is None:
            return None
        else:
            txt = ''
            actual = self.empresas.primero
            while actual is not None:
                txt += str(actual.id) + '.\tId: ' + actual.dato.id + '\tNombre: ' + actual.dato.nombre + '\n'
                actual = actual.siguiente
            return txt

    def restart(self):
        self.empresas.primero = None

    def getEmpresa(self, idEmpresa):
        empresa = None
        actual = self.empresas.primero
        while actual:
            if actual.dato.id == str(idEmpresa):
                empresa = actual.dato
                break
            actual = actual.siguiente
        return empresa


DB = DataBase()
