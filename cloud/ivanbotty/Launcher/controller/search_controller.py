import re
from gi.repository import Gtk, Gio
from cloud.ivanbotty.Launcher.widget.row import Row

class SearchController:
    def __init__(self, entry_widget, listbox, services):
        """
        entry_widget: instance of SearchEntry
        listbox: Gtk.ListBox to update
        services: dict of available services, e.g. {"app": ApplicationsService(), "math": MathService()}
        """
        self.entry = entry_widget
        self.listbox = listbox
        self.services = services

        # Connect widget signals
        self.entry.connect("text-changed", self.on_text_changed)
        self.entry.connect("activated", self.on_activated)

    def interpret_input(self, text):
        # Parse input and determine its type
        text = text.strip()
        if not text:
            return "empty", None
        if re.fullmatch(r"[0-9+\-*/(). ]+", text):
            return "math", text
        if text.startswith(">"):
            return "command", text[1:].strip()
        if re.match(r"^https?://", text):
            return "link", text
        if text.startswith("ask"):
            return "ask", text
        return "app", text

    def on_text_changed(self, widget, text):
        # Handle text change event
        input_type, data = self.interpret_input(text)
        print(input_type, data)
        self.update_listbox(input_type, data)

    def on_activated(self, widget, text):
        # Handle activation event (e.g. Enter pressed)
        input_type, data = self.interpret_input(text)
        if input_type == "math":
            result = self.services["math"].calculate(data)
            print(f"Math result: {result}")
        elif input_type == "app":
            apps = self.services["app"].filter_applications(data)
            if apps:
                apps[0].launch()
        elif input_type == "link":
            print(f"Opening link: {data}")
            try:
                Gio.AppInfo.launch_default_for_uri(data, None)
            except Exception as e:
                print(f"Cannot open link: {e}")
        elif input_type == "ask":
            print(f"Asking: {data}")
        elif input_type == "command":
            command = self.services["command"].get_command(data)
            if command:
                command.run()

    def update_listbox(self, input_type, data):
        # Update the ListBox based on input type
        self.listbox.remove_all()
        if input_type == "empty":
            extensions_list = self.services["extensions"].list_extensions()
            self.listbox.bind_model(extensions_list, self.create_row_for_extension)
            return
        if input_type == "math":
            result = self.services["math"].calculate(data)
            self.listbox.append(Gtk.Label(label=f"Result: {result}"))
        elif input_type == "app":
            self.services["app"].load_applications()
            apps = self.services["app"].filter_applications(data)
            self.listbox.bind_model(apps, lambda app: self.create_row(app))
        elif input_type == "link":
            self.listbox.append(Gtk.Label(label=f"Link: {data}"))
        elif input_type == "ask":
            self.listbox.append(Gtk.Label(label=f"Ask: {data}"))
        elif input_type == "command":
            commands = self.services["command"].filter_commands(data)
            for cmd in commands:
                self.listbox.append(Gtk.Label(label=cmd.name))

    def create_row(self, app):
        # Create a Row widget for an application
        row = Row(app)
        row.app_model = app
        return row

    def create_row_for_extension(self, app):
        """Create a row widget for the given app extension."""
        if getattr(app, "enabled", False):
            row = Row(app)
            row.app_model = app
            return row
        return None
