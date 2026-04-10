# Authors: Dominick Panopoulos, Jace Hansen
# https://github.com/thegrey129/sprite-preview

# sprite previewer
# needs a sprites folder for the images to run properly
# github didn't allow to add folder, just images

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

        fps_layout = QHBoxLayout()
        fps_layout.addWidget(self.fps_text_label)
        fps_layout.addWidget(self.fps_value_label)

        self.main_layout.addLayout(top_layout)
        self.main_layout.addLayout(fps_layout)
        self.main_layout.addWidget(self.start_stop_button)

        self.sprite_files = []
        self.current_index = 0
        self.timer = QTimer()
        self.is_running = False

        self.timer.timeout.connect(self.next_frame)
        self.fps_slider.valueChanged.connect(self.update_fps)

        self.start_stop_button.clicked.connect(self.toggle_animation)

        self.pause_action.triggered.connect(self.pause_animation)
        self.exit_action.triggered.connect(self.close)

        self.load_sprites()

    def load_sprites(self):
        folder = "sprites"

        if not os.path.exists(folder):
            self.image_label.setText("No Sprite Loaded")
            return

        files = os.listdir(folder)

        sprite_names = []
        for file in files:
            if file.endswith(".png") and file.startswith("sprite_"):
                sprite_names.append(file)

        sprite_names.sort()
        self.sprite_files = [os.path.join(folder, name) for name in sprite_names]

        if len(self.sprite_files) > 0:
            self.current_index = 0
            self.show_current_sprite()
        else:
            self.image_label.setText("No Sprite Loaded")

    def show_current_sprite(self):
        if len(self.sprite_files) == 0:
            return

        pixmap = QPixmap(self.sprite_files[self.current_index])

        if pixmap.isNull():
            self.image_label.setText("Image Failed to Load")
            return

        scaled = pixmap.scaled(
            200, 200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.FastTransformation
        )

        self.image_label.setPixmap(scaled)

    def next_frame(self):
        if len(self.sprite_files) == 0:
            return

        self.current_index += 1

        if self.current_index >= len(self.sprite_files):
            self.current_index = 0

        self.show_current_sprite()

    def update_fps(self):
        fps = self.fps_slider.value()
        self.fps_value_label.setText(str(fps))

        delay_ms = int(1000 / fps)

        if self.is_running:
            self.timer.start(delay_ms)

    def toggle_animation(self):
        if not self.is_running:
            fps = self.fps_slider.value()
            delay_ms = int(1000 / fps)

            self.timer.start(delay_ms)
            self.start_stop_button.setText("Stop")
            self.is_running = True

        else:
            self.timer.stop()
            self.start_stop_button.setText("Start")
            self.is_running = False
    def pause_animation(self):
        self.timer.stop()
        self.is_running = False
        self.start_stop_button.setText("Start")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpritePreviewer()
    window.show()
    sys.exit(app.exec())