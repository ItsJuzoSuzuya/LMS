from PyQt6.QtWidgets import QPushButton


class StartButton(QPushButton):
    def __init__(self, duration: str):
        super().__init__("Start")
        self.setCheckable(True)
        self.duration = duration
        self.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 5px;")
        self.setFixedSize(100, 40)


