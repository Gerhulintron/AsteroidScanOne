

def parseJsonData(jsonData):
	asteroidString = jsonData
	#json dumps needs double quotes
	asteroidString = asteroidString.replace("'",'"')
	#turn the json into a string
	#CONVERTS FROM PYTHON INTO JSON STRING
	asteroidParsed = json.dumps(asteroidString)
	#character replacement
	return asteroidParsed
	
def removeJsonChar(asteroidParsed):
	asteroidParsed = asteroidParsed.replace(",","\n")
	asteroidParsed = asteroidParsed.strip("\"\\[](){}\'")
	asteroidParsed = asteroidParsed.replace("[", "")
	asteroidParsed = asteroidParsed.replace("]", "")
	asteroidParsed = asteroidParsed.replace("}", "")
	asteroidParsed = asteroidParsed.replace("{", "")
	asteroidParsed = asteroidParsed.replace("\\", "")
	asteroidParsed = asteroidParsed.replace("\"", "")
	return asteroidParsed
	
def getApiUrl(yearEntry, monthEntry, dayEntry):
#	userDay = str(dayEntry.get())
#	userMonth = str(monthEntry.get())
#	userYear = str(yearEntry.get())
#	userFullDate = userYear+'-'+userMonth+'-'+userDay
	userFullDate = yearEntry, monthEntry, dayEntry
	apiURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+userFullDate+"&end_date="+userFullDate+"&api_key=9RmEI1n5UNrfxpI69VgHkDGfTwVXZmDdKavZ8BxO"
	return apiURL