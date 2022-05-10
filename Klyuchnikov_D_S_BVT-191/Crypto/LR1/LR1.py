from cProfile import label
import wx
import math

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='LR1', size=(500,400))
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)   
             
        self.text_ctrl = wx.TextCtrl(panel, pos=(20,20))
        self.data = wx.TextCtrl(panel, wx.ID_ANY, size=(100,100),style = wx.TE_MULTILINE|wx.TE_READONLY|wx.VSCROLL,pos=(20,100))
        self.alphabet = wx.TextCtrl(panel, wx.ID_ANY, size=(100,100),style = wx.TE_MULTILINE|wx.VSCROLL,pos=(20,150))
        self.rb1 = wx.RadioButton(panel,11, label = 'en', pos = (10,10), style = wx.RB_GROUP) 
        self.rb2 = wx.RadioButton(panel,22, label = 'ru',pos = (10,40)) 

        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)

        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)   
        my_sizer.Add(self.data, 0, wx.ALL | wx.EXPAND, 5)   
        my_sizer.Add(self.alphabet, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.rb1, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.rb2, 0, wx.ALL | wx.EXPAND, 5)

        my_btn = wx.Button(panel, label='Code', pos=(100, 100))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)     
        panel.SetSizer(my_sizer)       
        self.Show()

    def on_press(self, event):
        message = self.text_ctrl.GetValue()
        self.data.Clear()

        alphabet = self.alphabet.GetValue()
        alphabet.split()
        sum = 0
        for c in message:
            for s in alphabet:
                if s.find(c) == 0:
                    sum += 1
                    break
        M = len(alphabet)
        i = math.log2(M)
        I = math.ceil(sum*i)
        self.data.AppendText("Количество информации = " + str(I))
       

    def OnRadiogroup(self, e): 
      rb = e.GetEventObject()
      label = rb.GetLabel() 
      alphabet = readAlphabet(label)
      self.alphabet.Clear()
      self.alphabet.AppendText(alphabet)

    def calculate():
        pass

def readAlphabet(selected_type):
    if selected_type == 'ru':
        with open('Klyuchnikov_D_S_BVT-191/Crypto/LR1/russian.txt', encoding="utf-8") as f:
            rus = f.read()
            return rus
    else :
        with open('Klyuchnikov_D_S_BVT-191/Crypto/LR1/en.txt', "rb") as f:
            en = f.read()
            return en
        



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()