class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    def get_finished_tasks(self):
        finished_task = []
        for task in self.tasks:
            if task.completed:
                finished_task.append(task)
        return finished_task