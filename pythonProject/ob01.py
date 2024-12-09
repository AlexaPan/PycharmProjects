# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, title_task, date_task = None):
        self.title_task = title_task
        if date_task is not None: self.date_task = date_task
        else: self.date_task = "Didn't set deadline"
        self.status_task = False

    def task_complete(self):
        self.status_task = True

    def __str__(self):
        return f"Task: {self.title_task}. Deadline: {self.date_task}. Status: {self.status_task}"


class TackManager():

    def __init__(self):
        self.list_task = []

    # add task
    def add_task(self, title_task, date_task):
        task = Task(title_task, date_task)
        self.list_task.append(task)
        print(f"Task '{task}' added")

    #delete task
    def del_task(self, title_task):
        for task in self.list_task:
            if task.title_task == title_task:
                self.list_task.remove(task)
                print(f"Task '{task}' deleted")
                return
        print(f"Task '{title_task}' not found")


    def mark_task(self, title_task):
        for task in self.list_task:
            if task.title_task == title_task:
                task.task_complete()
                print(f"Task '{task}' marked as complete")
                return
        print(f"Task '{title_task}' not found")


    def print_task(self):
        count = 0
        print("Current tasks:")
        for task in self.list_task:
            if task.status_task == False:
                print(task)
                count += 1
        if count == 0:
            print("No current tasks")


if __name__ == "__main__":
    task_manager = TackManager()
    task_manager.add_task("Task 1", "2023-01-01")
    task_manager.add_task("Task 2", "2023-01-02")
    task_manager.add_task("Task 3", "2023-01-03")
    task_manager.print_task()
    task_manager.mark_task("Task 1")
    task_manager.print_task()
    task_manager.del_task("Task 2")
    task_manager.print_task()


