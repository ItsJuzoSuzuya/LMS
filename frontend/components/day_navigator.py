from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QWidget
from datetime import date, timedelta

from components.date_label import DateLabel

class DayNavigator(QWidget):
    def __init__(self, page):
        super().__init__()
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        self.currentDay = date.today() 

        self.previousDayButton = QPushButton("<")
        self.previousDayButton.clicked.connect(self.previousDay)
        self.previousDayButton.setFixedSize(40, 30)
        self.previousDayButton.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.nextDayButton = QPushButton(">")
        self.nextDayButton.clicked.connect(self.nextDay)
        self.nextDayButton.setFixedSize(40, 30)
        self.nextDayButton.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.dateLabel = DateLabel(self.currentDay.strftime("%B %d"), page)
        self.dateLabel.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.dateLabel.setMinimumSize(100, 30)

        layout.addWidget(self.previousDayButton)
        layout.addWidget(self.dateLabel)
        layout.addWidget(self.nextDayButton)

        self.setLayout(layout)
        self.setFixedSize(200, 50)

        self.page = page 


    def previousDay(self):
        self.currentDay -= timedelta(days=1)
        self.updateDate()

    def nextDay(self):
        self.currentDay += timedelta(days=1)
        self.updateDate()

    def updateDate(self):
        self.dateLabel.setText(self.currentDay.strftime("%B %d"))
        self.page.load()








