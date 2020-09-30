import xmlrpclib

class clienteServidorCentralDeServidorPozo:
    def __init__(self, dirServidorPozo):
        self.servidor = xmlrpclib.Server(dirServidorPozo)
        print "clienteServidorCentralDeServidorPozo inicializado"

    def actualizarMonto(self, monto):
        return self.servidor.actualizarMonto(monto)

    def actualizarUltimasApuestas(self, apuestas):
        return self.servidor.actualizarUltimasApuestas(apuestas)
