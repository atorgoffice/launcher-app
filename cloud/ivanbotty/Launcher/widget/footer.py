import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from cloud.ivanbotty.Launcher.config.config import UI_CONFS, PREFERENCES
from cloud.ivanbotty.Launcher.widget.preferences import Preferences

class Footer(Gtk.Box):
    def __init__(self, app):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        self.set_margin_top(UI_CONFS[PREFERENCES]["margin_top"])
        self.set_margin_bottom(UI_CONFS[PREFERENCES]["margin_bottom"])
        self.set_margin_start(UI_CONFS[PREFERENCES]["margin_start"])
        self.set_margin_end(UI_CONFS[PREFERENCES]["margin_end"])
        self.app = app
        shortcuts = [
            ("Return", "Select"),
            ("Down", "Navigate"),
            ("Up", None)
        ]

        logo_button = Gtk.Button()
        logo_button.set_valign(Gtk.Align.CENTER)
        logo_button.set_halign(Gtk.Align.START)
        logo_content = Adw.ButtonContent()
        logo_content.set_icon_name("applications-system")
        logo_button.set_child(logo_content)

        logo_button.connect("clicked", lambda button: Preferences(self.app).present())

        spacer = Gtk.Box()
        spacer.set_hexpand(True)

        shortcuts_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        for key, desc in shortcuts:
            shortcut_label = Gtk.ShortcutLabel.new(key)
            shortcut_label.set_margin_end(UI_CONFS[PREFERENCES]["margin_end"])
            desc_label = Gtk.Label(label=desc)
            desc_label.set_xalign(0)
            shortcuts_box.append(desc_label)
            shortcuts_box.append(shortcut_label)
            
        self.append(logo_button)
        self.append(spacer)
        self.append(shortcuts_box)
