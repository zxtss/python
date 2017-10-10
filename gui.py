import wx
class wxGUI(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Login', size=(250,150), pos=(350,350))
        panel = wx.Panel(frame, -1)

        label1 = wx.StaticText(panel, -1, 'UserName:', pos=(0,10), style=wx.ALIGN_RIGHT)
        label2 = wx.StaticText(panel, -1, 'Password:', pos=(0,30), style=wx.ALIGN_RIGHT)

        self.textName = wx.TextCtrl(panel, -1, pos=(70,10), size=(160,20))
        self.textPwd = wx.TextCtrl(panel, -1, pos=(70,30), size=(160,20),style=wx.TE_PASSWORD)
        
        buttonOK = wx.Button(panel, -1, 'OK', pos=(30,60))
        self.Bind(wx.EVT_BUTTON, self.OnButtonOK, buttonOK)
        buttonCancel = wx.Button(panel, -1, 'Cancel', pos=(120,60))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCancel, buttonCancel)
        buttonOK.SetDefault()

        frame.Show()
        return True
    def OnButtonOK(self, event):
        usrName = self.textName.GetValue()
        usrPwd = self.textPwd.GetValue()
        if usrName=='123456' and usrPwd=='654321':
            wx.MessageBox('Right')
        else:
            wx.MessageBox('Wrong')
    def OnButtonCancel(self, event):
        pass
app = wxGUI()
app.MainLoop()







'''
import wx
class wxGUI(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='wxGUI', size=(160,140))
        panel = wx.Panel(frame, -1)        
        
        self.buttonOK = wx.Button(panel, -1, 'Start', pos=(0,0))
        self.Bind(wx.EVT_BUTTON, self.OnButtonOK, self.buttonOK)
        
        frame.Show()
        return True
    def OnButtonOK(self, event):
        text = self.buttonOK.GetLabelText()
        if text == 'Start':
            self.buttonOK.SetLabelText('End')
        elif text == 'End':
            self.buttonOK.SetLabelText('Start')
    
app = wxGUI()
app.MainLoop()
'''