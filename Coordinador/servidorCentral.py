#!/usr/bin/python 

from SimpleXMLRPCServer import *
from conexionBd import *
import math
import os
import random
from clienteServidorCentralDeServidorPozo import *


class servidorCentral:
    def __init__(self):
        """Inicia la conexion con la base de datos y con el pozo"""
        self.conexion = conexionBd("bd")
        # cliente de pozo
        c = open("pozo.conf")
        dirPozo = c.readline()[:-1]
        c.close()
        self.clientePozo = clienteServidorCentralDeServidorPozo(dirPozo)
        print "servidorCentral inicializado"

    # ---
    # --- funciones para las maquinas
    # ---

    def insertarBillete(self, ip, puerto, valor):
        """Inserta el billete introducido en una maquina actualizando el dinero disponible"""
        try:
            # id de la maquina que introdujo el billete
            idM = self.getIdMaquina(ip, puerto)
            # id del valor del billete introducido
            idB = self.conexion.ejecutarSQL("select id from billetes where valor=%s"%(valor))[0][0]
            # insercion del billete en la maquina
            self.conexion.ejecutarSQL("insert into billetesXmaquinas (fecha,hora,id_Billete,id_Maquina) values (DATE('now','localtime'),TIME('now','localtime'),%s,%s)"%(idB, idM))
            # actualizacion del dinero disponible
	    ant = self.conexion.ejecutarSQL("select dinero from maquinas where id=%s"%(idM))[0][0]
	    self.conexion.ejecutarSQL("update maquinas set dinero=%s where id=%s"%(ant+valor, idM))
            # comprometer
	    self.conexion.commit()
            return True
        except Exception, e:
            print "insertarBillete excepcion: ", e
            self.conexion.rollback()
            return False


    def getMinMaxXtipoOpcion(self):
        """Retorna el valor minimo y maximo de los tipos de opciones para apostar"""
        return self.conexion.ejecutarSQL("select min, max from tipoOpciones")

    def apostar(self, ip, puerto, apuestas, disponible):
        """Apuesta las opciones recibidas a la maquina con el ip y puerto recibidos y actualiza dinero"""
        try:
            idM = self.getIdMaquina(ip,puerto)
            # insertar en apuestas
            self.conexion.ejecutarSQL("insert into apuestas (fecha,hora,id_ronda,id_maquina) values (DATE('now','localtime'),TIME('now','localtime'),%s,%s)"%(self.getIdUltimaRonda(),idM))
            # saber el id de las apuestas
            idA = self.conexion.ejecutarSQL("select id from apuestas order by id desc")[0][0]
            # insertar en apuestasXopciones
            for i in range(len(apuestas)):
                a = apuestas[i]
                if a != 0:
                    self.conexion.ejecutarSQL("insert into apuestasXopciones (id_apuesta,id_opcion,valorApostado) values (%s,%s,%s)"%(idA,i+1,a))
                    self.incrementarPozo(a)
            # actualizar dinero disponible
            self.conexion.ejecutarSQL("update maquinas set dinero=%s where id=%s"%(disponible,idM))
            self.conexion.commit()
            return True
        except Exception, e:
            print "apostar excepcion: ", e
            self.conexion.rollback()
            return False


    def incrementarPozo(self, valorApostado):
        """Incrementa el monto actual y el monto de reserva del pozo segun el valor de la apuesta y los factores de incremento y de reserva del pozo"""
        self.setMontoActualPozo(self.getMontoActualPozo() + int(math.floor(self.getFactorIncrementoPozo() * valorApostado)))
        self.setMontoReservaPozo(self.getMontoReservaPozo() + int(math.floor(self.getFactorReservaPozo() * valorApostado)))
        try:
            self.clientePozo.actualizarMonto(self.getMontoActualPozo())
        except Exception, e:
            print "incrementarPozo :: error actualizando monto de Pozo : ", e


    def getUltimasGanadoras(self, n):
        """Retorna las n ultimas bolas ganadoras."""
        return self.conexion.ejecutarSQL("select ganadora from rondas order by id desc limit %s"%(n))


    def getUltimasApuestas(self, ip, puerto):
        """Retorna las apuestas de la maquina dada hechas en la ultima ronda."""
        idM = self.getIdMaquina(ip, puerto)
        idR = self.getIdUltimaRonda()
        #obtener id apuesta de la maquina dada en la ultima ronda
        idA = self.conexion.ejecutarSQL("select id from apuestas where id_ronda=%s and id_maquina=%s"%(idR,idM))
        if idA != []:
            return self.conexion.ejecutarSQL("select id_opcion, valorApostado from apuestasXopciones where id_apuesta=%s"%(idA[0][0]))
        else:
            return []



    # ---
    # --- funciones para los coordinadores
    # ---

    def getNombresCoordinadores(self):
        """Retorna los nombres de los coordinadores del esferodromo"""
        return self.conexion.ejecutarSQL("select nombre from coordinadores order by nombre")

    def getIdCoordinador(self, nombreC):
        """Retorna el id del coordinador con el nombre dado"""
        return self.conexion.ejecutarSQL("select id from coordinadores where nombre='%s'"%(nombreC))[0][0]
        
    def getClaveCoordinador(self, idC):
        """Retorna la clave del coordinador identificado por el id dado"""
        return self.conexion.ejecutarSQL("select clave from coordinadores where id=%s"%(idC))[0][0]

    def crearRonda(self, idC):
        """Crea una nueva ronda en el juego para el coordinador dado"""
        try:
            self.conexion.ejecutarSQL("insert into rondas (fecha,horaInicio,nit_Esferodromo,id_Coordinador) values (DATE('now','localtime'), TIME('now','localtime'), '%s', %s)"%(self.getNit(),idC))
            self.conexion.commit()
            return True
        except Exception, e:
            print "crearRonda excepcion: ", e
            self.conexion.rollback()
            return False

    def getIpsYpuertosMaquinas(self):
        """Retorna los ips y puertos de cada maquina del juego"""
        return self.conexion.ejecutarSQL("select ip, puerto from maquinas order by id")

    def cerrarApuestas(self):
        """Cierra las apuestas de la ronda en curso"""
        try:
            self.conexion.ejecutarSQL("update rondas set horaCierreApuestas=TIME('now','localtime') where id=%s"%(self.getIdUltimaRonda()))
            self.conexion.commit()
            return True
        except Exception, e:
            print "cerrarApuestas excepcion: ", e
            self.conexion.rollback()
            return False

    def asignarGanancias(self, idsO):
        """Asigna el dinero ganado por las opciones apostadas de cada maquina en la ronda.
        Retorna 3 cosas:
        la lista de ganancias para cada maquina,
        si hay o no ganadores del Pozo
        y la lista de ganancias para cada maquina gracias al pozo"""
        def sumarListas(lista1, lista2):
            resultado = [0]*len(lista1)
            for i in range(len(lista1)):
                resultado[i] = lista1[i] + lista2[i]
            return resultado
        
        try:
            idR = self.getIdUltimaRonda()

            # trabajo para ganancias pozo
            # id de la opcion ganadora siempre es la primera que viene en la lista de opciones ganadoras
            idOpcionGanadora = idsO[0]
            revisarGanadoresPozo = False
            hayGanadoresPozo = False
            montoMinimoPozo = 999999
            listaGanadoresPozo = []
            idUltimaRondaJugadaPozo = self.getUltimaRondaJugadaPozo()
            # si pozo aposto en esta ronda y al numero que aposto pozo es el mismo numero que cayo..."
            if (idR == idUltimaRondaJugadaPozo) and (idOpcionGanadora == self.getIdOpcionUltimaApuestaPozo()):
                revisarGanadoresPozo = True
                montoMinimoPozo = self.getMontoMinimoParaConcursarPozo()
            # trabajo para ganancias Pozo
                
            # asignar dinero ganado a las apuestasXopcion y actualizar dinero disponible de las maquinas
            # [(idMaquina,idApuesta,idOpcion,vApostado,pagaPor), ...]
            superConsulta = self.conexion.ejecutarSQL("select m.id, aXo.id_apuesta, aXo.id_opcion, aXo.valorApostado, tipo.pagaPor from apuestasXopciones aXo, opciones o, tipoOpciones tipo, maquinas m, apuestas a, rondas r where a.id_ronda=r.id and a.id_maquina=m.id and aXo.id_apuesta=a.id and aXo.id_opcion=o.id and o.id_tipoOpcion=tipo.id and r.id=%s"%(idR))
            ganancias = [0]*len(self.getIpsYpuertosMaquinas())
            gananciasPozo = [0]*len(ganancias)
            for idMaquina,idApuesta,idOpcion,vApostado,pagaPor in superConsulta:
                if idOpcion in idsO:
                    vGanado = int(math.floor(vApostado + vApostado*pagaPor)) #actualizar valor ganado
                    self.conexion.ejecutarSQL("update apuestasXopciones set valorGanado=%s where id_apuesta=%s and id_opcion=%s"%(vGanado,idApuesta,idOpcion))
                    self.agregarDineroMaquina(idMaquina, vGanado) #actualizar dinero de maquina
                    ganancias[idMaquina-1] += vGanado #acumular en ganancias
                else:
                    #poner 0 a valor ganado
                    self.conexion.ejecutarSQL("update apuestasXopciones set valorGanado=%s where id_apuesta=%s and id_opcion=%s"%(0,idApuesta,idOpcion))

                # si revisar ganadores = cayo el mismo numero del pozo ...
                if revisarGanadoresPozo:
                    # entonces asignar ganancias a las apuestas que jugaron el mismo numero del pozo y cumplen minimo monto de apuesta plena
                    if idOpcionGanadora == idOpcion and vApostado >= montoMinimoPozo:
                        listaGanadoresPozo.append((idUltimaRondaJugadaPozo, idMaquina, idApuesta, idOpcion))
                        hayGanadoresPozo = True

            if revisarGanadoresPozo:
                # asignar ganancias del pozo a quienes esten en listaGanadoresPozo
                if len(listaGanadoresPozo) > 0:
                    gananciasPozo =  self.asignarGananciasPorPozo(listaGanadoresPozo)
                    # reiniciar pozo en monto en reserva
                    self.reiniciarPozo()


            # sumar ganancias por apuestas y ganancias por pozo
            ganancias = sumarListas(ganancias, gananciasPozo)
                
            self.conexion.commit()
            # retorna las ganancias de cada maquina totalizadas >> ganancias por apuestas + ganancias por pozo
            # y si hay ganadores del pozo
            return ganancias, hayGanadoresPozo, gananciasPozo
        except Exception, e:
            print "asignarGanancias excepcion: ", e
            self.conexion.rollback()
            return [-1], hayGanadoresPozo, gananciasPozo


    def asignarGananciasPorPozo(self, listaGanadores):
        """Reparte el dinero del pozo entre las maquinas que esten en la lista de ganadores del pozo"""
        montoActualPozo = self.getMontoActualPozo()
        numGanadores = len(listaGanadores)
        montoGanado = montoActualPozo / numGanadores
        gananciasPozo = [0]*len(self.getIpsYpuertosMaquinas())
        for idjugadaPozo, idMaquina, idApuesta, idOpcion in listaGanadores:
            self.conexion.ejecutarSQL("insert into ganadoresPozo (id_jugadaPozo, id_maquina, id_apuesta, id_opcion, montoGanado) values (%s,%s,%s,%s,%s)"%(idjugadaPozo,idMaquina,idApuesta,idOpcion,montoGanado))
            # agregar dinero ganado por pozo a maquina
            self.agregarDineroMaquina(idMaquina, montoGanado)
            # agregar a lista de ganancias por pozo el monto ganado
            gananciasPozo[idMaquina-1] += montoGanado
        return gananciasPozo
    

    def reiniciarPozo(self):
        """Monto actual de pozo queda igual a lo que se tenia de reserva y monto reserva queda igual a monto inicial"""
        # no se usan opciones de set... porque tienen commit y se tirarian transaccionalidad de funcion asignarGanancias
        self.conexion.ejecutarSQL("update pozos set montoActual = %s"%(self.getMontoReservaPozo()))
        self.conexion.ejecutarSQL("update pozos set montoReserva = %s"%(self.getMontoInicialPozo()))
        

    def asignarGanadora(self, tB):
        """Asigna la bola ganadora a la ronda."""
        try:
            idR = self.getIdUltimaRonda()
            self.conexion.ejecutarSQL("update rondas set ganadora='%s' where id=%s"%(tB,idR))
            self.conexion.commit()
            return True
        except Exception, e:
            print "asignarGanadora excepcion: ", e
            self.conexion.rollback()
            return False

    def finalizarRonda(self):
        """Finaliza la ronda vigente asignando la hora de fin."""
        try:
            idR = self.getIdUltimaRonda()
            self.conexion.ejecutarSQL("update rondas set horaFin=TIME('now','localtime') where id=%s"%(idR))
            self.conexion.commit()
            return True
        except Exception, e:
            print "finalizarRonda excepcion: ", e
            self.conexion.rollback()
            return False
            

    def agregarDineroMaquina(self, idM, monto):
        """Agrega el monto recibido a la maquina identificada con idM"""
        dA = self.conexion.ejecutarSQL("select dinero from maquinas where id=%s"%(idM))[0][0]
        self.conexion.ejecutarSQL("update maquinas set dinero=%s where id=%s"%(dA+monto,idM))



    def pagar(self, idC, idM, monto, cedulaCliente="", enviado="N"):
        """Paga el monto a la maquina recibida"""
        try:
            self.conexion.ejecutarSQL("insert into pagos (valor,fecha,hora,id_coordinador,id_maquina,idCliente,enviadoMegaManager) values (%s,DATE('now','localtime'),TIME('now','localtime'),%s,%s, '%s', '%s')"%(monto,idC,idM, cedulaCliente, enviado))
            #actualizar maquinas
            self.agregarDineroMaquina(idM,monto*-1)
            self.conexion.commit()
            return True
        except Exception, e:
            print "pagar excepcion: ", e
            self.conexion.rollback()
            return False



    def agregarCreditoManual(self, idC, idM, monto, enviado="N"):
        """Agrega el monto a la maquina recibida dejando el rastro en la tabla creditosManualesXmaquinas."""
        try:
            # dejar registro en creditosManualesXmaquinas
            self.conexion.ejecutarSQL("insert into creditosManualesXmaquinas (fecha, hora, id_coordinador, id_maquina, valor, enviadoMegaManager) values (DATE('now','localtime'),TIME('now','localtime'),%s,%s,%s, '%s')"%(idC,idM,monto, enviado))
            #actualizar maquina
            self.agregarDineroMaquina(idM,monto)
            self.conexion.commit()
            return True
        except Exception, e:
            print "agregarCreditoManual excepcion: ", e
            self.conexion.rollback()
            return False



    def cancelarRonda(self):
        """Cancela la mas reciente ronda abierta."""
        try:
            idR = self.getIdUltimaRonda()
            # regresar dinero apostado en la ronda a todas las maquinas y eliminar todas las apuestasXopciones de la ronda
            aXo = self.conexion.ejecutarSQL("select aXo.id_apuesta, aXo.id_opcion, m.id id_maquina, aXo.valorApostado from apuestasXopciones aXo, opciones o, tipoOpciones tipo, maquinas m, apuestas a, rondas r where a.id_ronda=r.id and a.id_maquina=m.id and aXo.id_apuesta=a.id and aXo.id_opcion=o.id and o.id_tipoOpcion=tipo.id and r.id=%s"%(idR))
            for idApuesta, idOpcion, idMaquina, monto in aXo:
                self.agregarDineroMaquina(idMaquina, monto)
                self.conexion.ejecutarSQL("delete from apuestasXopciones where id_apuesta=%s and id_opcion=%s"%(idApuesta,idOpcion))
            # eliminar las apuestas de la ronda
            self.conexion.ejecutarSQL("delete from apuestas where id_ronda=%s"%(idR))
            # eliminar la ronda
            self.conexion.ejecutarSQL("delete from rondas where id=%s"%(idR))
            # comprometer
            self.conexion.commit()
            return True
        except Exception, e:
            print "cancelarRonda excepcion: ", e
            self.conexion.rollback()
            return False


    def getClaveAdmin(self):
        """Retorna la clave del administrador del esferodromo."""
        return self.conexion.ejecutarSQL("select claveAdmin from esferodromos")[0][0]


    # ---
    # --- para ambos
    # ---

    def getDinero(self, ip, puerto):
        """Retorna el dinero disponible en una maquina"""
        return self.conexion.ejecutarSQL("select dinero from maquinas where ip='%s' and puerto=%s"%(ip,puerto))[0][0]

    # llamada por el administrador
    def getValoresXmonedas(self):
        """Retorna los valores de las monedas vigentes"""
        vXm = self.conexion.ejecutarSQL("select valorM1, valorM2, valorM3, valorM4, valorM5 from valoresXmonedas order by id desc")
        return vXm[0]


    def rondaAbierta(self):
        """Retorna True si la ultima ronda esta abierta. False en otro caso."""
        idUr = self.getIdUltimaRonda()
        if idUr != 0:
            return self.conexion.ejecutarSQL("select * from rondas where id=%s and horaFin notnull"%(idUr)) == []
        else:
            return False #si idUr=0 quiere decir que no se ha jugado la primera ronda


    def apuestasAbiertas(self):
        """Retorna True si en la ultima ronda estan las apuestas abiertas. False en otro caso."""
        return self.conexion.ejecutarSQL("select * from rondas where id=%s and horaCierreApuestas isnull"%(self.getIdUltimaRonda())) != []



    # ---
    # --- funciones para el administrador pero llamadas por el cliente coordinador
    # ---
    def agregarCoordinador(self, nombre, clave, codMegaManager):
        """Agrega un nuevo coordinador."""
        try:
            self.conexion.ejecutarSQL("insert into coordinadores (nombre,clave,codMegaManager) values ('%s','%s','%s')"%(nombre,clave,codMegaManager))
            self.conexion.commit()
            return True
        except Exception, e:
            print "agregarCoordinador excepcion: ", e
            self.conexion.rollback()
            return False

    def eliminarCoordinador(self, nombre):
        """Elimina el coordinador con el nombre dado."""
        try:
            self.conexion.ejecutarSQL("delete from coordinadores where nombre='%s'"%(nombre))
            self.conexion.commit()
            return True
        except Exception, e:
            print "eliminarCoordinador excepcion: ", e
            self.conexion.rollback()
            return False

    def getFechaValoresMonedasVigentes(self):
        """Retorna la fecha en la cual fueron asignados los valores de las monedas vigentes."""
        return self.conexion.ejecutarSQL("select fechaIngreso from valoresXmonedas order by id desc")[0][0]

    def cambiarValorMoneda(self, moneda, valor):
        """Cambia el valor de la moneda dada y actualiza la fecha de ultima modificacion."""
        try:
            self.conexion.ejecutarSQL("update valoresXmonedas set %s = %s"%(moneda,valor))
            self.conexion.ejecutarSQL("update valoresXmonedas set fechaIngreso = DATE('now','localtime')")
            self.conexion.commit()
            return True
        except Exception, e:
            print "cambiarValorMoneda excepcion: ", e
            self.conexion.rollback()
            return False

    def getTipoOpciones(self):
        """Retorna pagaPor, min y max de los tipos de opciones (pleno, medio, cuadro y chanza)."""
        return self.conexion.ejecutarSQL("select pagaPor, min, max from tipoOpciones")

    def cambiarTipoOpcion(self, ids, v):
        """Cambia el valor pagaPor, min o max del tipo de opcion dado en ids."""
        try:
            self.conexion.ejecutarSQL("update tipoOpciones set %s = %s where id = %s"%(ids[1], v, ids[0]))
            self.conexion.commit()
            return True
        except Exception, e:
            print "cambiarTipoOpcion excepcion: ", e
            self.conexion.rollback()
            return False



    def getRondas(self, fecha1="", fecha2=""):
        """Retorna todas las rondas jugadas (id, fecha, horaInicio, horaFin, ganadora, coordinador) entre las fechas dadas."""
        if fecha1 == "":
            return self.conexion.ejecutarSQL("select r.id,r.fecha,r.horaInicio,r.horaFin,r.ganadora,c.nombre from rondas r left join coordinadores c on r.id_coordinador=c.id order by r.id desc")
        else:
            return self.conexion.ejecutarSQL("select r.id,r.fecha,r.horaInicio,r.horaFin,r.ganadora,c.nombre from rondas r left join coordinadores c on r.id_coordinador=c.id where r.fecha between '%s' and '%s' order by r.id desc"%(fecha1,fecha2))


    def getInfoUltimasRondas(self, n):
        """Retorna info basica de las ultimas n rondas jugadas"""
        return self.conexion.ejecutarSQL("select r.id,r.fecha,r.horaInicio,r.horaFin,r.ganadora,c.nombre from rondas r left join coordinadores c on r.id_coordinador=c.id order by r.id desc limit %s"%(n))


    
    # Para cuadre real
    # Total entradas por maquina = total billetes entrados x maquina + total creditos manuales X maquina
    def getTotalBilletesYcreditosManualesXmaquina(self, fecha1, fecha2):
        """Retorna el monto total de los billetes entrados por maquina y los creditos manuales dados en la fecha dada por cada maquina."""
        def sumEntradasReales(tB, tCM):
            # normalizar las 2 listas hasta el numero de maquinas registradas
            totalB = tB
            totalCM = tCM
            for i in range(len(self.getIpsYpuertosMaquinas())):
                try:
                    if totalB[i][0] != i+1:
                        totalB.insert(i,(i+1,0))
                except:
                    totalB.insert(i,(i+1,0))
                try:
                    if totalCM[i][0] != i+1:
                        totalCM.insert(i,(i+1,0))
                except:
                    totalCM.insert(i,(i+1,0))
            # sumar en paralelo las 2 listas
            total = []
            for i,r in enumerate(totalB):
                total.append((r[0],r[1]+totalCM[i][1]))
            return total
        
        if fecha1 == "":
            totalBilletes = self.conexion.ejecutarSQL("select bXm.id_maquina, sum(b.valor) from billetesXmaquinas bXm, billetes b where b.id=bXm.id_billete group by bXm.id_maquina")
            totalCreditosManuales = self.conexion.ejecutarSQL("select id_maquina, sum(valor) from creditosManualesXmaquinas group by id_maquina")
            totalEntradasReales = sumEntradasReales(totalBilletes, totalCreditosManuales)
            return totalEntradasReales
        else:
            totalBilletes = self.conexion.ejecutarSQL("select bXm.id_maquina, sum(b.valor) from billetesXmaquinas bXm, billetes b where b.id=bXm.id_billete and bXm.fecha between '%s' and '%s' group by bXm.id_maquina"%(fecha1,fecha2))
            totalCreditosManuales = self.conexion.ejecutarSQL("select id_maquina, sum(valor) from creditosManualesXmaquinas where fecha between '%s' and '%s' group by id_maquina"%(fecha1,fecha2))
            totalEntradasReales = sumEntradasReales(totalBilletes, totalCreditosManuales)
            return totalEntradasReales


    # Para cuadre real
    # Total salidas por maquina = total pagos x maquina
    def getTotalPagosXmaquina(self, fecha1, fecha2):
        """Retorna el monto total de los pagos hechos a cada maquina en la fecha dada."""
        if fecha1 == "":
            return self.conexion.ejecutarSQL("select id_maquina, sum(valor) from pagos group by id_maquina")
        else:
            return self.conexion.ejecutarSQL("select id_maquina, sum(valor) from pagos where fecha between '%s' and '%s' group by id_maquina"%(fecha1,fecha2))


    # Para cuadre virtual
    # Total entradas X maquina = Total apostado X maquina
    def getTotalApostadoXmaquina(self, fecha1, fecha2):
        """Retorna el monto total apostado por cada maquina en la fecha dada."""
        if fecha1 == "":
            return self.conexion.ejecutarSQL("select a.id_maquina, sum(aXo.valorApostado) from apuestas a, apuestasXopciones aXo where a.id=aXo.id_apuesta group by a.id_maquina")
        else:
            return self.conexion.ejecutarSQL("select a.id_maquina, sum(aXo.valorApostado) from apuestas a, apuestasXopciones aXo where a.id=aXo.id_apuesta and a.fecha between '%s' and '%s' group by a.id_maquina"%(fecha1,fecha2))

    
    # Para cuadre virtual
    # Total salidas X maquina = Total ganado X maquina
    def getTotalGanadoXmaquina(self, fecha1, fecha2):
        """Retorna el monto total ganado por cada maquina en la fecha dada."""
        if fecha1 == "":
            return self.conexion.ejecutarSQL("select a.id_maquina, sum(aXo.valorGanado) from apuestas a, apuestasXopciones aXo where a.id=aXo.id_apuesta group by a.id_maquina")
        else:
            return self.conexion.ejecutarSQL("select a.id_maquina, sum(aXo.valorGanado) from apuestas a, apuestasXopciones aXo where a.id=aXo.id_apuesta and a.fecha between '%s' and '%s' group by a.id_maquina"%(fecha1,fecha2))


    def getCantidadBilletesXmaquina(self, fecha1="", fecha2=""):
        """Retorna la cantidad de billetes por denominacion que han entrado en cada maquina."""
        if fecha1 == "":
            return self.conexion.ejecutarSQL("select id_maquina, id_billete, count(*) from billetesXmaquinas group by id_maquina, id_billete")
        else:
            return self.conexion.ejecutarSQL("select id_maquina, id_billete, count(*) from billetesXmaquinas where fecha between '%s' and '%s' group by id_maquina, id_billete"%(fecha1,fecha2))



    def getPagosDetallado(self, fecha1, fecha2):
        """Retorna los pagos hechos a cada maquina junto con el coordinador que lo efectuo, valor, fecha y hora."""
        if fecha1 == "":
            return self.conexion.ejecutarSQL("select c.nombre, p.id_maquina, p.valor, p.fecha, p.hora from pagos p left join coordinadores c on p.id_coordinador=c.id")
        else:
            return self.conexion.ejecutarSQL("select c.nombre, p.id_maquina, p.valor, p.fecha, p.hora from pagos p left join coordinadores c on p.id_coordinador=c.id where fecha between '%s' and '%s'"%(fecha1,fecha2))


    def getValorBillete(self, idB):
        """Retorna el valor del billete con el id dado."""
        return self.conexion.ejecutarSQL("select valor from billetes where id=%s"%(idB))[0][0]


    def cambiarClaveAdmin(self, nc):
        """Cambia la clave de administrador"""
        try:
            self.conexion.ejecutarSQL("update esferodromos set claveAdmin = '%s'"%(nc))
            self.conexion.commit()
            return True
        except Exception, e:
            print "cambiarClaveAdmin excepcion: ", e
            self.conexion.rollback()
            return False


    def getCreditosManualesDetallado(self, fecha1, fecha2):
        """Retorna los creditos manuales hechos a cada maquina: fecha, hora, coordinador, maquina, valor."""
        if fecha1 == "":
            return self.conexion.ejecutarSQL("select cm.fecha, cm.hora, c.nombre, cm.id_maquina, cm.valor from creditosmanualesXmaquinas cm left join coordinadores c on cm.id_coordinador=c.id")
        else:
            return self.conexion.ejecutarSQL("select cm.fecha, cm.hora, c.nombre, cm.id_maquina, cm.valor from creditosmanualesXmaquinas cm left join coordinadores c on cm.id_coordinador=c.id where fecha between '%s' and '%s'"%(fecha1,fecha2))


    def getMontoMinimoApuestasXmaquina(self):
        """Retorna el monto minimo de apuestas que debe hacer cada maquina"""
        return self.conexion.ejecutarSQL("select montoMinimoApuestasXmaquina from esferodromos")[0][0]

    def setMontoMinimoApuestasXmaquina(self, monto):
        """Cambia el monto minimo de apuestas por maquina."""
        try:
            self.conexion.ejecutarSQL("update esferodromos set montoMinimoApuestasXmaquina = %s"%(monto))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setMontoMinimoApuestasXmaquina excepcion: ", e
            self.conexion.rollback()
            return False


    def getDetalleApuestasClienteEnRonda(self, idMaquina, idRonda):
        """Retorna el detalle de todas las apuestas hechas por la maquina dada en la ronda dada."""
        return self.conexion.ejecutarSQL("""select r.id,
                                                                    r.fecha,
                                                                    r.horaFin,
                                                                    r.ganadora,
                                                                    aXo.id_opcion,
                                                                    o.desc,
                                                                    aXO.valorApostado,
                                                                    aXo.valorGanado
                                                        from rondas r,
                                                                apuestas a,
                                                                apuestasXopciones aXo,
                                                                opciones o
                                                        where r.id = a.id_ronda
                                                                and a.id = aXo.id_apuesta
                                                                and aXo.id_opcion = o.id
                                                                and a.id_maquina = %s
                                                                and r.id = %s"""%(idMaquina, idRonda))


    # Pozo 

    def getMontoInicialPozo(self):
        """Retorna el monto inicial del pozo"""
        return self.conexion.ejecutarSQL("select montoInicial from pozos")[0][0]

    def getMontoActualPozo(self):
        """Retorna el monto actual del pozo"""
        return self.conexion.ejecutarSQL("select montoActual from pozos")[0][0]

    def getMontoReservaPozo(self):
        """Retorna el monto en reserva del pozo"""
        return self.conexion.ejecutarSQL("select montoReserva from pozos")[0][0]

    def getMontoMinimoParaConcursarPozo(self):
        """Retorna el monto minimo para concursar en el pozo"""
        return self.conexion.ejecutarSQL("select montoMinimoParaConcursar from pozos")[0][0]

    def getFrecuenciaSorteoPozo(self):
        """Retorna la frecuencia del sorteo del pozo"""
        return self.conexion.ejecutarSQL("select frecuenciaSorteo from pozos")[0][0]

    def getFactorReservaPozo(self):
        """Retorna el factor de reserva del pozo"""
        return self.conexion.ejecutarSQL("select factorReserva from pozos")[0][0]

    def getFactorIncrementoPozo(self):
        """Retorna el factor de incremento del pozo"""
        return self.conexion.ejecutarSQL("select factorIncremento from pozos")[0][0]

    def getUltimaRondaJugadaPozo(self):
        """Retorna el id de la ultima ronda jugada por el pozo"""
        return self.conexion.ejecutarSQL("select id_ultimaRondaJugada from pozos")[0][0]


    def setMontoInicialPozo(self, monto):
        """Asigna el monto inicial del pozo. Si el montoActual y el montoReserva son menores que montoInicial tambien los actualiza."""
        try:
            self.conexion.ejecutarSQL("update pozos set montoInicial = %s"%(monto))
            if int(monto) > self.getMontoActualPozo():
                self.setMontoActualPozo(monto)
            if int(monto) > self.getMontoReservaPozo():
                self.setMontoReservaPozo(monto)
            self.conexion.commit()
            return True
        except Exception, e:
            print "setMontoInicialPozo excepcion: ", e
            self.conexion.rollback()
            return False

    def setMontoActualPozo(self, monto):
        """Asigna el monto actual del pozo"""
        try:
            self.conexion.ejecutarSQL("update pozos set montoActual = %s"%(monto))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setMontoActualPozo excepcion: ", e
            self.conexion.rollback()
            return False

    def setMontoReservaPozo(self, monto):
        """Asigna el monto en reserva del pozo"""
        try:
            self.conexion.ejecutarSQL("update pozos set montoReserva = %s"%(monto))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setMontoReservaPozo excepcion: ", e
            self.conexion.rollback()
            return False

    def setMontoMinimoParaConcursarPozo(self, monto):
        """Asigna el Monto Minimo Para Concursar en el pozo"""
        try:
            self.conexion.ejecutarSQL("update pozos set montoMinimoParaConcursar = %s"%(monto))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setMontoMinimoParaConcursarPozo excepcion: ", e
            self.conexion.rollback()
            return False

    def setFrecuenciaSorteoPozo(self, frecuencia):
        """Asigna la frecuencia de sorteo del pozo"""
        try:
            self.conexion.ejecutarSQL("update pozos set frecuenciaSorteo = %s"%(frecuencia))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setFrecuenciaSorteoPozo excepcion: ", e
            self.conexion.rollback()
            return False

    def setFactorReservaPozo(self, factor):
        """Asigna el Factor Reserva del pozo"""
        try:
            self.conexion.ejecutarSQL("update pozos set factorReserva = %s"%(factor))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setFactorReservaPozo excepcion: ", e
            self.conexion.rollback()
            return False

    def setFactorIncrementoPozo(self, factor):
        """Asigna el Factor Incremento del pozo"""
        try:
            self.conexion.ejecutarSQL("update pozos set factorIncremento = %s"%(factor))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setFactorIncrementoPozo excepcion: ", e
            self.conexion.rollback()
            return False

    def setUltimaRondaJugadaPozo(self, ronda):
        """Asigna el id de la Ultima Ronda Jugada del pozo"""
        try:
            self.conexion.ejecutarSQL("update pozos set id_ultimaRondaJugada = %s"%(ronda))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setUltimaRondaJugadaPozo excepcion: ", e
            self.conexion.rollback()
            return False



    def agregarJugadaPozo(self):
        """Actualiza la ultima ronda jugada del pozo y agrega una jugada al pozo en tabla jugadasPozo"""
        #Queda pendiente el monto pues se actualiza despues de cerradas todas las apuestas de los clientes
        try:
            rondaActual = self.getIdUltimaRonda()
            # escoger aleatoriamente bola a apostar
            id_opcion = self.escogerApuestaPozo()
            self.conexion.ejecutarSQL("update pozos set id_ultimaRondaJugada = %s"%(rondaActual))
            self.conexion.ejecutarSQL("insert into jugadasPozo (fecha, hora, id_pozo, id_ronda, id_opcion) values (DATE('now','localtime'),TIME('now','localtime'),%s,%s,%s)"%(1,rondaActual,id_opcion))
            # actualizo gui del pozo con esta nueva apuesta del pozo para crear expectativa en los clientes...
            try:
                self.clientePozo.actualizarUltimasApuestas(self.getUltimasApuestasPozo(11))
            except Exception, f:
                print "AgregarJugadaPozo :: error al intentar actualizar ultimas apuestas al pozo: ", f
            self.conexion.commit()
            return True
        except Exception, e:
            print "agregarJugadaPozo excepcion: ", e
            self.conexion.rollback()
            return False


    def escogerApuestaPozo(self):
        """Escoge aleatoriamente la bola a la que apostara el pozo"""
        return random.randint(1,11)



    def getUltimasApuestasPozo(self, n):
        """Retorna las n ultimas apuestas del pozo."""
        return self.conexion.ejecutarSQL("select id_opcion from jugadasPozo order by id desc limit %s"%(n))




    def actualizarMontoJugadaPozo(self):
        """Actualiza el monto de la mas reciente jugada del pozo tomando como monto el monto actual del pozo"""
        try:
            jugadaActualPozo = self.getIdUltimaJugadaPozo()
            self.conexion.ejecutarSQL("update jugadasPozo set monto = %s where id = %s"%(self.getMontoActualPozo(),jugadaActualPozo))
            self.conexion.commit()
            return True
        except Exception, e:
            print "actualizarMontoJugadaPozo excepcion: ", e
            self.conexion.rollback()
            return False


    def getIdOpcionUltimaApuestaPozo(self):
        """Retorna el id de la ultima opcion apostada por el pozo"""
        return self.conexion.ejecutarSQL("select id_opcion from jugadasPozo order by id desc")[0][0]
        

    
    # ---
    # --- auxiliares
    # ---

    def getIdUltimaRonda(self):
        """Retorna el id de la ultima ronda"""
        r = self.conexion.ejecutarSQL("select id from rondas order by id desc")
        if r != []:
            return r[0][0]
        else:
            return 0

    def getIdMaquina(self, ip, puerto):
        """Retorna el id de la maquina con el ip y puerto dados"""
        return self.conexion.ejecutarSQL("select id from maquinas where ip='%s' and puerto=%s"%(ip,puerto))[0][0]


    def getIdUltimaJugadaPozo(self):
        """Retorna el ide de la ultima jugada del pozo en jugadasPozo"""
        return self.conexion.ejecutarSQL("select max(id) from jugadasPozo")[0][0]



    # ---
    # --- generales
    # ---

    def getNit(self):
        """Retorna el nit del esferodromo"""
        return self.conexion.ejecutarSQL("select nit from esferodromos")[0][0]


    def getOpciones(self):
        """Retorna las opciones del juego"""
        return self.conexion.ejecutarSQL("select id, desc, id_TipoOpcion from opciones")


    # ---
    # --- Comunicacion con Mega Manager ---
    # ---

    def setMaquinasMegaManager(self, modulos, codigos):
        # modulos: ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']
        # codigos: ['0229', '0231', '0232', '0233', '0234', '0214']
        try:
            for i in range(len(modulos)):
                idMaquina = modulos[i][1:]
                cod = codigos[i]
                self.conexion.ejecutarSQL("update maquinas set codMegaManager = '%s' where id = %s"%(cod, idMaquina))
            self.conexion.commit()
            return True
        except Exception, e:
            print "setMaquinasMegaManager excepcion: ", e
            self.conexion.rollback()
            return False


    def getCodMaquinaMegaManager(self, idMaquina):
        """Dado el id de la maquina, devuelve el codigo en MegaManager"""
        try:
            r = self.conexion.ejecutarSQL("select codMegaManager from maquinas where id = %s"%(idMaquina))[0][0]
            return (True, r)
        except Exception, e:
            print "getCodMaquinaMegaManager excepcion: ", e
            return (False, "")


    def getCodCoordinadorMegaManager(self, idCoordinador):
        """Dado el id del coordinador, devuelve el codigo en MegaManager"""
        try:
            r = self.conexion.ejecutarSQL("select codMegaManager from coordinadores where id = %s"%(idCoordinador))[0][0]
            return (True, r)
        except Exception, e:
            print "getCodCoordinadorMegaManager excepcion: ", e
            return (False, "")


    def getPagosPendientesMegaManager(self):
        """Retorna todos los pagos que esten pendientes de enviar a MegaManager"""
        try:
            r = self.conexion.ejecutarSQL("select p.id, c.codMegaManager, m.codMegaManager, p.valor, idCliente from maquinas m, pagos p left join coordinadores c on p.id_coordinador=c.id where enviadoMegaManager = 'N' and p.id_Maquina = m.id ")
            return r
        except Exception, e:
            print "getPagosPendientesMegaManager excepcion: ", e
            return []


    def getRecargasPendientesMegaManager(self):
        """Retorna todas las recargas manuales que esten pendientes de enviar a MegaManager"""
        try:
            r = self.conexion.ejecutarSQL("select cm.id, valor, m.codMegaManager, c.CodMegaManager from maquinas m, creditosManualesXmaquinas cm left join coordinadores c on cm.id_Coordinador = c.id where enviadoMegaManager = 'N' and cm.id_Maquina = m.id")
            return r
        except Exception, e:
            print "getRecargasPendientesMegaManager excepcion: ", e
            return []


    def actualizarPagoMegaManager(self, idPago, estado, idCliente):
        try:
            self.conexion.ejecutarSQL("update pagos set enviadoMegaManager = '%s', idCliente = '%s' where id=%s"%(estado, idCliente, idPago))
            self.conexion.commit()
            return True
        except Exception, e:
            print "actualizarPagoMegaManager excepcion: ", e
            self.conexion.rollback()
            return False


    def actualizarRecargaManualMegaManager(self, idRecarga, estado):
        try:
            self.conexion.ejecutarSQL("update creditosManualesXmaquinas set enviadoMegaManager = '%s' where id=%s"%(estado, idRecarga))
            self.conexion.commit()
            return True
        except Exception, e:
            print "actualizarRecargaMegaManager excepcion: ", e
            self.conexion.rollback()
            return False


os.chdir(os.getcwd())
# leer ip y puerto de sc.conf
conf = open("sc.conf")
l = conf.readlines()
ip, puerto = l[0][:-1], int(l[1][:-1])
conf.close()
# definicion del servidor y puesta en marcha
s = SimpleXMLRPCServer((ip, puerto), allow_none=True)
s.register_introspection_functions()
s.register_instance(servidorCentral())
s.serve_forever()
