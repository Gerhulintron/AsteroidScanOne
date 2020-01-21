import turtle
from tkinter import *



def makeAsteroidInput():
	#GUI
	root = Tk()
	topFrame = Frame(root)
	bottomFrame = Frame(root)
	topFrame.pack()
	bottomFrame.pack(side=BOTTOM)

	titleLabel = Label(topFrame, text="Asteroid Tracker")
	instructionLabel = Label(topFrame, text="Enter a Date: ")
	dateLabel = Label(topFrame, text="dd/mm/yy")

	dayEntry = Entry(topFrame)
	monthEntry = Entry(topFrame)
	yearEntry = Entry(topFrame)

	submitButton = Button(topFrame, text="Submit", fg="purple")
	#submitButton.bind("<ButtonPress-1>", getUserData())

	titleLabel.grid(row=0)
	instructionLabel.grid(row=1)
	dateLabel.grid(row=2)

	dayEntry.grid(row=3, column=0)
	monthEntry.grid(row=3, column=1)
	yearEntry.grid(row=3, column=2)
	submitButton.grid(row=4)
	




	#scrollbar.pack( side = RIGHT, fill = Y )
	root.mainloop()
	
makeAsteroidInput()