#!/usr/bin/env python3
import sys, json, os, subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, pyqtSlot, QObject
from PyQt6.QtGui import QColor
from PyQt6.QtWebChannel import QWebChannel
from web.backend import Backend

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("TV Launcher")
window.showFullScreen()

view = QWebEngineView()
view.setStyleSheet("background-color: #121212;") # dark gray / black
view.page().setBackgroundColor(QColor("#121212"))
window.setCentralWidget(view)

# Web channel for JS-Python communication
channel = QWebChannel()
backend = Backend()
channel.registerObject("backend", backend)
view.page().setWebChannel(channel)

# Load local HTML
html_path = os.path.join(os.path.dirname(__file__), "web/index.html")
view.load(QUrl.fromLocalFile(html_path))

sys.exit(app.exec())

