from connectionString import connectionString
from AsteroidConnString import *
from AsteroidUI import *
from Asteroid import Asteroid
from AsteroidViz import AsteroidViz
import turtle


class AsteroidScanControl():

	def __init__(self):
		self.root = Tk()
		self.astroGUI = AsteroidUI(self.root)
		self.asteroidConnection = asteroidConnString()
		self.userDate = "2018-09-07"
		self.astroGUI.submitButton.bind("<Button>", self.getAsteroidData)

		print(str(self.asteroidConnection.apiURL))

	#runs the program. Runs the mainloop for the tkinter window
	def run(self):
		self.root.mainloop()
	
	#Gets and prints the completed APIURL from the user.
	def getUserAsteroidUrl(self):
		self.userDate = str(self.astroGUI.getUserDate())
		print("************TEST************")
		print(self.userDate)
		self.asteroidConnection.setApiUrlDate(self.userDate)
		print(self.asteroidConnection.apiURL)
		print("************TEST************")
		return self.asteroidConnection.apiURL
	
	#Takes the URL and gets and prints the JSON data
	def getAsteroidJson(self):
		return self.asteroidConnection.getjsonData(self.asteroidConnection.apiURL)

	#gets and prints the raw and parsed data for an asteroid.
	def getAsteroidData(self, event):
		self.getUserAsteroidUrl()
		astroJson = self.getAsteroidJson()
		astroRawData = self.asteroidConnection.parseJsonData(str(astroJson))
		astroParsedData = self.asteroidConnection.removeJsonChar(str(astroRawData))
		print(astroJson['near_earth_objects'][str(self.userDate)][1]['name'])
		print("Length " + str(len(astroJson['near_earth_objects'][str(self.userDate)])))
		asteroidName = astroJson['near_earth_objects'][str(self.userDate)][1]['name']
		orbitingBody = astroJson['near_earth_objects'][self.userDate][1]['close_approach_data'][0]['orbiting_body']
		potentialHazard = astroJson['near_earth_objects'][self.userDate][1]['is_potentially_hazardous_asteroid']
		closeApproachDate = astroJson['near_earth_objects'][self.userDate][1]['close_approach_data'][0]['close_approach_date']
		estDimMinM = astroJson['near_earth_objects'][self.userDate][1]['estimated_diameter']['meters']['estimated_diameter_min']
		estDimMaxM = astroJson['near_earth_objects'][self.userDate][1]['estimated_diameter']['meters']['estimated_diameter_max']
		kilometers_per_second = astroJson['near_earth_objects'][self.userDate][1]['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
		missDistKM = astroJson['near_earth_objects'][self.userDate][1]['close_approach_data'][0]['miss_distance']['kilometers']	
		newAsteroid = Asteroid(asteroidName, orbitingBody, potentialHazard, closeApproachDate, estDimMinM, estDimMaxM, float(kilometers_per_second), float(missDistKM))
		
		newAstroViz = AsteroidViz(vizFrame, vizPen)
		vizPen.clear()
		newAstroViz.makeViz(vizPen, missDistKM, newAsteroid.estDimAvgM, newAsteroid.asteroidName)
		
		print("***Asteroid Created***")
		print (newAsteroid.asteroidName)
		print(str(newAsteroid.ToString()))
		self.astroGUI.asteroidText.config(text=(str(newAsteroid.ToString())))
		self.getAllAsteroids()
	
	
	
	def getAllAsteroids(self):
		
		self.getUserAsteroidUrl()
		astroJson = self.getAsteroidJson()
		astroRawData = self.asteroidConnection.parseJsonData(str(astroJson))
		astroParsedData = self.asteroidConnection.removeJsonChar(str(astroRawData))
		newAsteroidList = []
		newAstroViz = AsteroidViz(vizFrame, vizPen)
		vizPen.clear()		
		for i in range(0, len(astroJson['near_earth_objects'][str(self.userDate)])):
			print(astroJson['near_earth_objects'][str(self.userDate)][i]['name'])
			asteroidName = astroJson['near_earth_objects'][str(self.userDate)][i]['name']
			orbitingBody = astroJson['near_earth_objects'][self.userDate][i]['close_approach_data'][0]['orbiting_body']
			potentialHazard = astroJson['near_earth_objects'][self.userDate][i]['is_potentially_hazardous_asteroid']
			closeApproachDate = astroJson['near_earth_objects'][self.userDate][i]['close_approach_data'][0]['close_approach_date']
			estDimMinM = astroJson['near_earth_objects'][self.userDate][i]['estimated_diameter']['meters']['estimated_diameter_min']
			estDimMaxM = astroJson['near_earth_objects'][self.userDate][i]['estimated_diameter']['meters']['estimated_diameter_max']
			kilometers_per_second = astroJson['near_earth_objects'][self.userDate][i]['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
			missDistKM = astroJson['near_earth_objects'][self.userDate][i]['close_approach_data'][0]['miss_distance']['kilometers']	
			newAsteroid = Asteroid(asteroidName, orbitingBody, potentialHazard, closeApproachDate, estDimMinM, estDimMaxM, kilometers_per_second, missDistKM)
	
#			newAstroViz.makeViz(vizPen, missDistKM, estDimMinM, estDimMaxM, newAsteroid.asteroidName, str(newAsteroid.ToString()))			
			
			print(str(newAsteroid.ToString()))
			newAsteroidList.append(newAsteroid)
		print ("------------ASTEROID LIST TEST------------")	
		newAsteroidList.sort(key=lambda x:x.estDimAvgM, reverse=True)
		for j in range(0, len(newAsteroidList)):
			print(str(newAsteroidList[j].ToString()))
	#		newAstroViz.makeViz(vizPen, newAsteroidList[j].missDistKM, newAsteroidList[j].estDimAvgM,newAsteroidList[j].asteroidName, (str(newAsteroidList[j].ToRow())))
			newAstroViz.makeViz(vizPen, newAsteroidList[j].missDistKM, newAsteroidList[j].estDimAvgM,newAsteroidList[j].asteroidName)
		newAstroViz.writeAllAsteroids(vizPen, str(Asteroid.listToString(newAsteroidList)))	
			
			
	# def getAllAsteroidData(self)
		# self.getUserAsteroidUrl()
		# astroJson = self.getAsteroidJson()
		# astroRawData = self.asteroidConnection.parseJsonData(str(astroJson))
		# astroParsedData = self.asteroidConnection.removeJsonChar(str(astroRawData))
		


	def makeAsteroid(self, asteroidData):

		asteroidName = asteroidData["near_earth_objects"][self.userDate][1]["name"]
		orbitingBody = asteroidData["near_earth_objects"][self.userDate][1]["close_approach_data"][0]["orbiting_body"]
		potentialHazard = asteroidData["near_earth_objects"][self.userDate][1]["is_potentially_hazardous_asteroid"]
		closeApproachDate = asteroidData["near_earth_objects"][self.userDate][1]["close_approach_data"][0]["close_approach_date"]
		estDimMinM = asteroidData["near_earth_objects"][self.userDate][1]["estimated_diameter"]["meters"]["estimated_diameter_min"]
		estDimMaxM = asteroidData["near_earth_objects"][self.userDate][1]["estimated_diameter"]["meters"]["estimated_diameter_max"]
		kilometers_per_second = asteroidData["near_earth_objects"][self.userDate][1]["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]
		missDistKM = asteroidData["near_earth_objects"][self.userDate][1]["close_approach_data"][0]["miss_distance"]["kilometers"]	
		newAsteroid = Asteroid(asteroidName, orbitingBody, potentialHazard, closeApproachDate, estDimMinM, estDimMaxM, kilometers_per_second, missDistKM)


vizFrame = turtle.Screen()
vizPen = turtle.Turtle()
	
runner = AsteroidScanControl()
runner.run()