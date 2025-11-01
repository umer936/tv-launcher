import sys
import os
import subprocess
import json
from PyQt6.QtCore import QObject, pyqtSlot

class Backend(QObject):
    @pyqtSlot(str)
    def launch(self, app_name):
        apps_path = os.path.join(os.path.dirname(__file__), "../apps.json")
        with open(apps_path) as f:
            apps = json.load(f)
        for a in apps:
            if a["name"] == app_name:
                subprocess.Popen(a["command"], shell=True)
                return

    @pyqtSlot()
    def closeApp(self):
        sys.exit(0)

    @pyqtSlot(str)
    def wakePC(self, mac):
        try:
            subprocess.Popen(f"wakeonlan {mac}", shell=True)
        except Exception as e:
            print(f"WOL failed: {e}")

    @pyqtSlot()
    def shutdownPi(self):
        subprocess.Popen("sudo shutdown now", shell=True)

    @pyqtSlot()
    def rebootPi(self):
        subprocess.Popen("sudo reboot", shell=True)

