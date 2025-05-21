from PyQt6.QtCore import Qt
from components.clickable_lable import ClickableLabel
from datetime import date


class DateLabel(ClickableLabel):
    def __init__(self, text='', page = None):
        super().__init__(text)
        self.page = page
        self.setText(text)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def mousePressEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            self.page.dayNavigator.currentDay = date.today()
            self.page.dayNavigator.updateDate()
            self.page.load()

