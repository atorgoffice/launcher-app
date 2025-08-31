class Parser:
    def __init__(self):
        pass

    def parse_desktop_entry(self, file_path):
        entry = {}
        current_section = None
        terminal = False

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                if not line or line.startswith("#"):
                    continue

                # Handle sections
                if line.startswith("[") and line.endswith("]"):
                    current_section = line[1:-1]
                    continue

                # Consider only the main Desktop Entry section
                if current_section == "Desktop Entry":
                    if line.startswith("Terminal="):
                        terminal = line.split("=", 1)[1].strip().lower() == "true"
                    elif line.startswith("Type="):
                        entry["type"] = line.split("=", 1)[1].strip()
                    elif line.startswith("Name="):
                        entry["name"] = line.split("=", 1)[1].strip()
                    elif line.startswith("Exec="):
                        entry["exec_cmd"] = line.split("=", 1)[1].strip()
                    elif line.startswith("Icon="):
                        entry["icon"] = line.split("=", 1)[1].strip()

        # Ignore entries that require a terminal
        if terminal:
            return None

        return entry
