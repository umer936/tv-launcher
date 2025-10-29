#!/usr/bin/env python3
import sys, json, subprocess, os
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize

# Load apps
with open(os.path.join(os.path.dirname(__file__), "apps.json")) as f:
    apps = json.load(f)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("TV Launcher")
window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
window.showFullScreen()

layout = QGridLayout()
layout.setSpacing(20)
window.setLayout(layout)

# Add app buttons
for i, a in enumerate(apps):
    btn = QPushButton(a["name"])
    btn.setIcon(QIcon(a["icon"]))
    btn.setIconSize(QSize(128,128))
    btn.setFixedSize(200,200)
    btn.setStyleSheet("""
        QPushButton {
            font-size: 16px;
            background-color: #222;
            color: white;
            border-radius: 15px;
        }
        QPushButton:hover {
            background-color: #444;
        }
    """)
    btn.clicked.connect(lambda checked, cmd=a["command"]: subprocess.Popen(cmd, shell=True))
    layout.addWidget(btn, i//2, i%2)

sys.exit(app.exec())

