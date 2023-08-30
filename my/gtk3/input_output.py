import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ScrollableInputButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="スクロール可能な入力とボタンウィンドウ")
        self.set_default_size(400, 300)

        # レイアウトボックスを作成
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        # スクロール可能な領域
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        self.box.pack_start(scrolled_window, True, True, 0)

        # 複数行入力テキストボックス
        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text("テキストを入力してください")
        scrolled_window.add(self.textview)

        # ボタン
        self.button = Gtk.Button(label="表示")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, False, False, 0)

        # スクロール可能な領域
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        self.box.pack_start(scrolled_window, True, True, 0)

        # ラベル
        self.label = Gtk.Label(label="")
        scrolled_window.add(self.label)

    def on_button_clicked(self, widget):
        start_iter = self.textbuffer.get_start_iter()
        end_iter = self.textbuffer.get_end_iter()
        text = self.textbuffer.get_text(start_iter, end_iter, True)
        self.label.set_text(f"入力されたテキスト:\n{text}")

# ウィンドウを生成して表示
win = ScrollableInputButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
