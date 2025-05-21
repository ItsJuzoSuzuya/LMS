from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel


class ClickableLabel(QLabel):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
