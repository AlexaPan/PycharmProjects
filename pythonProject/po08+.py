import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime


# Функция для добавления задачи
def add_task():
    task = task_entry.get()
    deadline = deadline_entry.get()
    if task:
        if deadline:
            task_listBox.insert(tk.END, f"{task} (Срок: {deadline})")
        else:
            task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)


# Функция для удаления задачи
def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)


# Функция для отметки задачи
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, foreground="lime green")


# Функция для редактирования задачи
def edit_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        current_task = task_listBox.get(selected_task)
        if ' (Срок:' in current_task:
            task_text, deadline = current_task.split(' (Срок:')
            deadline = deadline.rstrip(')')
        else:
            task_text, deadline = current_task, ''

        new_task = simpledialog.askstring("Редактировать задачу", "Введите новую задачу:", initialvalue=task_text)
        new_deadline = simpledialog.askstring("Редактировать срок", "Введите новый срок выполнения:",
                                              initialvalue=deadline)

        if new_task:
            if new_deadline:
                task_listBox.delete(selected_task)
                task_listBox.insert(selected_task, f"{new_task} (Срок: {new_deadline})")
            else:
                task_listBox.delete(selected_task)
                task_listBox.insert(selected_task, new_task)


# Создание основного окна
root = tk.Tk()
root.title("Список задач")
root.configure(background="azure3")

# Метка для ввода задачи
text1 = tk.Label(root, text="Введите вашу задачу:", bg="azure3")
text1.pack(pady=5)

# Поле для ввода задачи
task_entry = tk.Entry(root, width=30, bg="azure4")
task_entry.pack(pady=10)

# Метка для ввода срока выполнения
text2 = tk.Label(root, text="Введите срок выполнения (необязательно):", bg="azure3")
text2.pack(pady=5)

# Поле для ввода срока выполнения
deadline_entry = tk.Entry(root, width=30, bg="azure4")
deadline_entry.pack(pady=10)

# Кнопки
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

edit_button = tk.Button(root, text="Редактировать задачу", command=edit_task)
edit_button.pack(pady=5)

text3 = tk.Label(root, text="Список задач:", bg="azure3")
text3.pack(pady=5)

# Список задач
task_listBox = tk.Listbox(root, height=10, width=50, bg="azure4")
task_listBox.pack(pady=10)

root.mainloop()