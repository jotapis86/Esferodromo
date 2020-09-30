#Boa:Frame:Frame1

import wx
import wx.calendar
import os
import md5
import time
from clienteCoordinadorDeServidorCentral import *
from clienteCoordinadorDeServidorMaquina import *
from clienteCoordinadorDeServidorPozo import *
from clienteCoordinadorDeMegaManager import *
import tecladoNumerico
from separadorMiles import *
import random

# Reporte con historia de jugadas hechas por un cliente
from frameHistoriaJugadas import frameHistoriaJugadas


# Numero de opciones para apostar
__NUM_OPCIONES__ = 11

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON0, wxID_FRAME1BUTTON00, wxID_FRAME1BUTTON1, 
 wxID_FRAME1BUTTON11, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON22, 
 wxID_FRAME1BUTTON3, wxID_FRAME1BUTTON33, wxID_FRAME1BUTTON4, 
 wxID_FRAME1BUTTON44, wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON55, 
 wxID_FRAME1BUTTON6, wxID_FRAME1BUTTON66, wxID_FRAME1BUTTON7, 
 wxID_FRAME1BUTTON77, wxID_FRAME1BUTTON8, wxID_FRAME1BUTTON88, 
 wxID_FRAME1BUTTON9, wxID_FRAME1BUTTON99, wxID_FRAME1BUTTONA, 
 wxID_FRAME1BUTTONABRIRRONDA, wxID_FRAME1BUTTONACEPTAR, 
 wxID_FRAME1BUTTONACEPTARCAMBIARCLAVE, wxID_FRAME1BUTTONACEPTARCAMBIOMONEDA, 
 wxID_FRAME1BUTTONACEPTARCAMBIOOPCION, wxID_FRAME1BUTTONACEPTARPAGO, 
 wxID_FRAME1BUTTONAGREGAR, wxID_FRAME1BUTTONAGREGARCOORDINADOR, 
 wxID_FRAME1BUTTONB, wxID_FRAME1BUTTONBORRAR, wxID_FRAME1BUTTONBORRARBORRAR, 
 wxID_FRAME1BUTTONC, wxID_FRAME1BUTTONCAMBIARCLAVE, 
 wxID_FRAME1BUTTONCANCELARCAMBIARCLAVE, wxID_FRAME1BUTTONCANCELARCAMBIOMONEDA, 
 wxID_FRAME1BUTTONCANCELARCAMBIOOPCION, wxID_FRAME1BUTTONCANCELARCOORDINADOR, 
 wxID_FRAME1BUTTONCANCELARPAGO, wxID_FRAME1BUTTONCANCELARRONDA, 
 wxID_FRAME1BUTTONCERRARAPUESTAS, wxID_FRAME1BUTTONCERRARSESION, 
 wxID_FRAME1BUTTOND, wxID_FRAME1BUTTONE, wxID_FRAME1BUTTONELIMINAR, 
 wxID_FRAME1BUTTONESPACIO, wxID_FRAME1BUTTONF, wxID_FRAME1BUTTONG, 
 wxID_FRAME1BUTTONGUARDAR, wxID_FRAME1BUTTONH, wxID_FRAME1BUTTONI, 
 wxID_FRAME1BUTTONJ, wxID_FRAME1BUTTONK, wxID_FRAME1BUTTONL, 
 wxID_FRAME1BUTTONM, wxID_FRAME1BUTTONMENUADMINISTRADOR, 
 wxID_FRAME1BUTTONMENUBILLETES, wxID_FRAME1BUTTONMENUCOORDINADORES, 
 wxID_FRAME1BUTTONMENUCUADRE, wxID_FRAME1BUTTONMENUMONEDAS, 
 wxID_FRAME1BUTTONMENUOPCIONES, wxID_FRAME1BUTTONMENUPAGOS, 
 wxID_FRAME1BUTTONMENURONDAS, wxID_FRAME1BUTTONMENUSALIR, wxID_FRAME1BUTTONN, 
 wxID_FRAME1BUTTONNUMERO0, wxID_FRAME1BUTTONNUMERO1, wxID_FRAME1BUTTONNUMERO2, 
 wxID_FRAME1BUTTONNUMERO3, wxID_FRAME1BUTTONNUMERO4, wxID_FRAME1BUTTONNUMERO5, 
 wxID_FRAME1BUTTONNUMERO6, wxID_FRAME1BUTTONNUMERO7, wxID_FRAME1BUTTONNUMERO8, 
 wxID_FRAME1BUTTONNUMERO9, wxID_FRAME1BUTTONNUMEROBORRAR, wxID_FRAME1BUTTONO, 
 wxID_FRAME1BUTTONP, wxID_FRAME1BUTTONPAGOS, wxID_FRAME1BUTTONPUNTO, 
 wxID_FRAME1BUTTONQ, wxID_FRAME1BUTTONR, wxID_FRAME1BUTTONRONDAS, 
 wxID_FRAME1BUTTONS, wxID_FRAME1BUTTONT, wxID_FRAME1BUTTONTECLADOBORRAR, 
 wxID_FRAME1BUTTONU, wxID_FRAME1BUTTONV, wxID_FRAME1BUTTONVOLVERCLAVE, 
 wxID_FRAME1BUTTONW, wxID_FRAME1BUTTONX, wxID_FRAME1BUTTONY, 
 wxID_FRAME1BUTTONZ, wxID_FRAME1CALENDARCTRLBILLETES1, 
 wxID_FRAME1CALENDARCTRLBILLETES2, wxID_FRAME1CALENDARCTRLCUADRE1, 
 wxID_FRAME1CALENDARCTRLCUADRE2, wxID_FRAME1CALENDARCTRLPAGOS1, 
 wxID_FRAME1CALENDARCTRLPAGOS2, wxID_FRAME1CALENDARCTRLRONDAS1, 
 wxID_FRAME1CALENDARCTRLRONDAS2, wxID_FRAME1LISTCTRLADMINCOORDINADORES, 
 wxID_FRAME1LISTCTRLBILLETES, wxID_FRAME1LISTCTRLCOORDINADORES, 
 wxID_FRAME1LISTCTRLCUADRE, wxID_FRAME1LISTCTRLPAGOS, 
 wxID_FRAME1LISTCTRLRONDAS, wxID_FRAME1PANELADMINADMINISTRADOR, 
 wxID_FRAME1PANELADMINBILLETES, wxID_FRAME1PANELADMINCOORDINADORES, 
 wxID_FRAME1PANELADMINCUADRE, wxID_FRAME1PANELADMINISTRADOR, 
 wxID_FRAME1PANELADMINMONEDAS, wxID_FRAME1PANELADMINOPCIONES, 
 wxID_FRAME1PANELADMINPAGOS, wxID_FRAME1PANELADMINRONDAS, 
 wxID_FRAME1PANELAGREGARCOORDINADOR, wxID_FRAME1PANELCALCUMONTO, 
 wxID_FRAME1PANELCLAVE, wxID_FRAME1PANELCOORDINADORES, 
 wxID_FRAME1PANELGUARDAR, wxID_FRAME1PANELMAQUINA1, wxID_FRAME1PANELMAQUINA2, 
 wxID_FRAME1PANELMAQUINA3, wxID_FRAME1PANELMAQUINA4, wxID_FRAME1PANELMAQUINA5, 
 wxID_FRAME1PANELMAQUINA6, wxID_FRAME1PANELMENUADMINISTRADOR, 
 wxID_FRAME1PANELMENUPRINCIPAL, wxID_FRAME1PANELMONTOPAGOS, 
 wxID_FRAME1PANELNUMEROS, wxID_FRAME1PANELPAGNO, wxID_FRAME1PANELPAGOS, 
 wxID_FRAME1PANELRONDAS, wxID_FRAME1PANELTECLADO, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICBITMAP10, wxID_FRAME1STATICBITMAP2, 
 wxID_FRAME1STATICBITMAP3, wxID_FRAME1STATICBITMAP4, wxID_FRAME1STATICBITMAP5, 
 wxID_FRAME1STATICBITMAP6, wxID_FRAME1STATICBITMAP7, wxID_FRAME1STATICBITMAP8, 
 wxID_FRAME1STATICBITMAP9, wxID_FRAME1STATICBITMAPBLANCA, 
 wxID_FRAME1STATICBITMAPMAQUINA1, wxID_FRAME1STATICBITMAPMAQUINA2, 
 wxID_FRAME1STATICBITMAPMAQUINA3, wxID_FRAME1STATICBITMAPMAQUINA4, 
 wxID_FRAME1STATICBITMAPMAQUINA5, wxID_FRAME1STATICBITMAPMAQUINA6, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, 
 wxID_FRAME1STATICTEXT11, wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, 
 wxID_FRAME1STATICTEXT14, wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT16, 
 wxID_FRAME1STATICTEXT17, wxID_FRAME1STATICTEXT18, wxID_FRAME1STATICTEXT19, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT20, wxID_FRAME1STATICTEXT21, 
 wxID_FRAME1STATICTEXT22, wxID_FRAME1STATICTEXT23, wxID_FRAME1STATICTEXT24, 
 wxID_FRAME1STATICTEXT25, wxID_FRAME1STATICTEXT26, wxID_FRAME1STATICTEXT27, 
 wxID_FRAME1STATICTEXT28, wxID_FRAME1STATICTEXT29, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT30, wxID_FRAME1STATICTEXT31, wxID_FRAME1STATICTEXT32, 
 wxID_FRAME1STATICTEXT33, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT64, wxID_FRAME1STATICTEXT7, 
 wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, 
 wxID_FRAME1STATICTEXTCOORDINADOR, wxID_FRAME1STATICTEXTDISPONIBLE, 
 wxID_FRAME1STATICTEXTERRORFECHARONDAS, 
 wxID_FRAME1STATICTEXTFECHAVALORESMONEDASVIGENTES, 
 wxID_FRAME1STATICTEXTMONTODISPONIBLE, wxID_FRAME1STATICTEXTMSG, 
 wxID_FRAME1STATICTEXTMSGAGREGARCOORDINADOR, 
 wxID_FRAME1STATICTEXTMSGCAMBIARCLAVEADMIN, wxID_FRAME1STATICTEXTMSGCLAVE, 
 wxID_FRAME1STATICTEXTPAGAR, wxID_FRAME1TEXTCTRLCHANZAMAXIMO, 
 wxID_FRAME1TEXTCTRLCHANZAMINIMO, wxID_FRAME1TEXTCTRLCHANZAPAGAPOR, 
 wxID_FRAME1TEXTCTRLCLAVE, wxID_FRAME1TEXTCTRLCLAVEACTUAL, 
 wxID_FRAME1TEXTCTRLCLAVENUEVA, wxID_FRAME1TEXTCTRLCLAVENUEVOCOORDINADOR, 
 wxID_FRAME1TEXTCTRLCONFIRMARCLAVENUEVA, wxID_FRAME1TEXTCTRLCUADROMAXIMO, 
 wxID_FRAME1TEXTCTRLCUADROMINIMO, wxID_FRAME1TEXTCTRLCUADROPAGAPOR, 
 wxID_FRAME1TEXTCTRLMEDIOMAXIMO, wxID_FRAME1TEXTCTRLMEDIOMINIMO, 
 wxID_FRAME1TEXTCTRLMEDIOPAGAPOR, wxID_FRAME1TEXTCTRLMONEDA1, 
 wxID_FRAME1TEXTCTRLMONEDA2, wxID_FRAME1TEXTCTRLMONEDA3, 
 wxID_FRAME1TEXTCTRLMONEDA4, wxID_FRAME1TEXTCTRLMONEDA5, 
 wxID_FRAME1TEXTCTRLNOMBRENUEVOCOORDINADOR, wxID_FRAME1TEXTCTRLPAGAR, 
 wxID_FRAME1TEXTCTRLPLENOMAXIMO, wxID_FRAME1TEXTCTRLPLENOMINIMO, 
 wxID_FRAME1TEXTCTRLPLENOPAGAPOR, 
] = [wx.NewId() for _init_ctrls in range(222)]

