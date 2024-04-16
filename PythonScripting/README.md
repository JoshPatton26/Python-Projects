# Python Scripting

This project introduces the idea of using Python to execute system-level commands. The program parses through a directory called "data" and retrieves all the game data from within this directory. It then copies this data into a newly created directory called "target". This project also includes running commands that compile and execute the `.go` game files that are contained within the newly created directory.

## Features

- Parses through the specified directory and retrieves game data.
- Copies game data into a new directory.
- Compiles and runs Go code found within the game directories.
- Generates a metadata JSON file containing information about the games.
- Utilizes commands to create and save a .json file containing data about the games such as the names of the games and the amount of games found.

## Learning Objectives

- Utilizing Python's `os` module for file and directory operations.
- Parsing directory structures using `os.walk()`.
- Working with command-line arguments using `sys.argv`.
- Copying directories and files using `shutil.copytree()`.
- Creating and writing to JSON files.
- Running system commands from within Python using `subprocess.run()`.

## Installation

Clone the repository:
   ```bash
   git clone https://github.com/JoshPatton26/Python-Projects/PythonScripting.git
   ```
Navigate to the correct directory:
   ```bash
   cd ../PythonScripting
   ```
Make sure you have the Go interpreter installed by going to https://go.dev/ and downloading for the respective operating system:

Run the Python file using "python main.py (source directory) (target directory)":
   ```bash
   python main.py data target
   ```

