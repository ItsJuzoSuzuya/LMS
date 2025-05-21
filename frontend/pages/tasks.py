from datetime import date, datetime, time
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QCheckBox, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget
from components.title import Title
from components.day_navigator import DayNavigator
from components.task import Task
from threading import Thread, Event

from components.days.friday import Friday
from components.days.monday import Monday
from components.days.saturday import Saturday
from components.days.sunday import Sunday
from components.days.thursday import Thursday
from components.days.tuesday import Tuesday
from components.days.wednesday import Wednesday

import sys
import os

from components.checklist import CheckList
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..", "backend", "build"))

import db

day_classes = {
    0: Monday,
    1: Tuesday,
    2: Wednesday,
    3: Thursday,
    4: Friday,
    5: Saturday,
    6: Sunday
}

def getTasks(date) -> dict[str, Task]:
    weekday_index = date.weekday()
    day_class = day_classes.get(weekday_index)
    if not day_class:
        raise ValueError("Invalid weekday")
    return day_class(date.strftime("%A")).tasks

class TaskPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dayNavigator = DayNavigator(self)
        self.checkList = CheckList()
        self.load()

    def load(self) -> None:
        day = self.dayNavigator.dateLabel.text()
        page = db.get_page(day)

        self.setUp()
        self.tasks = getTasks(self.dayNavigator.currentDay)
        self.activeTask = None
        self.layouts = list[QHBoxLayout]()

        if page:
            self._load_existing_tasks(page, day)
            self._load_checklist_tasks(page, day)
        elif day == date.today().strftime("%B %d"):
            self._initialize_today(day)
            self._load_default_checklist_tasks()
        else:
            self._load_default_tasks(day)
            self._load_default_checklist_tasks()
        
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)


    def setUp(self) -> None:
        # Main Layout
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Title 
        title = Title()
        self.mainLayout.addWidget(title.label)
        self.mainLayout.addWidget(self.dayNavigator, alignment=Qt.AlignmentFlag.AlignHCenter)

    def _create_task_layout(self, name: str, task: Task, day: str) -> None:
            task.startButton.clicked.connect(lambda _, name=name: self.handleToggle(name))
            layout = QHBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            task.addToLayout(layout, day)
            self.mainLayout.addLayout(layout)
            self.layouts.append(layout)

    def _load_existing_tasks(self, page: dict, day: str) -> None:
            for name, task in self.tasks.items():
                if name in page:
                    task.duration = int(page[name])
                    task.timeLable.setText(f"{page[name]} min")
                self._create_task_layout(name, task, day)

    def _load_checklist_tasks(self, page: dict, day: str) -> None:
            for task in self.checkList.dailyTasks:
                checkBox = QCheckBox(task)
                checkBox.setStyleSheet("""
                    QCheckBox::indicator { width: 30; height: 30; }
                    font-size: 16px; padding: 10px; border-radius: 5px;
                    font-weight: bold; color: #000; background-color: #FFF;
                    margin: 5px; text-align: left;
                """)
                checkBox.setFixedWidth(180)
                checkBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
                checkBox.clicked.connect(
                    lambda _, cb=checkBox, t=task: self.checkList.handleToggle(cb, t, day)
                )

                isChecked = page.get(task.lower()) == "t"
                checkBox.setChecked(isChecked)

                self.mainLayout.addWidget(checkBox, alignment=Qt.AlignmentFlag.AlignRight)

    def _initialize_today(self, day: str) -> None:
            db.add_page(
                day,
                self.tasks["piano"].duration,
                self.tasks["chess"].duration,
                self.tasks["japanese"].duration,
                self.tasks["programming"].duration
            )
            for name, task in self.tasks.items():
                self._create_task_layout(name, task, day)

    def _load_default_tasks(self, day: str) -> None:
        for name, task in self.tasks.items():
            self._create_task_layout(name, task, day)

    def _load_default_checklist_tasks(self) -> None:
        for task in self.checkList.dailyTasks:
            checkBox = QCheckBox(task)
            checkBox.setStyleSheet("""
                QCheckBox::indicator { width: 30; height: 30; }
                font-size: 16px; padding: 10px; border-radius: 5px;
                font-weight: bold; color: #000; background-color: #FFF;
                margin: 5px; text-align: left;
            """)
            checkBox.setFixedWidth(180)
            checkBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
            checkBox.setCheckable(False)
            self.mainLayout.addWidget(checkBox, alignment=Qt.AlignmentFlag.AlignRight)


    def handleToggle(self, name) -> None:
        task = self.tasks[name]
        clicked_button = task.startButton

        if self.activeTask is None:
            self.activeTask = task
            task.status.setText("Running")
            task.status.setStyleSheet("background-color: #FF9800; color: white; font-size: 16px; padding: 10px; border-radius: 5px;")
            clicked_button.setText("Stop")
            self.stopEvent = Event()
            self.taskThread = Thread(target=task.updateTime, args=(self.stopEvent,))
            self.taskThread.start()
        elif self.activeTask == task:
            self.activeTask = None
            task.status.setText("")
            task.status.setStyleSheet(None)
            clicked_button.setText("Start")

            self.stopEvent.set()
            self.taskThread.join(timeout=1)
            db.update_page(self.dayNavigator.dateLabel.text(), task.name, task.duration)















