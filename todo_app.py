from tkinter import *
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '20Bcs@125395',
    database = 'To_Do_App'
)

cursor = db.cursor()

def add_btn():
    task = entry1.get()
    if task:
        cursor.execute('''INSERT INTO TaskAccess (TASK)
                       VALUES (%s)''', (task,))
        db.commit()
        messagebox.showinfo(title = 'Success',
                            message = 'Task Added Successfully')
        entry1.delete(0, END)
        load_tasks()
    else:
        messagebox.showwarning(title = 'Warning',
                               message = 'Task cannot be Empty.')

def delete_btn():
    select = listbox.curselection()
    if select:
        task = listbox.get(select[0])
        cursor.execute('''DELETE FROM TaskAccess
                       WHERE TASK = %s''', (task, ))
        messagebox.showinfo(title = 'Success',
                            message = 'Task Deleted Successfully')
        db.commit()
        load_tasks()
    else:
        messagebox.showwarning(title = 'Warning',
                               message = 'Select a task to delete')

def load_tasks():
    listbox.delete(0, END)
    cursor.execute('''SELECT TASK FROM TaskAccess''')
    for task in cursor.fetchall():
        listbox.insert(END, task[0])

root = Tk()
root.title('TO DO List App')

entry1 = Entry(root)
entry1.grid(row = 0,
            column = 0,
            padx = 20,
            pady = 20,
            columnspan = 2)

add_button = Button(root,
                    text = 'Add Task',
                    command = add_btn)
add_button.grid(row = 1,
                column = 0,
                padx = 20,
                pady = 10)

delete_button = Button(root,
                       text = 'Delete Task',
                       command = delete_btn)
delete_button.grid(row = 1,
                   column = 1,
                   padx = 20,
                   pady = 10)

listbox = Listbox(root,
                  width = 50,
                  height = 10)
listbox.grid(row = 2,
             column = 0,
             columnspan = 2,
             padx = 20,
             pady = 10)

load_tasks()

root.mainloop()
