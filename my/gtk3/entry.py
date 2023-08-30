#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gi.repository import GLib
import signal

class Sample(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('Gtk+3 sample')
        self.set_border_width(20)

        vbox = Gtk.Box()
        vbox.set_orientation(Gtk.Orientation.VERTICAL)
        vbox.set_spacing(10)
        self.add(vbox)

        topbox = Gtk.Box()
        topbox.set_spacing(10)
        vbox.pack_start(topbox, True, True, 0)

        button = Gtk.Button()
        button.set_label('swap')
        button.connect('clicked', self.on_click_swap)
        topbox.pack_start(button, True, True, 0)

        button = Gtk.Button()
        button.set_label('close')
        button.set_use_underline(True)
        button.connect('clicked', self.on_click_close)
        topbox.pack_start(button, True, True, 0)

        bottombox = Gtk.Box()
        bottombox.set_spacing(10)
        vbox.pack_start(bottombox, True, True, 0)

        self.entry = Gtk.Entry()
        self.entry.set_text('left')
        bottombox.pack_start(self.entry, True, True, 0)

        self.label = Gtk.Label()
        self.label.set_text('right')
        bottombox.pack_start(self.label, True, True, 0)

        self.connect('delete-event', Gtk.main_quit)

        GLib.unix_signal_add(GLib.PRIORITY_HIGH, signal.SIGINT, \
                             self.handle_unix_signal, None)

    def handle_unix_signal(self, user_data):
        self.on_click_close( None)

    def on_click_swap(self, button):
        label = self.label.get_text()
        self.label.set_text(self.entry.get_text())
        self.entry.set_text(label)

    def on_click_close(self, button):
        Gtk.main_quit()

win = Sample()
win.show_all()

Gtk.main()
