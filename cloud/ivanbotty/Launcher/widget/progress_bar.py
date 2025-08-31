import threading
from gi.repository import Gtk, GLib

class ProgressBar(Gtk.ProgressBar):
    def __init__(self, text="Loading..."):
        super().__init__()
        self.set_show_text(True)
        self.set_text(text)
        self.set_fraction(0.0)

    def update_progress(self, fraction, text=None):
        fraction = max(0.0, min(1.0, fraction))
        percent = int(fraction * 100)
        display_text = text if text is not None else f"{percent}%"
        # Update GUI in the main thread
        GLib.idle_add(self._set_progress, fraction, display_text, priority=GLib.PRIORITY_DEFAULT)

    def _set_progress(self, fraction, display_text):
        self.set_fraction(fraction)
        self.set_text(display_text)
        return False  # Remove idle handler after execution

    def start_long_task(self, steps=100, delay=0.05):
        def task():
            for i in range(steps + 1):
                self.update_progress(i / steps)
                time.sleep(delay)
        import time
        threading.Thread(target=task, daemon=True).start()