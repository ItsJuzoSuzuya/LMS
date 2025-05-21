from components.day import Day
from components.task import Task


class Sunday(Day):
    def __init__(self, date):
        super().__init__(date)
        self.name = "Sunday"
        self.tasks = {}

        # Initialize the tasks for Sunday
        self.tasks["programming"] = (Task("Programming", 60))
        self.tasks["rest1"] = (Task("Rest", 15))
        self.tasks["piano"] = (Task("Piano", 45))
        self.tasks["japanese"] = (Task("Japanese", 45))
        self.tasks["rest2"] = (Task("Rest", 120))
        self.tasks["chess"] = (Task("Chess", 60))
        self.tasks["rest3"] = (Task("Rest", 15))
        self.tasks["free"] = (Task("Free", 0))

