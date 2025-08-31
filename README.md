# Launcher

<p align="center">
    <img src="./cloud/ivanbotty/Launcher/resources/icons8-ricerca-96.svg" alt="Launcher Icon" width="96">
</p>

**Launcher** is a modern desktop application launcher for Linux, built with GTK4 and Adwaita. It offers instant search, a sleek user interface, and seamless integration for launching your installed applications.

<p align="center">
    <video src="./assets/launcher.mp4" controls width="480">
        Your browser does not support the video tag.
    </video>
</p>

> Icon rights: [https://icons8.it/icon/qW0hxm9M3J5x/ricerca](https://icons8.it/icon/qW0hxm9M3J5x/ricerca)

## Features

- Modern user interface with Adwaita and GTK4
- Instant search among installed applications
- Flatpak and sandbox environment support
- Selectable compact and extended layouts
- SVG icon display and app information
- Integrated user preferences

## Installation

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

> [!NOTE]
>  If you install the app as a Flatpak, system-installed apps will not be visible.

The project includes a `manifest.yaml` file for building a Flatpak package.

```bash
flatpak-builder build-dir manifest.yaml --force-clean
flatpak-builder --run build-dir manifest.yaml launcher
```

## Project Structure

- `cloud/ivanbotty/Launcher/`: main source code
- `resources/`: SVG icons and appdata files
- `manifest.yaml`: Flatpak manifest
- `pyproject.toml`: Python configuration

## Development

To contribute, create a fork and submit a pull request. Follow PEP8 conventions and ensure your code is tested.

## License

GPL-3.0-or-later