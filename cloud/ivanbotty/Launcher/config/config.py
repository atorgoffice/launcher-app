from pathlib import Path

# Standard paths for Flatpak launcher applications
USER_DIR = Path.home() / ".local/share/applications"
SYSTEM_DIRS = [
    Path("/usr/share/applications"),          # Exposed by Flatpak
    Path("/run/host/share/applications"),     # Host Flatpak
]

ALL_APP_DIRS = [USER_DIR] + SYSTEM_DIRS

# Define style names
COMPACT_STYLE = "compact"
DEFAULT_STYLE = "default"

# UI configuration for each style
UI_CONFS = {
    COMPACT_STYLE: {
        "width": 800,
        "height": 540,
        "entry_width": 760,
        "entry_height": 48,
        "margin_top": 16,
        "margin_bottom": 16,
        "margin_start": 16,
        "margin_end": 16
    },
    DEFAULT_STYLE: {
        "width": 1280,
        "height": 900,
        "entry_width": 1000,
        "entry_height": 72,
        "margin_top": 24,
        "margin_bottom": 24,
        "margin_start": 24,
        "margin_end": 24
    }
}

# Default user preference for style
PREFERENCES = COMPACT_STYLE
