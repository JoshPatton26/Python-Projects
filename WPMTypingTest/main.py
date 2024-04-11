import curses
from curses import wrapper
import time
import random

def startScreen(stdscr):
    # Clear out the screen before adding text.
    stdscr.clear()
    # Adding the text to the screen, same as a print() function would. By using the "0, 0" I am specifying where I want the text in the terminal to show up. In this case it will start from the 0th row and 0th column.
    stdscr.addstr(0, 0, "Welcome to my speed typing test!")
    stdscr.addstr("\nPress any key to begin!")
    # Refresh the screen.
    stdscr.refresh()
    # This function is allowing for the text to be displayed on the screen until the user clicks a button. Otherwise, it would show for a millisecond then vanish.
    stdscr.getkey()

def displayText(stdscr, target, current, wpm=0):
    # Add the target text for the user to copy during the test.
    stdscr.addstr(target)

    # Display the WPM underneath the target text.
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    # Changing the color of each letter typed by the user to the green & black color pair, and overwriting the target text with user's text input. 
    # The enumerate() funtion is an easy way to go through a list and get the index and value of the list element.
    for i, char in enumerate(current):
        if current[i] == target[i]:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        else:
            stdscr.addstr(0, i, char, curses.color_pair(2))

# This function is used to read the text from the file and return a randomly selected line from the file.
def loadText():
    with open("text.txt", "r") as f:
        # Read each ine of text and store it in a variable.
        lines = f.readlines()
        # Return a randomly selected line of text from the file.
        return random.choice(lines).strip()

def wpmTest(stdscr):
    # Target text will be displayed on the terminal for the user to copy while being tested.
    targetText = loadText()
    # Used to store the keys that the user types.
    currentText = []

    wpm = 0
    start = time.time()
    stdscr.nodelay(True)

    while True:
        timeElapsed = max(time.time() - start, 1)
        wpm = round((len(currentText) / (timeElapsed / 60) / 5))
        # Clear the terminal from all other text.
        stdscr.clear()

        displayText(stdscr, targetText, currentText, wpm)

        # Refresh the screen.
        stdscr.refresh()

        # Combines the characters of the list together into a string to be able for comparrison.
        if "".join(currentText) == targetText:
            stdscr.nodelay(False)
            break

        # Use the try and except to avoid a 'no input' error with the getkey() function.
        try:
            # Getting the key that the user inputs from keyboard.
            key = stdscr.getkey()
        except:
            continue

        # This is checking to see if the user clicks the 'esc' button to close out the terminal.
        if ord(key) == 27:
            break
        
        # Checking to see if the user is clicking the 'backspace' button so that we can remove the text and not add it to the currentText list. If they click any other button, add to currentText list.
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(currentText) > 0:
                currentText.pop()
        elif len(currentText) < len(targetText):
            currentText.append(key)

    
            
def main(stdscr):
    # Setting up color pairs so that we can change the color of the text in the terminal. First color is text color (foreground) second color is background color.
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    startScreen(stdscr)

    while True:
        wpmTest(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue.")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)