from connectionString import connectionString
from AsteroidConnString import *
from AsteroidUI import *
from Asteroid import Asteroid
from AsteroidViz import AsteroidViz
import turtle
from COLOUR_CONSTANTS import *
import datetime
from PIL import Image, EpsImagePlugin
import os

print(os.environ['PATH'])

class AsteroidScanControl():

    def __init__(self):
        self.root = Tk()
        self.astroGUI = AsteroidUI(self.root)
        self.asteroidConnection = asteroidConnString()
        self.userDate = "2018-09-07"
        self.astroGUI.submitButton.bind("<Button>", self.getAsteroidData)

        print(str(self.asteroidConnection.apiURL))

    # Runs the program. Runs the mainloop for the tkinter window
    def run(self):
        self.root.mainloop()

    # Gets and prints the completed API URL from the user.
    def getUserAsteroidUrl(self):
        self.userDate = str(self.astroGUI.getUserDate())
        print("************TEST************")
        print(self.userDate)
        self.asteroidConnection.setApiUrlDate(self.userDate)
        print(self.asteroidConnection.apiURL)
        print("************TEST************")
        return self.asteroidConnection.apiURL

    # Takes the URL and gets and prints the JSON data
    def getAsteroidJson(self):
        return self.asteroidConnection.getjsonData(self.asteroidConnection.apiURL)

    # Gets and prints the raw and parsed data for an asteroid.
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
        closeApproachDate = astroJson['near_earth_objects'][self.userDate][1]['close_approach_data'][0][
            'close_approach_date']
        estDimMinM = astroJson['near_earth_objects'][self.userDate][1]['estimated_diameter']['meters'][
            'estimated_diameter_min']
        estDimMaxM = astroJson['near_earth_objects'][self.userDate][1]['estimated_diameter']['meters'][
            'estimated_diameter_max']
        kilometers_per_second = \
        astroJson['near_earth_objects'][self.userDate][1]['close_approach_data'][0]['relative_velocity'][
            'kilometers_per_second']
        missDistKM = astroJson['near_earth_objects'][self.userDate][1]['close_approach_data'][0]['miss_distance'][
            'kilometers']
        asteroidColour = str(randomColour())
        newAsteroid = Asteroid(asteroidName, orbitingBody, potentialHazard, closeApproachDate, estDimMinM, estDimMaxM,
                               float(kilometers_per_second), float(missDistKM), asteroidColour)

        newAstroViz = AsteroidViz(vizFrame, vizPen)
        vizPen.clear()
        newAstroViz.makeViz(vizPen, missDistKM, newAsteroid.estDimAvgM, newAsteroid.asteroidName,
                            newAsteroid.asteroidColour)

        # Save the image after drawing
        # save_turtle_image(vizFrame, self.userDate)

        print("***Asteroid Created***")
        print(newAsteroid.asteroidName)
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
            closeApproachDate = astroJson['near_earth_objects'][self.userDate][i]['close_approach_data'][0][
                'close_approach_date']
            estDimMinM = astroJson['near_earth_objects'][self.userDate][i]['estimated_diameter']['meters'][
                'estimated_diameter_min']
            estDimMaxM = astroJson['near_earth_objects'][self.userDate][i]['estimated_diameter']['meters'][
                'estimated_diameter_max']
            kilometers_per_second = \
            astroJson['near_earth_objects'][self.userDate][i]['close_approach_data'][0]['relative_velocity'][
                'kilometers_per_second']
            missDistKM = astroJson['near_earth_objects'][self.userDate][i]['close_approach_data'][0]['miss_distance'][
                'kilometers']
            asteroidColour = str(randomColour())
            newAsteroid = Asteroid(asteroidName, orbitingBody, potentialHazard, closeApproachDate, estDimMinM,
                                   estDimMaxM, kilometers_per_second, missDistKM, asteroidColour)

            print(str(newAsteroid.ToString()))
            newAsteroidList.append(newAsteroid)

        print("------------ASTEROID LIST TEST------------")
        newAsteroidList.sort(key=lambda x: x.estDimAvgM, reverse=True)

        for j in range(0, len(newAsteroidList)):
            print(str(newAsteroidList[j].ToString()))
            newAstroViz.makeViz(vizPen, newAsteroidList[j].missDistKM, newAsteroidList[j].estDimAvgM,
                                newAsteroidList[j].asteroidName, newAsteroidList[j].asteroidColour)

        # Prepare the list of all asteroids
        asteroid_list_details = Asteroid.listToString(newAsteroidList)

        # Save the image and the consolidated text file
        save_turtle_image(vizFrame, self.userDate, asteroid_list_details)



def draw_background(vizPen, screen_width, screen_height, background_color="#251A21"):
    # Hide the pen while drawing the background
    vizPen.penup()
    vizPen.goto(-screen_width // 2, screen_height // 2)  # Move to the top-left corner
    vizPen.pendown()
    vizPen.fillcolor(background_color)
    vizPen.begin_fill()

    for _ in range(2):
        vizPen.forward(screen_width)
        vizPen.right(90)
        vizPen.forward(screen_height)
        vizPen.right(90)

    vizPen.end_fill()
    vizPen.penup()


def save_turtle_image(screen, user_date, asteroid_list_details, background_color="#251A21", folder="AsteroidVisualizations"):
    # Set Ghostscript path manually if needed
    gs_path = r"C:\Program Files\gs\gs10.03.1\bin\gswin64c.exe"
    EpsImagePlugin.gs_windows_binary = gs_path

    # Create a subfolder inside the main folder based on current timestamp or user_date
    subfolder = os.path.join(folder, user_date)
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    # Save the turtle canvas as a postscript file
    canvas = screen.getcanvas()
    canvas.postscript(file="temp_canvas.ps")

    # Open the postscript file using PIL
    img = Image.open("temp_canvas.ps")

    # Convert to RGB before processing
    img = img.convert("RGB")

    # Create a background image with the same size as the turtle canvas
    background = Image.new("RGB", img.size, background_color)

    # Paste the turtle drawing onto the background
    background.paste(img)

    # Prepare the filename with the user's input date
    base_filename = user_date
    filename = f"{base_filename}.png"
    filepath = os.path.join(subfolder, filename)
    count = 1

    # Check for duplicates and add a number if necessary
    while os.path.exists(filepath):
        filename = f"{base_filename}_{count}.png"
        filepath = os.path.join(subfolder, filename)
        count += 1

    # Save the combined image as PNG
    background.save(filepath)

    # Close the images to release the file
    img.close()

    # Now remove the temporary postscript file
    os.remove("temp_canvas.ps")

    # Prepare the text filename with the user's input date
    text_filename = f"{base_filename}_asteroid_data.txt"
    text_filepath = os.path.join(subfolder, text_filename)
    text_count = 1

    # Check for text file duplicates and add a number if necessary
    while os.path.exists(text_filepath):
        text_filename = f"{base_filename}_asteroid_data_{count - 1}.txt"
        text_filepath = os.path.join(subfolder, text_filename)
        text_count += 1

    # Save the list of all asteroids to a single text file
    with open(text_filepath, 'w') as file:
        file.write(asteroid_list_details)

    print(f"Image saved as {filepath}")
    print(f"Asteroid data saved as {asteroid_list_details}")


vizFrame = turtle.Screen()
vizFrame.bgcolor("#251A21")
vizFrame.setup(width=1920, height=1080)

vizPen = turtle.Turtle()
draw_background(vizPen, 1920, 1080, background_color="#251A21")
runner = AsteroidScanControl()
runner.run()
