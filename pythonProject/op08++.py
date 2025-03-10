import tkinter as tk
from asyncio import all_tasks
from tkinter import simpledialog
from datetime import datetime
from tkinter import messagebox

list_of_listbox = []

def add_task():
    task = task_entry.get()
    deadline = deadline_entry.get()
    if deadline:
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid deadline format. Please use YYYY-MM-DD format.")
            return
    if task:
        count_listbox = task_ListBox.size()+1
        if deadline:
            task_ListBox.insert(tk.END, f"{count_listbox}."
                                        f" {task} (Task deadline: {deadline.strftime('%Y-%m-%d')})")
            list_of_listbox.append(f"{task} (Task deadline: {deadline.strftime('%Y-%m-%d')})")
        else:
            task_ListBox.insert(tk.END, f"{count_listbox}. {task})")
            list_of_listbox.append(f"{task}")
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)

def mark_task():
    selected_task = task_ListBox.curselection()
    if selected_task:
        task_ListBox.itemconfig(selected_task, foreground="Red")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

def delete_task():
    selected_task = task_ListBox.curselection()
    if selected_task:
        task_ListBox.delete(selected_task)
        list_of_listbox.pop(selected_task[0])
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task_listbox():
    selection_task = task_ListBox.curselection()
    if selection_task:
        current_task = task_ListBox.get(selection_task)

        new_title = simpledialog.askstring("Update Task", "Enter the new task:",
                                           parent=root, initialvalue=current_task)
        if "(Task deadline:" in new_title:
            title_task, deadline_task = new_title.split("(Task deadline: ")
            deadline_task = deadline_task.rstrip(")")
            print(deadline_task)
            if deadline_task is not None:
                try:
                    datetime.strptime(deadline_task, "%Y-%m-%d")
                except ValueError:
                    messagebox.showerror("Error", "Invalid deadline format. Please use YYYY-MM-DD format.")
                    return


        if new_title is not None:
            task_ListBox.delete(selection_task)
            list_of_listbox.pop(selection_task[0])
            task_ListBox.insert(selection_task, new_title)
            list_of_listbox.append(new_title)
            update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark to update.")

def update_listbox():
    task_ListBox.delete(0, tk.END)
    count = 1
    for task in list_of_listbox:
        task_ListBox.insert(tk.END, f"{count}. {task}")
        count += 1

root = tk.Tk()

root.title("Task Manager")
root.configure(bg="#f0f0f0")

text_add = tk.Label(root, text = "Enter your task:")
text_add.pack(pady=5)

task_entry = tk.Entry(root, width=100)
task_entry.pack(pady=5)

text_date = tk.Label(root, text = "Enter deadline for the task (YYYY-MM-DD) or leave blank:")
text_date.pack(pady=5)

deadline_entry = tk.Entry(root, width=100)
deadline_entry.pack(pady=5)

bottom_add = tk.Button(root, text="Add Task", command=add_task)
bottom_add.pack(fill=tk.X, pady=5)

bottom_mark_task = tk.Button(root, text="Mark Task as Complete", command=mark_task)
bottom_mark_task.pack(fill=tk.X, pady=5)

bottom_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
bottom_delete_task.pack(fill=tk.X, pady=5)

bottom_update_task = tk.Button(root, text="Update Task", command=update_task_listbox)
bottom_update_task.pack(fill=tk.X, pady=5)

text_list = tk.Label(root, text="Task List:")
text_list.pack(pady=5)

task_ListBox = tk.Listbox(root, width=100, height=15)
task_ListBox.pack(fill=tk.X, pady=5)

root.mainloop()