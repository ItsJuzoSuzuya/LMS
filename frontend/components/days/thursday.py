from components.day import Day
from components.task import Task

class Thursday(Day):
    def __init__(self, date):
        super().__init__(date)
        self.name = "Thursday"
        self.tasks = {}

        # Initialize the tasks for Thursday
        self.tasks["programming"] = (Task("Programming", 45))
        self.tasks["rest1"] = (Task("Rest", 15))
        self.tasks["piano"] = (Task("Piano", 30))
        self.tasks["japanese"] = (Task("Japanese", 30))
        self.tasks["chess"] = (Task("Chess", 30))
        self.tasks["rest2"] = (Task("Rest", 30))
        self.tasks["free"] = (Task("Free", 0))
