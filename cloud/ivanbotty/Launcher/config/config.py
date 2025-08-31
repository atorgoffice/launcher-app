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
        "width": 700,
        "height": 400,
        "entry_width": 660,
        "entry_height": 36,
        "margin_top": 8,
        "margin_bottom": 8,
        "margin_start": 8,
        "margin_end": 8
    },
    DEFAULT_STYLE: {
        "width": 800,
        "height": 540,
        "entry_width": 760,
        "entry_height": 48,
        "margin_top": 16,
        "margin_bottom": 16,
        "margin_start": 16,
        "margin_end": 16
    }
}

# Default user preference for style
PREFERENCES = DEFAULT_STYLE

SYSTEM_PROMPT = (
    "You are a helpful assistant focused on concise, accurate answers. "
    "Respond only to the user's question, avoiding unnecessary details. "
    "Always reply in JSON format: {\"response\": \"your answer\"}. "
    "Example questions: What is the capital of France? How do I create a virtual environment in Python? "
    "Example response: {\"response\": \"Paris is the capital of France.\"} "
    "Keep responses brief and relevant."
)
