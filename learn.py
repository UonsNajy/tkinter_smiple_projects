from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("learn to code ")
root.iconbitmap("C:/Users/pc/coding.ico")

def popup():
    #showinfo , showwarning, showerror, askokcancel, askquaistion, askyes/no
    respone = messagebox.askquestion('this is my popup!', 'Hello, python')
    Label(root, text=respone).pack()
    if respone == 1:

        Label(root,text="You clicked Yes").pack()
    else:
        Label(root, text="You Clicked No!").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()