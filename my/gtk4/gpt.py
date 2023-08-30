import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Gtk4 Text Entry Example")
        
        # Create a text view for multi-line input
        text_view = Gtk.TextView()
        text_view.set_wrap_mode(Gtk.WrapMode.WORD)  # Enable word wrapping
        text_view.set_vexpand(True)  # Expand vertically to fill available space
        
        # Create a buffer for the text view
        buffer = text_view.get_buffer()
        buffer.set_text("This is a multi-line text entry.")
        
        # Create a button and set its label
        button = Gtk.Button(label="Get Text")
        button.connect("clicked", self.on_button_clicked, buffer)
        
        # Create a vertical box layout and add widgets to it
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.pack_start(text_view, True, True, 0)
        vbox.pack_start(button, False, False, 0)
        
        # Add the vertical box to the window
        self.add(vbox)

    def on_button_clicked(self, button, buffer):
        # Get the text from the buffer
        start_iter = buffer.get_start_iter()
        end_iter = buffer.get_end_iter()
        text = buffer.get_text(start_iter, end_iter, True)
        print("Text from text view:", text)

# Create a Gtk application
app = Gtk.Application()
# Connect the "activate" signal to a callback function
app.connect("activate", lambda app: MyWindow())
# Run the application
app.run(None)
