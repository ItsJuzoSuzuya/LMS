from components.day import Day
from components.task import Task


class Tuesday(Day):
    def __init__(self, date):
        super().__init__(date)
        self.name = "Tuesday"
        self.tasks = {}

        # Initialize the tasks for Tuesday
        self.tasks["programming"] = (Task("Programming", 45))
        self.tasks["rest"] = (Task("Rest", 15))
        self.tasks["piano"] = (Task("Piano", 30))
        self.tasks["chess"] = (Task("Chess", 30))
        self.tasks["japanese"] = (Task("Japanese", 30))


