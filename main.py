from taskController import TaskController
from taskModel import TaskModel
from taskView import TaskView


model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

controller.add_task("Uloha 1")
controller.add_task("Uloha 2")
controller.add_task("Uloha 3")

print("------")

controller.finish_task("Uloha 2")
controller.finish_task("Uloha 3")

controller.finished_tasks()

controller.delete_task("Uloha 1")