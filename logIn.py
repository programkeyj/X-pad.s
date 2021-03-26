import tkinter
import tkinter.messagebox as mb


# from tkinter import Label, Button, Entry


"""
def send():
    name = enter.get()
    passwd = enter1.get()
    try:
        send.send_mail(name, passwd)
    except:
        print("we have error")
"""

root = tkinter.Tk()
root.geometry('220x220')
root.title("log in")

nameL = tkinter.Label(root, text="enter name here\\/")
nameL.place(x=1, y=1)
enter = tkinter.Entry(root)
enter.place(x=1, y=25)
nameL2 = tkinter.Label(root, text="enter password here \\/")
nameL2.place(x=1, y=55)
enter1 = tkinter.Entry(root)
enter1.place(x=1, y=75)
but = tkinter.Button(root, text="send")
but.place(x=0, y=110)

lab = tkinter.Label(root, text=".................................................................................")
lab.place(x=1, y=180)

root.resizable(False, False)
root.mainloop()
