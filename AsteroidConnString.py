from connectionString import connectionString
import requests
import json

class asteroidConnString(connectionString):
	def __init__(self):
		connectionString.__init__(self)
		self.apiURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2018-09-07&end_date=2018-09-08&api_key=9RmEI1n5UNrfxpI69VgHkDGfTwVXZmDdKavZ8BxO"
		self.userDate = "2018-09-07"

	def setApiUrlDate(self, userFullDate):
		self.apiURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+userFullDate+"&end_date="+userFullDate+"&api_key=9RmEI1n5UNrfxpI69VgHkDGfTwVXZmDdKavZ8BxO"
		return self.apiURL
		
	def getjsonData(self, apiURL):
		#Enters the URL
		jsonResponse = requests.get(apiURL)
		
		#Turns the data from the url into a dictionary/string
		jsonData = jsonResponse.json()
		
		#prints to the console
		print(jsonData)
		return jsonData

	def parseJsonData(self, jsonData):
		jsonString = jsonData
		#json dumps needs double quotes
#		jsonString = jsonString.replace("'",'"')
		#turn the json into a string
		#CONVERTS FROM PYTHON INTO JSON STRING
		jsonParsed = json.dumps(jsonString)
		#character replacement
		return jsonParsed
		
	def removeJsonChar(self, jsonStrip):
		jsonStrip = jsonStrip.replace(",","\n")
		jsonStrip = jsonStrip.strip("\"\\[](){}\'")
		jsonStrip = jsonStrip.replace("[", "")
		jsonStrip = jsonStrip.replace("]", "")
		jsonStrip = jsonStrip.replace("}", "")
		jsonStrip = jsonStrip.replace("{", "")
		jsonStrip = jsonStrip.replace("\\", "")
		jsonStrip = jsonStrip.replace("\"", "")
		return jsonStrip