import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GObject

class ApplicationModel(GObject.GObject):
    type = GObject.Property(type=str)
    name = GObject.Property(type=str)
    exec_cmd = GObject.Property(type=str, default=None)
    icon = GObject.Property(type=str, default=None)

    def __init__(self, type, name, exec_cmd=None, icon=None):
        super().__init__()
        self.type = type
        self.name = name
        self.exec_cmd = exec_cmd
        self.icon = icon
