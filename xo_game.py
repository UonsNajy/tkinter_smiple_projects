from tkinter import *
root = Tk()

root.title(" ⭕❌ ")

label = Label(root, text='❌⭕ Game').grid()
enter = Entry(root,
           width=35,borderwidth=30)
enter.grid(row=0, column=0, columnspan=3, padx=10, pady=10,)
if enter == "o":
    b1 = Button(root, border=0 ,font=("red"), bg="black",text="o" , padx=30,pady=20,command=lambda : button_click())
    
         
def button_click():
    return



b1 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())
b2 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())
b3 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())
b4 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())
b5 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())
b6 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())
b7 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())
b8 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())
b9 = Button(root, border=0 ,font=("red"), bg="black",text="" , padx=30,pady=20,command=lambda : button_click())





# Put the buttons on the screen
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)


root.mainloop()