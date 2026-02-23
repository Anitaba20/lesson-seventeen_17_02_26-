from task import Task

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task_name):
        task = Task(task_name)
        self.model.add_task(task)
        self.view.added_task(task)

    def finish_task(self, task_name):
        task = self.model.get_task(task_name)
        if task is None:
            self.view.task_not_found(task_name)
        else :
            task.completed = True
            self.view.finished_task(task)

    def finished_tasks(self):
        tasks = self.model.get_finished_tasks()
        self.view.display_finished_tasks(tasks)

    def delete_task(self, task_name):
        task = self.model.get_task(task_name)
        if task is None:
            self.view.task_not_found(task_name)
        else:
            self.model.remove_task(task)
            self.view.removed_task(task)

    def display_tasks(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)

