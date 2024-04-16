'''
# To run this file you MUST use "python main.py (source directory) (destination directory)"
# Example. python main.py data target
# This will specify that we want to get the data from the "data" directory, and paste all the contents into a directory called "target"

# Make sure that you are in the "PythonScripting" directory to avoid errors when running the file.
'''


import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_CMD = ["go", "build"]

def findGamePaths(source):
    gamePaths = []
    
    # This will loop through the given source directory and give the root, directories, and files contained within.
    for root, dirs, files in os.walk(source):
        # dirs will give me the names of the directories, not the full path. By doing this I am getting the full path of these game directories.
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                # Join the game path with the source directory.
                path = os.path.join(source, directory)
                # Append the path to the gamePaths list.
                gamePaths.append(path)

        break

    return gamePaths


# Function takes in the paths to the games in the data directory, and a string value of what to split from the path.
def getNameFromPath(paths, to_strip):
    # Initialize a list to store the directory names.
    newNames = []
    # For each given path, split the full directory path to get just the base directory for each of the games in the data directory.
    for path in paths:
        # This line will split the path and save the last part of the directory to the dirName variable.
        _, dirName = os.path.split(path)
        # This line will remove the "_game" from each of the directories in the data directory.
        newDirName = dirName.replace(to_strip, "")
        # Append the new directory name to the newNames list.
        newNames.append(newDirName)

    return newNames

# Function takes in a path and checks to see if it already exists. If it does not, it will run the mkdir command to create the new directory.
def createDir(path):
    # Checking to see if it does not exist.
    if not os.path.exists(path):
        # Creates the directory using the mkdir command.
        os.mkdir(path)


# Function takes in the source path and a destination path to copy the subdirectories and files into the new destination directory. If it already exists, overwrite it with the new data.
def copyAndOverwrite(source, dest):
    # Checks to see if the destination directory exists. If so, delete the directory and it's contents.
    if os.path.exists(dest):
        # Recursively deletes the directory and everything contained within.
        shutil.rmtree(dest)

    # Copy the contents of the source directory and paste them into the destination directory.
    shutil.copytree(source, dest)


# This function takes in the path and gameDirs so that it can create a JSON file that will contain some data about the games we are performing these actions on.
def make_JSON_metadata_file(path, gameDirs):
    # Create a dictionary that will hold the data about these game directories/files.
    data = {
        "gameNames": gameDirs,
        "numberOfGames": len(gameDirs)
    }
    # Save the dictionary into the dircetory using a context manager. This allows automatic cleanup once the code goes outside of the indentation.
    with open(path, "w") as f:
        json.dump(data, f)


# This function takes in a path that we want to compile the Go code inside of. It locates the files that end with ".go", builds the command to compile and run the code, then calls the function to execute the command.
def compileGameCode(path):
    codeFileName = None
    # Loop through all of the files in the given path.
    for root, dirs, files in os.walk(path):
        # For each file, check to see if the file ends with ".go"
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                codeFileName = file
                # Break because we just want the first one.
                break

        break

    # If there is no .go file found, return back to the program.
    if codeFileName is None:
        return
    
    # Create the command that we will be using to compile and run the .go code files.
    command = GAME_COMPILE_CMD + [codeFileName]
    runCommand(command, path)


# Function takes in the command and the path and runs the command to compile and run the .go code.
def runCommand(cmd, path):
    # Get the current working directory.
    cwd = os.getcwd()
    # Change into the directory of the given path.
    os.chdir(path)

    # Utilizing the PIPE to allow communication between the Python code to the process to run the command.
    result = run(cmd, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    print("Compile Result: ", result)

    # Change back into the current working directory to avoid potiental errors when running many times.
    os.chdir(cwd)


def main(source, target):
    # Get and store the current working directory.
    cwd = os.getcwd()
    # Join the cwd with the given source directory argument.
    sourcePath = os.path.join(cwd, source)
    # Join the cwd with the given target directory argument.
    targetPath = os.path.join(cwd, target)

    # Call the findGamePaths function to get all the game directories in the data directory.
    game_paths = findGamePaths(sourcePath)
    # Call the getNamesFromPaths() function to get the names of each directory that will be created in the new target directory. Strips the "_game" from each directory.
    newGameDirs = getNameFromPath(game_paths, "_game")

    # Create the new directory that we want to copy the data into.
    createDir(targetPath)

    # The zip() function will take matching elements (ie. at the same index) of two arrays and combine them into a tuple, allowing access to them at the same time.
    for src, dest in zip(game_paths, newGameDirs):
        # Joins the target path with the destination path to allow the copyAndOverwrite function to work properly.
        destPath = os.path.join(targetPath, dest)
        # Calling the copyAndOverwrite() function to copy/overwrite the data from the source path into the new destination path.
        copyAndOverwrite(src, destPath)
        # Call the compileGameCode() function to compile and run the .go files.
        compileGameCode(destPath)

    json_path = os.path.join(targetPath, "metadata.json")
    make_JSON_metadata_file(json_path, newGameDirs)


if __name__ == "__main__":
    # This line will get all the command line arguments and store them in a list variable.
    args = sys.argv
    # Checking to make sure that the correct amount of arguments are given.
    if len(args) != 3:
        raise Exception("You must have a soirce and target directory - only.")
    
    # Strips the first argument (Python file name) and stores the other two in variable.
    source, target = args[1:]
    main(source, target)