import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        font_size = 14
        entry_width = 35
        entry_height = 3  

        self.task_entry = tk.Text(self.root, width=entry_width, height=entry_height, wrap=tk.WORD, font=("Arial", font_size))
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=8, font=("Arial", font_size))
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_as_completed)

        self.task_entry.pack(pady=10, padx=10, fill=tk.X)
        self.add_button.pack(pady=5, padx=10, fill=tk.X)
        self.task_listbox.pack(pady=5, padx=10, expand=True, fill=tk.BOTH)
        self.complete_button.pack(pady=5, padx=10, fill=tk.X)
        self.remove_button.pack(pady=5, padx=10, fill=tk.X)

    def add_task(self):
        task_text = self.task_entry.get("1.0", tk.END).strip()
        if task_text:
            self.tasks.append((task_text, False))  
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Error", "Please enter a task to add.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
        else:
            messagebox.showwarning("Error", "Please select a task to remove.")

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            task, completed = self.tasks[task_index]
            if not completed:
                self.tasks[task_index] = (task, True)
                self.task_listbox.itemconfig(task_index, {'bg': 'dark green', 'selectbackground': 'dark green'})
            else:
                messagebox.showwarning("Task Completed", "This task is already marked as completed.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.geometry("400x400")  
    root.mainloop()
