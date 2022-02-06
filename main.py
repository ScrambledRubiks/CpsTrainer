from tkinter import *
import tkinter as tk
import random
import constants
win = Tk()
#dynamic variables
x = 0
totalClicks = 0
cpsLabelVar = StringVar()
buttonX = 0
buttonY = 0
currentX = 640
currentY = 360
seconds = 0
menubar = Menu(win)
win.configure(
  bg= constants.winBackground
  )

#creates the Replit Mode option, unused for now
filemenu = Menu(menubar, tearoff=0)
filemenu.add_checkbutton(label="Replit Mode", onvalue=1, offvalue=0, variable=x)
menubar.add_cascade(label="File", menu=filemenu)

#creates label at the top of the screen
cpsLabel = Label(
    win, 
    textvariable=cpsLabelVar, 
    font=('Consolas 15')
    ).pack()
win.geometry("1280x720")
#function when the button is clicked
def whenClicked():
    global totalClicks
    totalClicks = totalClicks + 1
    if totalClicks % 2 == 0:
        button.config(
        image= PhotoImage(file=constants.clickButton)
    )
    else:
        button.config(
            image= PhotoImage(file=constants.clickedButton)
    )
#sets which direction out of 16 possible for the button to drift
def changeValues():
     global buttonX
     global buttonY
     global currentX
     global currentY

     buttonX = random.randint(-2,2)*constants.speedMult
     buttonY = random.randint(-2,2)*constants.speedMult
     win.after(random.randint(250,1000), changeValues)

#creates the button
button = tk.Button(text="Click!", 
    command=whenClicked,
    bg="#0B090A",
    activebackground="#0B090A",
    borderwidth=0,
    image= PhotoImage(file=constants.clickButton)
    )

def onTick(): #tick every 10ms
    global buttonX
    global buttonY
    global currentX
    global currentY

    currentX = currentX + buttonX
    currentY = currentY + buttonY
    button.place(x=currentX, y=currentY)

    #makes sure the button doesn't go off the screen, should be changed later to add different screen sizes
    if currentX > 1200:
        currentX = 1200
    if currentX < 0:
        currentX =  0
    if currentY > 650:
        currentY = 650
    if currentY < 0:
        currentY = 0
    
    win.after(17, onTick)
def calcCPS():
    global seconds
    seconds = seconds + 1
    cpsLabelVar.set(str(round(totalClicks/(seconds/100),2)))
    win.after(10, calcCPS)

#calls all of the functions
win.after(2000, calcCPS)
win.after(2000, onTick)
win.after(2000, changeValues)

#final init
button.place(x=640,y=360)
win.config(menu=menubar)
win.mainloop()
