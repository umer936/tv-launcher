# TV Launcher for Raspberry Pi

A lightweight, fullscreen, Android-style TV launcher for Raspberry Pi.  
Launch your favorite apps (e.g., Plex, YouTube Music, Steam Link, Moonlight) with big, colorful tiles — no servers required.

[TODO: Screenshot here]

---

## Features

- Fullscreen, touch/TV-friendly launcher
- Big app tiles with icons
- Easy to add or remove apps via `apps.json`
- Launches local Linux applications directly
- Lightweight with minimal dependencies
- Optional controller/keyboard navigation

---

## Requirements

- Python 3+  
- PyQt6 + Qt WebEngine
- Installed apps you want to launch (e.g., `chromium`, `youtube-music-desktop-app`, `steamlink`, `moonlight`)

### Install Python dependencies

```bash
sudo apt update
sudo apt install python3-pyqt6 python3-pyqt6.qtwebengine -y
````

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url> ~/tv-launcher
cd ~/tv-launcher
```

2. Add your apps and icons in `apps.json` and `icons/` folder:

```json
[
    {
        "name": "Plex",
        "command": "chromium --app=https://app.plex.tv/web",
    },
    {
        "name": "YouTube Music",
        "command": "youtube-music-desktop-app",
    }
]
```

3. Download the icons:

```bash
./batch_download_icons.py
```

---

## Usage

Run the launcher manually:

```bash
./launcher.py
```

The launcher will open fullscreen with all your configured apps.

---

### Autostart on boot

1. Edit the LXDE autostart file:

```bash
mkdir -p ~/.config/lxsession/LXDE-pi
vim ~/.config/lxsession/LXDE-pi/autostart
```

2. Add the following lines:

```text
@xset s off
@xset -dpms
@xset s noblank
@/home/usalman/tv-launcher/launcher.py
```

> Reboot your Pi, and it should boot straight into the launcher.

---

## Optional

* Controller support: map arrow keys or D-pad to navigate tiles
* Themes: modify CSS in HTML version (if using WebEngine)
* All Apps page: add more tiles with additional pages

---

## License

This project is licensed under the **Do What The F*ck You Want To Public License (WTFPL)**.
