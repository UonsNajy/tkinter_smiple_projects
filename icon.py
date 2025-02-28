from tkinter import *
from PIL import ImageTk,Image


root = Tk()

root.title("Learn to code at coding.com")
root.iconbitmap("C:/Users/pc/coding.ico")





my_img1 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine.jpg') )
my_img2 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine2.jpg') )
my_img3 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine3.jpg') )
my_img4 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine4.jpg') )
my_img5 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine5.jpg') )
my_img6 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine6.jpg') )
my_img7 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine7.jpg') )
my_img8 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine8.jpg') )
my_img9 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine9.jpg') )
my_img10 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine10.jpg') )
my_img11 = ImageTk.PhotoImage(Image.open('C:/USers/pc/images/mine11.jpg') )
 
image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7,my_img8,my_img9,my_img10,my_img11]
len_list = len(image_list)

my_label = Label(image=my_img1)


my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>",bg="light blue",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<",bg="light blue",command=lambda: back(image_number-1))
    if image_number == len_list:
        button_forward = Button(root, text=">>",bg="light blue",state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)   
    button_forward.grid(row=1, column=2)
    
def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()

    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>",bg="light blue",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<",bg="light blue",command=lambda: back(image_number-1))
    if image_number == 1:
        button_back= Button(root, text="<<",bg="light blue",state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)   
    button_forward.grid(row=1, column=2)
    


button_back = Button(root, text="<<",bg="light blue",command=back,state=DISABLED)
button_exit = Button(root, text="exit app",bg="red", command=root.quit)
button_forward = Button(root, text=">>",bg="light blue",command=lambda: forward(2))
my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_exit.grid(row=1 , column=1)
button_forward.grid(row=1, column=2)


root.mainloop()


