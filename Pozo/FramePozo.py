#Boa:Frame:Frame1

import wx
import wx.lib.newevent
import time
from separadorMiles import *

# necesario para instanciar el servidorPozo
from SimpleXMLRPCServer import *
from servidorPozo import *
import thread

# cliente de servidorCentral
from clientePozoDeServidorCentral import *



# Evento para actualizar el monto actual del pozo
(actualizarMontoEvent, EVT_ACTUALIZAR_MONTO) = wx.lib.newevent.NewEvent()



def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1STATICBITMAPFONDO, 
] = [wx.NewId() for _init_ctrls in range(2)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(0, 0), size=wx.Size(1280, 800),
              style=wx.NO_BORDER, title='Pozo Esferodromo')
        self.SetClientSize(wx.Size(1280, 800))

        self.staticBitmapFondo = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Fondo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAPFONDO,
              name=u'staticBitmapFondo', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1280, 800), style=0)

        self.staticTextMonto = wx.StaticText(label=u'0', name=u'staticTextMonto', parent=self,
              pos=wx.Point(500, 550), size=wx.Size(400, 19), style=wx.ALIGN_RIGHT)
        self.staticTextMonto.SetForegroundColour(wx.Colour(254, 242, 0))
        self.staticTextMonto.SetFont(wx.Font(85, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'Sans'))

        # historia de apuestas del pozo...
        self.staticBitmapApuesta1 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta1', parent=self,
              pos=wx.Point(250, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta2 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta2', parent=self,
              pos=wx.Point(370, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta3 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta3', parent=self,
              pos=wx.Point(490, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta4 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta4', parent=self,
              pos=wx.Point(610, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta5 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta5', parent=self,
              pos=wx.Point(730, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta6 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta6', parent=self,
              pos=wx.Point(850, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta7 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta7', parent=self,
              pos=wx.Point(970, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta8 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta8', parent=self,
              pos=wx.Point(1090, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta9 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta9', parent=self,
              pos=wx.Point(1510, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta10 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta10', parent=self,
              pos=wx.Point(1630, 20), size=wx.Size(120, 120), style=0)

        self.staticBitmapApuesta11 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapApuesta11', parent=self,
              pos=wx.Point(1750, 20), size=wx.Size(120, 120), style=0)


        

    def __init__(self, parent):
        # inicio de interfaz grafica
        try:
            self._init_ctrls(parent)
            self.Bind(EVT_ACTUALIZAR_MONTO, self.actualizarMonto)
            # vinculo los eventos del servidorPozo con este frame
            self.Bind(EVT_ON_ACTUALIZAR_MONTO, self.OnActualizarMonto)
            self.Bind(EVT_ON_ACTUALIZAR_ULTIMAS_APUESTAS, self.OnActualizarUltimasApuestas)
            self.Bind(EVT_ON_POZO_JUGANDO, self.OnPozoJugando)
            self.Bind(EVT_ON_POZO_GANADO, self.OnPozoGanado)
        except Exception, e:
            dlg = wx.MessageDialog(self,'Error al iniciar interfaz grafica: ' + str(e),'Error',wx.ICON_ERROR)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
                self.Destroy()
                
        # configuracion de ip y puerto
        try:
            conf = open("pozo.conf")
            l = conf.readlines()
            self.ip, self.puerto = l[0][:-1], int(l[1][:-1])
            conf.close()
        except Exception, e:
            dlg = wx.MessageDialog(self,'Error al abrir archivo de configuracion: ' + str(e),'Error',wx.ICON_ERROR)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
                self.Destroy()

        # inicio del servidorPozo
        try:
            s = SimpleXMLRPCServer((self.ip, self.puerto))
            s.register_introspection_functions()
            s.register_instance(servidorPozo(self))
            thread.start_new_thread(s.serve_forever, tuple())
        except Exception, e:
            dlg = wx.MessageDialog(self,'Error al iniciar servidorPozo: ' + str(e),'Error',wx.ICON_ERROR)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
                self.Destroy()

        # inicio del cliente del servidor central
        try:
            c = open("sc.conf")
            dirSc = c.readline()[:-1]
            c.close()
            self.cliente = clientePozoDeServidorCentral(dirSc)
        except Exception, e:
            dlg = wx.MessageDialog(self,'Error al iniciar cliente de servidor central: ' + str(e),'Error',wx.ICON_ERROR)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
                self.Destroy()

        # cargar monto actual del pozo desde el servidor central
        try:
            evt = actualizarMontoEvent(valor=self.cliente.getMontoActualPozo())
            wx.PostEvent(self, evt)
        except Exception, e:
            dlg = wx.MessageDialog(self,'Error al cargar monto actual del pozo: ' + str(e),'Error',wx.ICON_ERROR)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
                self.Destroy()

        # cargar ultimas apuestas desde el servidor central
        try:
            self.actualizarUltimasApuestas(self.cliente.getUltimasApuestasPozo(11))
        except Exception, e:
            dlg = wx.MessageDialog(self,'Error al cargar ultimas apuestas: ' + str(e),'Error',wx.ICON_ERROR)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
                self.Destroy()
        


    def OnActualizarMonto(self, evt):
        """Evento invocado por el servidorPozo. Actualiza y hace titilar el monto del pozo"""
        thread.start_new_thread(self.titilarNum, (actualizarMontoEvent, int(self.staticTextMonto.GetLabel().replace(".","")), evt.montoActual, 0.1, 1.5))


    def actualizarMonto(self, evt):
        """Actualiza el monto del pozo con el valor pasado en montoActual"""
        self.staticTextMonto.SetLabel(separadorMiles(evt.valor))



    def titilarNum(self, evento, vInicial, vFinal, dormirXvez, crecimientoX):
        """Hace ver sensacion de crecimiento del numero relacionado al avento dado. Al final titila 3 veces el valor final."""
        i = 1
        while i < vFinal:
            evt = evento(valor=str(vInicial+i))
            wx.PostEvent(self, evt)
            time.sleep(dormirXvez)
            i += int(crecimientoX*i)
        for i in range(3):
            evt = evento(valor="")
            wx.PostEvent(self, evt)
            time.sleep(dormirXvez)
            evt = evento(valor=str(vFinal))
            wx.PostEvent(self, evt)
            time.sleep(dormirXvez)



    def OnActualizarUltimasApuestas(self, evt):
        """Evento invocado por el servidorPozo. Actualiza en la gui las apuestas realizadas por el pozo"""
        self.actualizarUltimasApuestas(evt.ultimasApuestas)


    def actualizarUltimasApuestas(self, bolasApostadas):
        # relucir ultima bola ganadora ... puede ser una barrita dorada debajo
        for i in range(len(bolasApostadas)):
            b = bolasApostadas[i][0]
            if b != None:
                if b == 1:
                    eval("self.staticBitmapApuesta"+str(i+1)+".SetBitmap(wx.Bitmap(u'Imagenes/Bolas/blanca.png',wx.BITMAP_TYPE_PNG))")
                else:
                    eval("self.staticBitmapApuesta"+str(i+1)+".SetBitmap(wx.Bitmap(u'Imagenes/Bolas/"+str(b-1)+".png',wx.BITMAP_TYPE_PNG))")


    def OnPozoJugando(self, evt):
        """Evento invocado por el servidorPozo. Emite sonido para indicar que el pozo esta jugando en la ronda actual"""
        self.pozoJugando()

    def pozoJugando(self):
        # hilos que lanzan sonidos cuando el pozo esta jugando en la ronda en curso
        thread.start_new_thread(os.system, ("playsound --volume 1.0 --loop 2 --seek '00:00:00;00:02:00' Sonidos/pozoJugando.mp3",))
        thread.start_new_thread(os.system, ("playsound --volume 5.0 --seek '00:00:00;00:10:00' Sonidos/timbales.mp3",))
        #thread.start_new_thread(os.system, ("playsound --loop 9 Sonidos/monedaCallendo.wav ",))


    def OnPozoGanado(self, evt):
        """Evento invocado por el servidorPozo. Emite sonidos para indicar que se han ganado el pozo"""
        self.pozoGanado()

    def pozoGanado(self):
        # hilos que lanzan sonidos cuando se han ganado el pozo
        thread.start_new_thread(os.system, ("playsound --volume 1.0 --loop 1 --seek '00:00:00;00:02:00' Sonidos/seHanGanadoElPozo.mp3",))
        thread.start_new_thread(os.system, ("playsound --volume 5.0 --loop 10 Sonidos/tada.wav",))

