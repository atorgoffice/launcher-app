import subprocess
import gi

from cloud.ivanbotty.Launcher.models.applications_model import ApplicationModel

gi.require_version("Gtk", "4.0")

from gi.repository import Gio

class CommandService:
    """Quick command management"""

    def __init__(self):
        # We use a ListStore so the controller can bind directly to Gtk.ListBox
        self.store = Gio.ListStore(item_type=ApplicationModel)

        # Here you can register default commands
        self.register_default_commands()

    def register_default_commands(self):
        """Adds basic system commands"""
        self.add_command(ApplicationModel("Terminal", "gnome-terminal", "Open the terminal"))
        self.add_command(ApplicationModel("File Manager", "nautilus", "Open the file manager"))
        self.add_command(ApplicationModel("Browser", "xdg-open https://www.google.com", "Open the browser"))
        self.add_command(ApplicationModel("Shutdown", "systemctl poweroff", "Shut down the system"))

    def add_command(self, command: ApplicationModel):
        """Adds a new command"""
        self.store.append(command)

    def filter_commands(self, search_text: str):
        """
        Filters commands by name or description
        """
        search_text = search_text.lower()
        filtered = Gio.ListStore(item_type=ApplicationModel)
        for i in range(self.store.get_n_items()):
            cmd = self.store.get_item(i)
            if search_text in cmd.name.lower() or search_text in cmd.description.lower():
                filtered.append(cmd)
        return filtered

    def get_command(self, search_text: str):
        """
        Returns the first command that matches the text
        """
        matches = self.filter_commands(search_text)
        if matches.get_n_items() > 0:
            return matches.get_item(0)
        return None
