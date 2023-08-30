import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class InputWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="入力テキストボックスウィンドウ")
        self.set_default_size(400, 200)

        # レイアウトボックスを作成
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        # 入力テキストボックス1
        self.entry1 = Gtk.Entry()
        self.entry1.set_text("テキストボックス1")
        self.box.pack_start(self.entry1, True, True, 0)

        # 入力テキストボックス2
        self.entry2 = Gtk.Entry()
        self.entry2.set_text("テキストボックス2")
        self.box.pack_start(self.entry2, True, True, 0)

# ウィンドウを生成して表示
win = InputWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
