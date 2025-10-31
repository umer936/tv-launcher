import requests
from bs4 import BeautifulSoup
import re
import os
import sys
import urllib.parse

def search_app_package(app_name):
    """Search Google Play and return the first matching package name."""
    query = urllib.parse.quote_plus(app_name)
    url = f"https://play.google.com/store/search?q={query}&c=apps&hl=en&gl=US"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/117.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Google Play often wraps app links like /store/apps/details?id=com.xxx
    link = soup.select_one('a[href^="/store/apps/details?id="]')
    if not link:
        raise Exception(f"No app found for '{app_name}'")

    match = re.search(r"id=([a-zA-Z0-9._]+)", link["href"])
    if not match:
        raise Exception("Failed to extract package name.")

    return match.group(1)

def download_high_res_icon(package_name, app_name=None):
    """Download the highest-resolution icon from the app page."""
    url = f"https://play.google.com/store/apps/details?id={package_name}&hl=en&gl=US"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/117.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    meta_tag = soup.find("meta", property="og:image")
    if not meta_tag or not meta_tag.get("content"):
        raise Exception("High-res icon info not found.")

    icon_url = meta_tag["content"]

    if app_name is None:
        app_name = package_name

    save_path = os.path.join(os.getcwd(), "icons", f"{app_name}.png")

    icon_response = requests.get(icon_url)
    icon_response.raise_for_status()

    with open(save_path, "wb") as f:
        f.write(icon_response.content)

    print(f"✅ Icon saved to: {save_path}")
    return save_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python download_play_icon.py <app name>")
        sys.exit(1)

    app_name = " ".join(sys.argv[1:]).strip()
    print(f"Searching for app: {app_name}")

    try:
        pkg = search_app_package(app_name)
        print(f"Found package: {pkg}")
        download_high_res_icon(pkg, app_name)
    except Exception as e:
        print("❌ Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
