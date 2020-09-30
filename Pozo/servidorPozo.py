import wx
import wx.lib.newevent


# Servidor del pozo que atendera las peticiones de actualizar el monto actual y la historia de apuesta que ha hecho el pozo


# This creates a new Event class and a EVT binder function

# Evento para actualizar monto del pozo
(onActualizarMontoEvent, EVT_ON_ACTUALIZAR_MONTO) = wx.lib.newevent.NewEvent()
# Evento para actualizar ultimas apuestas del pozo
(onActualizarUltimasApuestasEvent, EVT_ON_ACTUALIZAR_ULTIMAS_APUESTAS) = wx.lib.newevent.NewEvent()
# Evento para emitir sonido indicando que pozo esta jugando en la ronda actual
(onPozoJugandoEvent, EVT_ON_POZO_JUGANDO) = wx.lib.newevent.NewEvent()
# Evento para emitir sonido indicando que se han ganado el pozo
(onPozoGanadoEvent, EVT_ON_POZO_GANADO) = wx.lib.newevent.NewEvent()



class servidorPozo:
    def __init__(self, framePozo):
        self.framePozo = framePozo
        print "servidorPozo inicializado"

        
    def actualizarMonto(self, monto):
        """Lanza evento que actualiza el monto del pozo"""
        try:
            evt = onActualizarMontoEvent(montoActual=monto)
            wx.PostEvent(self.framePozo, evt)
            return True
        except Exception, e:
            print "servidorPozo::actualizarMonto = ", e
            return False


    def actualizarUltimasApuestas(self, apuestas):
        """Lanza evento que actualiza las ultimas apuestas realizadas por el pozo"""
        try:
            evt = onActualizarUltimasApuestasEvent(ultimasApuestas=apuestas)
            wx.PostEvent(self.framePozo, evt)
            return True
        except Exception, e:
            print "servidorPozo::actualizarUltimasApuestas = ", e
            return False


    def pozoJugando(self):
        """Lanza evento que emite sonido para indicar que el pozo esta jugando en la ronda actual"""
        try:
            evt = onPozoJugandoEvent()
            wx.PostEvent(self.framePozo, evt)
            return True
        except Exception, e:
            print "servidorPozo::pozoJugando = ", e
            return False


    def pozoGanado(self):
        """Lanza evento que emite sonido para indicar que se han ganado el pozo"""
        try:
            evt = onPozoGanadoEvent()
            wx.PostEvent(self.framePozo, evt)
            return True
        except Exception, e:
            print "servidorPozo::pozoGanado = ", e
            return False

    
