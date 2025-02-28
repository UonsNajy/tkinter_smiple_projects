from tkinter import * 
root = Tk()
root.title()

enter = Entry(root,bg="white",
           width=35,borderwidth=30)
enter.grid(row=0, column=0, columnspan=3, padx=10, pady=10,)

def button_click(number):
    current = enter.get()
    enter.delete(0,END)   
    enter.insert(0, str(current) + str(number))

 
def button_point():
    return   
def button_equal():
    return   
def button_clear():
    return   
def button_divide():
    return   
def button_multiply():
    return   
def button_subtracte():
    return   
def button_add():
    first_number=enter.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    enter.delete(0, END)
def button_divide():
    first_number=enter.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    enter.delete(0, END)
def button_equal():
    second_number = enter.get()
    enter.delete(0, END)
    if math == "addition":
        enter.insert(0, f_num + int(second_number))    
    if math == "subtraction":
        enter.insert(0, f_num - int(second_number))    
    if math == "multiplication":
        enter.insert(0, f_num * int(second_number))    
    if math == "division":
        enter.insert(0, f_num / int(second_number))


def button_clear():
    
    enter.delete(0, 1)
#انشاء ازرار لكل من الارقام و ادوات الجمع والطرح والضرب و القسمه 
b1 = Button(root, border=0 ,font=("red"), text="1" , padx=40 ,pady=40,command=lambda : button_click(1))
b2 = Button(root,border=0 ,font=("red"), text="2" , padx=40 ,pady=40,command=lambda : button_click(2))
b3 = Button(root,border=0 ,font=("red"), text="3" , padx=40 ,pady=40,command=lambda : button_click(3))
b4 = Button(root,border=0 , font=("red"),text="4" , padx=40 ,pady=40,command=lambda : button_click(4))
b5 = Button(root,border=0 ,font=("red"), text="5" , padx=40 ,pady=40,command=lambda : button_click(5))
b6 = Button(root,border=0 ,font=("red"), text="6" , padx=40 ,pady=40,command=lambda : button_click(6))
b7 = Button(root,border=0 , font=("red"),text="7" , padx=40 ,pady=40,command=lambda : button_click(7))
b8 = Button(root,border=0 , font=("red"),text="8" , padx=40 ,pady=40,command=lambda : button_click(8))
b9 = Button(root,border=0 , font=("red"),text="9" , padx=40 ,pady=40,command=lambda : button_click(9))
b0 = Button(root, border=0 ,font=("red"),text="0" , padx=40 ,pady=40,command=lambda : button_click(0))
b_emty = Button(root,border=0 , font=("red"),text="" , padx=40 ,pady=40,command=lambda : button_click())

#b_point = Button(root, text="." , padx=40 ,pady=40,command =button_point)
b_equal = Button(root,bg="blue",border=0 , font=("red"),text="=" , padx=40 ,pady=40,command= button_equal)
b_clear = Button(root, border=0 ,font=("red"),text="✂" , padx=40 ,pady=40,command=button_clear)
b_divide = Button(root,border=0 ,font=("red"), text="/" , padx=48 ,pady=40,command= button_divide)
b_multiply = Button(root,border=0 , font=("red"),text="*" , padx=48 ,pady=40,command=button_multiply)
b_subtract = Button(root, border=0 ,font=("red"),text="-" , padx=48,pady=40,command=button_subtracte)
b_add = Button(root,border=0 ,font=("red"), text="+" , padx=40 ,pady=40,command= button_add)




















b1.grid(row=3, column=0 )
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
#b_emty.grid(row=5, column=0)

#.grid(row=4, column=1)
b_equal.grid(row=4, column=2)

b_clear.grid(row=1, column=3)
b_divide.grid(row=2, column=3,)
b_multiply.grid(row=3, column=3)
b_subtract.grid(row=4, column=3)
b_add.grid(row=4, column=1,)
root.mainloop()