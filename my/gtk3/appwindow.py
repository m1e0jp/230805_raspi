#!/usr/bin/env python3
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gio,GLib

MENUBAR_XML_FILENAME = "./test.xml"

class TestAppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        maximize_action = Gio.SimpleAction.new_stateful("maximize", None, GLib.Variant.new_boolean(False))
        maximize_action.connect("change-state", self.on_maximize_toggle)
        self.add_action(maximize_action)
        self.connect("notify::is-maximized",lambda obj, pspec: maximize_action.set_state(GLib.Variant.new_boolean(obj.props.is_maximized)),)

    def on_maximize_toggle(self, action, value):
        if value.get_boolean():
            self.maximize()
        else:
            self.unmaximize()
class TestApplication(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_flags(Gio.ApplicationFlags.HANDLES_OPEN|Gio.ApplicationFlags.HANDLES_COMMAND_LINE)
        self.add_main_option("version",ord("v"),GLib.OptionFlags.IN_MAIN,GLib.OptionArg.NONE,"version info",None)

    def do_startup(self):
        Gtk.Application.do_startup(self)
        self.build_menubar()

    def do_activate(self):
        window=TestAppWindow(application=self)
        window.present()

    def do_open(self,files,n_files,hint):
        for gfile in files:
            print(gfile.get_path())
        print(hint)

    def do_command_line(self,command_line):
        options_dict = command_line.get_options_dict()
        options = options_dict.end().unpack()
        if "version" in options:
            if options["version"]:
                print("version:",0)
                return 0
        self.activate()
        return 0

    def build_menubar(self):
        builder = Gtk.Builder.new_from_file(MENUBAR_XML_FILENAME)
        menubar = builder.get_object("menubar")
        self.set_menubar(menubar)

        action = Gio.SimpleAction.new("new", None)
        action.connect("activate", self.on_new)
        self.add_action(action)

        action = Gio.SimpleAction.new("open", None)
        action.connect("activate", self.on_open)
        self.add_action(action)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.on_about)
        self.add_action(action)

        action = Gio.SimpleAction.new("help", None)
        action.connect("activate", self.on_help)
        self.add_action(action)

    def on_quit(self,action,param):
        self.quit()

    def on_about(self, action, param):
        about_dialog = Gtk.AboutDialog()
        about_dialog.set_program_name("TestApp") 
        about_dialog.present()

    def on_help(self, action, param):
        help_dialog = Gtk.MessageDialog(flags=0,buttons=Gtk.ButtonsType.OK,text="Help")
        help_dialog.format_secondary_text("Help for TestApp")
        link=Gtk.LinkButton.new_with_label("https://google.co.jp/","link to help")
        link.show()
        contentarea=help_dialog.get_content_area()
        contentarea.add(link)
        help_dialog.run()
        help_dialog.destroy()

    def on_new(self,action,param):
        self.activate()

    def on_open(self,action,param):
        dialog = Gtk.FileChooserDialog(action=Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN,Gtk.ResponseType.OK)

        filter = Gtk.FileFilter()
        filter.set_name("Zip files")
        filter.add_pattern("*.zip")
        filter.add_mime_type("application/zip")
        dialog.add_filter(filter)

        filter = Gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*")
        dialog.add_filter(filter)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            file=dialog.get_file()
            self.open([file],"")
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()

def main():
    app = TestApplication()
    app.run(sys.argv)

if __name__ == "__main__":
    main()
    