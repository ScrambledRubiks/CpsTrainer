#Import all the necessary libraries
from tkinter import *
import constants
#Define the tkinter instance
win= Tk()
win.title("Rounded Button")

#Define the size of the tkinter frame
win.geometry("700x300")

#Define the working of the button

def my_command():
   text.config(text= "You have clicked Me...")

#Import the image using PhotoImage function
click_btn= PhotoImage(file=constants.clickButton)

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
# button= Button(
#     win, 
#     image=click_btn,
#     command= my_command, 
#     borderwidth=0)
# button.pack(pady=30)

text= Label(win, text= "")
text.pack(pady=30)

#creates the button
button1 = Button(
    win,
    # text="Click!", 
    # command=whenClicked,
    # bg= constants.winBackground,
    # activebackground= constants.winBackground,
    borderwidth=10,
    image=PhotoImage(file=constants.clickButton),
    command= my_command, 
    # image=PhotoImage(file="C:\\Users\\alexa\\OneDrive\\Documents\\GitHub\\CpsTrainer\\assets\\Click.png")
    # image= PhotoImage(file=constants.clickButton)
    )
button1.pack(side = TOP)

win.mainloop()