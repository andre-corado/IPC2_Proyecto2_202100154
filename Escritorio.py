class Escritorio:
    def __init__(self, id, identificacion, encargado):
        self.activo = False
        self.disponible = True
        self.id = id
        self.identificacion = identificacion
        self.encargado = encargado
        self.tiempoPromedioAtencion = 0
        self.tiempoMaximoAtencion = 0
        self.tiempoMinimoAtencion = 0
        self.sumaTiempoAtencion = 0
        self.numPersonasAtendidas = 0
        self.cliente = None

    def asignarCliente(self, cliente):
        self.cliente = cliente
        self.disponible = False

    def atenderCliente(self):
        tiempoDeAtencion = self.cliente.tiempoDeAtencion
        if tiempoDeAtencion < self.tiempoMinimoAtencion:
            self.tiempoMinimoAtencion = tiempoDeAtencion
        elif tiempoDeAtencion > self.tiempoMaximoAtencion:
            self.tiempoMaximoAtencion = tiempoDeAtencion
        self.sumaTiempoAtencion += tiempoDeAtencion
        self.numPersonasAtendidas += 1
        self.tiempoPromedioAtencion = self.sumaTiempoAtencion / self.numPersonasAtendidas
        self.disponible = True

    def printEstado(self, no):
        print("----------------------------------------------------------------------\n\t\t\t\t\t\tESCRITORIO No. "
              + str(no) + self.id + "\nIdentificación: " + self.identificacion + "\t\tEncargado: " + self.encargado +
              "\n\nTiempo Prom. de Atención: " + str(self.tiempoPromedioAtencion) +
              "\t\tTiempo Máx. de Atención: " + str(self.tiempoMaximoAtencion) + "\t\tTiempo Mín. de Atención: " +
              str(self.tiempoMinimoAtencion))

