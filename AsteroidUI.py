from tkinter import *
from tkinter import ttk
import re

class AsteroidUI:
	def __init__(self, master):
		
		self.master = master.title("Asteroid Scanner")
		
		self.topFrame = Frame(master)
		self.bottomFrame = Frame(master)
		self.topFrame.pack()
		self.bottomFrame.pack(side=BOTTOM)

		self.titleLabel = Label(self.topFrame, text="Asteroid Tracker")
		self.instructionLabel = Label(self.topFrame, text="Enter a Date: ")
		self.dateLabel = Label(self.topFrame, text="dd/mm/yyyy", justify=CENTER)
		
#		self.asteroidMenu = ttk.Combobox(master)

		self.dayEntry = Entry(self.topFrame)
		self.monthEntry = Entry(self.topFrame)
		self.yearEntry = Entry(self.topFrame)
		
		self.submitButton = Button(self.topFrame, text="Submit", fg="purple")
		#submitButton = Button(topFrame, text="Submit", fg="purple", command=getUserData)

		self.asteroidText = Label(self.bottomFrame, text = "Greetings", justify=LEFT)
#		self.entryOutput.set("Enter a date :)")
		self.titleLabel.grid(row=0, column=1)
		self.instructionLabel.grid(row=1, column=1)
		self.dateLabel.grid(row=2, column=1)
		self.dayEntry.grid(row=3, column=0)
		self.monthEntry.grid(row=3, column=1)
		self.yearEntry.grid(row=3, column=2)
#		self.asteroidMenu.grid(row=3, column=3)
		
		self.submitButton.grid(row=4)
		self.asteroidText.grid(row=6)
		
	def dayCheckReg(self, dayEntry):
		if re.findall("[0-3][0-9]",dayEntry):
			return True
		else:
			return False
		
	def monthCheckReg(self, monthEntry):
		return re.findall("[0-1][0-9]",monthEntry)
		
	def yearCheckReg(self, yearEntry):
		return re.findall("[2][0][0-2][0-9]",yearEntry)
	
	def typeCheck(self, numToCheck):
		return(isinstance(int(numToChck), int))
		
		
	def setOutput(self, newEntry):
		self.entryOutput.set(newEntry)
		
	def getUserDate(self):
		userDay = str(self.dayEntry.get())
		userMonth = str(self.monthEntry.get())
		userYear = str(self.yearEntry.get())
		if self.dayCheckReg(userDay):
			if self.monthCheckReg(userMonth):
				if self.yearCheckReg(userYear):
	
					userFullDate = userYear+'-'+userMonth+'-'+userDay
					print("GET USER DATE TEST: " + userFullDate)
	#				self.asteroidText = Label(self.bottomFrame, text= userFullDate, justify=LEFT)
					return userFullDate
					
				else:
					self.entryOutput.set("Please Enter valid a valid date.")
			else:
				self.entryOutput.set("Please Enter valid a valid date.")
		else:
			self.entryOutput.set("Please Enter valid a valid date.")					
		
	def intCheck(self, aNum):
		if isinstance(aNum, int):
			print("TRUE")
			print(type(aNum))
			return(isinstance(aNum, int))
		else:
			print("FALSE")
			print(type(aNum))
			return(isinstance(aNum, int))		

			
	
		
# root = Tk()
# astroGUI = AsteroidUI(root)
# root.mainloop()