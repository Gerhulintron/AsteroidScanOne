import requests
import json


class connectionString:
	
	def __init__(self):
		self.apiURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2018-09-07&end_date=2018-09-08&api_key=9RmEI1n5UNrfxpI69VgHkDGfTwVXZmDdKavZ8BxO"
	

	def parseJsonData(jsonData):
		jsonString = jsonData
		#json dumps needs double quotes
#		jsonString = jsonString.replace("'",'"')
		#turn the json into a string
		#CONVERTS FROM PYTHON INTO JSON STRING
		jsonParsed = json.dumps(jsonString)
		#character replacement
		return jsonParsed
		
	def removeJsonChar(jsonStrip):
		jsonStrip = jsonStrip.replace(",","\n")
		jsonStrip = jsonStrip.strip("\"\\[](){}\'")
		jsonStrip = jsonStrip.replace("[", "")
		jsonStrip = jsonStrip.replace("]", "")
		jsonStrip = jsonStrip.replace("}", "")
		jsonStrip = jsonStrip.replace("{", "")
		jsonStrip = jsonStrip.replace("\\", "")
		jsonStrip = jsonStrip.replace("\"", "")
		return jsonStrip
		
	
	
