from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("How to make radio's button in python ")
root.iconbitmap("C:/Users/pc/coding.ico")

modes = [("cheese","🧀🧀🧀"),
         ("passta","🍜"),
         ("agges","🥚🥚"),
         ("Oinin","🧄🧄"),
]

pizza = StringVar()
pizza.set("cheese")

for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza,value=mode,bg="black").pack(anchor=W)

def clicked(value):
    my_lablel = Label(root, text=value).pack()


# Radiobutton(root,  text="Option 1 ", variable=radio,value=1,command=lambda : clicked(radio.get())).pack()
# Radiobutton(root,  text="Option 2 ", variable=radio,value=2,command=lambda : clicked(radio.get())).pack()

my_lablel = Label(root, text=pizza.get()).pack()

my_button = Button(root, text="click me!",command=lambda : clicked(pizza.get())).pack()






root.mainloop()