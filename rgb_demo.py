# This Python file uses the following encoding: utf-8
# rgb_demo.py
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from rgb_slider import RGBSlider, style_sheet

class ImageDemo(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setMinimumSize(225, 300)
        self.setWindowTitle("9.3 - Custom Widget")

        # Load image
        image = QImage("images/chameleon.jpg")

        # Create instance of RGB slider widget and pass the image as an argument to RGBSlider
        rgb_slider = RGBSlider(image)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignTop)
        image_label.setPixmap(QPixmap().fromImage(image))

        # Reimplement the label's mousePressEvent
        image_label.mousePressEvent = rgb_slider.getPixelValues

        h_box = QHBoxLayout()
        h_box.addWidget(rgb_slider)
        h_box.addWidget(image_label)

        self.setLayout(h_box)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Use the style_sheet from rgb_slider
    app.setStyleSheet(style_sheet)
    window = ImageDemo()
    sys.exit(app.exec_())
