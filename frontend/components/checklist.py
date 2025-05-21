from PyQt6.QtWidgets import QWidget

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..","..", "backend", "build"))
import db

class CheckList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainLayout = None
        self.mainWidget = None
        self.dailyTasks = ["B12", "Omega3", "Kreatin","Abwasch"]
        self.checkBoxes = []

    def handleToggle(self, checkbox, task, date):
        if checkbox.isChecked():
            db.update_page(date, task, None, True)
        else:
            db.update_page(date, task, None, False)

