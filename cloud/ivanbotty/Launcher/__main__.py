#!/usr/bin/env python3
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gio
from cloud.ivanbotty.Launcher.app import App

def main():
    try:
        resource = Gio.Resource.load("cloud/ivanbotty/Launcher/resources/resources.gresource")
        Gio.resources_register(resource)
    except Exception as e:
        print(f"Failed to load resources: {e}")
        return

    app = App()
    app.run()

if __name__ == "__main__":
    main()
