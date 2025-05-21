from components.day import Day
from components.task import Task


class Wednesday(Day):
    def __init__(self, date):
        super().__init__(date)
        self.name = "Wednesday"
        self.tasks = {}

        # Initialize the tasks for Wednesday
        self.tasks["programming"] = (Task("Programming", 45))
        self.tasks["rest"] = (Task("Rest", 15))
        self.tasks["japanese"] = (Task("Japanese", 30))
        self.tasks["piano"] = (Task("Piano", 30))
        self.tasks["chess"] = (Task("Chess", 30))

