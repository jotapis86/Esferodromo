import xmlrpclib

class clientePozoDeServidorCentral:
	def __init__(self, httpSer):
		self.servidor = xmlrpclib.Server(httpSer)
		print "clientePozoDeServidorCentral inicializado"

	def getMontoActualPozo(self):
                return self.servidor.getMontoActualPozo()

        def getUltimasApuestasPozo(self, n):
                return self.servidor.getUltimasApuestasPozo(n)