class Frame1(wx.Frame):
    def _init_coll_listCtrlGanadoresPozo_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER, heading=u'Maquina', width=100)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER, heading=u'Monto Ganado', width=200)
        
    def _init_coll_listCtrlCreditosManuales_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER, heading=u'Fecha', width=100)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER, heading=u'Hora', width=100)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER, heading=u'Coordinador', width=260)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER, heading=u'Maquina', width=70)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_CENTER, heading=u'Valor', width=120)
        
    def _init_coll_listCtrlPagos_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER,
              heading=u'Coordinador', width=260)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER,
              heading=u'Maquina', width=70)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER,
              heading=u'Valor', width=120)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER,
              heading=u'Fecha', width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_CENTER,
              heading=u'Hora', width=100)

    def _init_coll_listCtrlCoordinadores_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER,
              heading=u'Coordinadores', width=1280)

    def _init_coll_listCtrlRondas_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER, heading=u'Id',
              width=50)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER,
              heading=u'Fecha', width=100)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER,
              heading=u'Hora Inicio', width=85)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER,
              heading=u'Hora Fin', width=85)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_CENTER,
              heading=u'Ganadora', width=80)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_CENTER,
              heading=u'Coordinador', width=250)

    def _init_coll_listCtrlCuadre_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER,
              heading=u'Maquina', width=70)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER,
              heading=u'Concepto', width=80)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER,
              heading=u'Entradas', width=170)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER,
              heading=u'Salidas', width=170)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_CENTER,
              heading=u'Cuadre', width=160)

    def _init_coll_listCtrlBilletes_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER,
              heading=u'Maquina', width=100)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER,
              heading=u'Denominacion', width=250)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER,
              heading=u'Cantidad', width=300)

    def _init_coll_listCtrlAdminCoordinadores_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER,
              heading=u'Coordinadores', width=460)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(0, 0), size=wx.Size(1280, 1024), style=0,
              title=u'Coordinador Esferodromo')
        self.SetClientSize(wx.Size(1280, 1024))

        self.panelClave = wx.Panel(id=wxID_FRAME1PANELCLAVE, name=u'panelClave',
              parent=self, pos=wx.Point(362, 300), size=wx.Size(300, 360),
              style=wx.TAB_TRAVERSAL)
        self.panelClave.Show(False)

        self.buttonVolverClave = wx.Button(id=wxID_FRAME1BUTTONVOLVERCLAVE,
              label=u'Volver', name=u'buttonVolverClave',
              parent=self.panelClave, pos=wx.Point(200, 40), size=wx.Size(99,
              50), style=0)
        self.buttonVolverClave.Bind(wx.EVT_BUTTON,
              self.OnButtonVolverClaveButton, id=wxID_FRAME1BUTTONVOLVERCLAVE)

        self.button0 = wx.Button(id=wxID_FRAME1BUTTON0, label=u'0',
              name=u'button0', parent=self.panelClave, pos=wx.Point(5, 260),
              size=wx.Size(147, 50), style=0)
        self.button0.Bind(wx.EVT_BUTTON, self.OnButton0Button,
              id=wxID_FRAME1BUTTON0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'1',
              name='button1', parent=self.panelClave, pos=wx.Point(5, 205),
              size=wx.Size(60, 50), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'2',
              name='button2', parent=self.panelClave, pos=wx.Point(70, 205),
              size=wx.Size(60, 50), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'3',
              name='button3', parent=self.panelClave, pos=wx.Point(135, 205),
              size=wx.Size(60, 50), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'4',
              name='button4', parent=self.panelClave, pos=wx.Point(5, 150),
              size=wx.Size(60, 50), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label=u'5',
              name='button5', parent=self.panelClave, pos=wx.Point(70, 150),
              size=wx.Size(60, 50), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BUTTON5)

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6, label=u'6',
              name='button6', parent=self.panelClave, pos=wx.Point(135, 150),
              size=wx.Size(60, 50), style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_FRAME1BUTTON6)

        self.button7 = wx.Button(id=wxID_FRAME1BUTTON7, label=u'7',
              name='button7', parent=self.panelClave, pos=wx.Point(5, 95),
              size=wx.Size(60, 50), style=0)
        self.button7.Bind(wx.EVT_BUTTON, self.OnButton7Button,
              id=wxID_FRAME1BUTTON7)

        self.button8 = wx.Button(id=wxID_FRAME1BUTTON8, label=u'8',
              name='button8', parent=self.panelClave, pos=wx.Point(70, 95),
              size=wx.Size(60, 50), style=0)
        self.button8.Bind(wx.EVT_BUTTON, self.OnButton8Button,
              id=wxID_FRAME1BUTTON8)

        self.button9 = wx.Button(id=wxID_FRAME1BUTTON9, label=u'9',
              name='button9', parent=self.panelClave, pos=wx.Point(135, 95),
              size=wx.Size(60, 50), style=0)
        self.button9.Bind(wx.EVT_BUTTON, self.OnButton9Button,
              id=wxID_FRAME1BUTTON9)

        self.buttonBorrar = wx.Button(id=wxID_FRAME1BUTTONBORRAR,
              label=u'Borrar', name=u'buttonBorrar', parent=self.panelClave,
              pos=wx.Point(152, 260), size=wx.Size(147, 50), style=0)
        self.buttonBorrar.Bind(wx.EVT_BUTTON, self.OnButtonBorrarButton,
              id=wxID_FRAME1BUTTONBORRAR)

        self.buttonAceptar = wx.Button(id=wxID_FRAME1BUTTONACEPTAR,
              label=u'Aceptar', name=u'buttonAceptar', parent=self.panelClave,
              pos=wx.Point(200, 95), size=wx.Size(99, 160), style=0)
        self.buttonAceptar.Bind(wx.EVT_BUTTON, self.OnButtonAceptarButton,
              id=wxID_FRAME1BUTTONACEPTAR)

        self.textCtrlClave = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCLAVE,
              name=u'textCtrlClave', parent=self.panelClave, pos=wx.Point(5,
              40), size=wx.Size(190, 50), style=wx.TE_CENTER | wx.TE_PASSWORD,
              value=u'')
        self.textCtrlClave.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.panelCoordinadores = wx.Panel(id=wxID_FRAME1PANELCOORDINADORES,
              name=u'panelCoordinadores', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1280, 1024), style=wx.TAB_TRAVERSAL)

        self.listCtrlCoordinadores = wx.ListCtrl(id=wxID_FRAME1LISTCTRLCOORDINADORES,
              name=u'listCtrlCoordinadores', parent=self.panelCoordinadores,
              pos=wx.Point(0, 0), size=wx.Size(1280, 1024),
              style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_ICON)
        self.listCtrlCoordinadores.SetFont(wx.Font(32, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.listCtrlCoordinadores.SetBackgroundColour(wx.Colour(246, 243, 241))
        self._init_coll_listCtrlCoordinadores_Columns(self.listCtrlCoordinadores)
        self.listCtrlCoordinadores.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnListCtrlCoordinadoresListItemSelected,
              id=wxID_FRAME1LISTCTRLCOORDINADORES)

        self.staticTextMsgClave = wx.StaticText(id=wxID_FRAME1STATICTEXTMSGCLAVE,
              label=u'', name=u'staticTextMsgClave', parent=self.panelClave,
              pos=wx.Point(10, 10), size=wx.Size(280, 26),
              style=wx.ALIGN_CENTRE)
        self.staticTextMsgClave.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL,
              wx.BOLD, False, u'Sans'))

        self.panelMenuPrincipal = wx.Panel(id=wxID_FRAME1PANELMENUPRINCIPAL,
              name=u'panelMenuPrincipal', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1280, 100), style=wx.TAB_TRAVERSAL)
        self.panelMenuPrincipal.Show(False)

        self.buttonRondas = wx.Button(id=wxID_FRAME1BUTTONRONDAS,
              label=u'Rondas', name=u'buttonRondas',
              parent=self.panelMenuPrincipal, pos=wx.Point(160, 10),
              size=wx.Size(110, 60), style=0)
        self.buttonRondas.Bind(wx.EVT_BUTTON, self.OnButtonRondasButton,
              id=wxID_FRAME1BUTTONRONDAS)

        self.buttonPagos = wx.Button(id=wxID_FRAME1BUTTONPAGOS, label=u'Maquinas',
              name=u'buttonPagos', parent=self.panelMenuPrincipal,
              pos=wx.Point(290, 10), size=wx.Size(110, 60), style=0)
        self.buttonPagos.Bind(wx.EVT_BUTTON, self.OnButtonPagosButton,
              id=wxID_FRAME1BUTTONPAGOS)

        # --- para sincronizar con MegaManager
        self.buttonSincronizarMegaManager = wx.Button(id=wx.NewId(), label=u'Sincronizar con\n MegaManager', parent=self.panelMenuPrincipal,
                                                      pos=wx.Point(500, 10), size=wx.Size(110, 60), style=0)
        self.buttonSincronizarMegaManager.Bind(wx.EVT_BUTTON, self.OnButtonSincronizarMegaManagerButton)
        # ---

        self.panelRondas = wx.Panel(id=wxID_FRAME1PANELRONDAS,
              name=u'panelRondas', parent=self, pos=wx.Point(0, 100),
              size=wx.Size(1280, 924), style=wx.TAB_TRAVERSAL)
        self.panelRondas.Show(False)

        self.staticTextCoordinador = wx.StaticText(id=wxID_FRAME1STATICTEXTCOORDINADOR,
              label=u'', name=u'staticTextCoordinador',
              parent=self.panelMenuPrincipal, pos=wx.Point(813, 75),
              size=wx.Size(201, 23), style=wx.ALIGN_RIGHT)
        self.staticTextCoordinador.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC,
              wx.BOLD, False, u'Sans'))

        self.panelPagos = wx.Panel(id=wxID_FRAME1PANELPAGOS, name=u'panelPagos',
              parent=self, pos=wx.Point(0, 100), size=wx.Size(1280, 924),
              style=wx.TAB_TRAVERSAL)
        self.panelPagos.Show(False)

        self.buttonAbrirRonda = wx.Button(id=wxID_FRAME1BUTTONABRIRRONDA,
              label=u'Abrir Ronda', name=u'buttonAbrirRonda',
              parent=self.panelRondas, pos=wx.Point(894, 313), size=wx.Size(120,
              100), style=0)
        self.buttonAbrirRonda.Bind(wx.EVT_BUTTON, self.OnButtonAbrirRondaButton,
              id=wxID_FRAME1BUTTONABRIRRONDA)

        self.buttonCerrarApuestas = wx.Button(id=wxID_FRAME1BUTTONCERRARAPUESTAS,
              label=u'Cerrar Apuestas', name=u'buttonCerrarApuestas',
              parent=self.panelRondas, pos=wx.Point(894, 198), size=wx.Size(120,
              100), style=0)
        self.buttonCerrarApuestas.Show(True)
        self.buttonCerrarApuestas.Enable(False)
        self.buttonCerrarApuestas.Bind(wx.EVT_BUTTON,
              self.OnButtonCerrarApuestasButton,
              id=wxID_FRAME1BUTTONCERRARAPUESTAS)

        self.buttonCerrarSesion = wx.Button(id=wxID_FRAME1BUTTONCERRARSESION,
              label=u'Cerrar Sesion', name=u'buttonCerrarSesion',
              parent=self.panelMenuPrincipal, pos=wx.Point(774, 10),
              size=wx.Size(110, 60), style=0)
        self.buttonCerrarSesion.Bind(wx.EVT_BUTTON,
              self.OnButtonCerrarSesionButton,
              id=wxID_FRAME1BUTTONCERRARSESION)

        self.panelPagno = wx.Panel(id=wxID_FRAME1PANELPAGNO, name=u'panelPagno',
              parent=self.panelRondas, pos=wx.Point(5, 5), size=wx.Size(885,
              600), style=wx.TAB_TRAVERSAL)
        self.panelPagno.Enable(False)

        self.staticBitmapBlanca = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/blanca.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAPBLANCA,
              name=u'staticBitmapBlanca', parent=self.panelPagno,
              pos=wx.Point(70, 240), size=wx.Size(120, 120), style=0)
        self.staticBitmapBlanca.Bind(wx.EVT_LEFT_UP,
              self.OnStaticBitmapBlancaLeftUp)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/1.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panelPagno, pos=wx.Point(195,
              178), size=wx.Size(120, 120), style=0)
        self.staticBitmap1.SetBackgroundColour(wx.Colour(238, 234, 230))
        self.staticBitmap1.SetForegroundColour(wx.Colour(0, 255, 0))
        self.staticBitmap1.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap1LeftUp)

        self.staticBitmap2 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/2.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP2,
              name='staticBitmap2', parent=self.panelPagno, pos=wx.Point(195,
              303), size=wx.Size(120, 120), style=0)
        self.staticBitmap2.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap2LeftUp)

        self.staticBitmap3 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/3.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP3,
              name='staticBitmap3', parent=self.panelPagno, pos=wx.Point(320,
              303), size=wx.Size(120, 120), style=0)
        self.staticBitmap3.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap3LeftUp)

        self.staticBitmap4 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/4.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP4,
              name='staticBitmap4', parent=self.panelPagno, pos=wx.Point(320,
              178), size=wx.Size(120, 120), style=0)
        self.staticBitmap4.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap4LeftUp)

        self.staticBitmap5 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/5.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP5,
              name='staticBitmap5', parent=self.panelPagno, pos=wx.Point(445,
              178), size=wx.Size(120, 120), style=0)
        self.staticBitmap5.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap5LeftUp)

        self.staticBitmap6 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/6.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP6,
              name='staticBitmap6', parent=self.panelPagno, pos=wx.Point(445,
              303), size=wx.Size(120, 120), style=0)
        self.staticBitmap6.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap6LeftUp)

        self.staticBitmap7 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/7.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP7,
              name='staticBitmap7', parent=self.panelPagno, pos=wx.Point(570,
              303), size=wx.Size(120, 120), style=0)
        self.staticBitmap7.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap7LeftUp)

        self.staticBitmap8 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/8.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP8,
              name='staticBitmap8', parent=self.panelPagno, pos=wx.Point(570,
              178), size=wx.Size(120, 120), style=0)
        self.staticBitmap8.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap8LeftUp)

        self.staticBitmap9 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/9.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP9,
              name='staticBitmap9', parent=self.panelPagno, pos=wx.Point(695,
              178), size=wx.Size(120, 120), style=0)
        self.staticBitmap9.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap9LeftUp)

        self.staticBitmap10 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Bolas/10.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP10,
              name='staticBitmap10', parent=self.panelPagno, pos=wx.Point(695,
              303), size=wx.Size(120, 120), style=0)
        self.staticBitmap10.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap10LeftUp)

        self.panelMaquina1 = wx.Panel(id=wxID_FRAME1PANELMAQUINA1,
              name=u'panelMaquina1', parent=self.panelPagos, pos=wx.Point(50,
              50), size=wx.Size(120, 150), style=wx.TAB_TRAVERSAL)

        self.panelMaquina2 = wx.Panel(id=wxID_FRAME1PANELMAQUINA2,
              name=u'panelMaquina2', parent=self.panelPagos, pos=wx.Point(250,
              50), size=wx.Size(120, 150), style=wx.TAB_TRAVERSAL)

        self.panelMaquina3 = wx.Panel(id=wxID_FRAME1PANELMAQUINA3,
              name=u'panelMaquina3', parent=self.panelPagos, pos=wx.Point(450,
              50), size=wx.Size(120, 150), style=wx.TAB_TRAVERSAL)

        self.panelMaquina4 = wx.Panel(id=wxID_FRAME1PANELMAQUINA4,
              name=u'panelMaquina4', parent=self.panelPagos, pos=wx.Point(50,
              250), size=wx.Size(120, 150), style=wx.TAB_TRAVERSAL)

        self.panelMaquina5 = wx.Panel(id=wxID_FRAME1PANELMAQUINA5,
              name=u'panelMaquina5', parent=self.panelPagos, pos=wx.Point(250,
              250), size=wx.Size(120, 150), style=wx.TAB_TRAVERSAL)

        self.panelMaquina6 = wx.Panel(id=wxID_FRAME1PANELMAQUINA6,
              name=u'panelMaquina6', parent=self.panelPagos, pos=wx.Point(450,
              250), size=wx.Size(120, 150), style=wx.TAB_TRAVERSAL)

        self.panelMaquina7 = wx.Panel(name=u'panelMaquina7', parent=self.panelPagos, pos=wx.Point(50,
              450), size=wx.Size(120, 150), style=wx.TAB_TRAVERSAL)
        self.panelMaquina7.Show(False)

        self.panelMaquina8 = wx.Panel(name=u'panelMaquina8', parent=self.panelPagos, pos=wx.Point(250,
              450), size=wx.Size(120, 150), style=wx.TAB_TRAVERSAL)
        self.panelMaquina8.Show(False)

        self.staticBitmapMaquina1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Monitores/monitor.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAPMAQUINA1,
              name=u'staticBitmapMaquina1', parent=self.panelMaquina1,
              pos=wx.Point(0, 0), size=wx.Size(120, 120), style=0)
        self.staticBitmapMaquina1.Bind(wx.EVT_LEFT_UP,
              self.OnStaticBitmapMaquina1LeftUp)

        self.staticBitmapMaquina2 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Monitores/monitor.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAPMAQUINA2,
              name=u'staticBitmapMaquina2', parent=self.panelMaquina2,
              pos=wx.Point(0, 0), size=wx.Size(120, 120), style=0)
        self.staticBitmapMaquina2.Bind(wx.EVT_LEFT_UP,
              self.OnStaticBitmapMaquina2LeftUp)

        self.staticBitmapMaquina3 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Monitores/monitor.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAPMAQUINA3,
              name=u'staticBitmapMaquina3', parent=self.panelMaquina3,
              pos=wx.Point(0, 0), size=wx.Size(120, 120), style=0)
        self.staticBitmapMaquina3.Bind(wx.EVT_LEFT_UP,
              self.OnStaticBitmapMaquina3LeftUp)

        self.staticBitmapMaquina4 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Monitores/monitor.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAPMAQUINA4,
              name=u'staticBitmapMaquina4', parent=self.panelMaquina4,
              pos=wx.Point(0, 0), size=wx.Size(120, 120), style=0)
        self.staticBitmapMaquina4.Bind(wx.EVT_LEFT_UP,
              self.OnStaticBitmapMaquina4LeftUp)

        self.staticBitmapMaquina5 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Monitores/monitor.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAPMAQUINA5,
              name=u'staticBitmapMaquina5', parent=self.panelMaquina5,
              pos=wx.Point(0, 0), size=wx.Size(120, 120), style=0)
        self.staticBitmapMaquina5.Bind(wx.EVT_LEFT_UP,
              self.OnStaticBitmapMaquina5LeftUp)

        self.staticBitmapMaquina6 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Monitores/monitor.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAPMAQUINA6,
              name=u'staticBitmapMaquina6', parent=self.panelMaquina6,
              pos=wx.Point(0, 0), size=wx.Size(120, 120), style=0)
        self.staticBitmapMaquina6.Bind(wx.EVT_LEFT_UP,
              self.OnStaticBitmapMaquina6LeftUp)

        self.staticBitmapMaquina7 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Monitores/monitor.png',
              wx.BITMAP_TYPE_PNG), name=u'staticBitmapMaquina7', parent=self.panelMaquina7,
              pos=wx.Point(0, 0), size=wx.Size(120, 120), style=0)
        self.staticBitmapMaquina7.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmapMaquina7LeftUp)

        self.staticBitmapMaquina8 = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/Monitores/monitor.png',
              wx.BITMAP_TYPE_PNG), name=u'staticBitmapMaquina8', parent=self.panelMaquina8,
              pos=wx.Point(0, 0), size=wx.Size(120, 120), style=0)
        self.staticBitmapMaquina8.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmapMaquina8LeftUp)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=u'1',
              name='staticText1', parent=self.panelMaquina1, pos=wx.Point(56,
              120), size=wx.Size(12, 23), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label=u'2',
              name='staticText2', parent=self.panelMaquina2, pos=wx.Point(56,
              120), size=wx.Size(12, 23), style=0)
        self.staticText2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3, label=u'3',
              name='staticText3', parent=self.panelMaquina3, pos=wx.Point(56,
              120), size=wx.Size(12, 23), style=0)
        self.staticText3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4, label=u'4',
              name='staticText4', parent=self.panelMaquina4, pos=wx.Point(56,
              120), size=wx.Size(12, 23), style=0)
        self.staticText4.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5, label=u'5',
              name='staticText5', parent=self.panelMaquina5, pos=wx.Point(56,
              120), size=wx.Size(12, 23), style=0)
        self.staticText5.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6, label=u'6',
              name='staticText6', parent=self.panelMaquina6, pos=wx.Point(56,
              120), size=wx.Size(12, 23), style=0)
        self.staticText6.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText7 = wx.StaticText(label=u'7', name='staticText7', parent=self.panelMaquina7,
                                         pos=wx.Point(56,120), size=wx.Size(12, 23), style=0)
        self.staticText7.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticText8 = wx.StaticText(label=u'8', name='staticText8', parent=self.panelMaquina8,
                                         pos=wx.Point(56,120), size=wx.Size(12, 23), style=0)
        self.staticText8.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))


        # panel monto pagos

        self.panelMontoPagos = wx.Panel(id=wxID_FRAME1PANELMONTOPAGOS,
              name=u'panelMontoPagos', parent=self.panelPagos, pos=wx.Point(650,
              50), size=wx.Size(400, 500), style=wx.TAB_TRAVERSAL)
        self.panelMontoPagos.Show(False)

        # Inicio Historia de jugadas de una maquina:
        
        # boton para sacar reporte de historico de jugadas
        self.buttonHistoriaJugadas = wx.Button(id=wx.NewId(), label=u'Jugadas', parent=self.panelMontoPagos,
                                               pos=wx.Point(305, 8), size=wx.Size(95, 40), style=0)
        self.buttonHistoriaJugadas.Bind(wx.EVT_BUTTON, self.OnButtonHistoriaJugadasButton)
        
        # Fin Historia de Jugadas de una maquina.

        # static box maquina disponible
        self.staticBoxDisponible = wx.StaticBox(label='', name='staticBoxDisponible', parent=self.panelMontoPagos,
              pos=wx.Point(0, 0), size=wx.Size(300, 50), style=0)

        self.staticTextDisponible = wx.StaticText(id=wxID_FRAME1STATICTEXTDISPONIBLE, label=u'Disponible', name=u'staticTextDisponible',
              parent=self.panelMontoPagos, pos=wx.Point(10, 20), size=wx.Size(95,23), style=0)
        self.staticTextDisponible.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextMontoDisponible = wx.StaticText(id=wxID_FRAME1STATICTEXTMONTODISPONIBLE, label=u'', name=u'staticTextMontoDisponible',
              parent=self.panelMontoPagos, pos=wx.Point(129, 20), size=wx.Size(150, 35), style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        self.staticTextMontoDisponible.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        # static box pagos
        self.staticBoxPagos = wx.StaticBox(label='Pago', name='staticBoxPagos', parent=self.panelMontoPagos,
              pos=wx.Point(0, 60), size=wx.Size(300, 180), style=0)

        self.textCtrlPagar = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLPAGAR, parent=self.panelMontoPagos,
                                         pos=wx.Point(133, 80), size=wx.Size(150, 30),
                                         style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlPagar.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlPagar.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlPagarLeftUp)

        self.staticTextPagar = wx.StaticText(id=wxID_FRAME1STATICTEXTPAGAR, label=u'Monto', parent=self.panelMontoPagos,
                                             pos=wx.Point(10, 83), size=wx.Size(95,23), style=0)
        self.staticTextPagar.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        # cedula del cliente para reportar a MegaManager
        self.textCtrlCedulaCliente = wx.TextCtrl(id=wx.NewId(), parent=self.panelMontoPagos,
                                         pos=wx.Point(133, 120), size=wx.Size(150, 30),
                                         style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlCedulaCliente.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlCedulaCliente.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlCedulaClienteLeftUp)

        self.staticTextCedulaCliente = wx.StaticText(id=wx.NewId(), label=u'Cedula', parent=self.panelMontoPagos,
                                                     pos=wx.Point(10, 123), size=wx.Size(95,23), style=0)
        self.staticTextCedulaCliente.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        

        self.staticTextMsg = wx.StaticText(id=wxID_FRAME1STATICTEXTMSG, label=u'', name=u'staticTextMsg', parent=self.panelMontoPagos,
              pos=wx.Point(3, 155), size=wx.Size(297, 17), style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)

        self.buttonAceptarPago = wx.Button(id=wxID_FRAME1BUTTONACEPTARPAGO, label=u'Pagar', name=u'buttonAceptarPago',
              parent=self.panelMontoPagos, pos=wx.Point(100, 185), size=wx.Size(100, 50), style=0)
        self.buttonAceptarPago.Bind(wx.EVT_BUTTON, self.OnButtonAceptarPagoButton, id=wxID_FRAME1BUTTONACEPTARPAGO)

        self.buttonCancelarMontoPagos = wx.Button(id=wxID_FRAME1BUTTONCANCELARPAGO, label=u'Cancelar', name=u'buttonCancelarMontoPagos',
              parent=self.panelMontoPagos, pos=wx.Point(100, 430), size=wx.Size(100, 50), style=0)
        self.buttonCancelarMontoPagos.Bind(wx.EVT_BUTTON, self.OnButtonCancelarMontoPagosButton, id=wxID_FRAME1BUTTONCANCELARPAGO)


        # static box agregar credito
        self.staticBoxAgregarCredito = wx.StaticBox(label='Credito', name='staticBoxAgregarCredito', parent=self.panelMontoPagos,
              pos=wx.Point(0, 250), size=wx.Size(300, 160), style=0)

        self.textCtrlAgregar = wx.TextCtrl(name=u'textCtrlAgregar', parent=self.panelMontoPagos,
              pos=wx.Point(133, 270), size=wx.Size(150, 35), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlAgregar.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlAgregar.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlAgregarLeftUp)


        self.staticTextAgregar = wx.StaticText(label=u'Monto', name=u'staticTextAgregar',
              parent=self.panelMontoPagos, pos=wx.Point(10, 275), size=wx.Size(95,23), style=0)
        self.staticTextAgregar.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextMsgAgregarCredito = wx.StaticText(label=u'', name=u'staticTextMsgAgregarCredito', parent=self.panelMontoPagos,
              pos=wx.Point(3, 314), size=wx.Size(297, 17), style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)

        self.buttonAceptarAgregarCredito = wx.Button(label=u'Agregar', name=u'buttonAceptarAgregarCredito', parent=self.panelMontoPagos,
                                           pos=wx.Point(100, 345), size=wx.Size(100, 50), style=0)
        self.buttonAceptarAgregarCredito.Bind(wx.EVT_BUTTON, self.OnButtonAceptarAgregarCreditoButton)

        


        ###
        ##
        # Panel Administrador

        self.panelAdministrador = wx.Panel(id=wxID_FRAME1PANELADMINISTRADOR,
              name=u'panelAdministrador', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1280, 1024), style=wx.TAB_TRAVERSAL)
        self.panelAdministrador.Show(False)

        self.panelMenuAdministrador = wx.Panel(id=wxID_FRAME1PANELMENUADMINISTRADOR,
              name=u'panelMenuAdministrador', parent=self.panelAdministrador,
              pos=wx.Point(0, 0), size=wx.Size(1280, 120),
              style=wx.TAB_TRAVERSAL)

        self.buttonMenuAdministrador = wx.Button(id=wxID_FRAME1BUTTONMENUADMINISTRADOR,
              label=u'Administrador', name=u'buttonMenuAdministrador',
              parent=self.panelMenuAdministrador, pos=wx.Point(20, 20),
              size=wx.Size(120, 90), style=0)
        self.buttonMenuAdministrador.Bind(wx.EVT_BUTTON,
              self.OnButtonMenuAdministradorButton,
              id=wxID_FRAME1BUTTONMENUADMINISTRADOR)

        self.buttonMenuCoordinadores = wx.Button(id=wxID_FRAME1BUTTONMENUCOORDINADORES,
              label=u'Coordinadores', name=u'buttonMenuCoordinadores',
              parent=self.panelMenuAdministrador, pos=wx.Point(160, 20),
              size=wx.Size(120, 90), style=0)
        self.buttonMenuCoordinadores.Bind(wx.EVT_BUTTON,
              self.OnButtonMenuCoordinadoresButton,
              id=wxID_FRAME1BUTTONMENUCOORDINADORES)

        self.buttonMenuMonedas = wx.Button(id=wxID_FRAME1BUTTONMENUMONEDAS,
              label=u'Monedas', name=u'buttonMenuMonedas',
              parent=self.panelMenuAdministrador, pos=wx.Point(300, 20),
              size=wx.Size(120, 45), style=0)
        self.buttonMenuMonedas.Bind(wx.EVT_BUTTON,
              self.OnButtonMenuMonedasButton, id=wxID_FRAME1BUTTONMENUMONEDAS)


        # menu de configuracion del pozo
        self.buttonMenuPozo = wx.Button(label=u'Pozo', name=u'buttonMenuPozo',
              parent=self.panelMenuAdministrador, pos=wx.Point(300, 65), size=wx.Size(120, 45), style=0)
        self.buttonMenuPozo.Bind(wx.EVT_BUTTON, self.OnButtonMenuPozoButton)
        

        self.buttonMenuOpciones = wx.Button(id=wxID_FRAME1BUTTONMENUOPCIONES,
              label=u'Opciones', name=u'buttonMenuOpciones',
              parent=self.panelMenuAdministrador, pos=wx.Point(440, 20),
              size=wx.Size(120, 90), style=0)
        self.buttonMenuOpciones.Bind(wx.EVT_BUTTON,
              self.OnButtonMenuOpcionesButton,
              id=wxID_FRAME1BUTTONMENUOPCIONES)

        self.buttonMenuRondas = wx.Button(id=wxID_FRAME1BUTTONMENURONDAS,
              label=u'Rondas', name=u'buttonMenuRondas',
              parent=self.panelMenuAdministrador, pos=wx.Point(580, 20),
              size=wx.Size(120, 90), style=0)
        self.buttonMenuRondas.Bind(wx.EVT_BUTTON, self.OnButtonMenuRondasButton,
              id=wxID_FRAME1BUTTONMENURONDAS)

        # administrar billetes
        self.buttonMenuBilletes = wx.Button(id=wxID_FRAME1BUTTONMENUBILLETES, label=u'Billetes', name=u'buttonMenuBilletes',
              parent=self.panelMenuAdministrador, pos=wx.Point(720, 20), size=wx.Size(120, 45), style=0)
        self.buttonMenuBilletes.Bind(wx.EVT_BUTTON, self.OnButtonMenuBilletesButton, id=wxID_FRAME1BUTTONMENUBILLETES)

        # administrar creditos manuales
        self.buttonMenuCreditosManuales = wx.Button(label=u'Credito Manual', name=u'buttonMenuCreditosManuales',
              parent=self.panelMenuAdministrador, pos=wx.Point(720, 65), size=wx.Size(120, 45), style=0)
        self.buttonMenuCreditosManuales.Bind(wx.EVT_BUTTON, self.OnButtonMenuCreditosManualesButton)

        self.buttonMenuPagos = wx.Button(id=wxID_FRAME1BUTTONMENUPAGOS,
              label=u'Pagos', name=u'buttonMenuPagos',
              parent=self.panelMenuAdministrador, pos=wx.Point(860, 20),
              size=wx.Size(120, 90), style=0)
        self.buttonMenuPagos.Bind(wx.EVT_BUTTON, self.OnButtonMenuPagosButton,
              id=wxID_FRAME1BUTTONMENUPAGOS)

        self.buttonMenuCuadre = wx.Button(id=wxID_FRAME1BUTTONMENUCUADRE,
              label=u'Cuadre', name=u'buttonMenuCuadre',
              parent=self.panelMenuAdministrador, pos=wx.Point(1000, 20),
              size=wx.Size(120, 90), style=0)
        self.buttonMenuCuadre.Bind(wx.EVT_BUTTON, self.OnButtonMenuCuadreButton,
              id=wxID_FRAME1BUTTONMENUCUADRE)

        self.buttonMenuSalir = wx.Button(id=wxID_FRAME1BUTTONMENUSALIR,
              label=u'Salir', name=u'buttonMenuSalir',
              parent=self.panelMenuAdministrador, pos=wx.Point(1150, 20),
              size=wx.Size(120, 90), style=0)
        self.buttonMenuSalir.Bind(wx.EVT_BUTTON, self.OnButtonMenuSalirButton,
              id=wxID_FRAME1BUTTONMENUSALIR)

        self.panelAdminCoordinadores = wx.Panel(id=wxID_FRAME1PANELADMINCOORDINADORES,
              name=u'panelAdminCoordinadores', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904),
              style=wx.TAB_TRAVERSAL)
        self.panelAdminCoordinadores.Show(False)

        self.listCtrlAdminCoordinadores = wx.ListCtrl(id=wxID_FRAME1LISTCTRLADMINCOORDINADORES,
              name=u'listCtrlAdminCoordinadores',
              parent=self.panelAdminCoordinadores, pos=wx.Point(90, 50),
              size=wx.Size(460, 800),
              style=wx.LC_HRULES | wx.LC_SINGLE_SEL | wx.LC_REPORT | wx.LC_ICON)
        self.listCtrlAdminCoordinadores.SetBackgroundColour(wx.Colour(246, 243,
              241))
        self.listCtrlAdminCoordinadores.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.listCtrlAdminCoordinadores.SetAutoLayout(False)
        self._init_coll_listCtrlAdminCoordinadores_Columns(self.listCtrlAdminCoordinadores)
        self.listCtrlAdminCoordinadores.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnListCtrlAdminCoordinadoresListItemSelected,
              id=wxID_FRAME1LISTCTRLADMINCOORDINADORES)

        self.buttonAgregar = wx.Button(id=wxID_FRAME1BUTTONAGREGAR, label=u'+',
              name=u'buttonAgregar', parent=self.panelAdminCoordinadores,
              pos=wx.Point(580, 50), size=wx.Size(70, 60), style=0)
        self.buttonAgregar.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonAgregar.Bind(wx.EVT_BUTTON, self.OnButtonAgregarButton,
              id=wxID_FRAME1BUTTONAGREGAR)

        self.buttonEliminar = wx.Button(id=wxID_FRAME1BUTTONELIMINAR,
              label=u'-', name=u'buttonEliminar',
              parent=self.panelAdminCoordinadores, pos=wx.Point(580, 130),
              size=wx.Size(70, 60), style=0)
        self.buttonEliminar.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonEliminar.Enable(False)
        self.buttonEliminar.Bind(wx.EVT_BUTTON, self.OnButtonEliminarButton,
              id=wxID_FRAME1BUTTONELIMINAR)

        self.panelAgregarCoordinador = wx.Panel(id=wxID_FRAME1PANELAGREGARCOORDINADOR,
              name=u'panelAgregarCoordinador',
              parent=self.panelAdminCoordinadores, pos=wx.Point(700, 50),
              size=wx.Size(550, 800), style=wx.TAB_TRAVERSAL)
        self.panelAgregarCoordinador.Show(False)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Nombre', name='staticText7',
              parent=self.panelAgregarCoordinador, pos=wx.Point(30, 0),
              size=wx.Size(72, 23), style=0)
        self.staticText7.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        
        self.textCtrlNombreNuevoCoordinador = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLNOMBRENUEVOCOORDINADOR,
              name=u'textCtrlNombreNuevoCoordinador',
              parent=self.panelAgregarCoordinador, pos=wx.Point(30, 25),
              size=wx.Size(480, 30), style=0, value=u'')
        self.textCtrlNombreNuevoCoordinador.SetFont(wx.Font(14, wx.SWISS,
              wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlNombreNuevoCoordinador.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlNombreNuevoCoordinadorLeftUp)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Clave', name='staticText8',
              parent=self.panelAgregarCoordinador, pos=wx.Point(30, 55),
              size=wx.Size(72, 23), style=0)
        self.staticText8.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrlClaveNuevoCoordinador = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCLAVENUEVOCOORDINADOR,
              name=u'textCtrlClaveNuevoCoordinador',
              parent=self.panelAgregarCoordinador, pos=wx.Point(30, 80),
              size=wx.Size(480, 30), style=wx.TE_PASSWORD, value=u'')
        self.textCtrlClaveNuevoCoordinador.SetFont(wx.Font(14, wx.SWISS,
              wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlClaveNuevoCoordinador.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlClaveNuevoCoordinadorLeftUp)

        # Codigo de coordinador en MegaManager
        self.staticTextCodMegaManager = wx.StaticText(id=wx.NewId(), label=u'Cod MegaManager', parent=self.panelAgregarCoordinador,
                                                      pos=wx.Point(30, 110), size=wx.Size(72, 23), style=0)
        self.staticTextCodMegaManager.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlCodMegaManager = wx.TextCtrl(id=wx.NewId(), parent=self.panelAgregarCoordinador, pos=wx.Point(30, 135),
                                                  size=wx.Size(480, 30), style=0, value=u'')
        self.textCtrlCodMegaManager.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlCodMegaManager.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlCodMegaManagerLeftUp)


        self.staticTextMsgAgregarCoordinador = wx.StaticText(id=wxID_FRAME1STATICTEXTMSGAGREGARCOORDINADOR,
              label=u'', name=u'staticTextMsgAgregarCoordinador',
              parent=self.panelAgregarCoordinador, pos=wx.Point(30, 167),
              size=wx.Size(460, 23), style=wx.ALIGN_CENTRE)
        self.staticTextMsgAgregarCoordinador.SetFont(wx.Font(14, wx.SWISS,
              wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.panelTeclado = wx.Panel(id=wxID_FRAME1PANELTECLADO,
              name=u'panelTeclado', parent=self.panelAgregarCoordinador,
              pos=wx.Point(20, 190), size=wx.Size(500, 230),
              style=wx.TAB_TRAVERSAL)
        self.panelTeclado.Show(False)

        self.buttonQ = wx.Button(id=wxID_FRAME1BUTTONQ, label=u'Q',
              name=u'buttonQ', parent=self.panelTeclado, pos=wx.Point(0, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonQ.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonQ.Bind(wx.EVT_BUTTON, self.OnButtonQButton,
              id=wxID_FRAME1BUTTONQ)

        self.buttonW = wx.Button(id=wxID_FRAME1BUTTONW, label=u'W',
              name=u'buttonW', parent=self.panelTeclado, pos=wx.Point(50, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonW.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonW.Bind(wx.EVT_BUTTON, self.OnButtonWButton,
              id=wxID_FRAME1BUTTONW)

        self.buttonE = wx.Button(id=wxID_FRAME1BUTTONE, label=u'E',
              name=u'buttonE', parent=self.panelTeclado, pos=wx.Point(100, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonE.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonE.Bind(wx.EVT_BUTTON, self.OnButtonEButton,
              id=wxID_FRAME1BUTTONE)

        self.buttonR = wx.Button(id=wxID_FRAME1BUTTONR, label=u'R',
              name=u'buttonR', parent=self.panelTeclado, pos=wx.Point(150, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonR.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonR.Bind(wx.EVT_BUTTON, self.OnButtonRButton,
              id=wxID_FRAME1BUTTONR)

        self.buttonT = wx.Button(id=wxID_FRAME1BUTTONT, label=u'T',
              name=u'buttonT', parent=self.panelTeclado, pos=wx.Point(200, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonT.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonT.Bind(wx.EVT_BUTTON, self.OnButtonTButton,
              id=wxID_FRAME1BUTTONT)

        self.buttonY = wx.Button(id=wxID_FRAME1BUTTONY, label=u'Y',
              name=u'buttonY', parent=self.panelTeclado, pos=wx.Point(250, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonY.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonY.Bind(wx.EVT_BUTTON, self.OnButtonYButton,
              id=wxID_FRAME1BUTTONY)

        self.buttonU = wx.Button(id=wxID_FRAME1BUTTONU, label=u'U',
              name=u'buttonU', parent=self.panelTeclado, pos=wx.Point(300, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonU.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonU.Bind(wx.EVT_BUTTON, self.OnButtonUButton,
              id=wxID_FRAME1BUTTONU)

        self.buttonI = wx.Button(id=wxID_FRAME1BUTTONI, label=u'I',
              name=u'buttonI', parent=self.panelTeclado, pos=wx.Point(350, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonI.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonI.Bind(wx.EVT_BUTTON, self.OnButtonIButton,
              id=wxID_FRAME1BUTTONI)

        self.buttonO = wx.Button(id=wxID_FRAME1BUTTONO, label=u'O',
              name=u'buttonO', parent=self.panelTeclado, pos=wx.Point(400, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonO.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonO.Bind(wx.EVT_BUTTON, self.OnButtonOButton,
              id=wxID_FRAME1BUTTONO)

        self.buttonP = wx.Button(id=wxID_FRAME1BUTTONP, label=u'P',
              name=u'buttonP', parent=self.panelTeclado, pos=wx.Point(450, 10),
              size=wx.Size(48, 48), style=0)
        self.buttonP.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonP.Bind(wx.EVT_BUTTON, self.OnButtonPButton,
              id=wxID_FRAME1BUTTONP)

        self.buttonA = wx.Button(id=wxID_FRAME1BUTTONA, label=u'A',
              name=u'buttonA', parent=self.panelTeclado, pos=wx.Point(25, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonA.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonA.Bind(wx.EVT_BUTTON, self.OnButtonAButton,
              id=wxID_FRAME1BUTTONA)

        self.buttonS = wx.Button(id=wxID_FRAME1BUTTONS, label=u'S',
              name=u'buttonS', parent=self.panelTeclado, pos=wx.Point(75, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonS.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonS.Bind(wx.EVT_BUTTON, self.OnButtonSButton,
              id=wxID_FRAME1BUTTONS)

        self.buttonD = wx.Button(id=wxID_FRAME1BUTTOND, label=u'D',
              name=u'buttonD', parent=self.panelTeclado, pos=wx.Point(125, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonD.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonD.Bind(wx.EVT_BUTTON, self.OnButtonDButton,
              id=wxID_FRAME1BUTTOND)

        self.buttonF = wx.Button(id=wxID_FRAME1BUTTONF, label=u'F',
              name=u'buttonF', parent=self.panelTeclado, pos=wx.Point(175, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonF.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonF.Bind(wx.EVT_BUTTON, self.OnButtonFButton,
              id=wxID_FRAME1BUTTONF)

        self.buttonG = wx.Button(id=wxID_FRAME1BUTTONG, label=u'G',
              name=u'buttonG', parent=self.panelTeclado, pos=wx.Point(225, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonG.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonG.Bind(wx.EVT_BUTTON, self.OnButtonGButton,
              id=wxID_FRAME1BUTTONG)

        self.buttonH = wx.Button(id=wxID_FRAME1BUTTONH, label=u'H',
              name=u'buttonH', parent=self.panelTeclado, pos=wx.Point(275, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonH.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonH.Bind(wx.EVT_BUTTON, self.OnButtonHButton,
              id=wxID_FRAME1BUTTONH)

        self.buttonJ = wx.Button(id=wxID_FRAME1BUTTONJ, label=u'J',
              name=u'buttonJ', parent=self.panelTeclado, pos=wx.Point(325, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonJ.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonJ.Bind(wx.EVT_BUTTON, self.OnButtonJButton,
              id=wxID_FRAME1BUTTONJ)

        self.buttonK = wx.Button(id=wxID_FRAME1BUTTONK, label=u'K',
              name=u'buttonK', parent=self.panelTeclado, pos=wx.Point(375, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonK.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonK.Bind(wx.EVT_BUTTON, self.OnButtonKButton,
              id=wxID_FRAME1BUTTONK)

        self.buttonL = wx.Button(id=wxID_FRAME1BUTTONL, label=u'L',
              name=u'buttonL', parent=self.panelTeclado, pos=wx.Point(425, 65),
              size=wx.Size(48, 48), style=0)
        self.buttonL.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonL.Bind(wx.EVT_BUTTON, self.OnButtonLButton,
              id=wxID_FRAME1BUTTONL)

        self.buttonZ = wx.Button(id=wxID_FRAME1BUTTONZ, label=u'Z',
              name=u'buttonZ', parent=self.panelTeclado, pos=wx.Point(75, 120),
              size=wx.Size(48, 48), style=0)
        self.buttonZ.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonZ.Bind(wx.EVT_BUTTON, self.OnButtonZButton,
              id=wxID_FRAME1BUTTONZ)

        self.buttonX = wx.Button(id=wxID_FRAME1BUTTONX, label=u'X',
              name=u'buttonX', parent=self.panelTeclado, pos=wx.Point(125, 120),
              size=wx.Size(48, 48), style=0)
        self.buttonX.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonX.Bind(wx.EVT_BUTTON, self.OnButtonXButton,
              id=wxID_FRAME1BUTTONX)

        self.buttonC = wx.Button(id=wxID_FRAME1BUTTONC, label=u'C',
              name=u'buttonC', parent=self.panelTeclado, pos=wx.Point(175, 120),
              size=wx.Size(48, 48), style=0)
        self.buttonC.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonC.Bind(wx.EVT_BUTTON, self.OnButtonCButton,
              id=wxID_FRAME1BUTTONC)

        self.buttonV = wx.Button(id=wxID_FRAME1BUTTONV, label=u'V',
              name=u'buttonV', parent=self.panelTeclado, pos=wx.Point(225, 120),
              size=wx.Size(48, 48), style=0)
        self.buttonV.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonV.Bind(wx.EVT_BUTTON, self.OnButtonVButton,
              id=wxID_FRAME1BUTTONV)

        self.buttonB = wx.Button(id=wxID_FRAME1BUTTONB, label=u'B',
              name=u'buttonB', parent=self.panelTeclado, pos=wx.Point(275, 120),
              size=wx.Size(48, 48), style=0)
        self.buttonB.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonB.Bind(wx.EVT_BUTTON, self.OnButtonBButton,
              id=wxID_FRAME1BUTTONB)

        self.buttonN = wx.Button(id=wxID_FRAME1BUTTONN, label=u'N',
              name=u'buttonN', parent=self.panelTeclado, pos=wx.Point(325, 120),
              size=wx.Size(48, 48), style=0)
        self.buttonN.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonN.Bind(wx.EVT_BUTTON, self.OnButtonNButton,
              id=wxID_FRAME1BUTTONN)

        self.buttonM = wx.Button(id=wxID_FRAME1BUTTONM, label=u'M',
              name=u'buttonM', parent=self.panelTeclado, pos=wx.Point(375, 120),
              size=wx.Size(48, 48), style=0)
        self.buttonM.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Sans'))
        self.buttonM.Bind(wx.EVT_BUTTON, self.OnButtonMButton,
              id=wxID_FRAME1BUTTONM)

        self.buttonEspacio = wx.Button(id=wxID_FRAME1BUTTONESPACIO,
              label=u'Espacio', name=u'buttonEspacio', parent=self.panelTeclado,
              pos=wx.Point(75, 175), size=wx.Size(173, 48), style=0)
        self.buttonEspacio.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonEspacio.Bind(wx.EVT_BUTTON, self.OnButtonEspacioButton,
              id=wxID_FRAME1BUTTONESPACIO)

        self.buttonTecladoBorrar = wx.Button(id=wxID_FRAME1BUTTONTECLADOBORRAR,
              label=u'Borrar', name=u'buttonTecladoBorrar',
              parent=self.panelTeclado, pos=wx.Point(250, 175),
              size=wx.Size(173, 48), style=0)
        self.buttonTecladoBorrar.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.buttonTecladoBorrar.Bind(wx.EVT_BUTTON,
              self.OnButtonTecladoBorrarButton,
              id=wxID_FRAME1BUTTONTECLADOBORRAR)

        self.buttonAgregarCoordinador = wx.Button(id=wxID_FRAME1BUTTONAGREGARCOORDINADOR,
              label=u'Agregar', name=u'buttonAgregarCoordinador',
              parent=self.panelAgregarCoordinador, pos=wx.Point(270, 440),
              size=wx.Size(173, 80), style=0)
        self.buttonAgregarCoordinador.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.buttonAgregarCoordinador.Enable(False)
        self.buttonAgregarCoordinador.Bind(wx.EVT_BUTTON,
              self.OnButtonAgregarCoordinadorButton,
              id=wxID_FRAME1BUTTONAGREGARCOORDINADOR)

        self.buttonCancelarCoordinador = wx.Button(id=wxID_FRAME1BUTTONCANCELARCOORDINADOR,
              label=u'Cancelar', name=u'buttonCancelarCoordinador',
              parent=self.panelAgregarCoordinador, pos=wx.Point(95, 440),
              size=wx.Size(173, 80), style=0)
        self.buttonCancelarCoordinador.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.buttonCancelarCoordinador.Bind(wx.EVT_BUTTON,
              self.OnButtonCancelarCoordinadorButton,
              id=wxID_FRAME1BUTTONCANCELARCOORDINADOR)

        self.panelAdminMonedas = wx.Panel(id=wxID_FRAME1PANELADMINMONEDAS,
              name=u'panelAdminMonedas', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904),
              style=wx.TAB_TRAVERSAL)
        self.panelAdminMonedas.Show(False)


        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Moneda 1', name='staticText9',
              parent=self.panelAdminMonedas, pos=wx.Point(300, 210),
              size=wx.Size(90, 23), style=0)
        self.staticText9.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Moneda 2', name='staticText10',
              parent=self.panelAdminMonedas, pos=wx.Point(300, 280),
              size=wx.Size(90, 23), style=0)
        self.staticText10.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Moneda 3', name='staticText11',
              parent=self.panelAdminMonedas, pos=wx.Point(300, 350),
              size=wx.Size(90, 23), style=0)
        self.staticText11.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'Moneda 4', name='staticText12',
              parent=self.panelAdminMonedas, pos=wx.Point(300, 420),
              size=wx.Size(90, 23), style=0)
        self.staticText12.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'Moneda 5', name='staticText13',
              parent=self.panelAdminMonedas, pos=wx.Point(300, 490),
              size=wx.Size(90, 23), style=0)
        self.staticText13.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrlMoneda1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLMONEDA1,
              name=u'textCtrlMoneda1', parent=self.panelAdminMonedas,
              pos=wx.Point(400, 200), size=wx.Size(120, 40),
              style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMoneda1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.textCtrlMoneda1.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMoneda1LeftUp)

        self.textCtrlMoneda2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLMONEDA2,
              name=u'textCtrlMoneda2', parent=self.panelAdminMonedas,
              pos=wx.Point(400, 270), size=wx.Size(120, 40),
              style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMoneda2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.textCtrlMoneda2.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMoneda2LeftUp)

        self.textCtrlMoneda3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLMONEDA3,
              name=u'textCtrlMoneda3', parent=self.panelAdminMonedas,
              pos=wx.Point(400, 340), size=wx.Size(120, 40),
              style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMoneda3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.textCtrlMoneda3.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMoneda3LeftUp)

        self.textCtrlMoneda4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLMONEDA4,
              name=u'textCtrlMoneda4', parent=self.panelAdminMonedas,
              pos=wx.Point(400, 410), size=wx.Size(120, 40),
              style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMoneda4.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.textCtrlMoneda4.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMoneda4LeftUp)

        self.textCtrlMoneda5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLMONEDA5,
              name=u'textCtrlMoneda5', parent=self.panelAdminMonedas,
              pos=wx.Point(400, 480), size=wx.Size(120, 40),
              style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMoneda5.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.textCtrlMoneda5.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMoneda5LeftUp)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label=u'Modificado', name='staticText14',
              parent=self.panelAdminMonedas, pos=wx.Point(300, 120),
              size=wx.Size(96, 23), style=0)
        self.staticText14.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticTextFechaValoresMonedasVigentes = wx.StaticText(id=wxID_FRAME1STATICTEXTFECHAVALORESMONEDASVIGENTES,
              label=u'', name=u'staticTextFechaValoresMonedasVigentes',
              parent=self.panelAdminMonedas, pos=wx.Point(405, 120),
              size=wx.Size(120, 23), style=0)
        self.staticTextFechaValoresMonedasVigentes.SetFont(wx.Font(14, wx.SWISS,
              wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.panelNumeros = wx.Panel(id=wxID_FRAME1PANELNUMEROS,
              name=u'panelNumeros', parent=self.panelAdministrador,
              pos=wx.Point(720, 360), size=wx.Size(500, 230),
              style=wx.TAB_TRAVERSAL)
        self.panelNumeros.Show(False)

        self.buttonNumero0 = wx.Button(id=wxID_FRAME1BUTTONNUMERO0, label=u'0',
              name=u'buttonNumero0', parent=self.panelNumeros, pos=wx.Point(165,
              175), size=wx.Size(50, 50), style=0)
        self.buttonNumero0.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero0.Bind(wx.EVT_BUTTON, self.OnButtonNumero0Button,
              id=wxID_FRAME1BUTTONNUMERO0)

        self.buttonNumero1 = wx.Button(id=wxID_FRAME1BUTTONNUMERO1, label=u'1',
              name=u'buttonNumero1', parent=self.panelNumeros, pos=wx.Point(165,
              120), size=wx.Size(50, 50), style=0)
        self.buttonNumero1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero1.Bind(wx.EVT_BUTTON, self.OnButtonNumero1Button,
              id=wxID_FRAME1BUTTONNUMERO1)

        self.buttonNumero2 = wx.Button(id=wxID_FRAME1BUTTONNUMERO2, label=u'2',
              name=u'buttonNumero2', parent=self.panelNumeros, pos=wx.Point(220,
              120), size=wx.Size(50, 50), style=0)
        self.buttonNumero2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero2.Bind(wx.EVT_BUTTON, self.OnButtonNumero2Button,
              id=wxID_FRAME1BUTTONNUMERO2)

        self.buttonNumero3 = wx.Button(id=wxID_FRAME1BUTTONNUMERO3, label=u'3',
              name=u'buttonNumero3', parent=self.panelNumeros, pos=wx.Point(275,
              120), size=wx.Size(50, 50), style=0)
        self.buttonNumero3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero3.Bind(wx.EVT_BUTTON, self.OnButtonNumero3Button,
              id=wxID_FRAME1BUTTONNUMERO3)

        self.buttonNumero4 = wx.Button(id=wxID_FRAME1BUTTONNUMERO4, label=u'4',
              name=u'buttonNumero4', parent=self.panelNumeros, pos=wx.Point(165,
              65), size=wx.Size(50, 50), style=0)
        self.buttonNumero4.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero4.Bind(wx.EVT_BUTTON, self.OnButtonNumero4Button,
              id=wxID_FRAME1BUTTONNUMERO4)

        self.buttonNumero5 = wx.Button(id=wxID_FRAME1BUTTONNUMERO5, label=u'5',
              name=u'buttonNumero5', parent=self.panelNumeros, pos=wx.Point(220,
              65), size=wx.Size(50, 50), style=0)
        self.buttonNumero5.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero5.Bind(wx.EVT_BUTTON, self.OnButtonNumero5Button,
              id=wxID_FRAME1BUTTONNUMERO5)

        self.buttonNumero6 = wx.Button(id=wxID_FRAME1BUTTONNUMERO6, label=u'6',
              name=u'buttonNumero6', parent=self.panelNumeros, pos=wx.Point(275,
              65), size=wx.Size(50, 50), style=0)
        self.buttonNumero6.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero6.Bind(wx.EVT_BUTTON, self.OnButtonNumero6Button,
              id=wxID_FRAME1BUTTONNUMERO6)

        self.buttonNumero7 = wx.Button(id=wxID_FRAME1BUTTONNUMERO7, label=u'7',
              name=u'buttonNumero7', parent=self.panelNumeros, pos=wx.Point(165,
              10), size=wx.Size(50, 50), style=0)
        self.buttonNumero7.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero7.Bind(wx.EVT_BUTTON, self.OnButtonNumero7Button,
              id=wxID_FRAME1BUTTONNUMERO7)

        self.buttonNumero8 = wx.Button(id=wxID_FRAME1BUTTONNUMERO8, label=u'8',
              name=u'buttonNumero8', parent=self.panelNumeros, pos=wx.Point(220,
              10), size=wx.Size(50, 50), style=0)
        self.buttonNumero8.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero8.Bind(wx.EVT_BUTTON, self.OnButtonNumero8Button,
              id=wxID_FRAME1BUTTONNUMERO8)

        self.buttonNumero9 = wx.Button(id=wxID_FRAME1BUTTONNUMERO9, label=u'9',
              name=u'buttonNumero9', parent=self.panelNumeros, pos=wx.Point(275,
              10), size=wx.Size(50, 50), style=0)
        self.buttonNumero9.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonNumero9.Bind(wx.EVT_BUTTON, self.OnButtonNumero9Button,
              id=wxID_FRAME1BUTTONNUMERO9)

        self.buttonPunto = wx.Button(id=wxID_FRAME1BUTTONPUNTO, label=u'.',
              name=u'buttonPunto', parent=self.panelNumeros, pos=wx.Point(220,
              175), size=wx.Size(50, 50), style=0)
        self.buttonPunto.Enable(False)
        self.buttonPunto.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Sans'))
        self.buttonPunto.Bind(wx.EVT_BUTTON, self.OnButtonPuntoButton,
              id=wxID_FRAME1BUTTONPUNTO)

        self.buttonNumeroBorrar = wx.Button(id=wxID_FRAME1BUTTONNUMEROBORRAR,
              label=u'B', name=u'buttonNumeroBorrar', parent=self.panelNumeros,
              pos=wx.Point(275, 175), size=wx.Size(50, 50), style=0)
        self.buttonNumeroBorrar.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.buttonNumeroBorrar.Bind(wx.EVT_BUTTON,
              self.OnButtonNumeroBorrarButton,
              id=wxID_FRAME1BUTTONNUMEROBORRAR)

        self.buttonCancelarCambioMoneda = wx.Button(id=wxID_FRAME1BUTTONCANCELARCAMBIOMONEDA,
              label=u'Cancelar', name=u'buttonCancelarCambioMoneda',
              parent=self.panelAdminMonedas, pos=wx.Point(845, 490),
              size=wx.Size(120, 70), style=0)
        self.buttonCancelarCambioMoneda.Show(False)
        self.buttonCancelarCambioMoneda.Bind(wx.EVT_BUTTON,
              self.OnButtonCancelarCambioMonedaButton,
              id=wxID_FRAME1BUTTONCANCELARCAMBIOMONEDA)

        self.buttonAceptarCambioMoneda = wx.Button(id=wxID_FRAME1BUTTONACEPTARCAMBIOMONEDA,
              label=u'Aceptar', name=u'buttonAceptarCambioMoneda',
              parent=self.panelAdminMonedas, pos=wx.Point(970, 490),
              size=wx.Size(120, 70), style=0)
        self.buttonAceptarCambioMoneda.Show(False)
        self.buttonAceptarCambioMoneda.Bind(wx.EVT_BUTTON,
              self.OnButtonAceptarCambioMonedaButton,
              id=wxID_FRAME1BUTTONACEPTARCAMBIOMONEDA)


        # Admin Pozo
        self.panelAdminPozo = wx.Panel(name=u'panelAdminPozo', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904), style=wx.TAB_TRAVERSAL)
        self.panelAdminPozo.Show(False)

        self.staticBoxConfigPozo = wx.StaticBox(label='Configuracion Pozo', name='staticBoxConfigPozo',
                                                      parent=self.panelAdminPozo, pos=wx.Point(50, 50), size=wx.Size(700, 500))
        self.staticBoxConfigPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        # monto inicial
        self.staticTextMontoInicialPozo = wx.StaticText(label=u'Monto inicial', name='staticTextMontoInicialPozo',
                                                        parent=self.panelAdminPozo, pos=wx.Point(80, 100), size=wx.Size(60, 23), style=0)
        self.staticTextMontoInicialPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlMontoInicialPozo = wx.TextCtrl(name=u'textCtrlMontoInicialPozo', parent=self.panelAdminPozo,
              pos=wx.Point(300, 92), size=wx.Size(300, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMontoInicialPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlMontoInicialPozo.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMontoInicialPozoLeftUp)

        # montoActual
        self.staticTextMontoActualPozo = wx.StaticText(label=u'Monto actual', name='staticTextMontoActualPozo',
                                                       parent=self.panelAdminPozo, pos=wx.Point(80, 150), size=wx.Size(60, 23), style=0)
        self.staticTextMontoActualPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlMontoActualPozo = wx.TextCtrl(name=u'textCtrlMontoActualPozo', parent=self.panelAdminPozo,
              pos=wx.Point(300, 142), size=wx.Size(300, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMontoActualPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlMontoActualPozo.Disable()
        
        # montoReserva
        self.staticTextMontoReservaPozo = wx.StaticText(label=u'Monto reserva', name='staticTextMontoReservaPozo',
                                                       parent=self.panelAdminPozo, pos=wx.Point(80, 200), size=wx.Size(60, 23), style=0)
        self.staticTextMontoReservaPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlMontoReservaPozo = wx.TextCtrl(name=u'textCtrlMontoReservaPozo', parent=self.panelAdminPozo,
              pos=wx.Point(300, 192), size=wx.Size(300, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMontoReservaPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        #self.textCtrlMontoReservaPozo.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMontoReservaPozoLeftUp)
        self.textCtrlMontoReservaPozo.Disable()
        
        # MinimoParaConcursar = apuesta minima
        self.staticTextMinimoParaConcursarPozo = wx.StaticText(label=u'Apuesta minima', name='staticTextMinimoParaConcursarPozo',
                                                       parent=self.panelAdminPozo, pos=wx.Point(80, 250), size=wx.Size(60, 23), style=0)
        self.staticTextMinimoParaConcursarPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlMinimoParaConcursarPozo = wx.TextCtrl(name=u'textCtrlMinimoParaConcursarPozo', parent=self.panelAdminPozo,
              pos=wx.Point(300, 242), size=wx.Size(300, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMinimoParaConcursarPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlMinimoParaConcursarPozo.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMinimoParaConcursarPozoLeftUp)
        
        # frecuenciaSorteo
        self.staticTextFrecuenciaSorteoPozo = wx.StaticText(label=u'Sortear despues de', name='staticTextFrecuenciaSorteoPozo',
                                                       parent=self.panelAdminPozo, pos=wx.Point(80, 300), size=wx.Size(60, 23), style=0)
        self.staticTextFrecuenciaSorteoPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextFrecuenciaSorteo2Pozo = wx.StaticText(label=u'rondas', name='staticTextFrecuenciaSorteo2Pozo',
                                                       parent=self.panelAdminPozo, pos=wx.Point(610, 300), size=wx.Size(60, 23), style=0)
        self.staticTextFrecuenciaSorteo2Pozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlFrecuenciaSorteoPozo = wx.TextCtrl(name=u'textCtrlFrecuenciaSorteoPozo', parent=self.panelAdminPozo,
              pos=wx.Point(300, 292), size=wx.Size(300, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlFrecuenciaSorteoPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlFrecuenciaSorteoPozo.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlFrecuenciaSorteoPozoLeftUp)
        
        # factorReserva
        self.staticTextFactorReservaPozo = wx.StaticText(label=u'Factor de reserva', name='staticTextFactorReservaPozo',
                                                       parent=self.panelAdminPozo, pos=wx.Point(80, 350), size=wx.Size(60, 23), style=0)
        self.staticTextFactorReservaPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlFactorReservaPozo = wx.TextCtrl(name=u'textCtrlFrecuenciaSorteoPozo', parent=self.panelAdminPozo,
              pos=wx.Point(300, 342), size=wx.Size(300, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlFactorReservaPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlFactorReservaPozo.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlFactorReservaPozoLeftUp)
        
        # factorIncremento
        self.staticTextFactorIncrementoPozo = wx.StaticText(label=u'Factor de incremento', name='staticTextFactorIncrementoPozo',
                                                       parent=self.panelAdminPozo, pos=wx.Point(80, 400), size=wx.Size(60, 23), style=0)
        self.staticTextFactorIncrementoPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlFactorIncrementoPozo = wx.TextCtrl(name=u'textCtrlFrecuenciaSorteoPozo', parent=self.panelAdminPozo,
              pos=wx.Point(300, 392), size=wx.Size(300, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlFactorIncrementoPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlFactorIncrementoPozo.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlFactorIncrementoPozoLeftUp)

        # id_ultimaRondaJugada
        self.staticTextUltimaRondaJugadaPozo = wx.StaticText(label=u'Ultima ronda sorteada', name='staticTextUltimaRondaJugadaPozo',
                                                       parent=self.panelAdminPozo, pos=wx.Point(80, 450), size=wx.Size(60, 23), style=0)
        self.staticTextUltimaRondaJugadaPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlUltimaRondaJugadaPozo = wx.TextCtrl(name=u'textCtrlFrecuenciaSorteoPozo', parent=self.panelAdminPozo,
              pos=wx.Point(300, 442), size=wx.Size(300, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlUltimaRondaJugadaPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        #self.textCtrlUltimaRondaJugadaPozo.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlUltimaRondaJugadaPozoLeftUp)
        self.textCtrlUltimaRondaJugadaPozo.Disable()

        # modificables Admin Pozo
        self.modificablesAdminPozo = [self.textCtrlFactorIncrementoPozo, self.textCtrlFactorReservaPozo, self.textCtrlFrecuenciaSorteoPozo,
                                      self.textCtrlMinimoParaConcursarPozo, self.textCtrlMontoInicialPozo]

        


        # Admin Opciones
        
        self.panelAdminOpciones = wx.Panel(id=wxID_FRAME1PANELADMINOPCIONES,
              name=u'panelAdminOpciones', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904),
              style=wx.TAB_TRAVERSAL)
        self.panelAdminOpciones.Show(False)

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label=u'Pleno', name='staticText15',
              parent=self.panelAdminOpciones, pos=wx.Point(150, 50),
              size=wx.Size(60, 23), style=0)
        self.staticText15.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Sans'))

        self.staticText16 = wx.StaticText(id=wxID_FRAME1STATICTEXT16,
              label=u'Paga por', name='staticText16',
              parent=self.panelAdminOpciones, pos=wx.Point(230, 80),
              size=wx.Size(80, 23), style=0)
        self.staticText16.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText17 = wx.StaticText(id=wxID_FRAME1STATICTEXT17,
              label=u'M\xednimo', name='staticText17',
              parent=self.panelAdminOpciones, pos=wx.Point(393, 80),
              size=wx.Size(80, 23), style=0)
        self.staticText17.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText18 = wx.StaticText(id=wxID_FRAME1STATICTEXT18,
              label=u'M\xe1ximo', name='staticText18',
              parent=self.panelAdminOpciones, pos=wx.Point(550, 80),
              size=wx.Size(80, 23), style=0)
        self.staticText18.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrlPlenoPagaPor = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLPLENOPAGAPOR,
              name=u'textCtrlPlenoPagaPor', parent=self.panelAdminOpciones,
              pos=wx.Point(220, 110), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlPlenoPagaPor.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlPlenoPagaPor.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlPlenoPagaPorLeftUp)

        self.textCtrlPlenoMinimo = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLPLENOMINIMO,
              name=u'textCtrlPlenoMinimo', parent=self.panelAdminOpciones,
              pos=wx.Point(380, 110), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlPlenoMinimo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlPlenoMinimo.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlPlenoMinimoLeftUp)

        self.textCtrlPlenoMaximo = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLPLENOMAXIMO,
              name=u'textCtrlPlenoMaximo', parent=self.panelAdminOpciones,
              pos=wx.Point(540, 110), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlPlenoMaximo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlPlenoMaximo.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlPlenoMaximoLeftUp)

        self.staticText19 = wx.StaticText(id=wxID_FRAME1STATICTEXT19,
              label=u'Medio', name='staticText19',
              parent=self.panelAdminOpciones, pos=wx.Point(150, 200),
              size=wx.Size(60, 23), style=0)
        self.staticText19.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Sans'))

        self.staticText20 = wx.StaticText(id=wxID_FRAME1STATICTEXT20,
              label=u'Paga por', name='staticText20',
              parent=self.panelAdminOpciones, pos=wx.Point(230, 230),
              size=wx.Size(80, 23), style=0)
        self.staticText20.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText21 = wx.StaticText(id=wxID_FRAME1STATICTEXT21,
              label=u'M\xednimo', name='staticText21',
              parent=self.panelAdminOpciones, pos=wx.Point(393, 230),
              size=wx.Size(80, 23), style=0)
        self.staticText21.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText22 = wx.StaticText(id=wxID_FRAME1STATICTEXT22,
              label=u'M\xe1ximo', name='staticText22',
              parent=self.panelAdminOpciones, pos=wx.Point(550, 230),
              size=wx.Size(80, 23), style=0)
        self.staticText22.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrlMedioPagaPor = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLMEDIOPAGAPOR,
              name=u'textCtrlMedioPagaPor', parent=self.panelAdminOpciones,
              pos=wx.Point(220, 260), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlMedioPagaPor.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlMedioPagaPor.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlMedioPagaPorLeftUp)

        self.textCtrlMedioMinimo = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLMEDIOMINIMO,
              name=u'textCtrlMedioMinimo', parent=self.panelAdminOpciones,
              pos=wx.Point(380, 260), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlMedioMinimo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlMedioMinimo.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlMedioMinimoLeftUp)

        self.textCtrlMedioMaximo = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLMEDIOMAXIMO,
              name=u'textCtrlMedioMaximo', parent=self.panelAdminOpciones,
              pos=wx.Point(540, 260), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlMedioMaximo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlMedioMaximo.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlMedioMaximoLeftUp)

        self.staticText23 = wx.StaticText(id=wxID_FRAME1STATICTEXT23,
              label=u'Cuadro', name='staticText23',
              parent=self.panelAdminOpciones, pos=wx.Point(150, 350),
              size=wx.Size(66, 23), style=0)
        self.staticText23.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Sans'))

        self.staticText24 = wx.StaticText(id=wxID_FRAME1STATICTEXT24,
              label=u'Paga por', name='staticText24',
              parent=self.panelAdminOpciones, pos=wx.Point(230, 380),
              size=wx.Size(80, 23), style=0)
        self.staticText24.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText25 = wx.StaticText(id=wxID_FRAME1STATICTEXT25,
              label=u'M\xednimo', name='staticText25',
              parent=self.panelAdminOpciones, pos=wx.Point(393, 380),
              size=wx.Size(80, 23), style=0)
        self.staticText25.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText26 = wx.StaticText(id=wxID_FRAME1STATICTEXT26,
              label=u'M\xe1ximo', name='staticText26',
              parent=self.panelAdminOpciones, pos=wx.Point(550, 380),
              size=wx.Size(80, 23), style=0)
        self.staticText26.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrlCuadroPagaPor = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCUADROPAGAPOR,
              name=u'textCtrlCuadroPagaPor', parent=self.panelAdminOpciones,
              pos=wx.Point(220, 410), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlCuadroPagaPor.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlCuadroPagaPor.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlCuadroPagaPorLeftUp)

        self.textCtrlCuadroMinimo = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCUADROMINIMO,
              name=u'textCtrlCuadroMinimo', parent=self.panelAdminOpciones,
              pos=wx.Point(380, 410), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlCuadroMinimo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlCuadroMinimo.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlCuadroMinimoLeftUp)

        self.textCtrlCuadroMaximo = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCUADROMAXIMO,
              name=u'textCtrlCuadroMaximo', parent=self.panelAdminOpciones,
              pos=wx.Point(540, 410), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlCuadroMaximo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlCuadroMaximo.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlCuadroMaximoLeftUp)

        self.staticText27 = wx.StaticText(id=wxID_FRAME1STATICTEXT27,
              label=u'Chanza', name='staticText27',
              parent=self.panelAdminOpciones, pos=wx.Point(150, 500),
              size=wx.Size(70, 23), style=0)
        self.staticText27.SetFont(wx.Font(14, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Sans'))

        self.staticText28 = wx.StaticText(id=wxID_FRAME1STATICTEXT28,
              label=u'Paga por', name='staticText28',
              parent=self.panelAdminOpciones, pos=wx.Point(230, 530),
              size=wx.Size(80, 23), style=0)
        self.staticText28.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText29 = wx.StaticText(id=wxID_FRAME1STATICTEXT29,
              label=u'M\xednimo', name='staticText29',
              parent=self.panelAdminOpciones, pos=wx.Point(393, 530),
              size=wx.Size(80, 23), style=0)
        self.staticText29.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText30 = wx.StaticText(id=wxID_FRAME1STATICTEXT30,
              label=u'M\xe1ximo', name='staticText30',
              parent=self.panelAdminOpciones, pos=wx.Point(550, 530),
              size=wx.Size(80, 23), style=0)
        self.staticText30.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrlChanzaPagaPor = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCHANZAPAGAPOR,
              name=u'textCtrlChanzaPagaPor', parent=self.panelAdminOpciones,
              pos=wx.Point(220, 560), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlChanzaPagaPor.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlChanzaPagaPor.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlChanzaPagaPorLeftUp)

        self.textCtrlChanzaMinimo = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCHANZAMINIMO,
              name=u'textCtrlChanzaMinimo', parent=self.panelAdminOpciones,
              pos=wx.Point(380, 560), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlChanzaMinimo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlChanzaMinimo.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlChanzaMinimoLeftUp)

        self.textCtrlChanzaMaximo = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCHANZAMAXIMO,
              name=u'textCtrlChanzaMaximo', parent=self.panelAdminOpciones,
              pos=wx.Point(540, 560), size=wx.Size(100, 40),
              style=wx.TE_READONLY | wx.TE_CENTER, value=u'')
        self.textCtrlChanzaMaximo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlChanzaMaximo.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlChanzaMaximoLeftUp)

        self.buttonCancelarCambioOpcion = wx.Button(id=wxID_FRAME1BUTTONCANCELARCAMBIOOPCION,
              label=u'Cancelar', name=u'buttonCancelarCambioOpcion',
              parent=self.panelAdminOpciones, pos=wx.Point(860, 536),
              size=wx.Size(100, 60), style=0)
        self.buttonCancelarCambioOpcion.Show(False)
        self.buttonCancelarCambioOpcion.Bind(wx.EVT_BUTTON,
              self.OnButtonCancelarCambioOpcionButton,
              id=wxID_FRAME1BUTTONCANCELARCAMBIOOPCION)

        self.buttonAceptarCambioOpcion = wx.Button(id=wxID_FRAME1BUTTONACEPTARCAMBIOOPCION,
              label=u'Aceptar', name=u'buttonAceptarCambioOpcion',
              parent=self.panelAdminOpciones, pos=wx.Point(980, 536),
              size=wx.Size(100, 60), style=0)
        self.buttonAceptarCambioOpcion.Show(False)
        self.buttonAceptarCambioOpcion.Bind(wx.EVT_BUTTON,
              self.OnButtonAceptarCambioOpcionButton,
              id=wxID_FRAME1BUTTONACEPTARCAMBIOOPCION)

        # admin monto minimo de apuestas x maquina
        self.staticBoxMontoMinApuestas = wx.StaticBox(label='Minima apuesta por maquina', name='staticBoxMontoMinApuestas',
                                                      parent=self.panelAdminOpciones, pos=wx.Point(750, 60), size=wx.Size(400, 130))
        self.staticBoxMontoMinApuestas.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextMontoMinApuestas = wx.StaticText(label=u'Monto', name='staticTextMontoMinApuestas',
              parent=self.panelAdminOpciones, pos=wx.Point(780, 120), size=wx.Size(70, 23), style=0)
        self.staticTextMontoMinApuestas.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.textCtrlMontoMinApuestas = wx.TextCtrl(name=u'textCtrlMontoMinApuestas', parent=self.panelAdminOpciones,
              pos=wx.Point(880, 112), size=wx.Size(210, 40), style=wx.TE_READONLY | wx.TE_RIGHT, value=u'')
        self.textCtrlMontoMinApuestas.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlMontoMinApuestas.Bind(wx.EVT_LEFT_UP, self.OnTextCtrlMontoMinApuestasLeftUp)
        
        # Admin Opciones fin

        
        # Admin Rondas ini
        
        self.panelAdminRondas = wx.Panel(id=wxID_FRAME1PANELADMINRONDAS,
              name=u'panelAdminRondas', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904),
              style=wx.TAB_TRAVERSAL)
        self.panelAdminRondas.Show(False)

        self.listCtrlRondas = wx.ListCtrl(id=wxID_FRAME1LISTCTRLRONDAS,
              name=u'listCtrlRondas', parent=self.panelAdminRondas,
              pos=wx.Point(100, 50), size=wx.Size(650, 750),
              style=wx.LC_HRULES | wx.LC_REPORT)
        self.listCtrlRondas.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self._init_coll_listCtrlRondas_Columns(self.listCtrlRondas)

        self.staticTextErrorFechaRondas = wx.StaticText(id=wxID_FRAME1STATICTEXTERRORFECHARONDAS,
              label=u'Imposible hacer consulta',
              name=u'staticTextErrorFechaRondas', parent=self.panelAdminRondas,
              pos=wx.Point(910, 694), size=wx.Size(159, 17), style=0)
        self.staticTextErrorFechaRondas.Show(False)

        self.panelAdminCuadre = wx.Panel(id=wxID_FRAME1PANELADMINCUADRE,
              name=u'panelAdminCuadre', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904),
              style=wx.TAB_TRAVERSAL)
        self.panelAdminCuadre.Show(False)

        self.calendarCtrlRondas1 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=wxID_FRAME1CALENDARCTRLRONDAS1, name=u'calendarCtrlRondas1',
              parent=self.panelAdminRondas, pos=wx.Point(792, 50),
              size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlRondas1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.calendarCtrlRondas1.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED,
              self.OnCalendarCtrlRondas1CalendarSelChanged,
              id=wxID_FRAME1CALENDARCTRLRONDAS1)

        self.calendarCtrlRondas2 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=wxID_FRAME1CALENDARCTRLRONDAS2, name=u'calendarCtrlRondas2',
              parent=self.panelAdminRondas, pos=wx.Point(792, 400),
              size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlRondas2.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.calendarCtrlRondas2.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED,
              self.OnCalendarCtrlRondas2CalendarSelChanged,
              id=wxID_FRAME1CALENDARCTRLRONDAS2)

        self.calendarCtrlCuadre1 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=wxID_FRAME1CALENDARCTRLCUADRE1, name=u'calendarCtrlCuadre1',
              parent=self.panelAdminCuadre, pos=wx.Point(792, 50),
              size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlCuadre1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.calendarCtrlCuadre1.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED,
              self.OnCalendarCtrlCuadre1CalendarSelChanged,
              id=wxID_FRAME1CALENDARCTRLCUADRE1)

        self.calendarCtrlCuadre2 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=wxID_FRAME1CALENDARCTRLCUADRE2, name=u'calendarCtrlCuadre2',
              parent=self.panelAdminCuadre, pos=wx.Point(792, 400),
              size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlCuadre2.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.calendarCtrlCuadre2.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED,
              self.OnCalendarCtrlCuadre2CalendarSelChanged,
              id=wxID_FRAME1CALENDARCTRLCUADRE2)

        self.staticText31 = wx.StaticText(id=wxID_FRAME1STATICTEXT31,
              label=u'Todas las maquinas deben estar en 0', name='staticText31',
              parent=self.panelAdminCuadre, pos=wx.Point(200, 32),
              size=wx.Size(329, 19), style=0)
        self.staticText31.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Sans'))

        self.panelAdminBilletes = wx.Panel(id=wxID_FRAME1PANELADMINBILLETES,
              name=u'panelAdminBilletes', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904),
              style=wx.TAB_TRAVERSAL)
        self.panelAdminBilletes.Show(False)

        self.listCtrlBilletes = wx.ListCtrl(id=wxID_FRAME1LISTCTRLBILLETES,
              name=u'listCtrlBilletes', parent=self.panelAdminBilletes,
              pos=wx.Point(100, 50), size=wx.Size(650, 750),
              style=wx.LC_HRULES | wx.LC_REPORT)
        self._init_coll_listCtrlBilletes_Columns(self.listCtrlBilletes)

        self.calendarCtrlBilletes1 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=wxID_FRAME1CALENDARCTRLBILLETES1,
              name=u'calendarCtrlBilletes1', parent=self.panelAdminBilletes,
              pos=wx.Point(792, 50), size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlBilletes1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.calendarCtrlBilletes1.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED,
              self.OnCalendarCtrlBilletes1CalendarSelChanged,
              id=wxID_FRAME1CALENDARCTRLBILLETES1)

        self.calendarCtrlBilletes2 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=wxID_FRAME1CALENDARCTRLBILLETES2,
              name=u'calendarCtrlBilletes2', parent=self.panelAdminBilletes,
              pos=wx.Point(792, 400), size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlBilletes2.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.calendarCtrlBilletes2.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED,
              self.OnCalendarCtrlBilletes2CalendarSelChanged,
              id=wxID_FRAME1CALENDARCTRLBILLETES2)

        self.panelAdminPagos = wx.Panel(id=wxID_FRAME1PANELADMINPAGOS,
              name=u'panelAdminPagos', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904),
              style=wx.TAB_TRAVERSAL)
        self.panelAdminPagos.Show(False)

        self.listCtrlPagos = wx.ListCtrl(id=wxID_FRAME1LISTCTRLPAGOS,
              name=u'listCtrlPagos', parent=self.panelAdminPagos,
              pos=wx.Point(100, 50), size=wx.Size(650, 750),
              style=wx.LC_HRULES | wx.LC_REPORT)
        self._init_coll_listCtrlPagos_Columns(self.listCtrlPagos)

        self.calendarCtrlPagos1 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=wxID_FRAME1CALENDARCTRLPAGOS1, name=u'calendarCtrlPagos1',
              parent=self.panelAdminPagos, pos=wx.Point(792, 50),
              size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlPagos1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.calendarCtrlPagos1.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED,
              self.OnCalendarCtrlPagos1CalendarSelChanged,
              id=wxID_FRAME1CALENDARCTRLPAGOS1)

        self.calendarCtrlPagos2 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(),
              id=wxID_FRAME1CALENDARCTRLPAGOS2, name=u'calendarCtrlPagos2',
              parent=self.panelAdminPagos, pos=wx.Point(792, 400),
              size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlPagos2.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.calendarCtrlPagos2.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED,
              self.OnCalendarCtrlPagos2CalendarSelChanged,
              id=wxID_FRAME1CALENDARCTRLPAGOS2)

        # admin creditos manuales
        
        self.panelAdminCreditosManuales = wx.Panel(name=u'panelAdminCreditosManuales', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 904), style=wx.TAB_TRAVERSAL)
        self.panelAdminCreditosManuales.Show(False)

        self.listCtrlCreditosManuales = wx.ListCtrl(name=u'listCtrlCreditosManuales', parent=self.panelAdminCreditosManuales,
              pos=wx.Point(100, 50), size=wx.Size(650, 750), style=wx.LC_HRULES | wx.LC_REPORT)
        self._init_coll_listCtrlCreditosManuales_Columns(self.listCtrlCreditosManuales)

        self.calendarCtrlCreditosManuales1 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(), name=u'calendarCtrlCreditosManuales1',
              parent=self.panelAdminCreditosManuales, pos=wx.Point(792, 50), size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlCreditosManuales1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.calendarCtrlCreditosManuales1.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.OnCalendarCtrlCreditosManuales1CalendarSelChanged)

        self.calendarCtrlCreditosManuales2 = wx.calendar.CalendarCtrl(date=wx.DateTime.Now(), name=u'calendarCtrlCreditosManuales2',
              parent=self.panelAdminCreditosManuales, pos=wx.Point(792, 400), size=wx.Size(400, 300),
              style=wx.calendar.CAL_MONDAY_FIRST | wx.calendar.CAL_SHOW_HOLIDAYS | wx.calendar.CAL_SHOW_SURROUNDING_WEEKS)
        self.calendarCtrlCreditosManuales2.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.calendarCtrlCreditosManuales2.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.OnCalendarCtrlCreditosManuales2CalendarSelChanged)


        # admin administrador
        
        self.panelAdminAdministrador = wx.Panel(id=wxID_FRAME1PANELADMINADMINISTRADOR,
              name=u'panelAdminAdministrador', parent=self.panelAdministrador,
              pos=wx.Point(0, 120), size=wx.Size(1280, 1024),
              style=wx.TAB_TRAVERSAL)
        self.panelAdminAdministrador.Show(False)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Cambiar Clave Administrador', name='staticBox1',
              parent=self.panelAdminAdministrador, pos=wx.Point(100, 50),
              size=wx.Size(500, 500), style=0)
        self.staticBox1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.textCtrlClaveActual = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCLAVEACTUAL,
              name=u'textCtrlClaveActual', parent=self.panelAdminAdministrador,
              pos=wx.Point(350, 120), size=wx.Size(200, 35),
              style=wx.TE_PASSWORD, value=u'')
        self.textCtrlClaveActual.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlClaveActual.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlClaveActualLeftUp)

        self.textCtrlClaveNueva = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCLAVENUEVA,
              name=u'textCtrlClaveNueva', parent=self.panelAdminAdministrador,
              pos=wx.Point(350, 200), size=wx.Size(200, 35),
              style=wx.TE_PASSWORD, value=u'')
        self.textCtrlClaveNueva.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Sans'))
        self.textCtrlClaveNueva.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlClaveNuevaLeftUp)

        self.textCtrlConfirmarClaveNueva = wx.TextCtrl(id=wxID_FRAME1TEXTCTRLCONFIRMARCLAVENUEVA,
              name=u'textCtrlConfirmarClaveNueva',
              parent=self.panelAdminAdministrador, pos=wx.Point(350, 280),
              size=wx.Size(200, 35), style=wx.TE_PASSWORD, value=u'')
        self.textCtrlConfirmarClaveNueva.SetFont(wx.Font(14, wx.SWISS,
              wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.textCtrlConfirmarClaveNueva.Bind(wx.EVT_LEFT_UP,
              self.OnTextCtrlConfirmarClaveNuevaLeftUp)

        self.buttonCambiarClave = wx.Button(id=wxID_FRAME1BUTTONCAMBIARCLAVE,
              label=u'Cambiar Clave', name=u'buttonCambiarClave',
              parent=self.panelAdminAdministrador, pos=wx.Point(270, 408),
              size=wx.Size(150, 50), style=0)
        self.buttonCambiarClave.Bind(wx.EVT_BUTTON,
              self.OnButtonCambiarClaveButton,
              id=wxID_FRAME1BUTTONCAMBIARCLAVE)

        self.staticText32 = wx.StaticText(id=wxID_FRAME1STATICTEXT32,
              label=u'Clave actual', name='staticText32',
              parent=self.panelAdminAdministrador, pos=wx.Point(120, 128),
              size=wx.Size(113, 23), style=0)
        self.staticText32.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText33 = wx.StaticText(id=wxID_FRAME1STATICTEXT33,
              label=u'Clave nueva', name='staticText33',
              parent=self.panelAdminAdministrador, pos=wx.Point(120, 205),
              size=wx.Size(115, 23), style=0)
        self.staticText33.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.staticText64 = wx.StaticText(id=wxID_FRAME1STATICTEXT64,
              label=u'Confirmar clave nueva', name='staticText64',
              parent=self.panelAdminAdministrador, pos=wx.Point(120, 285),
              size=wx.Size(207, 23), style=0)
        self.staticText64.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))

        self.buttonAceptarCambiarClave = wx.Button(id=wxID_FRAME1BUTTONACEPTARCAMBIARCLAVE,
              label=u'Aceptar', name=u'buttonAceptarCambiarClave',
              parent=self.panelAdminAdministrador, pos=wx.Point(1000, 504),
              size=wx.Size(120, 50), style=0)
        self.buttonAceptarCambiarClave.Show(False)
        self.buttonAceptarCambiarClave.Bind(wx.EVT_BUTTON,
              self.OnButtonAceptarCambiarClaveButton,
              id=wxID_FRAME1BUTTONACEPTARCAMBIARCLAVE)

        self.buttonCancelarCambiarClave = wx.Button(id=wxID_FRAME1BUTTONCANCELARCAMBIARCLAVE,
              label=u'Cancelar', name=u'buttonCancelarCambiarClave',
              parent=self.panelAdminAdministrador, pos=wx.Point(850, 504),
              size=wx.Size(120, 50), style=0)
        self.buttonCancelarCambiarClave.Show(False)
        self.buttonCancelarCambiarClave.Bind(wx.EVT_BUTTON,
              self.OnButtonCancelarCambiarClaveButton,
              id=wxID_FRAME1BUTTONCANCELARCAMBIARCLAVE)

        self.staticTextMsgCambiarClaveAdmin = wx.StaticText(id=wxID_FRAME1STATICTEXTMSGCAMBIARCLAVEADMIN,
              label=u'MsgCambiarClaveAdmin',
              name=u'staticTextMsgCambiarClaveAdmin',
              parent=self.panelAdminAdministrador, pos=wx.Point(150, 368),
              size=wx.Size(400, 19), style=wx.ALIGN_CENTRE)
        self.staticTextMsgCambiarClaveAdmin.SetFont(wx.Font(12, wx.SWISS,
              wx.NORMAL, wx.BOLD, False, u'Sans'))
        self.staticTextMsgCambiarClaveAdmin.Show(False)


        # Exportar el reporte a USB

        self.panelExportar = wx.Panel(id=wxID_FRAME1PANELGUARDAR,
              name=u'panelExportar', parent=self.panelAdministrador,
              pos=wx.Point(630, 120), size=wx.Size(140, 40),
              style=wx.TAB_TRAVERSAL)
        self.panelExportar.Show(False)

        self.buttonExportar = wx.Button(id=wxID_FRAME1BUTTONGUARDAR,
              label=u'Exportar', name=u'buttonExportar', parent=self.panelExportar,
              pos=wx.Point(0, 0), size=wx.Size(120, 40), style=0)
        self.buttonExportar.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Sans'))
        self.buttonExportar.Bind(wx.EVT_BUTTON, self.OnButtonExportarButton,
              id=wxID_FRAME1BUTTONGUARDAR)


        # Guardar las actualizaciones hechas a los textCtrl. Solamente aplica para lo desarrollado del pozo en adelante

        self.panelGuardar = wx.Panel(name=u'panelGuardar', parent=self.panelAdministrador,
              pos=wx.Point(480, 120), size=wx.Size(140, 40), style=wx.TAB_TRAVERSAL)
        self.panelGuardar.Show(False)

        self.buttonGuardar = wx.Button(label=u'Guardar', name=u'buttonGuardar', parent=self.panelGuardar,
              pos=wx.Point(0, 0), size=wx.Size(120, 40), style=0)
        self.buttonGuardar.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.buttonGuardar.Bind(wx.EVT_BUTTON, self.OnButtonGuardarButton)
        

        self.listCtrlCuadre = wx.ListCtrl(id=wxID_FRAME1LISTCTRLCUADRE,
              name=u'listCtrlCuadre', parent=self.panelAdminCuadre,
              pos=wx.Point(100, 50), size=wx.Size(650, 750),
              style=wx.LC_REPORT | wx.LC_HRULES)
        self._init_coll_listCtrlCuadre_Columns(self.listCtrlCuadre)


        self.buttonCancelarRonda = wx.Button(id=wxID_FRAME1BUTTONCANCELARRONDA,
              label=u'Cancelar Ronda', name=u'buttonCancelarRonda',
              parent=self.panelRondas, pos=wx.Point(1100, 20), size=wx.Size(120,
              100), style=0)
        self.buttonCancelarRonda.Show(True)
        self.buttonCancelarRonda.Enable(False)
        self.buttonCancelarRonda.Bind(wx.EVT_BUTTON,
              self.OnButtonCancelarRondaButton,
              id=wxID_FRAME1BUTTONCANCELARRONDA)


        # panel historia de ganadoras

        self.panelGanadoras = wx.Panel(name=u'panelGanadoras', parent=self.panelRondas, pos=wx.Point(135, 500), size=wx.Size(900, 100), style=wx.TAB_TRAVERSAL)
        #self.panelGanadoras.SetBackgroundColour(wx.Colour(66, 90, 138))

        self.staticBoxGanadoras = wx.StaticBox(label='Ultimas ganadoras', name='staticBoxGanadoras', parent=self.panelGanadoras,
              pos=wx.Point(0, 0), size=wx.Size(900, 100), style=0)

        #self.staticBitmapElipseGanadoras = wx.StaticBitmap(bitmap=wx.Bitmap(u'Imagenes/elipseGanadoras.png', wx.BITMAP_TYPE_PNG),
        #      name='staticBitmapElipseGanadoras', parent=self.panelGanadoras, pos=wx.Point(0,5), size=wx.Size(1000, 100), style=0)

        self.staticBitmapGanadora1 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora1', parent=self.panelGanadoras,
              pos=wx.Point(50, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora2 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora2', parent=self.panelGanadoras,
              pos=wx.Point(125, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora3 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora3', parent=self.panelGanadoras,
              pos=wx.Point(200, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora4 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora4', parent=self.panelGanadoras,
              pos=wx.Point(275, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora5 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora5', parent=self.panelGanadoras,
              pos=wx.Point(350, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora6 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora6', parent=self.panelGanadoras,
              pos=wx.Point(425, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora7 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora7', parent=self.panelGanadoras,
              pos=wx.Point(500, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora8 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora8', parent=self.panelGanadoras,
              pos=wx.Point(575, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora9 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora9', parent=self.panelGanadoras,
              pos=wx.Point(650, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora10 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora10', parent=self.panelGanadoras,
              pos=wx.Point(725, 20), size=wx.Size(70, 70), style=0)

        self.staticBitmapGanadora11 = wx.StaticBitmap(bitmap=wx.NullBitmap, name=u'staticBitmapGanadora11', parent=self.panelGanadoras,
              pos=wx.Point(800, 20), size=wx.Size(70, 70), style=0)


        # panel para mostrar maquinas ganadoras del pozo al finalizar cada ronda
        self.panelGanadoresPozo = wx.Panel(name=u'panelGanadoresPozo',
                                           parent=self.panelRondas, pos=wx.Point(5, 5), size=wx.Size(885,700), style=wx.TAB_TRAVERSAL)
        self.panelGanadoresPozo.Show(False)

        self.staticTextGanadoresPozo = wx.StaticText(label=u'Se han ganado el Pozo!!!', name='staticTextGanadoresPozo',
              parent=self.panelGanadoresPozo, pos=wx.Point(200, 50), size=wx.Size(115, 23), style=0)
        self.staticTextGanadoresPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextGanadoresPozo2 = wx.StaticText(label=u'Monto total ganado: ', name='staticTextGanadoresPozo2',
              parent=self.panelGanadoresPozo, pos=wx.Point(200, 80), size=wx.Size(115, 23), style=0)
        self.staticTextGanadoresPozo2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextMontoTotalGanadoPozo = wx.StaticText(label=u'', name='staticTextMontoTotalGanadoPozo',
              parent=self.panelGanadoresPozo, pos=wx.Point(415, 80), size=wx.Size(115, 23), style=0)
        self.staticTextMontoTotalGanadoPozo.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextGanadoresPozo3 = wx.StaticText(label=u'Montos ganados por cada maquina: ', name='staticTextGanadoresPozo3',
              parent=self.panelGanadoresPozo, pos=wx.Point(200, 110), size=wx.Size(115, 23), style=0)
        self.staticTextGanadoresPozo3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.listCtrlGanadoresPozo = wx.ListCtrl(name=u'listCtrlGanadoresPozo', parent=self.panelGanadoresPozo,
              pos=wx.Point(200, 150), size=wx.Size(300, 200), style=wx.LC_HRULES | wx.LC_REPORT)
        self._init_coll_listCtrlGanadoresPozo_Columns(self.listCtrlGanadoresPozo)

        self.staticTextGanadoresPozo4 = wx.StaticText(label=u'Automaticamente se ha acreditado el monto ganado a cada maquina.', name='staticTextGanadoresPozo4',
              parent=self.panelGanadoresPozo, pos=wx.Point(200, 390), size=wx.Size(115, 23), style=0)
        self.staticTextGanadoresPozo4.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextGanadoresPozo5 = wx.StaticText(label=u'Por favor realice los procedimientos administrativos correspondientes.', name='staticTextGanadoresPozo5',
              parent=self.panelGanadoresPozo, pos=wx.Point(200, 420), size=wx.Size(115, 23), style=0)
        self.staticTextGanadoresPozo5.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextGanadoresPozo6 = wx.StaticText(label=u'Si el cliente lo desea, puede pagarsele mediante el menu Maquinas.', name='staticTextGanadoresPozo6',
              parent=self.panelGanadoresPozo, pos=wx.Point(200, 450), size=wx.Size(500, 23), style=0)
        self.staticTextGanadoresPozo6.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.staticTextGanadoresPozo7 = wx.StaticText(label=u'Finalmente, presione el boton Continuar para abrir una nueva ronda.', name='staticTextGanadoresPozo7',
              parent=self.panelGanadoresPozo, pos=wx.Point(200, 480), size=wx.Size(115, 23), style=0)
        self.staticTextGanadoresPozo7.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))

        self.buttonContinuarGanadoresPozo = wx.Button(label=u'Continuar', name=u'buttonContinuarGanadoresPozo', parent=self.panelGanadoresPozo,
              pos=wx.Point(550, 150), size=wx.Size(250, 200), style=0)
        self.buttonContinuarGanadoresPozo.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.buttonContinuarGanadoresPozo.Bind(wx.EVT_BUTTON, self.OnButtonContinuarGanadoresPozoButton)


        

        

    def __init__(self, parent):
        os.chdir(os.getcwd())
        self._init_ctrls(parent)
        # copia de seguridad de bd
        os.popen("echo '.dump' | sqlite3 bd | gzip -c >bd.dump.gz")
        #guardar una copia en otra carpeta
        lruta = os.getcwd().split("/")
        os.popen("echo '.dump' | sqlite3 bd | gzip -c >/home/%s/bd.dump.gz"%(lruta[2]))
        self.panelActivo = self.panelRondas
        self.panelAdminActivo = self.panelAdminCoordinadores
        self.apuestasAbiertas = False
        self.rondaAbierta = False
        # --- Cliente esporadico para MegaManager
        self.cedulaClienteEsporadico = "123456"
        # ---
        try:
            # cliente de servidor central
            conf = open("sc.conf")
            l = conf.readlines()
            ip, puerto = l[0][:-1], int(l[1][:-1])
            conf.close()
            s = "http://"+ip+":"+str(puerto)
            self.clienteServidorCentral = clienteCoordinadorDeServidorCentral(s)
            # clientes de cada maquina
            self.ipsYp = self.clienteServidorCentral.getIpsYpuertosMaquinas()
            self.clientesServidorMaquina = []
            for m in self.ipsYp:
                self.clientesServidorMaquina.append(clienteCoordinadorDeServidorMaquina(m[0],m[1]))
            # lista de coordinadores
            self.nombresCoordinadores = self.clienteServidorCentral.getNombresCoordinadores()
            # agregar administrador
            self.listCtrlCoordinadores.InsertStringItem(0,"ADMINISTRADOR")
            for i in range(len(self.nombresCoordinadores)):
                coord = self.nombresCoordinadores[i][0]
                self.listCtrlCoordinadores.InsertStringItem(i+1,coord)
                #para modulo administrativo
                self.listCtrlAdminCoordinadores.InsertStringItem(i,coord)
            # si la ronda quedo abierta hay que cancelarla y ajustar dinero de las maquinas
            if self.clienteServidorCentral.rondaAbierta():
                self.clienteServidorCentral.cancelarRonda()
                #actualizar maquinas si estan abiertas
                print "actualizando maquinas porque quedo ronda abierta..."
                for c in self.clientesServidorMaquina:
                    try:
                        c.anularTodo()
                        c.actualizarDisponible() #captura lo disponible de la bd y actualiza el dinero disponible del juego y el textoDisponible wx
                        c.bloquear(False)
                        # llamado a: c.anularTodo()
                        #   juego.anularTodo() ... suma al disponible del juego, apostado en 0 y dict apuestas a 0
                        #   limpiarPagno() ... oculta fichas y todos los textos wx a 0
                        #   asigna lo del juego al texto disponible
                        #   asigna lo del juego al texto apostado
                        #   asigna 0 al texto ganado
                    except Exception, e:
                        print "Maquina ", c.httpSer, " apagada"

        except Exception, e:
            print "Error al iniciar: ", e
            self.Destroy()
        # intentar comunicacion con el pozo
        try:
            confPozo = open("pozo.conf")
            dirPozo = confPozo.readline()[:-1]
            confPozo.close()
            self.clienteCoordinadorDeServidorPozo = clienteCoordinadorDeServidorPozo(dirPozo)
        except Exception, e:
            print "Error al iniciar: ", e
            self.Destroy()
        # intentar comunicacion con MegaManager
        try:
            confMegaManager = open("megaManager.conf")
            dirMegaManager = confMegaManager.readline()[:-1]
            confMegaManager.close()
            self.clienteCoordinadorDeMegaManager = clienteCoordinadorDeMegaManager(dirMegaManager)
            # sincronizar codigos de maquinas
            try:
                (modulos, codigos) = self.clienteCoordinadorDeMegaManager.getMaquinas()
                if not self.clienteServidorCentral.setMaquinasMegaManager(modulos, codigos):
                    dlg = wx.MessageDialog(self,'Error sincronizando codigos de maquinas: %s'%(e),'Error',wx.OK)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
            except Exception, e:
                dlg = wx.MessageDialog(self,'Error sincronizando codigos de maquinas: %s. Reinicie.'%(e),'Error',wx.OK)
                try:
                    dlg.ShowModal()
                finally:
                    dlg.Destroy()
        except Exception, e:
            dlg = wx.MessageDialog(self,'Error comunicando con MegaManager: %s. Reinicie'%(e),'Error',wx.OK)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

            

            
            
##    def separadorMiles(self, n):
##        """Formatea los numeros para presentarlos con separacion de miles"""
##        s = str(n)
##        cont = 1
##        sn = ""
##        i = len(s)
##        while i > 0:
##            if cont % 4 == 0 and s[i-1] != "-":
##                sn = s[i-1] + "." + sn
##                cont = 2
##            else:
##                sn = s[i-1] + sn
##                cont += 1
##            i -= 1
##        return sn
            
    def OnButtonVolverClaveButton(self, event):
        self.panelClave.Hide()
        self.textCtrlClave.SetValue("")
        self.panelCoordinadores.Show(True)
        
    def OnButton1Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"1")
        self.staticTextMsgClave.SetLabel("")

    def OnButton2Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"2")
        self.staticTextMsgClave.SetLabel("")

    def OnButton0Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"0")
        self.staticTextMsgClave.SetLabel("")

    def OnButton3Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"3")
        self.staticTextMsgClave.SetLabel("")

    def OnButton4Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"4")
        self.staticTextMsgClave.SetLabel("")

    def OnButton5Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"5")
        self.staticTextMsgClave.SetLabel("")

    def OnButton6Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"6")
        self.staticTextMsgClave.SetLabel("")

    def OnButton7Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"7")
        self.staticTextMsgClave.SetLabel("")

    def OnButton8Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"8")
        self.staticTextMsgClave.SetLabel("")

    def OnButton9Button(self, event):
        self.textCtrlClave.SetValue(self.textCtrlClave.GetValue()+"9")
        self.staticTextMsgClave.SetLabel("")

    def OnButtonBorrarButton(self, event):
        self.textCtrlClave.SetValue("")
        self.staticTextMsgClave.SetLabel("")

    def OnButtonAceptarButton(self, event):
        self.panelClave.Hide()
        cIntro = md5.md5(self.textCtrlClave.GetValue()).hexdigest()
        self.textCtrlClave.SetValue("")
        if self.coordinador != "ADMINISTRADOR": # validar clave para coordinador escogido
            cBd = self.clienteServidorCentral.getClaveCoordinador(self.idCoordinador)
            if cIntro == cBd:
                self.panelMenuPrincipal.Show(True)
            else:
                self.staticTextMsgClave.SetLabel("Clave Incorrecta")
                self.panelClave.Show(True)
        else:
            cBd = self.clienteServidorCentral.getClaveAdmin()
            if cIntro == cBd:
                self.panelAdministrador.Show(True)
            else:
                self.staticTextMsgClave.SetLabel("Clave Incorrecta")
                self.panelClave.Show(True)
                  

    def OnListCtrlCoordinadoresListItemSelected(self, event):
        self.coordinador = event.GetText() #guardar el coordinador que inicia sesion
        if self.coordinador != "ADMINISTRADOR":
            self.idCoordinador = self.clienteServidorCentral.getIdCoordinador(self.coordinador) #guardar su id
            self.staticTextCoordinador.SetLabel(self.coordinador) 
        self.panelCoordinadores.Hide()
        self.staticTextMsgClave.SetLabel("Introduzca su clave")
        self.panelClave.Show(True)

    def OnButtonRondasButton(self, event):
        self.panelPagos.Hide()
        self.panelRondas.Show(True)
        self.panelActivo = self.panelRondas
        self.actualizarBolasGanadoras()


    # actualizar historico de bolas ganadoras
    def actualizarBolasGanadoras(self):
        self.bolasGanadoras = self.clienteServidorCentral.getUltimasGanadoras(11)
        # relucir ultima bola ganadora ... puede ser una barrita dorada debajo
        for i in range(len(self.bolasGanadoras)):
            b = self.bolasGanadoras[i][0]
            if b != None:
                if b == "blanca":
                    eval("self.staticBitmapGanadora"+str(i+1)+".SetBitmap(wx.Bitmap(u'Imagenes/Ganadoras/blanca.png',wx.BITMAP_TYPE_PNG))")
                else:
                    eval("self.staticBitmapGanadora"+str(i+1)+".SetBitmap(wx.Bitmap(u'Imagenes/Ganadoras/"+b+".png',wx.BITMAP_TYPE_PNG))")


    def OnButtonPagosButton(self, event):
        self.panelRondas.Hide()   
        self.panelPagos.Show(True)
        self.panelActivo = self.panelPagos


    def OnButtonSincronizarMegaManagerButton(self, event):
        print "Sincronizando con MegaManager..."
        try:
            # traer pagos pendientes
            # [idPago, codCoordinador, codMaquina, valor, idCliente]
            pagosPendientes =  self.clienteServidorCentral.getPagosPendientesMegaManager()
            cantidadPagosPendientes = len(pagosPendientes)
            cantidadPagosSincronizadosMegaManager = 0
            cantidadPagosActualizadosBD = 0
            cantidadClientesEsporadicosAsignados = 0
            for pago in pagosPendientes:
                idPago = pago[0]
                idCliente = pago[4]
                enviado = ""
                # intentar verificar cedula del cliente
                try:
                    if not self.clienteCoordinadorDeMegaManager.existeCliente(idCliente):
                        idCliente = self.cedulaClienteEsporadico
                        cantidadClientesEsporadicosAsignados += 1
                except Exception, f:
                    idCliente = self.cedulaClienteEsporadico
                    cantidadClientesEsporadicosAsignados += 1
                # intentar envio a MegaManager
                try:
                    if self.clienteCoordinadorDeMegaManager.reportarPago(pago[1], pago[2], pago[3], idCliente):
                        enviado = "S"
                        cantidadPagosSincronizadosMegaManager += 1
                    else:
                        enviado = "N"
                except Exception, g:
                    enviado = "N"
                # si pudo enviar, actualizar en servidor central
                if enviado == "S":
                    if self.clienteServidorCentral.actualizarPagoMegaManager(idPago, enviado, idCliente):
                        cantidadPagosActualizadosBD += 1

            # traer recargas manuales pendientes
            # [idRecarga, valor, codMaquina, codCoordinador]
            recargasPendientes =  self.clienteServidorCentral.getRecargasPendientesMegaManager()
            cantidadRecargasPendientes = len(recargasPendientes)
            cantidadRecargasSincronizadasMegaManager = 0
            cantidadRecargasActualizadasBD = 0
            for recarga in recargasPendientes:
                idRecarga = recarga[0]
                enviado = ""
                # reportar recarga manual a MegaManager
                try:
                    if self.clienteCoordinadorDeMegaManager.reportarRecargaManual(recarga[1], recarga[2], recarga[3]):
                        enviado = "S"
                        cantidadRecargasSincronizadasMegaManager += 1
                    else:
                        enviado= "N"
                except Exception, e:
                    enviado = "N"
                # si pudo enviar, actualizar en servidor central
                if enviado == "S":
                    if self.clienteServidorCentral.actualizarRecargaManualMegaManager(idRecarga, enviado):
                        cantidadRecargasActualizadasBD += 1

            # mostrar resultados
            print "--- Pagos"
            print "Habian pendientes = ", cantidadPagosPendientes
            print "Sincronizados MegaManager = ", cantidadPagosSincronizadosMegaManager
            print "Actualizados BD = ", cantidadPagosActualizadosBD
            print "Clientes esporadicos asignados = ", cantidadClientesEsporadicosAsignados
            print "--- Recargas manuales"
            print "Habian pendientes = ", cantidadRecargasPendientes
            print "Sincronizadas MegaManager = ", cantidadRecargasSincronizadasMegaManager
            print "Actualizadas BD = ", cantidadRecargasActualizadasBD
            print "---"
            dlg = wx.MessageDialog(self,'Sincronizacion terminada!\n--- Pagos\nHabian pendientes = %s\nSincronizados MegaManager = %s\nActualizados BD = %s\nQuedan pendientes = %s\n--- Recargas manuales\nHabian pendientes = %s\nSincronizadas MegaManger = %s\nActualizadas BD = %s\nQuedan pendientes = %s\n'%(cantidadPagosPendientes, cantidadPagosSincronizadosMegaManager, cantidadPagosActualizadosBD, cantidadPagosPendientes-cantidadPagosActualizadosBD, cantidadRecargasPendientes, cantidadRecargasSincronizadasMegaManager, cantidadRecargasActualizadasBD, cantidadRecargasPendientes-cantidadRecargasActualizadasBD),'Info',wx.OK)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
        except Exception, e:
            dlg = wx.MessageDialog(self,'Error sincronizando con MegaManager: %s'%(e),'Error',wx.OK)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            

    def OnButtonAbrirRondaButton(self, event):
        if self.clienteServidorCentral.crearRonda(self.idCoordinador): #crear ronda en Bd
            self.buttonAbrirRonda.Disable()
            todoBien = True
            for c in self.clientesServidorMaquina: #desbloquear las maquinas
                try:
                    if c.limpiarPagno() and c.desbloquear():
                        #quitar candado de maquinas (candado abierto)
                        print "desbloqueada ", c.httpSer
                    else:
                        todoBien = False
                        print "error en maquina ", c.httpSer
                except:
                    print "Maquina ", c.httpSer, " apagada"
            if todoBien: 
                self.buttonCerrarApuestas.Enable()
                self.buttonCerrarSesion.Disable() #no puede cerrar sesion con ronda abierta
                self.buttonCancelarRonda.Enable() #puede cancelar ronda en cualquier momento
                self.apuestasAbiertas = True
                self.rondaAbierta = True
                print "ronda abierta"
            else:
                # solo dejar activo el boton para cancelar ronda
                dlg = wx.MessageDialog(self,'Error al abrir ronda en maquinas. Cancelar Ronda','Error',wx.OK)
                try:
                    dlg.ShowModal()
                finally:
                    dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self,'Imposible abrir ronda','Error',wx.OK)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()

    def OnButtonCerrarApuestasButton(self, event):
        self.buttonCerrarApuestas.Disable()
        todoBien = True
        pozoApuesta = False

        # inicio validar si al menos 1 cliente tiene apuestas
        hayApuestas = False
        for c in self.clientesServidorMaquina:
            try:
                if c.hayApuestas():
                    hayApuestas = True
            except Exception, e:
                print "OnCerrarApuestas >> validacionApuestasMaquina ", c.httpSer, " apagada"
        if not hayApuestas:
            dlg = wx.MessageDialog(self,'Todos los clientes sin apuestas minimas. Solicite por favor apuestas y luego vuelva a cerrar ronda','Info',wx.OK)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
            self.buttonCerrarApuestas.Enable()
            return
        # fin validar si al menos 1 cliente tiene apuestas
 
        # pozo va a apostar en esta ronda?
        if self.pozoApostara():
            pozoApuesta = True
            # entonces agregar jugada al pozo en jugadasPozo
            if not self.clienteServidorCentral.agregarJugadaPozo():
                todoBien = False

        if todoBien:
            #bloquear maquinas y recibir apuestas
            for c in self.clientesServidorMaquina: 
                try:
                    if c.bloquear(True):
                        #ir mostrando en gui candado a cada maquina
                        print "candado a m ", c.httpSer
                    else:
                        #colocar x de error a la maquina
                        todoBien = False
                        print "error en m ", c.httpSer
                except Exception, e:
                    #la maquina no responde. esta apagada
                    #colocar en gui apagada
                    print "Maquina ", c.httpSer, " apagada"
            if todoBien and self.clienteServidorCentral.cerrarApuestas():
                if pozoApuesta:
                    if self.clienteServidorCentral.actualizarMontoJugadaPozo():
                        #mostrar pagno para escoger bola ganadora
                        self.panelPagno.Enable()
                        self.apuestasAbiertas = False
                        print "apuestas cerradas y pozo jugando"
                        try:
                            self.clienteCoordinadorDeServidorPozo.pozoJugando()
                        except Exception, e:
                            print "OnButtonCerrarApuestasButton::pozoJugando > ", e
                    else:
                        # solo dejar activo el boton para cancelar ronda
                        dlg = wx.MessageDialog(self,'Imposible cerrar apuestas en actualizarMontoJugadaPozo. Cancelar Ronda','Error',wx.OK)
                        try:
                            dlg.ShowModal()
                        finally:
                            dlg.Destroy()
                else:
                    #mostrar pagno para escoger bola ganadora
                    self.panelPagno.Enable()
                    self.apuestasAbiertas = False
                    print "apuestas cerradas"
            else:
                # solo dejar activo el boton para cancelar ronda
                dlg = wx.MessageDialog(self,'Imposible cerrar apuestas. Cancelar Ronda','Error',wx.OK)
                try:
                    dlg.ShowModal()
                finally:
                    dlg.Destroy()
        else:
            # solo dejar activo el boton para cancelar ronda
            dlg = wx.MessageDialog(self,'Imposible cerrar apuestas en agregarJugadaPozo. Cancelar Ronda','Error',wx.OK)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()


    def pozoApostara(self):
        """Verifica que se cumpla con la frecuencia minima de sorteo y decide aleatoriamente si pozo apuesta en esta ronda o no"""
        frecuenciaSorteo = self.clienteServidorCentral.getFrecuenciaSorteoPozo()
        varRango = int(frecuenciaSorteo*__NUM_OPCIONES__/100.0)
        if varRango == 0:
            varRango = 1
        if self.clienteServidorCentral.getIdUltimaRonda() - self.clienteServidorCentral.getUltimaRondaJugadaPozo() > random.randrange(frecuenciaSorteo-varRango, frecuenciaSorteo+varRango):
            if random.randint(0,__NUM_OPCIONES__) == 1:
                return True
            else:
                return False
        else:
            return False



        

    def OnButtonCerrarSesionButton(self, event):
        #dlg = wx.MessageDialog(self,'Desea cerrar sesion y guardar reporte en memoria USB por defecto?','Confirmar',wx.YES_NO)
        #try:
            #if dlg.ShowModal() == wx.ID_YES:
        self.panelActivo.Hide()
        self.panelMenuPrincipal.Hide()
        self.panelCoordinadores.Show(True)
                #generar archivo de pagos hechos por el coordinador logueado en la fecha actual
        #finally:
            #dlg.Destroy()



    def mostrarGanadoresPozoActual(self, gananciasPozo):
        """Muestra las maquinas ganadoras del pozo en listCtrl mostrado cuando finaliza la ronda."""
        self.listCtrlGanadoresPozo.DeleteAllItems()
        for i in range(len(gananciasPozo)):
            self.listCtrlGanadoresPozo.InsertStringItem(i,str(i+1))   
            self.listCtrlGanadoresPozo.SetStringItem(i,1,separadorMiles(gananciasPozo[i]))
            # colocando color intermedio
            if (i+1) % 2 == 0:
                self.listCtrlGanadoresPozo.SetItemBackgroundColour(i, wx.LIGHT_GREY)


    def OnButtonContinuarGanadoresPozoButton(self, event):
        """Evento del boton para continuar cuando finaliza ronda y se han ganado el pozo."""
        # ocultar panel de ganadores pozo y mostrar de nuevo el pagno con los botones para poder abrir nueva ronda...
        self.panelGanadoresPozo.Show(False)
        self.panelPagno.Show(True)
        self.panelGanadoras.Show(True)
        self.buttonAbrirRonda.Show(True)
        self.buttonCerrarApuestas.Show(True)
        self.buttonCerrarSesion.Show(True)
        self.buttonCancelarRonda.Show(True)

                

    def confirmarGanadora(self, idsO, tB):
        #recibe los ids de las opciones ganadoras y el texto de la ganadora
        dlg = wx.MessageDialog(self,'Confirma bola %s como ganadora?'%(tB),'Confirmar',wx.YES_NO)
        try:
            if dlg.ShowModal() == wx.ID_YES:
                # asignar ganancias en servidor central
                ganancias, hayGanadoresPozo, gananciasPozo = self.clienteServidorCentral.asignarGanancias(idsO)
                if ganancias != [-1]: #todo estuvo bien. asignarGanadora a ronda y...
                    self.clienteServidorCentral.asignarGanadora(tB)

                    if hayGanadoresPozo:
                        try:
                            self.clienteCoordinadorDeServidorPozo.pozoGanado()
                        except Exception, ex:
                            print "confirmarGanadora::pozoGanado > ", ex
                    
                    #...actualizar maquinas con lo ganado
                    i = 0
                    for c in self.clientesServidorMaquina:
                        try:
                            c.actualizarGanadoras()
                            c.actualizarDisponible()
                            c.actualizarGanado(ganancias[i])
                            c.ocultarFichas()
                            c.mostrarApuestasGanadoras(tB)
                            print "Actualizada m ", c.httpSer
                        except Exception, e:
                            print "Maquina ", c.httpSer, " apagada" 
                            #print e
                        i += 1
                    if self.clienteServidorCentral.finalizarRonda():
                        # ronda finalizada correctamente...
                        # actualizo monto visual en Pozo
                        try:
                            self.clienteCoordinadorDeServidorPozo.actualizarMonto(self.clienteServidorCentral.getMontoActualPozo())
                        except Exception, f:
                            print "confirmarGanadora :: error actualizando monto del pozo: ", f
                            
                        # Actualizo gui del coordinador
                        if hayGanadoresPozo:
                            # Si hubo ganadores del pozo --> mostrar ganadores del pozo a coordinador"
                            self.panelPagno.Show(False)
                            self.panelGanadoras.Show(False)
                            self.buttonAbrirRonda.Show(False)
                            self.buttonCerrarApuestas.Show(False)
                            self.buttonCerrarSesion.Show(False)
                            self.buttonCancelarRonda.Show(False)
                            self.panelGanadoresPozo.Show(True)
                            self.staticTextMontoTotalGanadoPozo.SetLabel(str(sum(gananciasPozo)))
                            self.mostrarGanadoresPozoActual(gananciasPozo)
                        #else:
                            # no hay ganadores del pozo...
                        self.panelPagno.Disable()
                        self.buttonAbrirRonda.Enable()
                        self.buttonCerrarSesion.Enable()
                        self.buttonCancelarRonda.Disable() # no hay ronda abierta para cancelar
                        self.actualizarBolasGanadoras()
                        self.rondaAbierta = False
                    else:
                        # solo dejar activo el boton para cancelar ronda
                        dlg = wx.MessageDialog(self,'Imposible finalizar ronda. Cancelar Ronda','Error',wx.OK)
                        try:
                            dlg.ShowModal()
                        finally:
                            dlg.Destroy()
                else:
                    # solo dejar activo el boton para cancelar ronda
                    dlg = wx.MessageDialog(self,'Imposible asignar ganancias. Cancelar Ronda','Error',wx.OK)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
        finally:
            dlg.Destroy()
    
    def OnStaticBitmapBlancaLeftUp(self, event):
        self.confirmarGanadora([1],"blanca")

    def OnStaticBitmap1LeftUp(self, event):
        self.confirmarGanadora([2,12,15,16,18,26,31],"1")

    def OnStaticBitmap2LeftUp(self, event):
        self.confirmarGanadora([3,12,14,17,19,26,31],"2")

    def OnStaticBitmap3LeftUp(self, event):
        self.confirmarGanadora([4,12,15,17,19,21,27,31,32],"3")

    def OnStaticBitmap4LeftUp(self, event):
        self.confirmarGanadora([5,12,14,16,18,20,27,31,32],"4")

    def OnStaticBitmap5LeftUp(self, event):
        self.confirmarGanadora([6,12,15,16,20,22,28,32,33],"5")

    def OnStaticBitmap6LeftUp(self, event):
        self.confirmarGanadora([7,13,14,17,21,23,28,32,33],"6")

    def OnStaticBitmap7LeftUp(self, event):
        self.confirmarGanadora([8,13,15,17,23,25,29,33,34],"7")

    def OnStaticBitmap8LeftUp(self, event):
        self.confirmarGanadora([9,13,14,16,22,24,29,33,34],"8")

    def OnStaticBitmap9LeftUp(self, event):
        self.confirmarGanadora([10,13,15,16,24,30,34],"9")

    def OnStaticBitmap10LeftUp(self, event):
        self.confirmarGanadora([11,13,14,17,25,30,34],"10")
        
    def mostrarDetalleMaquina(self, posM):
        self.buttonRondas.Disable()
        self.buttonCerrarSesion.Disable()
        self.panelMontoPagos.Show(True)
        self.staticBoxDisponible.SetLabel("Maquina "+str(posM+1))
        self.dinero = self.clienteServidorCentral.getDinero(self.ipsYp[posM][0],self.ipsYp[posM][1])
        self.staticTextMontoDisponible.SetLabel(separadorMiles(self.dinero))
        self.textCtrlPagar.SetValue(separadorMiles(self.dinero))
        self.textCtrlCedulaCliente.SetValue("")


    def deshabilitarPanelMaquinas(self):
        self.panelMaquina1.Disable()
        self.panelMaquina2.Disable()
        self.panelMaquina3.Disable()
        self.panelMaquina4.Disable()
        self.panelMaquina5.Disable()
        self.panelMaquina6.Disable()
        self.panelMaquina7.Disable()
        self.panelMaquina8.Disable()
        

    def OnStaticBitmapMaquina1LeftUp(self, event):
        self.deshabilitarPanelMaquinas()
        self.panelMaquina1.Enable()
        try:
            #si no se han comprometido las apuestas anularlas
            if self.rondaAbierta and self.apuestasAbiertas:
                self.clientesServidorMaquina[0].anularTodo() 
            self.clientesServidorMaquina[0].bloquear(False) #bloquearla para impedir apuestas
        except:
            self.staticTextMsg.SetLabel("Maquina apagada o no responde")
            self.staticTextMsgAgregarCredito.SetLabel("Maquina apagada o no responde")
        self.idMaquina = 1
        self.mostrarDetalleMaquina(0)

    def OnStaticBitmapMaquina2LeftUp(self, event):
        self.deshabilitarPanelMaquinas()
        self.panelMaquina2.Enable()
        try:
            #si no se han comprometido las apuestas anularlas
            if self.rondaAbierta and self.apuestasAbiertas:
                self.clientesServidorMaquina[1].anularTodo()
            self.clientesServidorMaquina[1].bloquear(False)
        except:
            self.staticTextMsg.SetLabel("Maquina apagada o no responde")
            self.staticTextMsgAgregarCredito.SetLabel("Maquina apagada o no responde")
        self.idMaquina = 2
        self.mostrarDetalleMaquina(1)

    def OnStaticBitmapMaquina3LeftUp(self, event):
        self.deshabilitarPanelMaquinas()
        self.panelMaquina3.Enable()
        try:
            #si no se han comprometido las apuestas anularlas
            if self.rondaAbierta and self.apuestasAbiertas:
                self.clientesServidorMaquina[2].anularTodo()
            self.clientesServidorMaquina[2].bloquear(False)
        except:
            self.staticTextMsg.SetLabel("Maquina apagada o no responde")
            self.staticTextMsgAgregarCredito.SetLabel("Maquina apagada o no responde")
        self.idMaquina = 3
        self.mostrarDetalleMaquina(2)

    def OnStaticBitmapMaquina4LeftUp(self, event):
        self.deshabilitarPanelMaquinas()
        self.panelMaquina4.Enable()
        try:
            #si no se han comprometido las apuestas anularlas
            if self.rondaAbierta and self.apuestasAbiertas:
                self.clientesServidorMaquina[3].anularTodo()
            self.clientesServidorMaquina[3].bloquear(False)
        except:
            self.staticTextMsg.SetLabel("Maquina apagada o no responde")
            self.staticTextMsgAgregarCredito.SetLabel("Maquina apagada o no responde")
        self.idMaquina = 4
        self.mostrarDetalleMaquina(3)

    def OnStaticBitmapMaquina5LeftUp(self, event):
        self.deshabilitarPanelMaquinas()
        self.panelMaquina5.Enable()
        try:
            #si no se han comprometido las apuestas anularlas
            if self.rondaAbierta and self.apuestasAbiertas:
                self.clientesServidorMaquina[4].anularTodo()
            self.clientesServidorMaquina[4].bloquear(False)
        except:
            self.staticTextMsg.SetLabel("Maquina apagada o no responde")
            self.staticTextMsgAgregarCredito.SetLabel("Maquina apagada o no responde")
        self.idMaquina = 5
        self.mostrarDetalleMaquina(4)

    def OnStaticBitmapMaquina6LeftUp(self, event):
        self.deshabilitarPanelMaquinas()
        self.panelMaquina6.Enable()
        try:
            #si no se han comprometido las apuestas anularlas
            if self.rondaAbierta and self.apuestasAbiertas:
                self.clientesServidorMaquina[5].anularTodo()
            self.clientesServidorMaquina[5].bloquear(False)
        except:
            self.staticTextMsg.SetLabel("Maquina apagada o no responde")
            self.staticTextMsgAgregarCredito.SetLabel("Maquina apagada o no responde")
        self.idMaquina = 6
        self.mostrarDetalleMaquina(5)

    def OnStaticBitmapMaquina7LeftUp(self, event):
        self.deshabilitarPanelMaquinas()
        self.panelMaquina7.Enable()
        try:
            #si no se han comprometido las apuestas anularlas
            if self.rondaAbierta and self.apuestasAbiertas:
                self.clientesServidorMaquina[6].anularTodo()
            self.clientesServidorMaquina[6].bloquear(False)
        except:
            self.staticTextMsg.SetLabel("Maquina apagada o no responde")
            self.staticTextMsgAgregarCredito.SetLabel("Maquina apagada o no responde")
        self.idMaquina = 7
        self.mostrarDetalleMaquina(6)

    def OnStaticBitmapMaquina8LeftUp(self, event):
        self.deshabilitarPanelMaquinas()
        self.panelMaquina8.Enable()
        try:
            #si no se han comprometido las apuestas anularlas
            if self.rondaAbierta and self.apuestasAbiertas:
                self.clientesServidorMaquina[7].anularTodo()
            self.clientesServidorMaquina[7].bloquear(False)
        except:
            self.staticTextMsg.SetLabel("Maquina apagada o no responde")
            self.staticTextMsgAgregarCredito.SetLabel("Maquina apagada o no responde")
        self.idMaquina = 8
        self.mostrarDetalleMaquina(7)

    
        
    def activarPanelesMaquinas(self):
        self.panelMaquina1.Enable()
        self.panelMaquina2.Enable()
        self.panelMaquina3.Enable()
        self.panelMaquina4.Enable()
        self.panelMaquina5.Enable()
        self.panelMaquina6.Enable()
        self.panelMaquina7.Enable()
        self.panelMaquina8.Enable()


    def OnButtonHistoriaJugadasButton(self, event):
        idUltimaRonda = self.clienteServidorCentral.getIdUltimaRonda()
        infoUltima = self.clienteServidorCentral.getDetalleApuestasClienteEnRonda(self.idMaquina, idUltimaRonda)
        idPenultimaRonda = idUltimaRonda - 1
        infoPenultima = self.clienteServidorCentral.getDetalleApuestasClienteEnRonda(self.idMaquina, idPenultimaRonda)
        idAntepenultimaRonda = idUltimaRonda - 2
        infoAntepenultima = self.clienteServidorCentral.getDetalleApuestasClienteEnRonda(self.idMaquina, idAntepenultimaRonda)
        # preparando info para enviar al frame
        rondas = self.clienteServidorCentral.getInfoUltimasRondas(3)
        info = [infoUltima, infoPenultima, infoAntepenultima]
        opciones = self.clienteServidorCentral.getOpciones()
        # frame para mostrar historia de jugadas hechas por una maquina
        self.frameHistoriaJugadas = frameHistoriaJugadas(self, self.idMaquina, rondas, info, opciones)
        self.frameHistoriaJugadas.Show()
        self.frameHistoriaJugadas.SetFocus()
        

    def OnButtonAceptarPagoButton(self, event):
        v = self.textCtrlPagar.GetValue().replace(".","")
        # para reportar a MegaManager
        cedulaCliente = self.textCtrlCedulaCliente.GetValue().replace(".","")
        enviado = "N"
        #
        if v != "":
            aPagar = int(v)
            if aPagar > 0:
                if aPagar <= self.dinero:
                    self.panelMontoPagos.Hide()
                    self.buttonRondas.Enable()
                    if not self.rondaAbierta:
                        self.buttonCerrarSesion.Enable()
                    self.staticTextMsg.SetLabel("")
                    # activar todos los paneles de maquinas
                    self.activarPanelesMaquinas()

                    # --- Validaciones para Mega Manager ---
                    # intentar verificar cedula del cliente
                    try:
                        if not self.clienteCoordinadorDeMegaManager.existeCliente(cedulaCliente):
                            cedulaClienteOriginal = cedulaCliente
                            cedulaCliente = self.cedulaClienteEsporadico
                            dlg = wx.MessageDialog(self,'Cliente "%s" no existe. Cliente esporadico asignado'%(cedulaClienteOriginal),'Info',wx.OK)
                            try:
                                dlg.ShowModal()
                            finally:
                                dlg.Destroy()
                    except Exception, e:
                        #cedulaCliente = self.cedulaClienteEsporadico
                        dlg = wx.MessageDialog(self,'Error verificando cliente en MegaManager: %s'%(e),'Info',wx.OK)
                        try:
                            dlg.ShowModal()
                        finally:
                            dlg.Destroy()

                    # traer codigo de maquina y coordinador equivalentes en MegaManager
                    getCodMaquinaMegaManagerResponse = self.clienteServidorCentral.getCodMaquinaMegaManager(self.idMaquina)
                    getCodCoordinadorMegaManagerResponse = self.clienteServidorCentral.getCodCoordinadorMegaManager(self.idCoordinador)
                    if getCodMaquinaMegaManagerResponse[0] and getCodCoordinadorMegaManagerResponse[0]:
                        # reportar pago a MegaManager
                        try:
                            if self.clienteCoordinadorDeMegaManager.reportarPago(getCodCoordinadorMegaManagerResponse[1], getCodMaquinaMegaManagerResponse[1], aPagar, cedulaCliente):
                                enviado = "S"
                            else:
                                dlg = wx.MessageDialog(self,'MegaManager no proceso el pago y quedara pendiente hasta sincronizar.\nCoordinador: %s\nMaquina: %s\nValor: %s\nCliente: %s.'%(self.coordinador, self.idMaquina, aPagar, cedulaCliente),'Info',wx.OK)
                                try:
                                    dlg.ShowModal()
                                finally:
                                    dlg.Destroy()
                        except Exception, e:
                            dlg = wx.MessageDialog(self,'Error reportando pago a MegaManager. Quedara pendiente hasta sincronizar.\nCoordinador: %s\nMaquina: %s\nValor: %s\nCliente: %s.\nError: %s'%(self.coordinador, self.idMaquina, aPagar, cedulaCliente, e),'Info',wx.OK)
                            try:
                                dlg.ShowModal()
                            finally:
                                dlg.Destroy()
                    else:
                        dlg = wx.MessageDialog(self,'Imposible reportar a MegaManager. Error consiguiendo codigos equivalentes de maquina y coordinador. Reinicie el sistema.','Error',wx.OK)
                        try:
                            dlg.ShowModal()
                        finally:
                            dlg.Destroy()

                    # --- Final validaciones para Mega Manager
                    
                    # pagar en el servidor central
                    self.clienteServidorCentral.pagar(self.idCoordinador,self.idMaquina,aPagar,cedulaCliente, enviado)
                    
                    #intentar actualizar y desbloquear maquina si esta prendida
                    try:
                        m = self.clientesServidorMaquina[self.idMaquina-1]
                        m.actualizarDisponible()
                        if self.apuestasAbiertas:
                            m.desbloquear()
                    except:
                        self.staticTextMsg.SetLabel("")
                    
                else:
                    self.staticTextMsg.SetLabel("Monto a pagar debe ser menor del disponible")
            else:
                self.staticTextMsg.SetLabel("Entra valor mayor a 0")
        else:
            self.staticTextMsg.SetLabel("Entra valor a pagar")

    def OnButtonCancelarMontoPagosButton(self, event):
        self.panelMontoPagos.Hide()
        self.buttonRondas.Enable()
        if not self.rondaAbierta:
            self.buttonCerrarSesion.Enable()
        self.staticTextMsg.SetLabel("")
        self.staticTextMsgAgregarCredito.SetLabel("")
        self.activarPanelesMaquinas() #activar todos los paneles de maquinas
        try:
            if self.apuestasAbiertas:
                self.clientesServidorMaquina[self.idMaquina-1].desbloquear() #desbloquear maquina
        except:
            self.staticTextMsg.SetLabel("")

    def OnTextCtrlPagarLeftUp(self, event):
        # por facilidad para el coordinador, borro el monto mostrado
        #self.textCtrlPagar.SetValue("")
        # ocultar todo el panel activo
        self.panelMontoPagos.Hide()
        # crear teclado numerico
        self.tecladoNumerico = tecladoNumerico.tecladoNumerico(self.panelPagos,650,150)
        #self.tecladoNumerico.Hide()
        # asignar textCtrl activado a teclado
        self.tecladoNumerico.setTextCtrl(self.textCtrlPagar)
        # asignar un panel de regreso a donde volver cuando termine la entrada de teclado
        self.tecladoNumerico.setPanelRegreso(self.panelMontoPagos)
        # activar mostrar con separador de miles
        self.tecladoNumerico.setSeparadorMiles(True)
        # desactivar punto del teclado numerico
        self.tecladoNumerico.desactivarPunto()
        # mostrar teclado numerico
        self.tecladoNumerico.Show()
        event.Skip()


    def OnTextCtrlCedulaClienteLeftUp(self, event):
        """Cedula del cliente para reportar a MegaManager."""
        # ocultar todo el panel activo
        self.panelMontoPagos.Hide()
        # crear teclado numerico
        self.tecladoNumerico = tecladoNumerico.tecladoNumerico(self.panelPagos,650,150)
        # asignar textCtrl activado a teclado
        self.tecladoNumerico.setTextCtrl(self.textCtrlCedulaCliente)
        # asignar un panel de regreso a donde volver cuando termine la entrada de teclado
        self.tecladoNumerico.setPanelRegreso(self.panelMontoPagos)
        # activar mostrar con separador de miles
        self.tecladoNumerico.setSeparadorMiles(True)
        # desactivar punto del teclado numerico
        self.tecladoNumerico.desactivarPunto()
        # mostrar teclado numerico
        self.tecladoNumerico.Show()
        event.Skip()


    # botones para agregar credito
    def OnButtonAceptarAgregarCreditoButton(self, event):
        v = self.textCtrlAgregar.GetValue().replace(".","")
        # --- para reportar a MegaManager
        enviado = "N"
        # ---
        if v != "":
            aAgregar = int(v)
            if aAgregar > 0:
                # --- validaciones previas MegaManager
                # traer codigo de maquina y coordinador equivalentes en MegaManager
                getCodMaquinaMegaManagerResponse = self.clienteServidorCentral.getCodMaquinaMegaManager(self.idMaquina)
                getCodCoordinadorMegaManagerResponse = self.clienteServidorCentral.getCodCoordinadorMegaManager(self.idCoordinador)
                if getCodMaquinaMegaManagerResponse[0] and getCodCoordinadorMegaManagerResponse[0]:
                    # reportar recarga manual a MegaManager
                    try:
                        if self.clienteCoordinadorDeMegaManager.reportarRecargaManual(aAgregar, getCodMaquinaMegaManagerResponse[1], getCodCoordinadorMegaManagerResponse[1]):
                            enviado = "S"
                        else:
                            dlg = wx.MessageDialog(self,'MegaManager no proceso la recarga. Quedara pendiente hasta sincronizar.\nCoordinador: %s\nMaquina: %s\nRecarga: %s'%(self.coordinador, self.idMaquina, aAgregar),'Info',wx.OK)
                            try:
                                dlg.ShowModal()
                            finally:
                                dlg.Destroy()
                    except Exception, e:
                        dlg = wx.MessageDialog(self,'Error reportando recarga manual a MegaManager. Quedara pendiente hasta sincronizar.\nCoordinador: %s\nMaquina: %s\nRecarga: %s.\nError: %s'%(self.coordinador, self.idMaquina, aAgregar, e),'Info',wx.OK)
                        try:
                            dlg.ShowModal()
                        finally:
                            dlg.Destroy()
                else:
                    dlg = wx.MessageDialog(self,'Imposible reportar a MegaManager. Error consiguiendo codigos equivalentes de maquina y coordinador. Reinicie el sistema.','Error',wx.OK)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
                # --- Final validaciones para Mega Manager
                
                self.panelMontoPagos.Hide()
                self.buttonRondas.Enable()
                if not self.rondaAbierta:
                    self.buttonCerrarSesion.Enable()
                self.staticTextMsg.SetLabel("")
                self.staticTextMsgAgregarCredito.SetLabel("")
                # activar todos los paneles de maquinas
                self.activarPanelesMaquinas()
                # agregar en el servidor central
                if self.clienteServidorCentral.agregarCreditoManual(self.idCoordinador, self.idMaquina, aAgregar, enviado):
                    self.textCtrlAgregar.SetValue("")
                else:
                    self.staticTextMsgAgregarCredito.SetLabel("Imposible agregar credito")
                #intentar actualizar y desbloquear maquina si esta prendida
                try:
                    m = self.clientesServidorMaquina[self.idMaquina-1]
                    m.actualizarDisponible()
                    if self.apuestasAbiertas:
                        m.desbloquear()
                except:
                    self.staticTextMsg.SetLabel("")
                    self.staticTextMsgAgregarCredito.SetLabel("")
            else:
                self.staticTextMsgAgregarCredito.SetLabel("Entra valor mayor a 0")
        else:
            self.staticTextMsgAgregarCredito.SetLabel("Entra valor a agregar")




    # textCtrl para agregar credito a maquina seleccionada
    def OnTextCtrlAgregarLeftUp(self, event):
        #self.textCtrlAgregar.SetValue("")
        # ocultar todo el panel activo
        self.panelMontoPagos.Hide()
        # crear teclado numerico
        self.tecladoNumerico = tecladoNumerico.tecladoNumerico(self.panelPagos,650,150)
        #self.tecladoNumerico.Hide()
        # asignar textCtrl activado a teclado
        self.tecladoNumerico.setTextCtrl(self.textCtrlAgregar)
        # asignar un panel de regreso a donde volver cuando termine la entrada de teclado
        self.tecladoNumerico.setPanelRegreso(self.panelMontoPagos)
        # activar mostrar con separador de miles
        self.tecladoNumerico.setSeparadorMiles(True)
        # desactivar punto del teclado numerico
        self.tecladoNumerico.desactivarPunto()
        # mostrar teclado numerico
        self.tecladoNumerico.Show()
        event.Skip()



    def OnButtonMenuSalirButton(self, event):
        # menu salir de modulo administrativo
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdministrador.Hide()
        self.panelNumeros.Hide()
        self.panelCoordinadores.Show(True)

    def OnButtonMenuCoordinadoresButton(self, event):
        # administrar coordinadores
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminCoordinadores
        self.panelAdminCoordinadores.Show(True)

    def OnListCtrlAdminCoordinadoresListItemSelected(self, event):
        self.buttonEliminar.Enable()
        self.coordinadorSeleccionado = event.GetText()
        
    def activarMenues(self, b):
        # activa o desactiva los menues
        self.buttonMenuAdministrador.Enable(b)
        self.buttonMenuCoordinadores.Enable(b)
        self.buttonMenuMonedas.Enable(b)
        self.buttonMenuOpciones.Enable(b)
        self.buttonMenuRondas.Enable(b)
        self.buttonMenuBilletes.Enable(b)
        self.buttonMenuPagos.Enable(b)
        self.buttonMenuCuadre.Enable(b)
        self.buttonMenuSalir.Enable(b)
        self.buttonMenuCreditosManuales.Enable(b)
        self.buttonMenuPozo.Enable(b)

    def OnButtonAgregarButton(self, event):
        self.listCtrlAdminCoordinadores.Disable()
        self.buttonAgregar.Disable()
        self.buttonEliminar.Disable()
        print "deseleccionar todo del listCtrlAdminCoordinadores"
        self.panelAgregarCoordinador.Show(True)
        self.activarMenues(False)
        
    def actualizarListCtrlCoordinadores(self):
        self.listCtrlCoordinadores.DeleteAllItems()
        self.listCtrlAdminCoordinadores.DeleteAllItems()
        self.nombresCoordinadores = self.clienteServidorCentral.getNombresCoordinadores()
        self.listCtrlCoordinadores.InsertStringItem(0,"ADMINISTRADOR")
        for i in range(len(self.nombresCoordinadores)):
            self.listCtrlCoordinadores.InsertStringItem(i+1,self.nombresCoordinadores[i][0])
            self.listCtrlAdminCoordinadores.InsertStringItem(i,self.nombresCoordinadores[i][0])

    def OnButtonEliminarButton(self, event):
        if self.clienteServidorCentral.eliminarCoordinador(self.coordinadorSeleccionado):
            self.buttonEliminar.Disable()
            self.actualizarListCtrlCoordinadores()

    def OnTextCtrlNombreNuevoCoordinadorLeftUp(self, event):
        self.panelNumeros.Hide()
        self.textCtrlActivo = self.textCtrlNombreNuevoCoordinador
        self.panelTeclado.Show(True)

    def OnTextCtrlClaveNuevoCoordinadorLeftUp(self, event):
        #self.buttonAgregarCoordinador.Enable()
        self.panelTeclado.Hide()
        self.textCtrlActivo = self.textCtrlClaveNuevoCoordinador
        self.panelNumeros.Show(True)

    def OnTextCtrlCodMegaManagerLeftUp(self, event):
        self.buttonAgregarCoordinador.Enable()
        self.panelTeclado.Hide()
        self.textCtrlActivo = self.textCtrlCodMegaManager
        self.panelNumeros.Show(True)

    def OnButtonQButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"Q")

    def OnButtonWButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"W")

    def OnButtonEButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"E")

    def OnButtonRButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"R")

    def OnButtonTButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"T")

    def OnButtonYButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"Y")

    def OnButtonUButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"U")

    def OnButtonIButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"I")

    def OnButtonOButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"O")

    def OnButtonPButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"P")

    def OnButtonAButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"A")

    def OnButtonSButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"S")

    def OnButtonDButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"D")

    def OnButtonFButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"F")

    def OnButtonGButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"G")

    def OnButtonHButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"H")

    def OnButtonJButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"J")

    def OnButtonKButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"K")

    def OnButtonLButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"L")

    def OnButtonZButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"Z")

    def OnButtonXButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"X")

    def OnButtonCButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"C")

    def OnButtonVButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"V")

    def OnButtonBButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"B")

    def OnButtonNButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"N")

    def OnButtonMButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"M")

    def OnButtonEspacioButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+" ")

    def OnButtonTecladoBorrarButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()[:-1])

    def OnButtonNumero0Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"0")

    def OnButtonNumero1Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"1")

    def OnButtonNumero2Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"2")

    def OnButtonNumero3Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"3")

    def OnButtonNumero4Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"4")

    def OnButtonNumero5Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"5")

    def OnButtonNumero6Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"6")

    def OnButtonNumero7Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"7")

    def OnButtonNumero8Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"8")

    def OnButtonNumero9Button(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+"9")

    def OnButtonPuntoButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()+".")

    def OnButtonNumeroBorrarButton(self, event):
        self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue()[:-1])

    def OnButtonAgregarCoordinadorButton(self, event):
        c = self.textCtrlClaveNuevoCoordinador.GetValue()
        if len(c) == 4:
            codMegaManager = self.textCtrlCodMegaManager.GetValue()
            if len(codMegaManager) >= 1:
                nombre = self.textCtrlNombreNuevoCoordinador.GetValue()
                if len(nombre) >= 1:
                    if self.clienteServidorCentral.agregarCoordinador(nombre, md5.md5(c).hexdigest(), codMegaManager):
                        self.ocultarPanelAgregarCoordinador()
                        self.actualizarListCtrlCoordinadores()
                        self.activarMenues(True)
                    else:
                        self.staticTextMsgAgregarCoordinador.SetLabel("Error agregando coordinador")
                else:
                    self.staticTextMsgAgregarCoordinador.SetLabel("Nombre obligatorio")
            else:
                self.staticTextMsgAgregarCoordinador.SetLabel("Codigo MegaManager obligatorio")
        else:
            self.staticTextMsgAgregarCoordinador.SetLabel("La clave debe tener 4 digitos")

    def OnButtonCancelarCoordinadorButton(self, event):
        self.ocultarPanelAgregarCoordinador()
        self.activarMenues(True)
        
    def ocultarPanelAgregarCoordinador(self):
        self.panelAgregarCoordinador.Hide()
        self.textCtrlNombreNuevoCoordinador.SetValue("")
        self.textCtrlClaveNuevoCoordinador.SetValue("")
        self.textCtrlCodMegaManager.SetValue("")
        self.staticTextMsgAgregarCoordinador.SetLabel("")
        self.buttonAgregarCoordinador.Disable()
        self.panelTeclado.Hide()
        self.panelNumeros.Hide()
        self.buttonAgregar.Enable()
        self.listCtrlAdminCoordinadores.Enable()
        
    def actualizarValoresMonedas(self):
        self.staticTextFechaValoresMonedasVigentes.SetLabel(str(self.clienteServidorCentral.getFechaValoresMonedasVigentes()))
        vXm = self.clienteServidorCentral.getValoresXmonedas()
        self.textCtrlMoneda1.SetValue(separadorMiles(vXm[0]))
        self.textCtrlMoneda2.SetValue(separadorMiles(vXm[1]))
        self.textCtrlMoneda3.SetValue(separadorMiles(vXm[2]))
        self.textCtrlMoneda4.SetValue(separadorMiles(vXm[3]))
        self.textCtrlMoneda5.SetValue(separadorMiles(vXm[4]))

    def OnButtonMenuMonedasButton(self, event):
        # administrar monedas
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminMonedas
        self.panelAdminMonedas.Show(True)
        self.actualizarValoresMonedas() #mostrar valoresXmonedas vigentes



    def OnButtonMenuPozoButton(self, event):
        # administrar pozo
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminPozo
        self.panelAdminPozo.Show(True)
        self.actualizarValoresPozo()
        self.panelGuardar.Show(True)


    def actualizarValoresPozo(self):
        self.textCtrlMontoInicialPozo.SetValue(separadorMiles(self.clienteServidorCentral.getMontoInicialPozo()))
        self.textCtrlMontoActualPozo.SetValue(separadorMiles(self.clienteServidorCentral.getMontoActualPozo()))
        self.textCtrlMontoReservaPozo.SetValue(separadorMiles(self.clienteServidorCentral.getMontoReservaPozo()))
        self.textCtrlMinimoParaConcursarPozo.SetValue(separadorMiles(self.clienteServidorCentral.getMontoMinimoParaConcursarPozo()))
        self.textCtrlFrecuenciaSorteoPozo.SetValue(separadorMiles(self.clienteServidorCentral.getFrecuenciaSorteoPozo()))
        self.textCtrlFactorReservaPozo.SetValue(separadorMiles(self.clienteServidorCentral.getFactorReservaPozo()))
        self.textCtrlFactorIncrementoPozo.SetValue(separadorMiles(self.clienteServidorCentral.getFactorIncrementoPozo()))
        self.textCtrlUltimaRondaJugadaPozo.SetValue(separadorMiles(self.clienteServidorCentral.getUltimaRondaJugadaPozo()))


    def onTextCtrlAdminPozo(self, textCtrl, coma):
        # crear teclado numerico
        self.tecladoNumerico = tecladoNumerico.tecladoNumerico(self.panelAdminPozo,850,150)
        # asignar textCtrl activado a teclado
        self.tecladoNumerico.setTextCtrl(textCtrl)
        # asignar un panel de regreso a donde volver cuando termine la entrada de teclado
        self.tecladoNumerico.setPanelRegreso(self.panelAdminPozo)
        # activar mostrar con separador de miles
        self.tecladoNumerico.setSeparadorMiles(True)
        if not coma:
            # desactivar punto del teclado numerico
            self.tecladoNumerico.desactivarPunto()
        # asignar objetos impactados
        self.tecladoNumerico.setImpactados(self.modificablesAdminPozo)
        # mostrar teclado numerico
        self.tecladoNumerico.Show()


    def OnTextCtrlMontoInicialPozoLeftUp(self, event):
        self.onTextCtrlAdminPozo(self.textCtrlMontoInicialPozo, False)


    def OnTextCtrlMinimoParaConcursarPozoLeftUp(self, event):
        self.onTextCtrlAdminPozo(self.textCtrlMinimoParaConcursarPozo, False)


    def OnTextCtrlFrecuenciaSorteoPozoLeftUp(self, event):
        self.onTextCtrlAdminPozo(self.textCtrlFrecuenciaSorteoPozo, False)


    def OnTextCtrlFactorReservaPozoLeftUp(self, event):
        self.onTextCtrlAdminPozo(self.textCtrlFactorReservaPozo, True)


    def OnTextCtrlFactorIncrementoPozoLeftUp(self, event):
        self.onTextCtrlAdminPozo(self.textCtrlFactorIncrementoPozo, True)



    # Admin Monedas
        
    def OnTextCtrlMoneda1LeftUp(self, event):
        self.textCtrlActivo = self.textCtrlMoneda1
        self.monedaN = "ValorM1"
        self.valorMonedaActivaAnterior = self.textCtrlActivo.GetValue()
        self.textCtrlMoneda1.SetValue("")
        self.textCtrlMoneda2.Disable()
        self.textCtrlMoneda3.Disable()
        self.textCtrlMoneda4.Disable()
        self.textCtrlMoneda5.Disable()
        self.activarMenues(False)
        self.panelNumeros.Show(True)
        self.buttonCancelarCambioMoneda.Show(True)
        self.buttonAceptarCambioMoneda.Show(True)

    def OnTextCtrlMoneda2LeftUp(self, event):
        self.textCtrlActivo = self.textCtrlMoneda2
        self.monedaN = "ValorM2"
        self.valorMonedaActivaAnterior = self.textCtrlActivo.GetValue()
        self.textCtrlMoneda2.SetValue("")
        self.textCtrlMoneda1.Disable()
        self.textCtrlMoneda3.Disable()
        self.textCtrlMoneda4.Disable()
        self.textCtrlMoneda5.Disable()
        self.activarMenues(False)
        self.panelNumeros.Show(True)
        self.buttonCancelarCambioMoneda.Show(True)
        self.buttonAceptarCambioMoneda.Show(True)

    def OnTextCtrlMoneda3LeftUp(self, event):
        self.textCtrlActivo = self.textCtrlMoneda3
        self.monedaN = "ValorM3"
        self.valorMonedaActivaAnterior = self.textCtrlActivo.GetValue()
        self.textCtrlMoneda3.SetValue("")
        self.textCtrlMoneda1.Disable()
        self.textCtrlMoneda2.Disable()
        self.textCtrlMoneda4.Disable()
        self.textCtrlMoneda5.Disable()
        self.activarMenues(False)
        self.panelNumeros.Show(True)
        self.buttonCancelarCambioMoneda.Show(True)
        self.buttonAceptarCambioMoneda.Show(True)

    def OnTextCtrlMoneda4LeftUp(self, event):
        self.textCtrlActivo = self.textCtrlMoneda4
        self.monedaN = "ValorM4"
        self.valorMonedaActivaAnterior = self.textCtrlActivo.GetValue()
        self.textCtrlMoneda4.SetValue("")
        self.textCtrlMoneda1.Disable()
        self.textCtrlMoneda2.Disable()
        self.textCtrlMoneda3.Disable()
        self.textCtrlMoneda5.Disable()
        self.activarMenues(False)
        self.panelNumeros.Show(True)
        self.buttonCancelarCambioMoneda.Show(True)
        self.buttonAceptarCambioMoneda.Show(True)

    def OnTextCtrlMoneda5LeftUp(self, event):
        self.textCtrlActivo = self.textCtrlMoneda5
        self.monedaN = "ValorM5"
        self.valorMonedaActivaAnterior = self.textCtrlActivo.GetValue()
        self.textCtrlMoneda5.SetValue("")
        self.textCtrlMoneda1.Disable()
        self.textCtrlMoneda2.Disable()
        self.textCtrlMoneda3.Disable()
        self.textCtrlMoneda4.Disable()
        self.activarMenues(False)
        self.panelNumeros.Show(True)
        self.buttonCancelarCambioMoneda.Show(True)
        self.buttonAceptarCambioMoneda.Show(True)
        
    def activarTodosTextCtrlMonedas(self):
        self.textCtrlMoneda1.Enable()
        self.textCtrlMoneda2.Enable()
        self.textCtrlMoneda3.Enable()
        self.textCtrlMoneda4.Enable()
        self.textCtrlMoneda5.Enable()

    def OnButtonCancelarCambioMonedaButton(self, event):
        self.textCtrlActivo.SetValue(self.valorMonedaActivaAnterior)
        self.buttonCancelarCambioMoneda.Hide()
        self.buttonAceptarCambioMoneda.Hide()
        self.panelNumeros.Hide()
        self.activarTodosTextCtrlMonedas()
        self.activarMenues(True)

    def OnButtonAceptarCambioMonedaButton(self, event):
        self.clienteServidorCentral.cambiarValorMoneda(self.monedaN,self.textCtrlActivo.GetValue())
        self.textCtrlActivo.SetValue(separadorMiles(self.textCtrlActivo.GetValue()))
        self.buttonAceptarCambioMoneda.Hide()
        self.buttonCancelarCambioMoneda.Hide()
        self.panelNumeros.Hide()
        self.activarTodosTextCtrlMonedas()
        self.activarMenues(True)
        
    def actualizarTipoOpciones(self):
        pleno, medio, cuadro, chanza = self.clienteServidorCentral.getTipoOpciones()
        self.textCtrlPlenoPagaPor.SetValue(str(pleno[0]).replace(".",","))
        self.textCtrlPlenoMinimo.SetValue(separadorMiles(pleno[1]))
        self.textCtrlPlenoMaximo.SetValue(separadorMiles(pleno[2]))
        self.textCtrlMedioPagaPor.SetValue(str(medio[0]).replace(".",","))
        self.textCtrlMedioMinimo.SetValue(separadorMiles(medio[1]))
        self.textCtrlMedioMaximo.SetValue(separadorMiles(medio[2]))
        self.textCtrlCuadroPagaPor.SetValue(str(cuadro[0]).replace(".",","))
        self.textCtrlCuadroMinimo.SetValue(separadorMiles(cuadro[1]))
        self.textCtrlCuadroMaximo.SetValue(separadorMiles(cuadro[2]))
        self.textCtrlChanzaPagaPor.SetValue(str(chanza[0]).replace(".",","))
        self.textCtrlChanzaMinimo.SetValue(separadorMiles(chanza[1]))
        self.textCtrlChanzaMaximo.SetValue(separadorMiles(chanza[2]))
        # actualizar monto minimo apuestas x maquina
        self.textCtrlMontoMinApuestas.SetValue(separadorMiles(str(self.clienteServidorCentral.getMontoMinimoApuestasXmaquina())))

    def OnButtonMenuOpcionesButton(self, event):
        # administrar tipos de opciones
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminOpciones
        self.panelAdminOpciones.Show(True)
        self.actualizarTipoOpciones()
        
    def activarTextCtrlOpciones(self, b):
        self.textCtrlPlenoPagaPor.Enable(b)
        self.textCtrlPlenoMinimo.Enable(b)
        self.textCtrlPlenoMaximo.Enable(b)
        self.textCtrlMedioPagaPor.Enable(b)
        self.textCtrlMedioMinimo.Enable(b)
        self.textCtrlMedioMaximo.Enable(b)
        self.textCtrlCuadroPagaPor.Enable(b)
        self.textCtrlCuadroMinimo.Enable(b)
        self.textCtrlCuadroMaximo.Enable(b)
        self.textCtrlChanzaPagaPor.Enable(b)
        self.textCtrlChanzaMinimo.Enable(b)
        self.textCtrlChanzaMaximo.Enable(b)
        self.textCtrlMontoMinApuestas.Enable(b)
        
    def onCualquierTextCtrlOpciones(self, tCactivo):
        self.textCtrlActivo = tCactivo
        self.valorAnteriorTipoOpcion = self.textCtrlActivo.GetValue()
        self.textCtrlActivo.SetValue("")
        self.activarTextCtrlOpciones(False)
        self.textCtrlActivo.Enable()
        self.activarMenues(False)
        self.panelNumeros.Show(True)
        self.buttonCancelarCambioOpcion.Show(True)
        self.buttonAceptarCambioOpcion.Show(True)

    def OnTextCtrlPlenoPagaPorLeftUp(self, event):
        self.idTipoOpcion = (1,"pagaPor")
        self.buttonPunto.Enable() #se activa el punto para decimales
        self.onCualquierTextCtrlOpciones(self.textCtrlPlenoPagaPor)

    def OnTextCtrlPlenoMinimoLeftUp(self, event):
        self.idTipoOpcion = (1,"min")
        self.onCualquierTextCtrlOpciones(self.textCtrlPlenoMinimo)

    def OnTextCtrlPlenoMaximoLeftUp(self, event):
        self.idTipoOpcion = (1,"max")
        self.onCualquierTextCtrlOpciones(self.textCtrlPlenoMaximo)

    def OnTextCtrlMedioPagaPorLeftUp(self, event):
        self.idTipoOpcion = (2,"pagaPor")
        self.buttonPunto.Enable()
        self.onCualquierTextCtrlOpciones(self.textCtrlMedioPagaPor)

    def OnTextCtrlMedioMinimoLeftUp(self, event):
        self.idTipoOpcion = (2,"min")
        self.onCualquierTextCtrlOpciones(self.textCtrlMedioMinimo)

    def OnTextCtrlMedioMaximoLeftUp(self, event):
        self.idTipoOpcion = (2,"max")
        self.onCualquierTextCtrlOpciones(self.textCtrlMedioMaximo)

    def OnTextCtrlCuadroPagaPorLeftUp(self, event):
        self.idTipoOpcion = (3,"pagaPor")
        self.buttonPunto.Enable()
        self.onCualquierTextCtrlOpciones(self.textCtrlCuadroPagaPor)

    def OnTextCtrlCuadroMinimoLeftUp(self, event):
        self.idTipoOpcion = (3,"min")
        self.onCualquierTextCtrlOpciones(self.textCtrlCuadroMinimo)

    def OnTextCtrlCuadroMaximoLeftUp(self, event):
        self.idTipoOpcion = (3,"max")
        self.onCualquierTextCtrlOpciones(self.textCtrlCuadroMaximo)

    def OnTextCtrlChanzaPagaPorLeftUp(self, event):
        self.idTipoOpcion = (4,"pagaPor")
        self.buttonPunto.Enable()
        self.onCualquierTextCtrlOpciones(self.textCtrlChanzaPagaPor)

    def OnTextCtrlChanzaMinimoLeftUp(self, event):
        self.idTipoOpcion = (4,"min")
        self.onCualquierTextCtrlOpciones(self.textCtrlChanzaMinimo)

    def OnTextCtrlChanzaMaximoLeftUp(self, event):
        self.idTipoOpcion = (4,"max")
        self.onCualquierTextCtrlOpciones(self.textCtrlChanzaMaximo)

    # admin monto minimo de apuestas x maquina
    def OnTextCtrlMontoMinApuestasLeftUp(self, event):
        self.onCualquierTextCtrlOpciones(self.textCtrlMontoMinApuestas)

    def OnButtonCancelarCambioOpcionButton(self, event):
        self.textCtrlActivo.SetValue(self.valorAnteriorTipoOpcion)
        self.buttonCancelarCambioOpcion.Hide()
        self.buttonAceptarCambioOpcion.Hide()
        self.panelNumeros.Hide()
        self.buttonPunto.Disable()
        self.activarTextCtrlOpciones(True)
        self.activarMenues(True)

    def OnButtonAceptarCambioOpcionButton(self, event):
        if self.textCtrlActivo != self.textCtrlMontoMinApuestas:
            self.clienteServidorCentral.cambiarTipoOpcion(self.idTipoOpcion, self.textCtrlActivo.GetValue())
            if self.idTipoOpcion[1] == "pagaPor":
                self.textCtrlActivo.SetValue(self.textCtrlActivo.GetValue().replace(".",","))
            else:
                self.textCtrlActivo.SetValue(separadorMiles(self.textCtrlActivo.GetValue()))
        else:
            self.clienteServidorCentral.setMontoMinimoApuestasXmaquina(self.textCtrlActivo.GetValue())
            self.textCtrlActivo.SetValue(separadorMiles(self.textCtrlActivo.GetValue()))
        self.buttonAceptarCambioOpcion.Hide()
        self.buttonCancelarCambioOpcion.Hide()
        self.panelNumeros.Hide()
        self.buttonPunto.Disable()
        self.activarTextCtrlOpciones(True)
        self.activarMenues(True)
        
    def mostrarRondas(self, fecha1="", fecha2=""):
        self.listCtrlRondas.DeleteAllItems()
        r = self.clienteServidorCentral.getRondas(fecha1, fecha2)
        for i in range(len(r)):
            self.listCtrlRondas.InsertStringItem(i,str(r[i][0]))   
            self.listCtrlRondas.SetStringItem(i,1,str(r[i][1]))
            self.listCtrlRondas.SetStringItem(i,2,str(r[i][2]))
            self.listCtrlRondas.SetStringItem(i,3,str(r[i][3]))
            self.listCtrlRondas.SetStringItem(i,4,str(r[i][4]))
            self.listCtrlRondas.SetStringItem(i,5,str(r[i][5]))
            # colocando color intermedio
            if (i+1) % 2 == 0:
                self.listCtrlRondas.SetItemBackgroundColour(i, wx.LIGHT_GREY)

    def OnButtonMenuRondasButton(self, event):
        # administrar rondas
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminRondas
        self.panelAdminRondas.Show(True)
        self.cargarRondasFechasActuales() # cargar rondas de fecha actual
        self.panelExportar.Show(True)
        
    def arreglarMesYdia(self, m, d):
        if len(m) == 1:
            m = "0" + m
        if len(d) == 1:
            d = "0" + d
        return (m,d)
    
    def OnCalendarCtrlRondas1CalendarSelChanged(self, event):
        self.cargarRondasFechasActuales()

    def OnCalendarCtrlRondas2CalendarSelChanged(self, event):
        self.cargarRondasFechasActuales()
        
    def cargarRondasFechasActuales(self):
        d1 = self.calendarCtrlRondas1.GetDate()
        mes, dia = self.arreglarMesYdia(str(d1.GetMonth()+1), str(d1.GetDay()))
        f1 = str(d1.GetYear())+"-"+mes+"-"+dia
        d2 = self.calendarCtrlRondas2.GetDate()
        mes, dia = self.arreglarMesYdia(str(d2.GetMonth()+1), str(d2.GetDay()))
        f2 = str(d2.GetYear())+"-"+mes+"-"+dia
        self.mostrarRondas(f1,f2)

    def mostrarCuadre(self, fecha1="", fecha2=""):
        totalBilletes = self.clienteServidorCentral.getTotalBilletesYcreditosManualesXmaquina(fecha1,fecha2)
        totalPagos = self.clienteServidorCentral.getTotalPagosXmaquina(fecha1,fecha2)
        totalApostado = self.clienteServidorCentral.getTotalApostadoXmaquina(fecha1,fecha2)
        totalGanado = self.clienteServidorCentral.getTotalGanadoXmaquina(fecha1,fecha2)
        # crear filas segun maquinas existentes * 2 (real y virtual)
        filas = []
        realOvirtual = ['Real','Virtual']
        maquina = 1
        for i in range(len(self.ipsYp)*2):
            l = [maquina,realOvirtual[i%2], 0,0,0] # 5 columnas en el reporte
            filas.append(l)
            if (i+1) % 2 == 0:
                maquina += 1
        # asignando entradas reales a las filas correspondientes
        for er in totalBilletes:
            filas[(er[0]-1)*2][2] = er[1]
        # asignando salidas reales a las filas correspondientes
        for sr in totalPagos:
            filas[(sr[0]-1)*2][3] = sr[1]
        # asignando entradas virtuales a las filas correspondientes
        for ev in totalApostado:
            filas[(ev[0]-1)*2+1][2] = ev[1]
        # asignando salidas virtuales a las filas correspondientes
        for sv in totalGanado:
            filas[(sv[0]-1)*2+1][3] = sv[1]
        # calculando cuadre real y virtual 
        for f in filas:
            f[4] = f[2] - f[3]
        # cargar datos en el listCtrlCuadre
        self.listCtrlCuadre.DeleteAllItems()
        for i in range(len(filas)):
            self.listCtrlCuadre.InsertStringItem(i,str(filas[i][0]))
            self.listCtrlCuadre.SetStringItem(i,1,str(filas[i][1]))
            self.listCtrlCuadre.SetStringItem(i,2,separadorMiles(filas[i][2]))
            self.listCtrlCuadre.SetStringItem(i,3,separadorMiles(filas[i][3]))
            self.listCtrlCuadre.SetStringItem(i,4,separadorMiles(filas[i][4]))
            # colocando color intermedio
            if filas[i][0] % 2 == 0:
                self.listCtrlCuadre.SetItemBackgroundColour(i, wx.LIGHT_GREY)

    def OnButtonMenuCuadreButton(self, event):
        # administrar cuadre
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminCuadre
        self.panelAdminActivo.Show(True)
        self.cargarCuadreFechasActuales()
        self.panelExportar.Show(True)

    def cargarCuadreFechasActuales(self):
        d1 = self.calendarCtrlCuadre1.GetDate()
        mes, dia = self.arreglarMesYdia(str(d1.GetMonth()+1), str(d1.GetDay()))
        f1 = str(d1.GetYear())+"-"+mes+"-"+dia
        d2 = self.calendarCtrlCuadre2.GetDate()
        mes, dia = self.arreglarMesYdia(str(d2.GetMonth()+1), str(d2.GetDay()))
        f2 = str(d2.GetYear())+"-"+mes+"-"+dia
        self.mostrarCuadre(f1,f2)
        
    def OnCalendarCtrlCuadre1CalendarSelChanged(self, event):
        self.cargarCuadreFechasActuales()

    def OnCalendarCtrlCuadre2CalendarSelChanged(self, event):
        self.cargarCuadreFechasActuales()
    
    def mostrarBilletes(self, fecha1="", fecha2=""):
        self.listCtrlBilletes.DeleteAllItems()
        r = self.clienteServidorCentral.getCantidadBilletesXmaquina(fecha1,fecha2)
        #cambiar id de billete por denominacion
        for i in range(len(r)):
            self.listCtrlBilletes.InsertStringItem(i,str(r[i][0]))   
            self.listCtrlBilletes.SetStringItem(i,1,separadorMiles(self.clienteServidorCentral.getValorBillete(r[i][1])))
            self.listCtrlBilletes.SetStringItem(i,2,str(r[i][2]))
            # colocando color intermedio
            if (i+1) % 2 == 0:
                self.listCtrlBilletes.SetItemBackgroundColour(i, wx.LIGHT_GREY)
    
    def OnButtonMenuBilletesButton(self, event):
        # administrar billetes
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminBilletes
        self.panelAdminActivo.Show(True)
        self.cargarBilletesFechasActuales()
        self.panelExportar.Show(True)


    def cargarBilletesFechasActuales(self):
        d1 = self.calendarCtrlBilletes1.GetDate()
        mes, dia = self.arreglarMesYdia(str(d1.GetMonth()+1), str(d1.GetDay()))
        f1 = str(d1.GetYear())+"-"+mes+"-"+dia
        d2 = self.calendarCtrlBilletes2.GetDate()
        mes, dia = self.arreglarMesYdia(str(d2.GetMonth()+1), str(d2.GetDay()))
        f2 = str(d2.GetYear())+"-"+mes+"-"+dia
        self.mostrarBilletes(f1,f2)
        
    def OnCalendarCtrlBilletes1CalendarSelChanged(self, event):
        self.cargarBilletesFechasActuales()

    def OnCalendarCtrlBilletes2CalendarSelChanged(self, event):
        self.cargarBilletesFechasActuales()



    # administrar creditos manuales
    
    def OnButtonMenuCreditosManualesButton(self, event):
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminCreditosManuales
        self.panelAdminActivo.Show(True)
        self.cargarCreditosManualesFechasActuales()
        self.panelExportar.Show(True)

    def cargarCreditosManualesFechasActuales(self):
        d1 = self.calendarCtrlCreditosManuales1.GetDate()
        mes, dia = self.arreglarMesYdia(str(d1.GetMonth()+1), str(d1.GetDay()))
        f1 = str(d1.GetYear())+"-"+mes+"-"+dia
        d2 = self.calendarCtrlCreditosManuales2.GetDate()
        mes, dia = self.arreglarMesYdia(str(d2.GetMonth()+1), str(d2.GetDay()))
        f2 = str(d2.GetYear())+"-"+mes+"-"+dia
        self.mostrarCreditosManuales(f1,f2)

    def mostrarCreditosManuales(self, fecha1="", fecha2=""):
        self.listCtrlCreditosManuales.DeleteAllItems()
        r = self.clienteServidorCentral.getCreditosManualesDetallado(fecha1, fecha2)
        for i in range(len(r)):
            self.listCtrlCreditosManuales.InsertStringItem(i,str(r[i][0]))   
            self.listCtrlCreditosManuales.SetStringItem(i,1,str(r[i][1]))
            self.listCtrlCreditosManuales.SetStringItem(i,2,str(r[i][2]))
            self.listCtrlCreditosManuales.SetStringItem(i,3,str(r[i][3]))
            self.listCtrlCreditosManuales.SetStringItem(i,4,separadorMiles(r[i][4]))
            # colocando color intermedio
            if (i+1) % 2 == 0:
                self.listCtrlCreditosManuales.SetItemBackgroundColour(i, wx.LIGHT_GREY)

    def OnCalendarCtrlCreditosManuales1CalendarSelChanged(self, event):
        self.cargarCreditosManualesFechasActuales()

    def OnCalendarCtrlCreditosManuales2CalendarSelChanged(self, event):
        self.cargarCreditosManualesFechasActuales()


    # administrar pagos    
    def mostrarPagos(self, fecha1="", fecha2=""):
        self.listCtrlPagos.DeleteAllItems()
        r = self.clienteServidorCentral.getPagosDetallado(fecha1,fecha2)
        for i in range(len(r)):
            self.listCtrlPagos.InsertStringItem(i,str(r[i][0]))   
            self.listCtrlPagos.SetStringItem(i,1,str(r[i][1]))
            self.listCtrlPagos.SetStringItem(i,2,separadorMiles(r[i][2]))
            self.listCtrlPagos.SetStringItem(i,3,str(r[i][3]))
            self.listCtrlPagos.SetStringItem(i,4,str(r[i][4]))
            # colocando color intermedio
            if (i+1) % 2 == 0:
                self.listCtrlPagos.SetItemBackgroundColour(i, wx.LIGHT_GREY)
    
    def OnButtonMenuPagosButton(self, event):
        # administrar pagos
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminPagos
        self.panelAdminActivo.Show(True)
        self.cargarPagosFechasActuales()
        self.panelExportar.Show(True)

    def cargarPagosFechasActuales(self):
        d1 = self.calendarCtrlPagos1.GetDate()
        mes, dia = self.arreglarMesYdia(str(d1.GetMonth()+1), str(d1.GetDay()))
        f1 = str(d1.GetYear())+"-"+mes+"-"+dia
        d2 = self.calendarCtrlPagos2.GetDate()
        mes, dia = self.arreglarMesYdia(str(d2.GetMonth()+1), str(d2.GetDay()))
        f2 = str(d2.GetYear())+"-"+mes+"-"+dia
        self.mostrarPagos(f1,f2)
        
    def OnCalendarCtrlPagos1CalendarSelChanged(self, event):
        self.cargarPagosFechasActuales()

    def OnCalendarCtrlPagos2CalendarSelChanged(self, event):
        self.cargarPagosFechasActuales()
        

    def OnButtonMenuAdministradorButton(self, event):
        # administrar administrador
        self.panelExportar.Hide()
        self.panelGuardar.Hide()
        self.panelAdminActivo.Hide()
        self.panelAdminActivo = self.panelAdminAdministrador
        self.panelAdminActivo.Show(True)

    def OnTextCtrlClaveActualLeftUp(self, event):
        self.staticTextMsgCambiarClaveAdmin.Show(False)
        self.textCtrlActivo = self.textCtrlClaveActual
        self.textCtrlActivo.SetValue("")
        self.activarMenues(False)
        self.textCtrlClaveNueva.Disable()
        self.textCtrlConfirmarClaveNueva.Disable()
        self.panelNumeros.Show(True)
        self.buttonCancelarCambiarClave.Show(True)
        self.buttonAceptarCambiarClave.Show(True)
        self.buttonCambiarClave.Disable()

    def OnTextCtrlClaveNuevaLeftUp(self, event):
        self.staticTextMsgCambiarClaveAdmin.Show(False)
        self.textCtrlActivo = self.textCtrlClaveNueva
        self.textCtrlActivo.SetValue("")
        self.activarMenues(False)
        self.textCtrlClaveActual.Disable()
        self.textCtrlConfirmarClaveNueva.Disable()
        self.panelNumeros.Show(True)
        self.buttonCancelarCambiarClave.Show(True)
        self.buttonAceptarCambiarClave.Show(True)
        self.buttonCambiarClave.Disable()

    def OnTextCtrlConfirmarClaveNuevaLeftUp(self, event):
        self.staticTextMsgCambiarClaveAdmin.Show(False)
        self.textCtrlActivo = self.textCtrlConfirmarClaveNueva
        self.textCtrlActivo.SetValue("")
        self.activarMenues(False)
        self.textCtrlClaveActual.Disable()
        self.textCtrlClaveNueva.Disable()
        self.panelNumeros.Show(True)
        self.buttonCancelarCambiarClave.Show(True)
        self.buttonAceptarCambiarClave.Show(True)
        self.buttonCambiarClave.Disable()

    def OnButtonCambiarClaveButton(self, event):
        cActual = self.textCtrlClaveActual.GetValue()
        cActualMd5 = md5.md5(cActual).hexdigest()
        cNueva = self.textCtrlClaveNueva.GetValue()
        cNuevaMd5 = md5.md5(cNueva).hexdigest()
        cNuevaConfir = self.textCtrlConfirmarClaveNueva.GetValue()
        cNuevaConfirMd5 = md5.md5(cNuevaConfir).hexdigest()
        # que clave actual entrada se igual a la clave actual en la bd
        if self.clienteServidorCentral.getClaveAdmin() == cActualMd5:
            # validar longitud de contrasegnas = 4
            if len(cActual)==4 and len(cNueva)==4 and len(cNuevaConfir)==4:
                # que la confirmacion sea igual a la nueva
                if cNuevaMd5 == cNuevaConfirMd5:
                    self.staticTextMsgCambiarClaveAdmin.Show(True)
                    if self.clienteServidorCentral.cambiarClaveAdmin(cNuevaConfirMd5):
                        self.staticTextMsgCambiarClaveAdmin.SetLabel("Clave cambiada")
                    else:
                        self.staticTextMsgCambiarClaveAdmin.SetLabel("Imposible cambiar clave")
                else:
                    self.staticTextMsgCambiarClaveAdmin.Show(True)
                    self.staticTextMsgCambiarClaveAdmin.SetLabel("Confirmacion de clave no coincide")
            else:
                self.staticTextMsgCambiarClaveAdmin.Show(True)
                self.staticTextMsgCambiarClaveAdmin.SetLabel("Clave debe tener 4 digitos")
        else:
            self.staticTextMsgCambiarClaveAdmin.Show(True)
            self.staticTextMsgCambiarClaveAdmin.SetLabel("Clave actual entrada no coincide")
        # borrar todos los textCtrl
        self.textCtrlClaveActual.SetValue("")
        self.textCtrlClaveNueva.SetValue("")
        self.textCtrlConfirmarClaveNueva.SetValue("")

    def activarTextCtrlClaveAdmin(self, b):
        self.textCtrlClaveActual.Enable(b)
        self.textCtrlClaveNueva.Enable(b)
        self.textCtrlConfirmarClaveNueva.Enable(b)
        
    def OnButtonAceptarCambiarClaveButton(self, event):
        self.buttonAceptarCambiarClave.Hide()
        self.buttonCancelarCambiarClave.Hide()
        self.panelNumeros.Hide()
        self.activarTextCtrlClaveAdmin(True)
        self.activarMenues(True)
        self.buttonCambiarClave.Enable()

    def OnButtonCancelarCambiarClaveButton(self, event):
        self.textCtrlActivo.SetValue("")
        self.buttonCancelarCambiarClave.Hide()
        self.buttonAceptarCambiarClave.Hide()
        self.panelNumeros.Hide()
        self.activarTextCtrlClaveAdmin(True)
        self.activarMenues(True)
        self.buttonCambiarClave.Enable()
        
    def escribirReporteEnArchivo(self, file, calendario1, calendario2, listado):
        # reporte de las fechas:
        d1 = calendario1.GetDate()
        mes, dia = self.arreglarMesYdia(str(d1.GetMonth()+1), str(d1.GetDay()))
        f1 = str(d1.GetYear())+"-"+mes+"-"+dia
        d2 = calendario2.GetDate()
        mes, dia = self.arreglarMesYdia(str(d2.GetMonth()+1), str(d2.GetDay()))
        f2 = str(d2.GetYear())+"-"+mes+"-"+dia
        file.write("Fecha Inicial;" + f1 + "\n")
        file.write("Fecha Final;" + f2 + "\n")
        # escribir todo el listado
        for i in range(listado.GetItemCount()):
            for j in range(listado.GetColumnCount()):
                file.write(listado.GetItem(i,j).GetText()+";")
            file.write("\n")
        file.close()

    def OnButtonExportarButton(self, event):
        dirCambiado = False
        curDir = os.getcwd()
        nombreUSB = "ESFERODROMO"
        try:
            os.chdir("/media/%s/"%(nombreUSB))
            dirCambiado = True
        except:
            dlg = wx.MessageDialog(self,'Asegurese de que USB este conectada al equipo y se llame ESFERODROMO','Error',wx.OK)
            try:
                dlg.ShowModal()
            finally:
                dlg.Destroy()
        if dirCambiado:
            try:
                archivo = ""
                agno,mes,dia,hora,minutos,segundos,t1,t2,t3 = time.localtime()
                if self.panelAdminActivo == self.panelAdminRondas:
                    # archivo con fecha y hora de generacion
                    archivo = open("rondas%s-%s-%s_%s-%s-%s.xls"%(agno,mes,dia,hora,minutos,segundos), "w")
                    #funcion generica> archivo, calendar1, calendar2, listCtrl
                    self.escribirReporteEnArchivo(archivo, self.calendarCtrlRondas1, self.calendarCtrlRondas2, self.listCtrlRondas) 
                elif self.panelAdminActivo == self.panelAdminBilletes:
                    archivo = open("billetes%s-%s-%s_%s-%s-%s.xls"%(agno,mes,dia,hora,minutos,segundos), "w")
                    self.escribirReporteEnArchivo(archivo, self.calendarCtrlBilletes1, self.calendarCtrlBilletes2, self.listCtrlBilletes) 
                elif self.panelAdminActivo == self.panelAdminPagos:
                    archivo = open("pagos%s-%s-%s_%s-%s-%s.xls"%(agno,mes,dia,hora,minutos,segundos), "w")
                    self.escribirReporteEnArchivo(archivo, self.calendarCtrlPagos1, self.calendarCtrlPagos2, self.listCtrlPagos)
                elif self.panelAdminActivo == self.panelAdminCuadre:
                    archivo = open("cuadre%s-%s-%s_%s-%s-%s.xls"%(agno,mes,dia,hora,minutos,segundos), "w")
                    self.escribirReporteEnArchivo(archivo, self.calendarCtrlCuadre1, self.calendarCtrlCuadre2, self.listCtrlCuadre)
                elif self.panelAdminActivo == self.panelAdminCreditosManuales:
                    archivo = open("creditosManuales%s-%s-%s_%s-%s-%s.xls"%(agno,mes,dia,hora,minutos,segundos), "w")
                    self.escribirReporteEnArchivo(archivo, self.calendarCtrlCreditosManuales1, self.calendarCtrlCreditosManuales1, self.listCtrlCreditosManuales)
                archivo.close()
            except:
                dlg = wx.MessageDialog(self,'Error al intentar guardar archivo','Error',wx.OK)
                try:
                    dlg.ShowModal()
                finally:
                    dlg.Destroy()
            # restablecer directorio anterior
            os.chdir(curDir)



    # Guardar los cambios hechos a los textCtrl. Aplica para desarrollos hechos a partir del Pozo version 2
    def OnButtonGuardarButton(self, event):
        if self.panelAdminActivo == self.panelAdminPozo:
            self.clienteServidorCentral.setMontoInicialPozo(self.textCtrlMontoInicialPozo.GetValue().replace(".","").replace(",","."))
            self.clienteServidorCentral.setMontoMinimoParaConcursarPozo(self.textCtrlMinimoParaConcursarPozo.GetValue().replace(".","").replace(",","."))
            self.clienteServidorCentral.setFrecuenciaSorteoPozo(self.textCtrlFrecuenciaSorteoPozo.GetValue().replace(".","").replace(",","."))
            self.clienteServidorCentral.setFactorReservaPozo(self.textCtrlFactorReservaPozo.GetValue().replace(".","").replace(",","."))
            self.clienteServidorCentral.setFactorIncrementoPozo(self.textCtrlFactorIncrementoPozo.GetValue().replace(".","").replace(",","."))
            self.actualizarValoresPozo()

    

    def OnButtonCancelarRondaButton(self, event):
        print "*** si se cancela la ronda, se debe cancelar lo incrementado al pozo...MODIFICAR CANCELAR RONDA DE SERVIDOR CENTRAL"
        dlg = wx.MessageDialog(self,'Confirma Cancelar Ronda Actual?','Confirmar',wx.YES_NO)
        try:
            if dlg.ShowModal() == wx.ID_YES:
                if self.clienteServidorCentral.cancelarRonda():
                    #actualizar maquinas
                    print "actualizando maquinas porque ronda fue cancelada..."
                    for c in self.clientesServidorMaquina:
                        try:
                            c.anularTodo()
                            c.actualizarDisponible() #captura lo disponible de la bd y actualiza el dinero disponible del juego y el textoDisponible wx
                            c.bloquear(False)
                        except Exception, e:
                            print "Maquina ", c.httpSer, " apagada"
                    # actualizar Gui
                    self.panelPagno.Disable()
                    self.buttonCerrarApuestas.Disable()
                    self.buttonAbrirRonda.Enable()
                    self.buttonCerrarSesion.Enable()
                    self.buttonCancelarRonda.Disable()
                    self.rondaAbierta = False
                    self.apuestasAbiertas = False
                else:
                    dlg = wx.MessageDialog(self,'Imposible Cancelar Ronda','Error Fatal',wx.OK)
                    try:
                        dlg.ShowModal()
                    finally:
                        dlg.Destroy()
        finally:
            dlg.Destroy()
