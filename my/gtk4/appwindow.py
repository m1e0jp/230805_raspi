import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gdk, Gio, GLib, Adw, GObject

css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(600, 250)
        self.set_title("MyApp")


        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.button = Gtk.Button(label="Hello")
        self.button.connect('clicked', self.hello)

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        self.box1.append(self.box3)  # And another one, empty for now

        self.check = Gtk.CheckButton(label="And goodbye?")
        self.box2.append(self.button) # Put button in the first of the two vertial boxes
        self.box2.append(self.check)

        self.radio1 = Gtk.CheckButton(label="test1")
        self.radio2 = Gtk.CheckButton(label="test2")
        self.radio3 = Gtk.CheckButton(label="test3")
        self.radio2.set_group(self.radio1)
        self.radio1.connect("toggled", self.radio_toggled, "1")
        self.radio2.connect("toggled", self.radio_toggled, "2")
        self.radio3.connect("toggled", self.radio_toggled, "3")
        self.box2.append(self.radio1)
        self.box2.append(self.radio2)
        self.box2.append(self.radio3)


        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.switch = Gtk.Switch()
        self.switch.set_active(True)  # Let's default it to on
        self.switch.connect("state-set", self.switch_switched) # Lets trigger a function
        self.switch_box.append(self.switch)

        self.label = Gtk.Label(label="音声入力")
        self.label.set_css_classes(['title'])
        self.switch_box.append(self.label)
        self.switch_box.set_spacing(20)

        self.box2.append(self.switch_box)


        self.slider = Gtk.Scale()
        self.slider.set_digits(0)  # Number of decimal places to use
        self.slider.set_range(0, 10)
        self.slider.set_draw_value(True)  # Show a label with current value
        self.slider.set_value(5)  # Sets the current value/position
        self.slider.connect('value-changed', self.slider_changed)
        self.box2.append(self.slider)


        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        self.open_button = Gtk.Button(label="Open")
        self.open_button.set_icon_name("document-open-symbolic")
        self.open_button.connect("clicked", self.show_open_dialog)
        self.header.pack_start(self.open_button)


        self.open_dialog = Gtk.FileDialog.new()
        self.open_dialog.set_title("Select a File")
        

        # Create a new "Action"
        action = Gio.SimpleAction.new("something", None)
        action.connect("activate", self.print_something)
        self.add_action(action)  # Here the action is being added to the window, but you could add it to the
                                 # application or an "ActionGroup"

        # Create a new menu, containing that action
        menu = Gio.Menu.new()
        menu.append("Do Something", "win.something")  # Or you would do app.something if you had attached the
                                                      # action to the application

        # Create a popover
        self.popover = Gtk.PopoverMenu()  # Create a new popover menu
        self.popover.set_menu_model(menu)

        # Create a menu button
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")  # Give it a nice icon

        # Add menu button to the header bar
        self.header.pack_start(self.hamburger)


        # Set app name
        GLib.set_application_name("My App")

        # Create an action to run a *show about dialog* function we will create 
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.show_about)
        self.add_action(action)
        
        menu.append("About", "win.about")  # Add it to the menu we created in previous section



        # Drawing
        self.dw = Gtk.DrawingArea()

        # Make it fill the available space (It will stretch with the window)
        self.dw.set_hexpand(True)
        self.dw.set_vexpand(True)

        # Instead, If we didn't want it to fill the available space but wanted a fixed size
        #self.dw.set_content_width(100)
        #self.dw.set_content_height(100)

        self.dw.set_draw_func(self.draw, None)
        self.box3.append(self.dw)

        evk = Gtk.GestureClick.new()
        evk.set_button(0)  # 0 for all buttons
        evk.connect("released", self.dw_click)  # could be "pressed / released"
        self.dw.add_controller(evk)

        self.blobs = []

        evk = Gtk.EventControllerMotion.new()
        evk.connect("motion", self.mouse_motion)
        self.dw.add_controller(evk)

        # Mouse Cursor
        self.cursor_crosshair = Gdk.Cursor.new_from_name("crosshair")
        self.dw.set_cursor(self.cursor_crosshair)

        # Dark Theme
        app = self.get_application()
        sm = app.get_style_manager()
        sm.set_color_scheme(Adw.ColorScheme.PREFER_DARK)

        # margin spacing
        self.box2.set_spacing(10)
        self.box2.set_margin_top(10)
        self.box2.set_margin_bottom(10)
        self.box2.set_margin_start(10)
        self.box2.set_margin_end(10)

        # TextView
        self.textview1 = Gtk.TextView()
        self.box3.append(self.textview1)

        # GridView
        self.grid1 = Gtk.GridView()
        self.box3.append(self.grid1)

        fruits = ["Banana", "Apple", "Strawberry", "Pear", "Watermelon", "Blueberry"]

        class Fruit(GObject.Object):
            name = GObject.Property(type=str)
            def __init__(self, name):
                super().__init__()
                self.name = name

        self.ls = Gio.ListStore()

        for f in fruits:
            self.ls.append(Fruit(f))

        ss = Gtk.SingleSelection()
        ss.set_model(self.ls)

        self.grid1.set_model(ss)

        factory = Gtk.SignalListItemFactory()

        def f_setup(fact, item):
            label = Gtk.Label(halign=Gtk.Align.START)
            label.set_selectable(False)
            item.set_child(label)

        factory.connect("setup", f_setup)

        def f_bind(fact, item):
            item.get_child().set_label(item.get_item().name)
            fruit = item.get_item()
            fruit.bind_property("name",
              item.get_child(), "label",
              GObject.BindingFlags.SYNC_CREATE)
            print(ss.get_selected_item().name)

        factory.connect("bind", f_bind)

        def on_selected_items_changed(selection, position, n_items):
            selected_item = selection.get_selected_item()
            if selected_item is not None:
                print(f"Selected item changed to: {selected_item.name}")
        ss.connect("selection-changed", on_selected_items_changed)

        self.grid1.set_factory(factory)

                    
    def mouse_motion(self, motion, x, y):
        print(f"Mouse moved to {x}, {y}")

    def dw_click(self, gesture, data, x, y):
        button = gesture.get_current_button()
        print(button)
        self.blobs.append((x, y))
        self.dw.queue_draw()  # Force a redraw

    def draw(self, area, c, w, h, data):
        # c is a Cairo context

        # Fill background with a colour
        c.set_source_rgb(1, 1, 1)
        c.paint()

        c.set_source_rgb(1, 0, 1)
        for x, y in self.blobs:
            c.arc(x, y, 10, 0, 2 * 3.1415926)
            c.fill()

        # Draw a line
        c.set_source_rgb(0.5, 0.0, 0.5)
        c.set_line_width(3)
        c.move_to(10, 10)
        c.line_to(w - 10, h - 10)
        c.stroke()

        # Draw a rectangle
        c.set_source_rgb(0.8, 0.8, 0.0)
        c.rectangle(20, 20, 50, 20)
        c.fill()

        # Draw some text
        c.set_source_rgb(0.1, 0.1, 0.1)
        c.select_font_face("Sans")
        c.set_font_size(13)
        c.move_to(25, 35)
        c.show_text("Test")

    def show_about(self, action, param):
         dialog = Adw.AboutWindow(transient_for=app.get_active_window()) 
         dialog.set_application_name=("App name") 
         dialog.set_version("1.0") 
         dialog.set_developer_name("Developer") 
         dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0)) 
         dialog.set_comments("Adw about Window example") 
         dialog.set_website("https://github.com/Tailko2k/GTK4PythonTutorial") 
         dialog.set_issue_url("https://github.com/Tailko2k/GTK4PythonTutorial/issues") 
         dialog.add_credit_section("Contributors", ["Name1 url"]) 
         dialog.set_translator_credits("Name1 url") 
         dialog.set_copyright("© 2022 developer") 
         dialog.set_developers(["Developer"]) 
         dialog.set_application_icon("com.github.devname.appname") # icon must be uploaded in ~/.local/share/icons or /usr/share/icons
         dialog.set_visible(True)

    def print_something(self, action, param):
        print("Something!")


    def show_open_dialog(self, button):
        f = Gtk.FileFilter()
        f.set_name("Image files")
        f.add_mime_type("image/jpeg")
        f.add_mime_type("image/png")

        filters = Gio.ListStore.new(Gtk.FileFilter)  # Create a ListStore with the type Gtk.FileFilter
        filters.append(f)  # Add the file filter to the ListStore. You could add more.

        self.open_dialog.set_filters(filters)  # Set the filters for the open dialog
        self.open_dialog.set_default_filter(f)
    
        self.open_dialog.open(self, None, self.open_dialog_open_callback)
        
    def open_dialog_open_callback(self, dialog, result):
        try:
            file = dialog.open_finish(result)
            if file is not None:
                print(f"File path is {file.get_path()}")
                # Handle loading file from here
        except GLib.Error as error:
            print(f"Error opening file: {error.message}")
     

    def slider_changed(self, slider):
        print(int(slider.get_value()))

    def switch_switched(self, switch, state):
        print(f"The switch has been switched {'on' if state else 'off'}")

    def hello(self, button):
        print("Hello world")
        if self.check.get_active():
            print("Goodbye world!")
            self.close()

    def radio_toggled(self, radio, value):
        print(f"toggled: {radio} {value}")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
