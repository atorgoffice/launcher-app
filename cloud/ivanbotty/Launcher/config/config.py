from pathlib import Path

SYSTEM_DIRS = [
    Path("/usr/share/applications"),                                # system applications
    Path("/run/host/usr/share/applications"),                       # host applications
    Path("/run/host/var/lib/flatpak/exports/share/applications"),   # flatpak system-wide applications
    Path.home() / ".local/share/applications",                      # user applications
    Path("/run/host" + str(Path.home()) + "/.local/share/applications")  # user applications from host perspective
]

ALL_APP_DIRS = SYSTEM_DIRS

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
