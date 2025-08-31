import gi
gi.require_version("Adw", "1")
from gi.repository import Adw
from cloud.ivanbotty.Launcher.config.config import COMPACT_STYLE, DEFAULT_STYLE, PREFERENCES

class Preferences(Adw.PreferencesDialog):
    def __init__(self):
        super().__init__(title="Preferences")

        # Create the preferences page and group
        page = Adw.PreferencesPage()
        general_group = Adw.PreferencesGroup(title="General")

        # Switch row for enabling/disabling compact layout
        self.switch = Adw.SwitchRow(
            active=(PREFERENCES == COMPACT_STYLE),
            title="Use compact layout",
            subtitle="Switch between compact and default layout."
        )
        self.switch.connect("notify::active", self.on_switch_toggled)
        general_group.add(self.switch)

        about_group = Adw.PreferencesGroup(title="About")

        # Information row
        info_row = Adw.ActionRow(
            title="About",
            subtitle="Launcher App Preferences Demo"
        )
        info_row.set_activatable(True)
        def on_info_row_activated(row):
            Adw.AboutDialog.new_from_appdata("resource:///cloud/ivanbotty/Launcher/resources/appdata.xml").present()

        info_row.connect("activated", on_info_row_activated)

        about_group.add(info_row)

        # Add group to page and page to dialog
        page.add(general_group)
        page.add(about_group)
        self.add(page)

    def on_switch_toggled(self, switch, _):
        # Update the PREFERENCES variable
        global PREFERENCES
        PREFERENCES = COMPACT_STYLE if switch.get_active() else DEFAULT_STYLE
