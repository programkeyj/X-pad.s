import os
import tkinter
import tkinter.messagebox as mb


# from tkinter import Label, Button, Entry

def okey():
    path = enter.get()
    os.system("python3 "+path)


root = tkinter.Tk()
root.geometry('250x150')
root.title("run file")

nameL = tkinter.Label(root, text="enter path to python file here\\/")
nameL.place(x=1, y=1)
enter = tkinter.Entry(root)
enter.place(x=1, y=25)
but = tkinter.Button(root, text="ok", command=okey)
but.place(x=0, y=50)

lab = tkinter.Label(root, text=".................................................................................")
lab.place(x=1, y=80)

root.resizable(False, False)
root.mainloop()