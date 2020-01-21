#import constants 
from tkinter import *
import requests
import json
#from AsteroidTest import *

# class asteroidGUI():
	# def __init__ (self):
# dayEntry = Entry()
# monthEntry = Entry()
# yearEntry = Entry()

root = Tk()
dayEntry = Entry()
monthEntry = Entry()
yearEntry = Entry()

def makeSpace(root, dayEntry, monthEntry, yearEntry):
	#root = Tk()
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
	
	submitButton = Button(topFrame, text="Submit", fg="purple", command= getAsteroidData(dayEntry, monthEntry, yearEntry))
	#submitButton = Button(topFrame, text="Submit", fg="purple", command=getUserData)
	
	asteroidText = Label(bottomFrame, text="asteroidToString", justify=LEFT)

	titleLabel.grid(row=0)
	instructionLabel.grid(row=1)
	dateLabel.grid(row=2)
	dayEntry.grid(row=3, column=0)
	monthEntry.grid(row=3, column=1)
	yearEntry.grid(row=3, column=2)
	submitButton.grid(row=4)


	asteroidText.grid(row=6)
	
#	root.mainloop()
	
def getUserDate(userYear, userMonth, userDay):
	# userDay = str(dayEntry.get())
	# userMonth = str(monthEntry.get())
	# userYear = str(yearEntry.get())
	userFullDate = userYear+'-'+userMonth+'-'+userDay
	return userFullDate
	
def getApiUrl(userFullDate):
	# userDay = str(dayEntry.get())
	# userMonth = str(monthEntry.get())
	# userYear = str(yearEntry.get())
	# userFullDate = userYear+'-'+userMonth+'-'+userDay
	#userFullDate = getUserDate(str(yearEntry.get()), str(monthEntry.get()), str(dayEntry.get()))
	apiURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+userFullDate+"&end_date="+userFullDate+"&api_key=9RmEI1n5UNrfxpI69VgHkDGfTwVXZmDdKavZ8BxO"
	return apiURL

	
	
#CONTROL
def getAsteroidData(dayEntry, monthEntry, yearEntry):
	userDay = str(dayEntry.get())
	userMonth = str(monthEntry.get())
	userYear = str(yearEntry.get())
#	userFullDate = str(userYear)+'-'+str(userMonth)+'-'+str(userDay)
	userFullDate = getUserDate(userYear, userMonth, userDay)
	apiURL = getApiUrl(userFullDate)
#	apiURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+userFullDate+"&end_date="+userFullDate+"&api_key=9RmEI1n5UNrfxpI69VgHkDGfTwVXZmDdKavZ8BxO"

	# userFullDate = getUserDate(userYear, userMonth, userDay)
	# apiURL = getApiUrl()
	print(apiURL)
	asteroidResponse = requests.get(apiURL)
	asteroidData = asteroidResponse.json()
	print(asteroidData)	
	print("-----------------------")
	print("Filtered Data")
	
	
	asteroidName = asteroidData['near_earth_objects'][userFullDate][1]['name']
	orbitingBody = asteroidData['near_earth_objects'][userFullDate][1]['close_approach_data'][0]['orbiting_body']
	potentialHazard = asteroidData['near_earth_objects'][userFullDate][1]['is_potentially_hazardous_asteroid']
	closeApproachDate = asteroidData['near_earth_objects'][userFullDate][1]['close_approach_data'][0]['close_approach_date']
	estDimMinM = asteroidData['near_earth_objects'][userFullDate][1]['estimated_diameter']['meters']['estimated_diameter_min']
	estDimMaxM = asteroidData['near_earth_objects'][userFullDate][1]['estimated_diameter']['meters']['estimated_diameter_max']
	kilometers_per_second = asteroidData['near_earth_objects'][userFullDate][1]['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
	missDistKM = asteroidData['near_earth_objects'][userFullDate][1]['close_approach_data'][0]['miss_distance']['kilometers']
	
	newAsteroid = Asteroid(asteroidName, orbitingBody, potentialHazard, closeApproachDate, estDimMinM, estDimMaxM, kilometers_per_second, missDistKM)
	print("***********************************")
	print (newAsteroid.asteroidName)
	print (Asteroid.ToString(newAsteroid))
	print("***********************************")


makeSpace(root, dayEntry, monthEntry, yearEntry)
root.mainloop()