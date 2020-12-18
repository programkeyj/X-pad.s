import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox as mb
from tkinter import*
import sys
from tkinter import *
from tkinter import messagebox as mb

def ex():
    sys.exit()

def new_():
    print('you editing new file now')

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        mb.showerror('not working', 'more text___________')
    
def open_():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
 
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def save_():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()

root = Tk()
root.title('X.PAd 0.8')
root.geometry('400x400')

main_menu = Menu()
 
edit_menu = Menu()
file_menu = Menu()
break_menu = Menu()

edit_menu.add_command(label = 'editing offline')
edit_menu.add_command(label = 'edit')

break_menu.add_command(label = 'by keyj')
break_menu.add_command(label = 'FAQ')
break_menu.add_command(label = 'help')

file_menu.add_command(label="New", command = new_)
file_menu.add_command(label="Save_as", command = save_as)
file_menu.add_command(label="Save", command = save_)
file_menu.add_command(label="Open", command = open_)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = ex)

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu = edit_menu)
main_menu.add_cascade(label="help", menu=break_menu)


root.config(menu=main_menu)

text = Text(width=400, height=400, bg="#ffffff",
            fg='black', wrap=WORD)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
 
text.config(yscrollcommand=scroll.set)
 
text.pack()

root.mainloop()
