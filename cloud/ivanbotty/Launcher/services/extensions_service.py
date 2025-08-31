import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gio
from cloud.ivanbotty.Launcher.models.extension_model import ExtensionModel

class ExtensionService:
    def __init__(self):
        self.extensions = Gio.ListStore(item_type=ExtensionModel)

    def add_extension(self, name, description, service, enabled=True, version=None, author=None):
        self.extensions.append(
            ExtensionModel(
                name=name,
                description=description,
                enabled=enabled,
                service=service,
                version=version,
                author=author
            )
        )

    def list_extensions(self):
        return self.extensions

    def get_extension(self, name):
        for ext in self.extensions:
            if ext.name == name and ext.enabled:
                return ext.service
        return None
