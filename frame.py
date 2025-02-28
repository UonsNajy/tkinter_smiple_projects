from tkinter import * 
from PIL import ImageTk,Image
root = Tk()
root.title('learn fram in pythin with tkinter')

root.iconbitmap("C:/Users/pc/coding.ico")
#Create a simple frame
frame = LabelFrame(root, text="this is my frame",padx=50,pady=50)
frame.grid(row=0,column=0,padx=100,pady=100)

#Create a simple Button 
b= Button(frame, text="Don't click me!").pack()
b2= Button(frame, text="click me!").pack(padx=20,pady=20)


root.mainloop()