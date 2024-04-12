import curses
from curses import wrapper
import queue
import time

smaller_maze = [
    ["#", "O", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "X", "#"]
]

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", " ", "#"],
    ["#", "#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

larger_maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", " ", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def printMaze(maze, stdscr, path=[]):
    # Initialize the color pairs used to draw the maze and the path.
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    # Loop through the maze and print out each row with all the columns of that row.
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                # If the row and column are in the path, draw RED.
                stdscr.addstr(i, j*2, "X", RED)
            else:
                # If they are NOT in the path, draw BLUE.
                stdscr.addstr(i, j*2, value, BLUE)

def findPath(maze, stdscr):
    # Determine start symbol in the maze.
    start = "O"
    # Determine end symbol in the maze.
    end = "X"
    # Call the findStart() function to get the coordinates for the start of maze.
    startPos = findStart(maze, start)

    # Initialize the Queue data structure.
    q = queue.Queue()
    # Add the starting coordinates to the queue.
    q.put((startPos, [startPos]))

    # Create a set to hold all the visited coordinates of the maze to avoid double checking them.
    visited = set()

    # While the Queue is not empty, keep checking all the possible paths through the maze.
    while not q.empty():
        # Sleep the computer for 0.25 sec to allow better visualation of the algorithim working.
        time.sleep(0.25)
        # Get the current position and the path from the Queue.
        curPos, path = q.get()
        # Get the row and column of the current position.
        row, col = curPos

        # Clear the screen, Draw the maze everytime the algorithm makes a new step through the maze, and refresh the terminal.
        stdscr.clear()
        printMaze(maze, stdscr, path)
        stdscr.refresh()

        # Checking to make sure we havent already reached the end of the maze. If so, return the path.
        if maze[row][col] == end:
            return path
        
        # Call the findNeighbors() function to get the current positions neighbors.
        neighbors = findNeighbors(maze, row, col)
        # Loop through all the neighbor positions to see if they have been visited.
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            # Get the row and column of the neighbor.
            r, c = neighbor
            # Check to see if the neighbor is a wall. If so, skip it.
            if maze[r][c] == "#":
                continue
            
            # Add the valid neighbors to the path.
            newPath = path + [neighbor]
            # Add the neighbor and new path to the Queue.
            q.put((neighbor, newPath))
            # Add the neighbors to the visited set to avoid double checking them.
            visited.add(neighbor)

# Function used to check the current positions neighbors.
def findNeighbors(maze, row, col):
    # Used to store the neighbors.
    neighbors = []

    # Check to see if the surrounding neighbors are valid neighbors, not walls of the maze.
    if row > 0: # CHECK UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): # CHECK DOWN
        neighbors.append((row + 1, col))
    if col > 0: # CHECK LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): # CHECK RIGHT
        neighbors.append((row, col + 1))

    return neighbors


# Function used to loop through the maze to find the starting position.
def findStart(maze, start):
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == start:
                return i, j
    
    # If not starting position is found, return None.
    return None


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.addstr("Please enter a value of what size maze you would like to solve? (1 = small, 2 = medium, 3 = large): ")
    key = stdscr.getch()

    if chr(key) == "1":
        findPath(smaller_maze, stdscr)
        stdscr.getch()
    elif chr(key) == "2":
        findPath(maze, stdscr)
        stdscr.getch()
    elif chr(key) == "3":
        findPath(larger_maze, stdscr)
        stdscr.getch()

wrapper(main)