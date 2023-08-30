import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title='wxPython')

        ######################################
        #  ここに入るコードのみ、紹介していきます。
        ######################################
        text = wx.TextCtrl(self, -1, value='最初に表示する文字')
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
