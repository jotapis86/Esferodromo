import wx
from separadorMiles import *

class frameHistoriaJugadas(wx.Frame):        
    def __init__(self, parent, idMaquina, rondas, info, opciones):
        #wx.STAY_ON_TOP
        wx.Frame.__init__(self, parent, title='Historia de Jugadas Maquina %s'%(idMaquina), pos=(350,300), size=(1024, 768), style=wx.FRAME_FLOAT_ON_PARENT)
        self.Center()
        # ids rondas
        self.staticTextIdRonda = wx.StaticText(id=wx.NewId(), label=u'Id Ronda', parent=self, pos=wx.Point(30, 20), size=wx.Size(95,23), style=0)
        self.staticTextIdRonda.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextIdRonda0 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(250, 20), size=wx.Size(95,23), style=wx.CENTER)
        self.staticTextIdRonda0.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextIdRonda1 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(500, 20), size=wx.Size(95,23), style=wx.CENTER)
        self.staticTextIdRonda1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextIdRonda2 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(750, 20), size=wx.Size(95,23), style=wx.CENTER)
        self.staticTextIdRonda2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        # fecha
        self.staticTextFecha = wx.StaticText(id=wx.NewId(), label=u'Fecha', parent=self, pos=wx.Point(30, 40), size=wx.Size(95,23), style=0)
        self.staticTextFecha.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextFecha0 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(250,40), size=wx.Size(95,23), style=0)
        self.staticTextFecha0.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextFecha1 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(500,40), size=wx.Size(95,23), style=0)
        self.staticTextFecha1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextFecha2 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(750,40), size=wx.Size(95,23), style=0)
        self.staticTextFecha2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        # hora
        self.staticTextHora = wx.StaticText(id=wx.NewId(), label=u'Hora', parent=self, pos=wx.Point(30, 60), size=wx.Size(95,23), style=0)
        self.staticTextHora.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextHora0 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(250,60), size=wx.Size(95,23), style=0)
        self.staticTextHora0.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextHora1 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(500,60), size=wx.Size(95,23), style=0)
        self.staticTextHora1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextHora2 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(750,60), size=wx.Size(95,23), style=0)
        self.staticTextHora2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        # ganadora
        self.staticTextGanadora = wx.StaticText(id=wx.NewId(), label=u'Ganadora', parent=self, pos=wx.Point(30, 80), size=wx.Size(95,23), style=0)
        self.staticTextGanadora.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextGanadora0 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(250,80), size=wx.Size(95,23), style=0)
        self.staticTextGanadora0.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextGanadora1 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(500,80), size=wx.Size(95,23), style=0)
        self.staticTextGanadora1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextGanadora2 = wx.StaticText(id=wx.NewId(), label=u'', parent=self, pos=wx.Point(750,80), size=wx.Size(95,23), style=0)
        self.staticTextGanadora2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        # opciones
        # info viene en la forma
        #  [ [idRonda, fecha, horaFin, ganadora, id_opcion, descripcionOpcion, valorApostado, valorGanado], ...]
        self.listCtrlOpciones = wx.ListCtrl(id=wx.NewId(), parent=self, pos=wx.Point(30, 105), size=wx.Size(860, 500), style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        self._init_coll_listCtrlOpciones_Columns(self.listCtrlOpciones)
        # cargue de info a lista de opciones
        self.listCtrlOpciones.DeleteAllItems()
        for i in range(len(opciones)):
            self.listCtrlOpciones.InsertStringItem(i,str(opciones[i][1]))
            self.listCtrlOpciones.SetStringItem(i,1,"0")
            self.listCtrlOpciones.SetStringItem(i,2,"0")
            self.listCtrlOpciones.SetStringItem(i,3,"0")
            self.listCtrlOpciones.SetStringItem(i,4,"0")
            self.listCtrlOpciones.SetStringItem(i,5,"0")
            self.listCtrlOpciones.SetStringItem(i,6,"0")
            # colocando color intermedio
            if i % 2 == 1:
                self.listCtrlOpciones.SetItemBackgroundColour(i, wx.LIGHT_GREY)
        # acumulador de totales
        self.totalApostado0 = 0
        self.totalGanado0 = 0
        self.totalApostado1 = 0
        self.totalGanado1 = 0
        self.totalApostado2 = 0
        self.totalGanado2 = 0
        # cargue de apostado y ganado
        for i in range(len(info)):
            opciones = info[i]
            for j in range(len(opciones)):
                self.listCtrlOpciones.SetStringItem(opciones[j][4]-1,i*2+1,separadorMiles(opciones[j][6]))
                self.listCtrlOpciones.SetStringItem(opciones[j][4]-1,i*2+2,separadorMiles(opciones[j][7]))
                # sumar a totales
                if i == 0:
                    self.totalApostado0 += opciones[j][6]
                    self.totalGanado0 += opciones[j][7]
                elif i == 1:
                    self.totalApostado1 += opciones[j][6]
                    self.totalGanado1 += opciones[j][7]
                elif i == 2:
                    self.totalApostado2 += opciones[j][6]
                    self.totalGanado2 += opciones[j][7]
                    
        # totales
        self.staticTextTotal = wx.StaticText(id=wx.NewId(), label=u'Total', parent=self, pos=wx.Point(30, 608), size=wx.Size(95,23), style=0)
        self.staticTextTotal.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextTotalApostado0 = wx.StaticText(id=wx.NewId(), label=separadorMiles(self.totalApostado0), parent=self, pos=wx.Point(190, 608), size=wx.Size(95,23), style=wx.ALIGN_CENTRE)
        self.staticTextTotalApostado0.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextTotalGanado0 = wx.StaticText(id=wx.NewId(), label=separadorMiles(self.totalGanado0), parent=self, pos=wx.Point(300, 608), size=wx.Size(95,23), style=wx.ALIGN_CENTRE)
        self.staticTextTotalGanado0.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextTotalApostado1 = wx.StaticText(id=wx.NewId(), label=separadorMiles(self.totalApostado1), parent=self, pos=wx.Point(420, 608), size=wx.Size(95,23), style=wx.ALIGN_CENTRE)
        self.staticTextTotalApostado1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextTotalGanado1 = wx.StaticText(id=wx.NewId(), label=separadorMiles(self.totalGanado1), parent=self, pos=wx.Point(530, 608), size=wx.Size(95,23), style=wx.ALIGN_CENTRE)
        self.staticTextTotalGanado1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextTotalApostado2 = wx.StaticText(id=wx.NewId(), label=separadorMiles(self.totalApostado2), parent=self, pos=wx.Point(650, 608), size=wx.Size(95,23), style=wx.ALIGN_CENTRE)
        self.staticTextTotalApostado2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        self.staticTextTotalGanado2 = wx.StaticText(id=wx.NewId(), label=separadorMiles(self.totalGanado2), parent=self, pos=wx.Point(760, 608), size=wx.Size(95,23), style=wx.ALIGN_CENTRE)
        self.staticTextTotalGanado2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Sans'))
        
        
        # boton para cerrar la ventana
        self.buttonCerrar = wx.Button(id=wx.NewId(), label=u'Cerrar', parent=self, pos=wx.Point(450, 640), size=wx.Size(100, 50), style=0)
        self.buttonCerrar.Bind(wx.EVT_BUTTON, self.OnButtonCerrarButton)

        # info rondas
        for i in range(len(rondas)):
            eval("self.staticTextIdRonda%s.SetLabel(str(rondas[i][0]))"%(i))
            eval("self.staticTextFecha%s.SetLabel(str(rondas[i][1]))"%(i))
            eval("self.staticTextHora%s.SetLabel(str(rondas[i][3]))"%(i))
            eval("self.staticTextGanadora%s.SetLabel(str(rondas[i][4]))"%(i))



    def _init_coll_listCtrlOpciones_Columns(self, parent):
        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_CENTER, heading=u'Opcion', width=160)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_CENTER, heading=u'Apostado', width=105)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_CENTER, heading=u'Ganado', width=125)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_CENTER, heading=u'Apostado', width=105)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_CENTER, heading=u'Ganado', width=125)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_CENTER, heading=u'Apostado', width=105)
        parent.InsertColumn(col=6, format=wx.LIST_FORMAT_CENTER, heading=u'Ganado', width=125)
       

    def OnButtonCerrarButton(self, event):
        self.Close()
