#!/usr/bin/env python3
import json
import subprocess
import os
import sys

def main():
    script_path = os.path.join(os.getcwd(), "download_play_icon.py")
    apps_file = os.path.join(os.getcwd(), "apps.json")

    # Check files
    if not os.path.exists(script_path):
        print(f"Could not find {script_path}")
        sys.exit(1)
    if not os.path.exists(apps_file):
        print(f"Could not find {apps_file}")
        sys.exit(1)

    # Load app list
    with open(apps_file, "r", encoding="utf-8") as f:
        apps = json.load(f)

    # Ensure icons folder exists
    os.makedirs("icons", exist_ok=True)

    # Process each app
    for app in apps:
        name = app.get("name")
        if not name:
            print("Skipping entry with no 'name'")
            continue

        print(f"\nDownloading icon for: {name}")

        try:
            subprocess.run(
                [sys.executable, script_path, name],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Failed to download icon for {name}: {e}")

    print("\nAll downloads attempted.")

if __name__ == "__main__":
    main()
