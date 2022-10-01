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

