import xmlrpclib

class clienteCoordinadorDeServidorMaquina:
    def __init__(self, ip, puerto):
        self.ip = ip
        self.puerto = puerto
        self.httpSer = "http://" + ip + ":" + str(puerto)
        self.servidor = xmlrpclib.Server(self.httpSer)
        print "clienteCoordinadorDeServidorMaquina inicializado"

    def bloquear(self,mandarApuestas):
        return self.servidor.bloquear(mandarApuestas)

    def desbloquear(self):
        return self.servidor.desbloquear()

    def actualizarDisponible(self):
        return self.servidor.actualizarDisponible()

    def actualizarGanado(self, g):
        return self.servidor.actualizarGanado(g)

    def limpiarPagno(self):
        return self.servidor.limpiarPagno()

    def anularTodo(self):
        return self.servidor.anularTodo()

    def actualizarGanadoras(self):
        return self.servidor.actualizarGanadoras()

    def mostrarApuestasGanadoras(self, g):
        return self.servidor.mostrarApuestasGanadoras(g)

    def ocultarFichas(self):
        return self.servidor.ocultarFichas()

    def hayApuestas(self):
        return self.servidor.hayApuestas()

    
