from pysimplesoap.client import SoapClient
from pysimplesoap.client import SoapFault

import urllib2
from xml.etree import ElementTree

import time

class clienteCoordinadorDeMegaManager:
    def __init__(self, url):
        self.clientesCreados = True
        self.url = url
        self.conectar()
        
    def conectar(self):
        try:
            self.clienteMegaManager = SoapClient(wsdl=self.url, trace=False)
            self.clienteMegaManagerNOparams = SoapClient(wsdl=self.url, trace=False, soap_server="oracle")
            print "Clientes MegaManager creados!"
        except Exception, e:
            print "Error creando clientes de MegaManager: ", e
            self.clientesCreados = False
            raise

    def getMaquinas(self):
        if not self.clientesCreados:
            self.conectar()
        try:
            response = self.clienteMegaManagerNOparams.getMaquinas()
            result = response['out']
            xml = ElementTree.fromstring(result)
            registros = xml.findall(".//registro")
            modulos = []
            codigos = []
            for r in registros:
                modulos.append(r.findtext(".//num"))
                codigos.append(r.findtext(".//cod"))
            #print "modulos = ", modulos
            #print "codigos = ", codigos
            return (modulos, codigos)
        except Exception, e:
            print "Error consiguiendo codigos de maquinas: ", e
            raise

    def existeCliente(self, cliente):
        if not self.clientesCreados:
            self.conectar()
        try:
            # response = {'out': xml datos del cliente o None}
            response = self.clienteMegaManager.getCliente(cliente)
            result = response['out']
            if result == None:
                return False
            else:
                return True
        except Exception, e:
            print "Error consiguiendo cliente: ", e
            raise


    def reportarPago(self, codCoordinador, codMaquina, aPagar, cedulaCliente):
        if not self.clientesCreados:
            self.conectar()
        try:
            # response = {'out': True}
            xml = """<?xml version='1.0' encoding='UTF-8'?> 
                        <datos>
                        <registro>
                        <cli>%s</cli>
                        <ced></ced>
                        <nom></nom>
                        <ape></ape>
                        <cre>%s</cre>
                        <maq>%s</maq>
                        <pes>%s</pes>
                        <ges>%s</ges>
                        <fec>%s</fec>
                        <fot>sin-foto</fot>
                        <pro>no</pro>
                        <ret>no</ret>
                        </registro>
                        </datos>"""%(cedulaCliente, aPagar, codMaquina, aPagar, codCoordinador, time.strftime("%Y-%m-%d %H:%M:%S")) 
            response = self.clienteMegaManager.pagoDePremio(xml)
            result = response['out']
            return result
        except Exception, e:
            print "Error al reportar pago: ", e
            raise


    def reportarRecargaManual(self, valor, codMaquina, codCoordinador):
        if not self.clientesCreados:
            self.conectar()
        try:
            # response = {'out': True}
            xml = """<?xml version='1.0' encoding='UTF-8'?>
                        <datos>
                        <registro>
                        <val>%s</val>
                        <maq>%s</maq>
                        <ges>%s</ges>
                        </registro>
                        </datos>"""%(valor, codMaquina, codCoordinador)
            response = self.clienteMegaManager.saveRecargaRuleta(xml)
            result = response['out']
            return result
        except Exception, e:
            print "Error al reportar recarga manual: ", e
            raise

        
