# WPM Typing Test

WPM Typing Test is a Python project that allows users to test their typing speed within the terminal. It utilizes the curses module to facilitate text modification within the terminal environment, the time module to track the progress of the user, and the random module to randomly select a line of text from a .txt file.

## Learning Objectives

- Utilizing the curses module to manipulate text within the terminal environment.
- Implementing a typing test to measure typing speed.
- Utilizing the time module to track user progress.
- Utilizing the random module to randomly select text for typing.

## Features

- Displays a line of text for the user to type.
- Calculates typing speed in words per minute (WPM).
- Highlights correct and incorrect characters typed by the user.
- Prompts the user to play again after completing a test.
- Libraries included: 'curses', 'time', and 'random'. 

## Usage

1. Run the Python script `main.py`.
2. Follow the instructions displayed in the terminal:
   - Press any key to start the typing test.
   - Type the displayed text as accurately and quickly as possible.
   - Correctly typed characters are displayed in green, while incorrectly typed characters are displayed in red.
   - After completing the test, the WPM (words per minute) score is displayed.
   - Press any key to play again or press the 'esc' key to exit.

## Installation

Clone the repository:
   ```bash
   git clone https://github.com/your-username/wpm-typing-test.git
   ```
Navigate to the correct directory:
   ```bash
   cd ../WPMTypingTest
   ```
Make sure the libratries are installed:
   ```bash
   pip install TIME-python
   ```
   ```bash
   pip install windows-curses
   ```
Run the Python file:
   ```bash
   python main.py
   ```
