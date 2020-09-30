import wx
import separadorMiles

class tecladoNumerico(wx.Panel):
    def __init__(self, padre, x, y, textCtrl="", panelRegreso=""):
        # textCtrl a modificar con los eventos
        self.textCtrlModificar = textCtrl
        # panel de regreso cuando ocurra cancelar
        self.panelRegreso = panelRegreso
        # flag para mostrar numeros con separador de miles
        self.flagSeparadorMiles = False
        # tamanno de los botones
        self.buttonWidth = 60
        self.buttonHeigth = 50
        self.buttonSpace = 10
        # tamanno del textCtrl donde se muestra lo entrado
        self.textCtrlShowHeigth = 28
        # tamanno del panel
        self.panelWidth = 4*self.buttonWidth + 3*self.buttonSpace
        self.panelHeigth = 5*self.buttonHeigth + self.textCtrlShowHeigth + 5*self.buttonSpace
        # se crea el panel
        wx.Panel.__init__(self, parent=padre, pos=wx.Point(x, y), size=wx.Size(self.panelWidth, self.panelHeigth), style=wx.TAB_TRAVERSAL)
        # se crear textCtrl para mostrar lo que va escrito...
        self.textCtrlShow = wx.TextCtrl(name='textCtrlShow', parent=self, pos=wx.Point(0,0), size=wx.Size(self.panelWidth, self.textCtrlShowHeigth), style=wx.TE_RIGHT, value='')
        # numero entrado en string
        self.strNum = ""
        # se crean los botones
        self.b7 = wx.Button(self, -1, label="7", pos=(0,self.textCtrlShowHeigth+self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b8 = wx.Button(self, -1, label="8", pos=(self.buttonWidth+self.buttonSpace,self.textCtrlShowHeigth+self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b9 = wx.Button(self, -1, label="9", pos=(2*(self.buttonWidth+self.buttonSpace),self.textCtrlShowHeigth+self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b4 = wx.Button(self, -1, label="4", pos=(0,self.buttonHeigth+self.textCtrlShowHeigth+2*self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b5 = wx.Button(self, -1, label="5", pos=(self.buttonWidth+self.buttonSpace,self.buttonHeigth+self.textCtrlShowHeigth+2*self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b6 = wx.Button(self, -1, label="6", pos=(2*(self.buttonWidth+self.buttonSpace),self.buttonHeigth+self.textCtrlShowHeigth+2*self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b1 = wx.Button(self, -1, label="1", pos=(0,2*self.buttonHeigth+self.textCtrlShowHeigth+3*self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b2 = wx.Button(self, -1, label="2", pos=(self.buttonWidth+self.buttonSpace,2*self.buttonHeigth+self.textCtrlShowHeigth+3*self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b3 = wx.Button(self, -1, label="3", pos=(2*(self.buttonWidth+self.buttonSpace),2*self.buttonHeigth+self.textCtrlShowHeigth+3*self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        self.b0 = wx.Button(self, -1, label="0", pos=(0,3*self.buttonHeigth+self.textCtrlShowHeigth+4*self.buttonSpace),
                       size=(self.buttonWidth*2+self.buttonSpace,self.buttonHeigth))
        self.bComa = wx.Button(self, -1, label=",", pos=(2*(self.buttonWidth+self.buttonSpace),3*self.buttonHeigth+self.textCtrlShowHeigth+4*self.buttonSpace),
                       size=(self.buttonWidth,self.buttonHeigth))
        # boton cancelar
        self.bCancelar = wx.Button(self, -1, label="Cancelar", pos=(0,4*self.buttonHeigth+self.textCtrlShowHeigth+5*self.buttonSpace),
                       size=(2*self.buttonWidth+self.buttonSpace,self.buttonHeigth))
        # boton enter
        self.bEnter = wx.Button(self, -1, label="Ok", pos=(3*(self.buttonWidth+self.buttonSpace),self.textCtrlShowHeigth+self.buttonSpace),
                       size=(self.buttonWidth,4*self.buttonHeigth+3*self.buttonSpace))
        # boton borrar
        self.bBorrar = wx.Button(self, -1, label="Borrar", pos=(2*(self.buttonWidth+self.buttonSpace),4*self.buttonHeigth+self.textCtrlShowHeigth+5*self.buttonSpace),
                       size=(2*self.buttonWidth+self.buttonSpace,self.buttonHeigth))

        # lista de objetos impactados al modificar el textCtrl a modificar
        self.listaImpactados = []

        # eventos de botones
        self.b0.Bind(wx.EVT_BUTTON, self.onButton0, self.b0)
        self.b1.Bind(wx.EVT_BUTTON, self.onButton1, self.b1)
        self.b2.Bind(wx.EVT_BUTTON, self.onButton2, self.b2)
        self.b3.Bind(wx.EVT_BUTTON, self.onButton3, self.b3)
        self.b4.Bind(wx.EVT_BUTTON, self.onButton4, self.b4)
        self.b5.Bind(wx.EVT_BUTTON, self.onButton5, self.b5)
        self.b6.Bind(wx.EVT_BUTTON, self.onButton6, self.b6)
        self.b7.Bind(wx.EVT_BUTTON, self.onButton7, self.b7)
        self.b8.Bind(wx.EVT_BUTTON, self.onButton8, self.b8)
        self.b9.Bind(wx.EVT_BUTTON, self.onButton9, self.b9)
        self.bComa.Bind(wx.EVT_BUTTON, self.onButtonComa, self.bComa)
        self.bCancelar.Bind(wx.EVT_BUTTON, self.onButtonCancelar, self.bCancelar)
        self.bEnter.Bind(wx.EVT_BUTTON, self.onButtonEnter, self.bEnter)
        self.bBorrar.Bind(wx.EVT_BUTTON, self.onButtonBorrar, self.bBorrar)


    def setTextCtrl(self, tc):
        self.textCtrlModificar = tc
        #self.textCtrlShow.SetValue(self.textCtrlModificar.GetValue())
        self.textCtrlShow.SetValue("")
        self.strNum = self.textCtrlShow.GetValue()
        

    def setPanelRegreso(self, pr):
        self.panelRegreso = pr
        

    def desactivarPunto(self):
        self.bComa.Disable()

    def activarPunto(self):
        self.bComa.Enable()

    def desactivar0(self):
        self.b0.Disable()

    def activar0(self):
        self.b0.Enable()


    def setSeparadorMiles(self, b):
        self.flagSeparadorMiles = b

    def getSeparadorMiles(self):
        return self.flagSeparadorMiles
        

    def onButton0(self, event):
        self.strNum = self.strNum+"0"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
        
    def onButton1(self, event):
        self.strNum = self.strNum+"1"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
    
    def onButton2(self, event):
        self.strNum = self.strNum+"2"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
    
    def onButton3(self, event):
        self.strNum = self.strNum+"3"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
    
    def onButton4(self, event):
        self.strNum = self.strNum+"4"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
    
    def onButton5(self, event):
        self.strNum = self.strNum+"5"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
    
    def onButton6(self, event):
        self.strNum = self.strNum+"6"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
    
    def onButton7(self, event):
        self.strNum = self.strNum+"7"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
        
    def onButton8(self, event):
        self.strNum = self.strNum+"8"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)
    
    def onButton9(self, event):
        self.strNum = self.strNum+"9"
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)

    def onButtonComa(self, event):
        self.strNum = self.strNum+","
        if self.flagSeparadorMiles:
            self.textCtrlShow.SetValue(separadorMiles.separadorMiles(self.strNum.replace(".","").replace(",",".")))
        else:
            self.textCtrlShow.SetValue(self.strNum)


    def onButtonCancelar(self, event):
        self.textCtrlShow.SetValue("")
        self.strNum = ""
        self.Hide()
        self.enableMasivo()
        self.panelRegreso.Show()

    def onButtonEnter(self, event):
        self.textCtrlModificar.SetValue(self.textCtrlShow.GetValue())
        self.textCtrlShow.SetValue("")
        self.strNum = ""
        self.Hide()
        self.enableMasivo()
        self.panelRegreso.Show()

    def onButtonBorrar(self, event):
        self.textCtrlShow.SetValue("")
        self.strNum = ""


    def setImpactados(self, listaImpactados):
        """Asigna los objetos impactados que pueden ser desactivados mientras se modifica el valor del textCtrl a modificar y los desactiva"""
        self.listaImpactados = listaImpactados
        self.disableMasivo()


    def disableMasivo(self):
        map(lambda x: x.Disable(), self.listaImpactados)

    def enableMasivo(self):
        map(lambda x: x.Enable(), self.listaImpactados)
