import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from .services.extensions_service import ExtensionService
from .services.applications_service import ApplicationsService
from .services.math_service import MathService
from .services.command_service import CommandService
from .services.ai_service import AIService
from .controller.keyboard_controller import KeyboardController
from .controller.search_controller import SearchController
from cloud.ivanbotty.Launcher.config.config import UI_CONFS, PREFERENCES
from .widget.window import Window
from .widget.search_entry import SearchEntry
from .widget.row import Row
from .widget.footer import Footer

class App(Adw.Application):
    """Main application class."""

    def __init__(self):
        """Initialize the application and its components."""
        super().__init__(application_id="cloud.ivanbotty.Launcher")
        self.name = "Main Application"
        self.win = None

        # Create widgets
        self.listbox = Gtk.ListBox()
        self.listbox.set_visible(False)
        self.entry = SearchEntry(
            placeholder="Type to search...",
            width=UI_CONFS[PREFERENCES]["entry_width"],
            height=UI_CONFS[PREFERENCES]["entry_height"]
        )

        # Initialize services
        self.extensions_service = ExtensionService()
        self.extensions_service.add_extension(
            name="Application",
            description="Find applications",
            service=ApplicationsService(),
            version="1.0",
            author="ivanbotty"
        )
        self.extensions_service.add_extension(
            name="Math",
            description="Perform math calculations",
            service=MathService(),
            version="1.0",
            author="ivanbotty"
        )
        self.extensions_service.add_extension(
            name="Command",
            description="Execute system commands",
            service=CommandService(),
            version="1.0",
            author="ivanbotty"
        )
        self.extensions_service.add_extension(
            name="AI",
            description="AI-powered assistance",
            service=AIService(),
            version="1.0",
            author="ivanbotty"
        )

    def do_startup(self):
        """Startup routine for the application."""
        Gtk.Application.do_startup(self)
        print("Application startup")

        # Prepare services dictionary
        services = {
            "app": self.extensions_service.get_extension("Application"),
            "math": self.extensions_service.get_extension("Math"),
            "command": self.extensions_service.get_extension("Command"),
            "ai": self.extensions_service.get_extension("AI")
        }

        # Initialize controllers
        self.search_controller = SearchController(
            entry_widget=self.entry,
            listbox=self.listbox,
            services=services
        )

        # Adwaita setup
        Adw.init()
        Adw.StyleManager.get_default().set_color_scheme(Adw.ColorScheme.DEFAULT)

        # Create main window
        self.win = Window(self)
        event_controller = KeyboardController(self)
        self.win.add_controller(event_controller)

        # Listbox setup
        self.listbox.set_visible(True)
        self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.listbox.set_vexpand(True)
        self.listbox.set_hexpand(True)

        # Create scrolled window for the listbox
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.set_vexpand(True)
        scrolled_window.set_hexpand(True)
        scrolled_window.set_child(self.listbox)

        extensions_list = self.extensions_service.list_extensions()
        self.listbox.bind_model(extensions_list, self.create_row)

        # Create footer widget
        footer = Footer(self)

        # Layout setup
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.set_margin_top(UI_CONFS[PREFERENCES]["margin_top"])
        box.set_margin_bottom(UI_CONFS[PREFERENCES]["margin_bottom"])
        box.set_margin_start(UI_CONFS[PREFERENCES]["margin_start"])
        box.set_margin_end(UI_CONFS[PREFERENCES]["margin_end"])
        box.append(self.entry)
        box.append(scrolled_window)
        box.append(footer)

        self.win.set_content(box)

    def create_row(self, app):
        """Create a row widget for the given app."""
        if app.enabled is True:
            row = Row(app)
            row.app_model = app
            return row

    def do_activate(self):
        """Activate the application and show the window."""
        print("Application activated")
        if self.win is not None:
            self.win.present()