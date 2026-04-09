# Authors: Dominick Panopoulos, Jace Hansen
# Github link

import os
import sys

from PyQt6.QtWidgets import *

from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import Qt, QTimer

class SpritePreviewer(QMainWindow):
    def __init__(self, image):
        super().__init__()

        self.setWindowTitle("Sprite Previewer")
        self.resize(400,500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        self.pause_action = QAction("Pause", self)
        self.exit_action = QAction("Exit", self)

        file_menu.addAction(self.pause_action)
        file_menu.addAction(self.exit_action)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpritePreviewer()
    window.show()
    sys.exit(app.exec())
