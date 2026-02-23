class TaskView:

    def display_tasks(self, tasks):
        print(tasks)

    def added_task(self, task):
        print(f"Uloha s nazvom {task.name} bola vlozena do systemu")

    def task_not_found(self, task_name):
        print(f"Uloha s nazvom {task_name} sa v systeme nenachadza")

    def finished_task(self, task):
        print(f"Uloha s nazvom {task.name} bola dokoncena")

    def display_finished_tasks(self, tasks):
        print("Dokoncene ulohy:")
        for task in tasks:
            print(f"- {task.name}")

