import xmlrpclib

class clienteCoordinadorDeServidorCentral:
        def __init__(self, httpSer):
                self.servidor = xmlrpclib.Server(httpSer)
		print "clienteCoordinadorDeServidorCentral inicializado"

	def getNombresCoordinadores(self):
                return self.servidor.getNombresCoordinadores()

        def getIdCoordinador(self, nombreC):
                return self.servidor.getIdCoordinador(nombreC)

        def getClaveCoordinador(self, idC):
                return self.servidor.getClaveCoordinador(idC)

        def crearRonda(self, idC):
                return self.servidor.crearRonda(idC)

        def getIpsYpuertosMaquinas(self):
                return self.servidor.getIpsYpuertosMaquinas()

        def cerrarApuestas(self):
                return self.servidor.cerrarApuestas()

        def asignarGanancias(self, idsO):
                return self.servidor.asignarGanancias(idsO)

        def asignarGanadora(self, tB):
                return self.servidor.asignarGanadora(tB)

        def finalizarRonda(self):
                return self.servidor.finalizarRonda()

        def getDinero(self, ip, puerto):
                return self.servidor.getDinero(ip, puerto)

        def pagar(self, idC, idM, monto, cedulaCliente="", enviado="N"):
                return self.servidor.pagar(idC, idM, monto, cedulaCliente, enviado)

        def rondaAbierta(self):
                return self.servidor.rondaAbierta()

        def cancelarRonda(self):
                return self.servidor.cancelarRonda()

        def agregarCreditoManual(self, idC, idM, monto, enviado="N"):
                return self.servidor.agregarCreditoManual(idC, idM, monto, enviado)

        # para modulo administrativo

        def getClaveAdmin(self):
                return self.servidor.getClaveAdmin()

        def agregarCoordinador(self, nombre, clave, codMegaManager):
                return self.servidor.agregarCoordinador(nombre, clave, codMegaManager)

        def eliminarCoordinador(self, nombre):
                return self.servidor.eliminarCoordinador(nombre)

        def getValoresXmonedas(self):
                return self.servidor.getValoresXmonedas()

        def getFechaValoresMonedasVigentes(self):
                return self.servidor.getFechaValoresMonedasVigentes()

        def cambiarValorMoneda(self, moneda, valor):
                return self.servidor.cambiarValorMoneda(moneda, valor)

        def getTipoOpciones(self):
                return self.servidor.getTipoOpciones()

        def cambiarTipoOpcion(self, ids, v):
                return self.servidor.cambiarTipoOpcion(ids, v)

        def getRondas(self, fecha1, fecha2):
                return self.servidor.getRondas(fecha1, fecha2)

        def getTotalBilletesYcreditosManualesXmaquina(self, fecha1, fecha2):
                return self.servidor.getTotalBilletesYcreditosManualesXmaquina(fecha1, fecha2)

        def getTotalPagosXmaquina(self, fecha1, fecha2):
                return self.servidor.getTotalPagosXmaquina(fecha1, fecha2)

        def getTotalApostadoXmaquina(self, fecha1, fecha2):
                return self.servidor.getTotalApostadoXmaquina(fecha1, fecha2)

        def getTotalGanadoXmaquina(self, fecha1, fecha2):
                return self.servidor.getTotalGanadoXmaquina(fecha1, fecha2)

        def getCantidadBilletesXmaquina(self, fecha1, fecha2):
                return self.servidor.getCantidadBilletesXmaquina(fecha1, fecha2)

        def getPagosDetallado(self, fecha1, fecha2):
                return self.servidor.getPagosDetallado(fecha1, fecha2)

        def getValorBillete(self, idB):
                return self.servidor.getValorBillete(idB)

        def cambiarClaveAdmin(self, nc):
                return self.servidor.cambiarClaveAdmin(nc)

        def getCreditosManualesDetallado(self, fecha1, fecha2):
                return self.servidor.getCreditosManualesDetallado(fecha1, fecha2)

        def getUltimasGanadoras(self, n):
                return self.servidor.getUltimasGanadoras(n)

        def getMontoMinimoApuestasXmaquina(self):
                return self.servidor.getMontoMinimoApuestasXmaquina()

        def setMontoMinimoApuestasXmaquina(self, monto):
                return self.servidor.setMontoMinimoApuestasXmaquina(monto)


        # Pozo

        def getMontoInicialPozo(self):
                return self.servidor.getMontoInicialPozo()

        def getMontoActualPozo(self):
                return self.servidor.getMontoActualPozo()

        def getMontoReservaPozo(self):
                return self.servidor.getMontoReservaPozo()

        def getMontoMinimoParaConcursarPozo(self):
                return self.servidor.getMontoMinimoParaConcursarPozo()

        def getFrecuenciaSorteoPozo(self):
                return self.servidor.getFrecuenciaSorteoPozo()

        def getFactorReservaPozo(self):
                return self.servidor.getFactorReservaPozo()

        def getFactorIncrementoPozo(self):
                return self.servidor.getFactorIncrementoPozo()

        def getUltimaRondaJugadaPozo(self):
                return self.servidor.getUltimaRondaJugadaPozo()

        def setMontoInicialPozo(self, monto):
                return self.servidor.setMontoInicialPozo(monto)

        def setMontoActualPozo(self, monto):
                return self.servidor.setMontoActualPozo(monto)

        def setMontoReservaPozo(self, monto):
                return self.servidor.setMontoReservaPozo(monto)

        def setMontoMinimoParaConcursarPozo(self, monto):
                return self.servidor.setMontoMinimoParaConcursarPozo(monto)

        def setFrecuenciaSorteoPozo(self, frecuencia):
                return self.servidor.setFrecuenciaSorteoPozo(frecuencia)

        def setFactorReservaPozo(self, factor):
                return self.servidor.setFactorReservaPozo(factor)

        def setFactorIncrementoPozo(self, factor):
                return self.servidor.setFactorIncrementoPozo(factor)

        def setUltimaRondaJugadaPozo(self, ronda):
                return self.servidor.setUltimaRondaJugadaPozo(ronda)

        def getIdUltimaRonda(self):
                return self.servidor.getIdUltimaRonda()

        def agregarJugadaPozo(self):
                return self.servidor.agregarJugadaPozo()

        def actualizarMontoJugadaPozo(self):
                return self.servidor.actualizarMontoJugadaPozo()

        def setMaquinasMegaManager(self, modulos, codigos):
                return self.servidor.setMaquinasMegaManager(modulos, codigos)

        def getCodMaquinaMegaManager(self, idMaquina):
                return self.servidor.getCodMaquinaMegaManager(idMaquina)

        def getCodCoordinadorMegaManager(self, idCoordinador):
                return self.servidor.getCodCoordinadorMegaManager(idCoordinador)

        def getPagosPendientesMegaManager(self):
                return self.servidor.getPagosPendientesMegaManager()

        def getRecargasPendientesMegaManager(self):
                return self.servidor.getRecargasPendientesMegaManager()

        def actualizarPagoMegaManager(self, idPago, estado, idCliente):
                return self.servidor.actualizarPagoMegaManager(idPago, estado, idCliente)

        def actualizarRecargaManualMegaManager(self, idRecarga, estado):
                return self.servidor.actualizarRecargaManualMegaManager(idRecarga, estado)

        def getDetalleApuestasClienteEnRonda(self, idMaquina, idRonda):
                return self.servidor.getDetalleApuestasClienteEnRonda(idMaquina, idRonda)

        def getInfoUltimasRondas(self, n):
                return self.servidor.getInfoUltimasRondas(n)

        def getOpciones(self):
                return self.servidor.getOpciones()
