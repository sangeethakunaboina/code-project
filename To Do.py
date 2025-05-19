import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Entry field for new task
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, font=("Arial", 14), selectbackground="gray")
listbox.pack(pady=10, expand=True, fill=tk.BOTH)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), command=delete_task)
delete_button.pack(pady=5)

# Run the app
root.mainloop()
