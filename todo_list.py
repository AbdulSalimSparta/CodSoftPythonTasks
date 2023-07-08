import tkinter as tk
from tkinter import messagebox


# importing Tk library for creating GUI
def add_task():
    """ Adding Task in the list box"""
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    """ Deleting Task From the list box"""
    try:
        selected_index = listbox.curselection()
        listbox.delete(selected_index)

    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")


def clear_tasks():
    """ Clearing All Task From the list box"""
    listbox.delete(0, tk.END)


# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create the listbox
listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

# Create the entry field
entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack(pady=5)

# Create the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Add Button
add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0)

# Delete button
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1)

# Clear Button
clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks)
clear_button.grid(row=0, column=2)

# Start the main event loop
window.mainloop()

# Code by Abdul saleem
