class Asteroid:
	def __init__(self, asteroidName,orbitingBody, potentialHazard, closeApproachDate,estDimMinM,estDimMaxM,kilometers_per_second,missDistKM):		
		self.asteroidName = asteroidName 
		self.orbitingBody = orbitingBody 
		self.potentialHazard = potentialHazard
		self.closeApproachDate = closeApproachDate 
#		self.estDimMinKM = estDimMinKM
#		self.estDimMaxKM = estDimMaxKM
		self.estDimMinM = estDimMinM
		self.estDimMaxM = estDimMaxM
		self.estDimAvgM = round(((self.estDimMaxM - self.estDimMinM)/2 + self.estDimMinM), 2)
		self.kilometers_per_second = kilometers_per_second
		self.missDistKM = missDistKM
		print("***Asteroid Created***")
		
	def ToString(self):
		print("TO STRING")
		asteroidToString = "Asteroid Name:\t\t\t" + self.asteroidName + "\n"
		asteroidToString = asteroidToString + "Orbiting Body:\t\t\t" +  self.orbitingBody + "\n"
		asteroidToString = asteroidToString + "Potential Hazard:\t\t\t" + str(self.potentialHazard) + "\n"
		asteroidToString = asteroidToString + "Close Approach Date:\t\t" +  self.closeApproachDate + "\n"
		asteroidToString = asteroidToString + "Estimated Diatmeter Min(M):\t\t" + str(self.estDimMinM) + " M\n"
		asteroidToString = asteroidToString + "Estimated Diatmeter Max(M):\t\t" + str(self.estDimMaxM) + " M\n"
		asteroidToString = asteroidToString + "Estimated Diatmeter Average(M):\t" + str(self.estDimAvgM) + " M\n"
		asteroidToString = asteroidToString + "Kilometers per second:\t\t" + str(self.kilometers_per_second) + "\n"
		asteroidToString = asteroidToString + "Miss Distance(KM):\t\t\t" + str(self.missDistKM) + " KM\n"
		return asteroidToString
		
	def ToRow(self):
		return str(self.asteroidName + "\t\t|" + self.orbitingBody + "\t|" + str(self.potentialHazard) + "\t|" + str(self.closeApproachDate) + "\t|" + str(self.estDimAvgM) + "\t\t\t|" + str(self.kilometers_per_second) + "\t|" + str(self.missDistKM) + "\n")
		
	
	def listToString(asteroidList):
		asteroidString = "Asteroid Name \t\t|Orbits \t|Hazard\t|Approach Date\t|Estimated Diameter M\t|Speed Km/S\t|Miss Distance Km \n"
		for z in range(0, len(asteroidList)):
			asteroidString = str(asteroidString) + str(asteroidList[z].ToRow())
		print (asteroidString)
		return asteroidString