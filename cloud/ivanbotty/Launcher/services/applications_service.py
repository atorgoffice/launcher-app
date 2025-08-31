import os, gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gio

from cloud.ivanbotty.Launcher.config.config import ALL_APP_DIRS
from cloud.ivanbotty.Launcher.helper.parser import Parser
from cloud.ivanbotty.Launcher.models.applications_model import ApplicationModel

class ApplicationsService:
    """Service for loading and filtering application entries."""

    def __init__(self):
        """Initialize the ApplicationsService with a parser and an empty store."""
        self.parser = Parser()
        self.store = Gio.ListStore(item_type=ApplicationModel)

    def load_applications(self):
        """
        Load application entries from directories specified in ALL_APP_DIRS.

        Iterates through each directory, finds files ending with '.desktop',
        parses them into ApplicationModel instances, and appends them to the store.

        Returns:
            Gio.ListStore: Store containing loaded ApplicationModel instances.
        """
        for app_dir in ALL_APP_DIRS:
            # Ensure the directory exists and is a directory
            if app_dir.exists() and app_dir.is_dir():
                # Iterate over all files in the directory
                for file in os.listdir(app_dir):
                    # Only process files with '.desktop' extension
                    if file.endswith(".desktop"):
                        # Parse the desktop entry file
                        new_entry = self.parser.parse_desktop_entry(os.path.join(app_dir, file))
                        # If parsing was successful, add to the store
                        if new_entry:
                            self.store.append(ApplicationModel(**new_entry))
        return self.store

    def filter_applications(self, search_text=""):
        """
        Filter applications by name using the provided search text.

        Args:
            search_text (str): Text to search for in application names.

        Returns:
            Gio.ListStore: Store containing filtered ApplicationModel instances.
        """
        filtered_apps = []
        search_text = search_text.lower()
        # Iterate over all applications in the store
        for i in range(self.store.get_n_items()):
            app = self.store.get_item(i)
            # Check if the application's name contains the search text (case-insensitive)
            if search_text in app.name.lower():
                filtered_apps.append(app)
        # Sort the filtered applications alphabetically by name
        filtered_apps.sort(key=lambda a: a.name.lower())
        # Create a new ListStore for the filtered applications
        filtered_store = Gio.ListStore(item_type=ApplicationModel)
        for app in filtered_apps:
            filtered_store.append(app)
        return filtered_store
