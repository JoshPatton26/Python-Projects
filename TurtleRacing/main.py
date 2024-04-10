import turtle
import time
import random

# Constants used to determine the size of the screen.
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

# Function used to get the number of turtles that will be raced. Performs error checking to make sure the input is valid.
def getNumOfTurtles():
    racers = 0
    while True:
        racers = input("How many racers would you like to race? (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input, try again!")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Please enter a value between 2 - 10")

# Function is used to begin the race and generate random values for each racer to move until one reaches the finish line.
def race(colors):
    # Create the turtles and put them into starting position.
    turtles = createTurtles(colors)
    while True:
        for racer in turtles:
            # Generate a random distance for the racer to move.
            dist = random.randrange(1, 20)
            racer.forward(dist)

            # Get the coordinates of the racer.
            x, y = racer.pos()
            
            # Checks to see if the racer has passed the finish line.
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

# Function used to create all the turtles, set the distinct colors, and get them into starting position.
def createTurtles(colors):
    # List used to store all the different racers with their unique attributes.
    turtles = []
    # Gets the equal spacing between the edges of the screen and the distance between each racer.
    spacing = WIDTH // (len(colors) + 1)
    # Loops through the colors array and creates a new racer with the color at that index.
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
        
    return turtles

# Function used to initialize the Python Turtle screen, setting it on top of all other applications, and setting the attributes of the screen.
def initTurtle():
    # Creating the screen.
    screen = turtle.Screen()

    # These three lines below are used to place the Turtle screen on the topmost position of the screen. That way you can see the screen without closing/moving any other application.
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

    # Setting the screens attributes: width, height, and title.
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

# Calls the function to get the user input for how many racers there will be.
racers = getNumOfTurtles()
# Initialize the Python Turtle screen.
initTurtle()
# This line is shuffling the COLORS array so that the numbers are different evertime the program is ran.
random.shuffle(COLORS)
# By using the ":" symbol we are slicing the array by the given value. In this case we are slicing the array to be the same length and the number if racers.
colors = COLORS[:racers]

# Begin the race!!!
winner = race(colors)
print("The winner is the {} turtle!!!".format(winner))