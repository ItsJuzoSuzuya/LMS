from PyQt6.QtWidgets import QApplication

from components.task import Task
from pages.tasks import TaskPage


app = QApplication([])

TaskPage = TaskPage()
TaskPage.show()

app.exec()

TaskPage.dropEvent = TaskPage.dropEvent
TaskPage.taskThread.join()
