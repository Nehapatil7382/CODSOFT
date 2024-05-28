import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_name_var = tk.StringVar()
        self.task_description_var = tk.StringVar()
        self.task_category_var = tk.StringVar()
        self.task_priority_var = tk.StringVar()
        self.task_due_date_var = tk.StringVar()

        self.selected_task_index = None

        self.create_widgets()

    def create_widgets(self):
        # Task Name Entry
        tk.Label(self.root, text="Task Name:").grid(row=0, column=0, sticky="w")
        self.task_name_entry = tk.Entry(self.root, textvariable=self.task_name_var)
        self.task_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Task Description Entry
        tk.Label(self.root, text="Task Description:").grid(row=1, column=0, sticky="w")
        self.task_description_entry = tk.Entry(self.root, textvariable=self.task_description_var)
        self.task_description_entry.grid(row=1, column=1, padx=5, pady=5)

        # Task Category Entry
        tk.Label(self.root, text="Task Category:").grid(row=2, column=0, sticky="w")
        self.task_category_entry = tk.Entry(self.root, textvariable=self.task_category_var)
        self.task_category_entry.grid(row=2, column=1, padx=5, pady=5)

        # Task Priority Entry
        tk.Label(self.root, text="Task Priority:").grid(row=3, column=0, sticky="w")
        self.task_priority_entry = tk.Entry(self.root, textvariable=self.task_priority_var)
        self.task_priority_entry.grid(row=3, column=1, padx=5, pady=5)

        # Task Due Date Entry
        tk.Label(self.root, text="Task Due Date:").grid(row=4, column=0, sticky="w")
        self.task_due_date_entry = tk.Entry(self.root, textvariable=self.task_due_date_var)
        self.task_due_date_entry.grid(row=4, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Tasks", command=self.view_tasks).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Update Task", command=self.update_task).grid(row=7, column=0, columnspan=2, pady=10)

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
        self.task_listbox.bind('<<ListboxSelect>>', self.on_task_select)

    def add_task(self):
        name = self.task_name_var.get()
        description = self.task_description_var.get()
        category = self.task_category_var.get()
        priority = self.task_priority_var.get()
        due_date = self.task_due_date_var.get()

        if name:
            task_info = f"Name: {name}\nDescription: {description}\nCategory: {category}\nPriority: {priority}\nDue Date: {due_date}"
            self.tasks.append(task_info)
            self.task_listbox.insert(tk.END, name)
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showerror("Error", "Task name cannot be empty!")

    def view_tasks(self):
        if self.tasks:
            task_info = "\n\n".join(self.tasks)
            messagebox.showinfo("Tasks", task_info)
        else:
            messagebox.showinfo("No Tasks", "No tasks found!")

    def update_task(self):
        if self.selected_task_index is None:
            messagebox.showerror("Error", "Please select a task to update!")
            return

        name = self.task_name_var.get()
        description = self.task_description_var.get()
        category = self.task_category_var.get()
        priority = self.task_priority_var.get()
        due_date = self.task_due_date_var.get()

        if name:
            task_info = f"Name: {name}\nDescription: {description}\nCategory: {category}\nPriority: {priority}\nDue Date: {due_date}"
            self.tasks[self.selected_task_index] = task_info
            self.task_listbox.delete(self.selected_task_index)
            self.task_listbox.insert(self.selected_task_index, name)
            messagebox.showinfo("Success", "Task updated successfully!")
        else:
            messagebox.showerror("Error", "Task name cannot be empty!")

    def on_task_select(self, event):
        selection = event.widget.curselection()
        if selection:
            self.selected_task_index = selection[0]
            task_info = self.tasks[self.selected_task_index]
            task_info_lines = task_info.split('\n')
            self.task_name_var.set(task_info_lines[0].split(': ')[1])
            self.task_description_var.set(task_info_lines[1].split(': ')[1])
            self.task_category_var.set(task_info_lines[2].split(': ')[1])
            self.task_priority_var.set(task_info_lines[3].split(': ')[1])
            self.task_due_date_var.set(task_info_lines[4].split(': ')[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
