import gi
gi.require_version("Adw", "1")
from gi.repository import Adw
from cloud.ivanbotty.Launcher.config.config import COMPACT_STYLE, DEFAULT_STYLE, PREFERENCES

class Preferences(Adw.PreferencesDialog):
    def __init__(self, app):
        super().__init__(title="Preferences")
        self.app = app

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

        extension_group = Adw.PreferencesGroup(title="Extensions")

        extension_list = self.app.extensions_service.list_extensions()
        for extension in extension_list:
            # Switch row for enabling/disabling extension support
            self.switch = Adw.SwitchRow(
                active=extension.enabled,
                title=extension.name if extension.name else "Unnamed Extension",
                subtitle=extension.description if extension.description else "No description available."
            )
            self.switch.connect("notify::active", self.on_switch_toggled)
            extension_group.add(self.switch)

        about_group = Adw.PreferencesGroup(title="About")

        # Information row
        info_row = Adw.ActionRow(
            title="About",
            subtitle="Launcher App Preferences Demo"
        )
        info_row.set_activatable(True)
        def on_info_row_activated(row):
            about = Adw.AboutDialog.new_from_appdata("/cloud/ivanbotty/Launcher/resources/appdata.xml", "0.0.1")
            about.set_developers(["Ivan Bottigelli https://ivanbotty.cloud"])
            about.set_copyright("© 2025 Ivan Bottigelli.")
            about.present()

        info_row.connect("activated", on_info_row_activated)

        about_group.add(info_row)

        # Add group to page and page to dialog
        page.add(general_group)
        page.add(extension_group)
        page.add(about_group)
        self.add(page)

    def on_switch_toggled(self, switch, _):
        # Update the PREFERENCES variable
        global PREFERENCES
        PREFERENCES = COMPACT_STYLE if switch.get_active() else DEFAULT_STYLE
