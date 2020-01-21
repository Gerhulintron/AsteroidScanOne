import turtle
from COLOUR_CONSTANTS import *

class AsteroidViz:

# spaceColour = "#251A21"
# whiteOutline = "#FDFDFC"
# astroColour = "#2D1445"
# astroGreen = "#194C31"
# earthBlue = "#11788A"



	def __init__ (self, vizFrame, vizPen):
#		vizFrame = turtle.Screen()
#		vizPen = turtle.Turtle()
		vizPen.speed(0)
		vizFrame.bgcolor("#251A21")
		vizPen.pencolor("#FDFDFC")
		vizPen.ht()
		

	def writeAllAsteroids(self, vizPen, asteroidString):
		# vizPen.goto(-250, -100)
		# #vizPen.write(asteroidString,False, align="left")
		# vizPen.pendown()
		# vizPen.write(asteroidName, False, align = "left",  font=("Felix Titling", 24, "bold"))
		# vizPen.penup()
		vizPen.goto(-490, -350)
		vizPen.pendown()
		vizPen.write(asteroidString, False, align="left",  font=("Tahoma", 12, "normal"))
		vizPen.penup()
		
		
	def makeViz(self, vizPen, missDistKM, avgDiam, asteroidName):
		print("-----------------------")
		print("Turtles")
		
		#Write the Asteroid Data
#		vizPen.clear()
		vizPen.penup()
		vizPen.home()
		vizPen.penup()



		
		#Draw "Earth"
		vizPen.goto(0, -8000)
		vizPen.pendown()
		vizPen.fillcolor("#11788A")
		vizPen.begin_fill()
		vizPen.circle(4000)
		vizPen.end_fill()
		vizPen.penup()
		
		#Write Asteroid Data
		# vizPen.goto(-250, -100)
		# #vizPen.write(asteroidString,False, align="left")
		# vizPen.pendown()
		# vizPen.write(asteroidName, False, align = "left",  font=("Felix Titling", 24, "bold"))
		# vizPen.penup()
		# vizPen.goto(-450, -300)
		# vizPen.pendown()
		# vizPen.write(asteroidString, False, align="left",  font=("Tahoma", 12, "normal"))
		# vizPen.penup()
		
		# #Write the Asteroid String Again??
		# vizPen.goto(-100, -200)
		# #vizPen.write(asteroidString,False, align="left")
		# vizPen.pendown()
		# vizPen.write(asteroidString, False, align="left")
		# vizPen.penup()
		

		
		# #Draw "Miss Distance" and turn right?
		# vizPen.goto(0,0)
		# vizPen.pendown()
		# vizPen.forward(float(missDistKM)/1000000)
# #		vizPen.right(90)
		# vizPen.penup()


		# #Maximum estimated diameter
		# vizPen.goto(0, float(missDistKM)/1000000)
		# vizPen.pendown()
		# vizPen.fillcolor(str(randomColour()))		
# #		vizPen.fillcolor("#194C31")
		# vizPen.fillcolor()
		# vizPen.begin_fill()
		# vizPen.circle(float(maxDiam))
		# vizPen.end_fill()
		# vizPen.penup()
		
		#Average estimated diameter
		vizPen.goto(0, float(missDistKM)/1000000)
		vizPen.fillcolor(str(randomColour()))
#		vizPen.fillcolor("#2D1445")
		vizPen.begin_fill()
		vizPen.circle(float(avgDiam))
		vizPen.end_fill()
		vizPen.penup()
		
		#Draw "Miss Distance" and turn right?
		# vizPen.goto(0,0)
		# vizPen.pendown()
		# vizPen.left(90)
		# vizPen.forward(float(missDistKM)/1000000)
# #		vizPen.right(90)
		# vizPen.penup()
		
		# #Miss Distance
		# vizPen.goto(200,0)
		# vizPen.pendown()
		# vizPen.write(str(missDistKM), False)
		# vizPen.left(90)
		# vizPen.penup()
		
		#Write Minimum Diameter
		# vizPen.goto(200, minDiam)
		# vizPen.pendown()
		# vizPen.write("Estimated Minimum Diameter: \n" + str(minDiam) + " M", False, align="center",  font=("Tahoma", 16, "normal"))
		# vizPen.penup()
		
		#Write max diameter
		# vizPen.goto(200, maxDiam)
		# vizPen.pendown()		
		# vizPen.write("Estimated Maximum Diameter: \n" + str(maxDiam) + " M", False, align="center",  font=("Tahoma", 16, "normal"))
		# vizPen.penup()
		
		#Miss Distance
		# vizPen.goto(200,0)
		# vizPen.pendown()
		# vizPen.write("Miss Distance: \n" + str(missDistKM) + " M", False,  font=("Tahoma", 16, "normal"))
		# vizPen.left(90)
		# vizPen.penup()	

