import os
import sys
import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox as mb

def run():
    import run


def exit():
    sys.exit()


def new_():
    text.clipboard_clear()
    text.option_clear()
    text.selection_clear()
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


def log_in():
    import logIn


def log_out():
    pass


root = tkinter.Tk()
root.geometry('300x300')
root.title('X pad 0.9')

tkinter.Label(root, text="Welcome to x_pad_0.9").pack()
text = tkinter.Text(width=400, height=400, bg="#ffffff",
            fg='black', wrap=tkinter.WORD)
scroll = tkinter.Scrollbar(command=text.yview)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

text.config(yscrollcommand=scroll.set)

text.pack()

main_menu = tkinter.Menu()

log = tkinter.Menu()
edit_menu = tkinter.Menu()
file_menu = tkinter.Menu()
break_menu = tkinter.Menu()
run_menu = tkinter.Menu()

edit_menu.add_command(label='editing offline')
edit_menu.add_command(label='edit')

break_menu.add_command(label='by keyj')
break_menu.add_command(label='FAQ')
break_menu.add_command(label='help')

file_menu.add_command(label="New", command=new_)
file_menu.add_command(label="Save_as", command=save_as)
file_menu.add_command(label="Save", command=save_)
file_menu.add_command(label="Open", command=open_)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

log.add_command(label="log in", command=log_in)
log.add_command(label="log out", command=log_out)

run_menu.add_command(label="run file", command=run)


main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="run", menu=run_menu)
main_menu.add_cascade(label="autorise", menu=log)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="help", menu=break_menu)


root.config(menu=main_menu)
#root.resizable(False, True)
root.mainloop()

