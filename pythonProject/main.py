import tkinter as tk

def button_click(button_id):
    print(f"Button {button_id} clicked")

root = tk.Tk()
root.title("Auto-Resizing Buttons")

# Создаем кнопки
button1 = tk.Button(root, text="Button 1", command=lambda: button_click(1))
button2 = tk.Button(root, text="Button 2", command=lambda: button_click(2))
button3 = tk.Button(root, text="Button 3", command=lambda: button_click(3))

# Размещаем кнопки в сетке
button1.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
button2.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
button3.grid(row=0, column=2, sticky="ew", padx=10, pady=5)

# Устанавливаем вес для колонок, чтобы они растягивались
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
