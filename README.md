# Launcher
> [!IMPORTANT]
> **Launcher** is currently under active development. Features, interfaces, and functionality may change frequently. Contributions and feedback are welcome!

<p align="center">
    <img src="./cloud/ivanbotty/Launcher/resources/cloud.ivanbotty.Launcher.svg" alt="Launcher Icon" width="96">
</p>

**Launcher** is a modern desktop application launcher for Linux, built with GTK4 and Adwaita. It features instant search, a sleek user interface, and seamless integration for launching your installed applications.

<p align="center">
    <video src="./assets/launcher.mp4" controls width="480">
        Your browser does not support the video tag.
    </video>
</p>

> Icon rights: [https://icons8.it/icon/qW0hxm9M3J5x/ricerca](https://icons8.it/icon/qW0hxm9M3J5x/ricerca)

## Features

- Sleek, modern interface built with Adwaita and GTK4
- Flatpak support for sandboxed environments
- Switchable compact and extended layouts
- SVG icon rendering and detailed app information
- Integrated user preferences for customization
- Extension system for enabling/disabling features

### Core Services

- **ApplicationsService**
    - Automatically discovers installed apps from `.desktop` files
    - Provides instant search and filtering by name
    - Maintains a dynamic, ordered app list via `Gio.ListStore`

- **ExtensionService**
    - Manages extensions: add, remove, enable, disable
    - Supports searching and listing extensions by name
    - Allows extensions to register custom services, expanding functionality

- **CommandService**
    - Executes commands linked to applications for fast launching
    - Integrates with the app model for seamless execution

- **MathService**
    - Built-in calculator for evaluating mathematical expressions

- **AIService**
    > [!NOTE]
    >  Currently under development; not yet available
    - Integration with AI APIs for natural language queries and smart assistance


### Requirements

- Python >= 3.11
- PyGObject >= 3.44
- GTK4 and Adwaita libraries

### Local Execution

```bash
pip install .
python -m cloud.ivanbotty.Launcher
```

### Flatpak

> [!WARNING]
> If you install the app as a Flatpak, application icons may not display correctly due to sandboxing limitations.

The project includes a `manifest.yaml` file for building a Flatpak package.

```bash
flatpak-builder build-dir manifest.yaml --force-clean
flatpak-builder --run build-dir manifest.yaml launcher
```

## Project Structure

- `cloud/ivanbotty/database/`: SQLite integration layer for managing persistent data and queries
- `cloud/ivanbotty/Launcher/`: main source code
- `resources/`: SVG icons and appdata files
- `manifest.yaml`: Flatpak manifest
- `pyproject.toml`: Python configuration

## Development

To contribute, create a fork and submit a pull request. Follow PEP8 conventions and ensure your code is tested.

## License

GPL-3.0-or-later