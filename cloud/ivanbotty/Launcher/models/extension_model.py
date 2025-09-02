import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GObject

class ExtensionModel(GObject.GObject):
    name = GObject.Property(type=str)
    description = GObject.Property(type=str, default=None)
    enabled = GObject.Property(type=bool, default=True)
    version = GObject.Property(type=str, default=None)
    author = GObject.Property(type=str, default=None)

    def __init__(self, name, description=None, enabled=True, service=None, version=None, author=None):
        super().__init__()
        self.name = name
        self.description = description
        self.service = service
        self.enabled = enabled
        self.version = version
        self.author = author
