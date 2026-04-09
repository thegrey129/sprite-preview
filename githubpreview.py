# Authors: Dominick Panopoulos, Jace Hansen
# Github link

import os
import sys

from PyQt6.QtWidgets import *

from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import Qt, QTimer

class SpritePreviewer(QMainWindow):
    def __init__(self):
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

        self.image_label = QLabel("No Sprite Loaded")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedHeight(250)

        self.fps_slider = QSlider(Qt.Orientation.Vertical)
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(100)
        self.fps_slider.setValue(1)

        self.fps_text_label = QLabel("Frames per second")
        self.fps_value_label = QLabel("1")
        self.fps_value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.start_stop_button = QPushButton("Start")

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.image_label)
        top_layout.addWidget(self.fps_slider)

        fps_layout = QVBoxLayout()
        top_layout.addWidget(self.fps_text_label)
        fps_layout.addWidget(self.fps_value_label)

        self.main_layout.addLayout(top_layout)
        self.main_layout.addLayout(fps_layout)
        self.main_layout.addWidget(self.start_stop_button)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpritePreviewer()
    window.show()
    sys.exit(app.exec())
