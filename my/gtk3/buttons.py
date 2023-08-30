import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ボタンウィンドウ")
        self.set_default_size(400, 300)

        # グリッドを作成
        self.grid = Gtk.Grid()
        self.add(self.grid)

        # ボタンを配置
        for row in range(2):
            for col in range(3):
                button_label = f"ボタン {row+1}-{col+1}"
                button = Gtk.Button(label=button_label)
                self.grid.attach(button, col, row, 1, 1)

# ウィンドウを生成して表示
win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
