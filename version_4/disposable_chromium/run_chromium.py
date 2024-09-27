# Imports the modules necessary for GUI development
import time
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Provides access to the web - opens "localhost:3000"
from PyQt5.QtWebEngineWidgets import *

class RunDisposableChromium():
   def __init__(self):
      os.system("docker-compose -f docker-compose.yml up -d")
      
      # Prevents the program from crashing (from loading too early)
      time.sleep(3)

      # Builds the program window
      self.window = QWidget()

      # Sets the window title unique to the program's purpose
      self.window.setWindowTitle("Disposable Chromium")

      # Widget that opens the web
      self.browser = QWebEngineView()

      # Places the widget in the window
      self.layout = QVBoxLayout()
      self.layout.addWidget(self.browser)

      # Sets the program route to the webtop
      self.browser.setUrl(QUrl("http://localhost:3000/"))

      # Displays the program window
      self.window.setLayout(self.layout)
      self.window.show()

      app.aboutToQuit.connect(self.closeEvent)
      
   def closeEvent(self):
      os.system("docker-compose -f docker-compose.yml down")

# Runs the window
app = QApplication([]) 
window = RunDisposableChromium()
app.exec()
