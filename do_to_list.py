import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def edit_task():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        entry.delete(0, tk.END)
        entry.insert(tk.END, task)
        delete_task()
    except IndexError:
        pass

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass

def main():
    global entry, listbox

    root = tk.Tk()
    root.title("To-Do List")

    # Create and configure the entry field
    entry = tk.Entry(root, width=35)
    entry.pack(pady=10)

    # Create and configure the listbox
    listbox = tk.Listbox(root, width=40, height=10)
    listbox.pack()

    # Create and configure the scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Connect the scrollbar to the listbox
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Create the buttons
    add_btn = tk.Button(root, text="Add Task", command=add_task)
    add_btn.pack(pady=5)

    edit_btn = tk.Button(root, text="Edit Task", command=edit_task)
    edit_btn.pack(pady=5)

    del_btn = tk.Button(root, text="Delete Task", command=delete_task)
    del_btn.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
