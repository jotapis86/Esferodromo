import xmlrpclib

class clienteCoordinadorDeServidorPozo:
    def __init__(self, httpSer):
        self.servidor = xmlrpclib.Server(httpSer)
        print "clienteCoordinadorDeServidorPozo inicializado"

    def actualizarMonto(self, monto):
        return self.servidor.actualizarMonto(monto)

    def pozoJugando(self):
        return self.servidor.pozoJugando()

    def pozoGanado(self):
        return self.servidor.pozoGanado()



    
