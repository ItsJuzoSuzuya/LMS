from components.day import Day
from components.task import Task

class Friday(Day):
    def __init__(self, date):
        super().__init__(date)
        self.name = "Friday"
        self.tasks = {}

        # Initialize the tasks for Friday
        self.tasks["programming"] = (Task("Programming", 45))
        self.tasks["rest"] = (Task("Rest", 15))
        self.tasks["piano"] = (Task("Piano", 30))
        self.tasks["chess"] = (Task("Chess", 30))
        self.tasks["japanese"] = (Task("Japanese", 30))

