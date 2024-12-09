# import tkinter as tk
# from tkinter import messagebox
# from tkinter import simpledialog
# from datetime import datetime
#
# class Task:
#     def __init__(self, title, start_date, due_date, progress=0):
#         self.title = title
#         self.start_date = start_date
#         self.due_date = due_date
#         self.progress = progress
#         self.subtasks = []
#
#     def add_subtask(self, subtask):
#         self.subtasks.append(subtask)
#
#     def mark_complete(self):
#         self.progress = 100
#
# class TaskManagerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Task Manager")
#
#         # Список задач
#         self.tasks = []
#
#         # Создание интерфейса
#         self.task_listbox = tk.Listbox(root, width=50, height=15)
#         self.task_listbox.pack(pady=20)
#
#         self.add_task_button = tk.Button(root, text="Добавить задачу", command=self.add_task)
#         self.add_task_button.pack(pady=5)
#
#         self.mark_complete_button = tk.Button(root, text="Отметить как выполненную", command=self.mark_complete)
#         self.mark_complete_button.pack(pady=5)
#
#         self.remove_task_button = tk.Button(root, text="Удалить задачу", command=self.remove_task)
#         self.remove_task_button.pack(pady=5)
#
#         self.add_subtask_button = tk.Button(root, text="Добавить подзадачу", command=self.add_subtask)
#         self.add_subtask_button.pack(pady=5)
#
#     def add_task(self):
#         title = simpledialog.askstring("Заголовок задачи", "Введите заголовок задачи:")
#         start_date = simpledialog.askstring("Дата начала", "Введите дату начала (YYYY-MM-DD):")
#         due_date = simpledialog.askstring("Дата выполнения", "Введите дату выполнения (YYYY-MM-DD):")
#
#         if title and start_date and due_date:
#             try:
#                 start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
#                 due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
#                 new_task = Task(title, start_date_obj, due_date_obj)
#                 self.tasks.append(new_task)
#                 self.update_task_listbox()
#             except ValueError:
#                 messagebox.showerror("Ошибка", "Неверный формат даты. Используйте YYYY-MM-DD.")
#
#     def mark_complete(self):
#         selected_index = self.task_listbox.curselection()
#         if selected_index:
#             task = self.tasks[selected_index[0]]
#             task.mark_complete()
#             self.update_task_listbox()
#         else:
#             messagebox.showwarning("Предупреждение", "Сначала выберите задачу.")
#
#     def remove_task(self):
#         selected_index = self.task_listbox.curselection()
#         if selected_index:
#             del self.tasks[selected_index[0]]
#             self.update_task_listbox()
#         else:
#             messagebox.showwarning("Предупреждение", "Сначала выберите задачу.")
#
#     def add_subtask(self):
#         selected_index = self.task_listbox.curselection()
#         if selected_index:
#             subtask_title = simpledialog.askstring("Заголовок подзадачи", "Введите заголовок подзадачи:")
#             if subtask_title:
#                 subtask = Task(subtask_title, None, None)
#                 self.tasks[selected_index[0]].add_subtask(subtask)
#                 self.update_task_listbox()
#         else:
#             messagebox.showwarning("Предупреждение", "Сначала выберите задачу.")
#
#     def update_task_listbox(self):
#         self.task_listbox.delete(0, tk.END)
#         for task in self.tasks:
#             task_info = f"{task.title} | Начало: {task.start_date.strftime('%Y-%m-%d')} | Завершение: {task.due_date.strftime('%Y-%m-%d')} | Прогресс: {task.progress}%"
#             self.task_listbox.insert(tk.END, task_info)
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TaskManagerApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

# Список задач
tasks = []

# Функция для добавления задачи
def add_task():
    title = simpledialog.askstring("Заголовок задачи", "Введите заголовок задачи:")
    start_date = simpledialog.askstring("Дата начала", "Введите дату начала (YYYY-MM-DD):")
    due_date = simpledialog.askstring("Дата выполнения", "Введите дату выполнения (YYYY-MM-DD):")

    if title and start_date and due_date:
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
            new_task = {
                'title': title,
                'start_date': start_date_obj,
                'due_date': due_date_obj,
                'progress': 0,
                'subtasks': []
            }
            tasks.append(new_task)
            update_task_listbox()
        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат даты. Используйте YYYY-MM-DD.")

# Функция для редактирования задачи
def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task = tasks[selected_index[0]]
        new_title = simpledialog.askstring("Редактировать заголовок", "Введите новый заголовок задачи:", initialvalue=task['title'])
        new_start_date = simpledialog.askstring("Редактировать дату начала", "Введите новую дату начала (YYYY-MM-DD):", initialvalue=task['start_date'].strftime('%Y-%m-%d'))
        new_due_date = simpledialog.askstring("Редактировать дату выполнения", "Введите новую дату выполнения (YYYY-MM-DD):", initialvalue=task['due_date'].strftime('%Y-%m-%d'))

        if new_title and new_start_date and new_due_date:
            try:
                new_start_date_obj = datetime.strptime(new_start_date, '%Y-%m-%d')
                new_due_date_obj = datetime.strptime(new_due_date, '%Y-%m-%d')
                task['title'] = new_title
                task['start_date'] = new_start_date_obj
                task['due_date'] = new_due_date_obj
                update_task_listbox()
            except ValueError:
                messagebox.showerror("Ошибка", "Неверный формат даты. Используйте YYYY-MM-DD.")
    else:
        messagebox.showwarning("Предупреждение", "Сначала выберите задачу.")
# Функция для отметки задачи как выполненной
def mark_complete():
    selected_index = task_listbox.curselection()
    if selected_index:
        task = tasks[selected_index[0]]
        task['progress'] = 100
        update_task_listbox()
    else:
        messagebox.showwarning("Предупреждение", "Сначала выберите задачу.")

# Функция для удаления задачи
def remove_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        del tasks[selected_index[0]]
        update_task_listbox()
    else:
        messagebox.showwarning("Предупреждение", "Сначала выберите задачу.")

# Функция для добавления подзадачи
def add_subtask():
    selected_index = task_listbox.curselection()
    if selected_index:
        subtask_title = simpledialog.askstring("Заголовок подзадачи", "Введите заголовок подзадачи:")
        if subtask_title:
            subtask = {
                'title': subtask_title,
                'progress': 0
            }
            tasks[selected_index[0]]['subtasks'].append(subtask)
            update_task_listbox()
    else:
        messagebox.showwarning("Предупреждение", "Сначала выберите задачу.")

# Функция для обновления списка задач в Listbox
def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_info = f"{task['title']} | Начало: {task['start_date'].strftime('%Y-%m-%d')} | Завершение: {task['due_date'].strftime('%Y-%m-%d')} | Прогресс: {task['progress']}%"
        task_listbox.insert(tk.END, task_info)

# Создание интерфейса
root = tk.Tk()
root.title("Task Manager")

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=20)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

edit_task_button = tk.Button(root, text="Редактировать задачу", command=edit_task)
edit_task_button.pack(pady=5)

mark_complete_button = tk.Button(root, text="Отметить как выполненную", command=mark_complete)
mark_complete_button.pack(pady=5)

remove_task_button = tk.Button(root, text="Удалить задачу", command=remove_task)
remove_task_button.pack(pady=5)

add_subtask_button = tk.Button(root, text="Добавить подзадачу", command=add_subtask)
add_subtask_button.pack(pady=5)

# Запуск главного цикла
root.mainloop()
