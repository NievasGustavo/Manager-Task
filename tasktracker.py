"""
    Agregar, actualizar y eliminar tareas
    Marcar una tarea como en progreso o realizada
    Listar todas las tareas
    Enumere todas las tareas que se realizan
    Enumere todas las tareas que no se han realizado
    Enumere todas las tareas que están en curso
 """
import json
import os 
import datetime
from classTask import Task
from formatterOutput import formatOutput
import cmd

__author__ = "Gustavo Nievas"

def binary_search(v: list[Task], elem_search: int) -> Task | None:
    elem = int(elem_search)
    izq, der = 0, len(v) - 1
    while izq <= der:
        med = (izq + der) // 2
        pivote = v[med]
        if pivote.id == elem:
            return pivote
        if pivote.id > elem:
            der = med - 1
        else:
            izq = med + 1
    return None


def getTasks() -> list[Task]:
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as f:
            json.dump([], f)
    try:
        with open("tasks.json", "r") as f:
            tasks_data = json.load(f)
            tasks = [Task.from_dict(task) for task in tasks_data]
    except json.JSONDecodeError:
        tasks = []
    return tasks


def addTask(tasks: list[Task], task: Task):
    tasks.append(task)
    with open("tasks.json", "w") as f:
        tasks_dict = [t.toJson() for t in tasks]
        json.dump(tasks_dict, f, indent=1)
    
    print(f"Task added successfully (ID: {task.id})")



def updateTask(tasks: list[Task], id_task: int, description: str):
    task = binary_search(tasks, id_task)
    if task is None:
        print("Task not found")
        return

    task.description = description
    task.updatedAt = datetime.datetime.now().strftime("%H:%M %d-%m-%Y")

    with open("tasks.json", "w") as f:
        tasks_dict = [t.toJson() for t in tasks]
        json.dump(tasks_dict, f, indent=1)


def deleteTask(tasks: list[Task], id_task: int):
    task = binary_search(tasks, id_task)
    if task is None:
        print("Task not found")
        return
    tasks.remove(task)

    with open("tasks.json", "w") as f:
        tasks_dict = [t.toJson() for t in tasks]
        json.dump(tasks_dict, f, indent=1)


def markTaskAsInProgress(tasks: list[Task], id_task: int):
    task = binary_search(tasks, id_task)
    if task is None:
        print("Task not found")
        return
    task.status = "in-progress"
    task.updatedAt = datetime.datetime.now().strftime("%H:%M %d-%m-%Y")
    with open("tasks.json", "w") as f:
        tasks_dict = [t.toJson() for t in tasks]
        json.dump(tasks_dict, f, indent=1)

def markTaskAsDone(tasks: list[Task], id_task: int):
    task = binary_search(tasks, id_task)
    if task is None:
        print("Task not found")
        return
    task.status = "done"
    task.updatedAt = datetime.datetime.now().strftime("%H:%M %d-%m-%Y")
    with open("tasks.json", "w") as f:
        tasks_dict = [t.toJson() for t in tasks]
        json.dump(tasks_dict, f, indent=1)


def listTasks(tasks: list[Task]):
    if not tasks:
        print("No tasks found")
    else:
        formatOutput(tasks)

def listTasksByStatus(tasks: list[Task], status: str):
    tasks = [t for t in tasks if t.status == status]
    formatOutput(tasks)

def validatorId(id_task) -> bool:
    if not id_task.isdigit() or int(id_task) < 1:
        print("Invalid ID")
        return False
    return True

class TaskCLI(cmd.Cmd):
    intro = 'Welcome to the Task Tracker CLI. Type "help" to see the available commands.'
    prompt = '(task-cli) '

    def __init__(self):
        super().__init__()
        self.tasks = getTasks()

    def do_add(self, description):
        """Add a new task"""
        task = Task(len(self.tasks) + 1, description, "todo", datetime.datetime.now().strftime("%H:%M %d-%m-%Y"), datetime.datetime.now().strftime("%H:%M %d-%m-%Y"))
        addTask(self.tasks, task)

    def do_update(self, args):
        """Update a task (id description)"""
        args = args.split(" ", 1)
        if len(args) < 2:
            print("Must provide both ID and new description")
            return
        task_id, description = args
        if not validatorId(task_id):
            return
        updateTask(self.tasks, int(task_id), description)

    def do_delete(self, task_id):
        """Delete a task by ID"""
        if not validatorId(task_id):
            return
        deleteTask(self.tasks, int(task_id))

    def do_mark_in_progress(self, task_id):
        """Mark a task as in-progress by ID"""
        if not validatorId(task_id):
            return
        markTaskAsInProgress(self.tasks, int(task_id))

    def do_mark_done(self, task_id):
        """Mark a task as done by ID"""
        if not validatorId(task_id):
            return
        markTaskAsDone(self.tasks, int(task_id))

    def do_list(self, status=''):
        """List all tasks or filter by status (todo, in-progress, done)"""
        if not status:
            listTasks(self.tasks)
        else:
            listTasksByStatus(self.tasks, status)

    def do_exit(self, arg):
        """Exit the Task Tracker CLI"""
        print("Goodbye!")
        return True


if __name__ == '__main__':
    TaskCLI().cmdloop()