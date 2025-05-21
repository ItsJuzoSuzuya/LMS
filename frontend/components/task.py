from datetime import date
import time
from os import wait
from PyQt6.QtGui import QFont, QFontMetrics
from PyQt6.QtWidgets import QLabel, QWidget

from components.start_button import StartButton


class Task(QWidget):
    def __init__(self, name: str, duration: int):
        super().__init__()
        font = QFont("Arial", 14)
        self.name = name
        self.label = QLabel(name)
        self.label.setFont(font)
        self.label.setMinimumWidth(175)

        self.duration = duration

        time = str(duration) + " min"

        font = QFont("Arial", 14)
        self.timeLable = QLabel(time)
        self.timeLable .setFont(font)
        self.timeLable .setStyleSheet("color: #A9A9A9;")
        self.timeLable .setMinimumWidth(75)

        font = QFont("Arial", 16)
        self.status = QLabel()
        self.status.setFont(font)
        
        metrics = QFontMetrics(font)
        placeHolderText = "Running"
        width = metrics.horizontalAdvance(placeHolderText) + 10
        height = metrics.height() + 10
        self.status.setFixedSize(width, height)

        self.startButton = StartButton(time)
        self.startButton.setCheckable(True)

        self.active = False

    def addToLayout(self, layout, day):
        layout.addWidget(self.label)
        layout.addWidget(self.timeLable)
        layout.addWidget(self.status)
        if day == date.today().strftime("%B %d"):
            layout.addWidget(self.startButton)

    def updateTime(self, stopEvent):
        while not stopEvent.is_set():
            if stopEvent.wait(timeout=60):
                break
            self.duration -= 1
            self.timeLable.setText(str(self.duration) + " min")
            if self.duration == 0:
                stopEvent.set()



