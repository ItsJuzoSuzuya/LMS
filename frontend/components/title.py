from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel


class Title():
    def __init__(self):
        font = QFont()
        font.setPointSize(20)  
        label = QLabel("Nick's Life")
        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        label.setMargin(20)
        label.setFont(font)
        self.label = label