#----------------------------------
#Previous version, draws min and max diam
#-------------------------------------		
	# def makeViz(self, vizPen, missDistKM, minDiam, maxDiam, asteroidName, asteroidString):
		# print("-----------------------")
		# print("Turtles")
		
		# #Write the Asteroid Data
# #		vizPen.clear()
		# vizPen.penup()
		# vizPen.home()
		# vizPen.penup()



		
		# #Draw "Earth"
		# vizPen.goto(0, -8000)
		# vizPen.pendown()
		# vizPen.fillcolor("#11788A")
		# vizPen.begin_fill()
		# vizPen.circle(4000)
		# vizPen.end_fill()
		# vizPen.penup()
		
		# #Write Asteroid Data
		# vizPen.goto(-250, -100)
		# #vizPen.write(asteroidString,False, align="left")
		# vizPen.pendown()
		# vizPen.write(asteroidName, False, align = "left",  font=("Felix Titling", 24, "bold"))
		# vizPen.penup()
		# vizPen.goto(-250, -290)
		# vizPen.pendown()
		# vizPen.write(asteroidString, False, align="left",  font=("Tahoma", 12, "normal"))
		# vizPen.penup()
		
		# # #Write the Asteroid String Again??
		# # vizPen.goto(-100, -200)
		# # #vizPen.write(asteroidString,False, align="left")
		# # vizPen.pendown()
		# # vizPen.write(asteroidString, False, align="left")
		# # vizPen.penup()
		

		
		# # #Draw "Miss Distance" and turn right?
		# # vizPen.goto(0,0)
		# # vizPen.pendown()
		# # vizPen.forward(float(missDistKM)/1000000)
# # #		vizPen.right(90)
		# # vizPen.penup()


		# #Maximum estimated diameter
		# vizPen.goto(0, float(missDistKM)/1000000)
		# vizPen.pendown()
		# vizPen.fillcolor(str(randomColour()))		
# #		vizPen.fillcolor("#194C31")
		# vizPen.fillcolor()
		# vizPen.begin_fill()
		# vizPen.circle(float(maxDiam))
		# vizPen.end_fill()
		# vizPen.penup()
		
		# #Minimum estimated diameter
		# vizPen.goto(0, float(missDistKM)/1000000)
		# vizPen.fillcolor(str(randomColour()))
# #		vizPen.fillcolor("#2D1445")
		# vizPen.begin_fill()
		# vizPen.circle(float(minDiam))
		# vizPen.end_fill()
		# vizPen.penup()
		
		# #Draw "Miss Distance" and turn right?
		# vizPen.goto(0,0)
		# vizPen.pendown()
		# vizPen.left(90)
		# vizPen.forward(float(missDistKM)/1000000)
# #		vizPen.right(90)
		# vizPen.penup()
		
		# # #Miss Distance
		# # vizPen.goto(200,0)
		# # vizPen.pendown()
		# # vizPen.write(str(missDistKM), False)
		# # vizPen.left(90)
		# # vizPen.penup()
		
		# #Write Minimum Diameter
		# # vizPen.goto(200, minDiam)
		# # vizPen.pendown()
		# # vizPen.write("Estimated Minimum Diameter: \n" + str(minDiam) + " M", False, align="center",  font=("Tahoma", 16, "normal"))
		# # vizPen.penup()
		
		# #Write max diameter
		# # vizPen.goto(200, maxDiam)
		# # vizPen.pendown()		
		# # vizPen.write("Estimated Maximum Diameter: \n" + str(maxDiam) + " M", False, align="center",  font=("Tahoma", 16, "normal"))
		# # vizPen.penup()
		
		# #Miss Distance
		# vizPen.goto(200,0)
		# vizPen.pendown()
		# vizPen.write("Miss Distance: \n" + str(missDistKM) + " M", False,  font=("Tahoma", 16, "normal"))
		# vizPen.left(90)
		# vizPen.penup()


# asteroidVisualizer = AsteroidViz()
# asteroidString = "astro blastro"
# asteroidVisualizer.makeViz(20000000, 30, 70)
# asteroidVisualizer.vizFrame.exitonclick()
