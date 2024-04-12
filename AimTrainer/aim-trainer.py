import math
import time
import random
import pygame
pygame.init()

# Initialize the width and height of the window.
WIDTH, HEIGHT = 800, 600

# Create the window and set the title.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

# Initialize some constants for the targets displayed on screen.
TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30

# Initialize the background color.
BG_COLOR = (0, 25, 40)

# Initialize the user's lives.
LIVES = 3
# Initialize the height of the top bar that will hold the users stats during the game.
TOP_BAR_HEIGHT = 50

# Initialize the font that will be used for the stats during and after the game.
LABEL_FONT = pygame.font.SysFont("comicsans", 24)


# Create a class for the targets.
class Target:
    # Set the max size of the target.
    MAXSIZE = 30
    # Set the growth rate of the target (in pixels).
    GROWTHRATE = 0.2
    # Set the primary color of the target.
    COLOR = "red"
    # Set the secondary color of the target.
    SECONDCOLOR = "white"

    # Constructor for the targets to be created.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    # Function used to update the targets, tell them when to grow and when to shrink.
    def update(self):
        # Tells the target to stop growing when it reaches max size.
        if self.size + self.GROWTHRATE >= self.MAXSIZE:
            self.grow = False

        # Tells the target to grow.
        if self.grow:
            self.size += self.GROWTHRATE
        # Tells the target to shrink.
        else:
            self.size -= self.GROWTHRATE

    # Function used to draw the individual targets. each target consists of 4 circles with alternating colors (red and white).
    def draw(self, win):
        # Draws the outer ring of the target (red).
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        # Draws the second biggest ring (white).
        pygame.draw.circle(win, self.SECONDCOLOR, (self.x, self.y), self.size * 0.8)
        # Draws the third ring of target (red).
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        # Draws the smallest (bullseye) of the target (white).
        pygame.draw.circle(win, self.SECONDCOLOR, (self.x, self.y), self.size * 0.4)

    # Function used determine whether the user's click is within the radius of the target.
    def collide(self, x, y):
        # Distance to a point formula.
        dist = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dist <= self.size


# Function is used to draw the different targets every time the frame refreshes.
def draw(win, targets):
    # Fills the screen with the background color.
    win.fill(BG_COLOR)

    # Loops through the targets list and draws all the targets that were on the screen in the last frame, plus the new ones.
    for target in targets:
        target.draw(win)


# Function takes in the seconds elapsed from start of game and formats it in min:sec:milli-secs 
def formatTime(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"

# Function is used to draw the top bar on the screen which is used to display the time, speed, # of hits, and the user's lives during the gameplay.
def drawTopBar(win, elapsedTime, targetsPressed, misses):
    # Draws a rectangle and sets the properties.
    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))
    # Creates the time text to add onto the rectangle.
    time_label = LABEL_FONT.render(f"Time: {formatTime(elapsedTime)}", 1, "black")

    # Calculates the speed of the user clicking the targets.
    speed = round(targetsPressed / elapsedTime, 1)
    # Creates the speed text to add onto the rectangle.
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")

    # Creates the # of hits text to add onto the rectangle.
    hits_label = LABEL_FONT.render(f"Hits: {targetsPressed}", 1, "black")

    # Creates the # of lives text to add onto the rectangle.
    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses}", 1, "black")

    # Adds all the stats labels onto the rectangle.
    win.blit(time_label, (5, 5))
    win.blit(speed_label, (200, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (650, 5))


# Function is used to create the end of game screen which is used to display all the user's stats once the user's lives reaches zero.
def endScreen(win, elapsedTime, targetsPressed, clicks):
    # Fills the screen with the background color.
    win.fill(BG_COLOR)

    # Creates the time text to add onto the end game screen.
    time_label = LABEL_FONT.render(f"Time: {formatTime(elapsedTime)}", 1, "white")

    # Calculates the users click speed.
    speed = round(targetsPressed / elapsedTime, 1)
    # Creates the users speed text to add onto the end game screen.
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "white")

    # Creates the # of hits text to add onto the end game screen.
    hits_label = LABEL_FONT.render(f"Hits: {targetsPressed}", 1, "white")

    # Calculated the users accuracy based on how many clicks were made and which ones were actually hitting a target.
    accuracy = round(targetsPressed / clicks * 100, 1)
    # Creates the users accuracy text to add onto the end game screen.
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "white")

    # Adds all the stat labels onto the end game screen.
    win.blit(time_label, (getMiddle(time_label), 100))
    win.blit(speed_label, (getMiddle(speed_label), 200))
    win.blit(hits_label, (getMiddle(hits_label), 300))
    win.blit(accuracy_label, (getMiddle(accuracy_label), 400))

    # Updates the window to display the end game screen.
    pygame.display.update()

    # Allows for the screen to stay present until the user clicks the "X" button, or presses any other button.
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()


# Function takes in a surface (in this case it is the end of game user stats) and calculates the middle so they can display correctly on the end game screen.
def getMiddle(surface):
    return WIDTH / 2 - surface.get_width()/2


def main():
    # Used to tell the program that the game is currently running.
    run = True
    # Used to store all the targets that are displayed on the screen.
    targets = []
    # Initialize a clock. Used to set the frame rate of the game.
    clock = pygame.time.Clock()

    # Used to track how many targets have been pressed.
    targetPressed = 0
    # Used to track how many times the user has clicked.
    clicks = 0
    # Used to track how many times the user missed a target.
    misses = 0
    # Initializes the start time of the game.
    startTime = time.time()

    # Triggers the user event every 400ms (Draws a new target every 400ms)
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        # Sets the frame rate of the game to 60fps.
        clock.tick(60)
        click = False
        # Gets the mouse click position.
        mousePos = pygame.mouse.get_pos()

        # Calculates teh elapsed time of the gameplay.
        elapsedTime = time.time() - startTime

        # Loops through all the events of the game and checks to see if the user clicks the "X" button. If so, quit the program.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            # generates a new target every 400ms using randomly generated coordinates, while using padding to avoid targets showing up behind the top bar or halfway through the edge.
            if event.type == TARGET_EVENT:
                # Randomly generates the x coordinate
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                # Randomly generates the y coordinate
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                # Creates a new target from teh Target class with the new coordinates.
                target = Target(x, y)
                # Appends the target to the targets list so we can redraw them every time the frame refreshes.
                targets.append(target)
            
            # Gets everytime the user clicks on the screen and increments the value that will be used for stats calculation.
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
        
        # Updates the screen everytime it refreshes and draws the circles back where they were.
        for target in targets:
            target.update()

            # Checks to see if the target reaches the size of zero. if so, remove it from the targets list so the game doesn't start running slower due to using to much storage. Also increments the misses variable.
            if target.size <= 0:
                targets.remove(target)
                misses += 1

            # Used to check is the users click is within the radius of the target. If so, remove the target and increment targetPressed variable which is used to calculate the users hits stat.
            if click and target.collide(*mousePos):
                targets.remove(target)
                targetPressed += 1
        
        # Checks to make sure the users missed targets is not more than the user's lives. If so, end the game.
        if misses >= LIVES:
            endScreen(WIN, elapsedTime, targetPressed, clicks)
        
        # Call the draw() function to begin drawing targets on the screen upon the game start.
        draw(WIN, targets)
        # Call the drawTopBar() function to draw the top bar and user's stats on the top of the screen.
        drawTopBar(WIN, elapsedTime, targetPressed, misses)
        # Update the screen.
        pygame.display.update()

    # Quit the game once the program exits the while loop above.
    pygame.quit()


if __name__ == "__main__":
    main()