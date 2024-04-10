# Madlibs Generator

This Python program, Madlibs Generator, reads in a story from the story.txt file and prompts the user to enter a value for each of the words to be replaced. Once the user has entered all the words, it prints out the new story for the user to read.

## How it Works

1. The program reads in a story template from a `.txt` file.
2. It identifies placeholders in the story template, indicated by angle brackets like `<word>`.
3. For each placeholder, the program prompts the user to input a word of the appropriate type (e.g., noun, adjective, name).
4. After the user has provided all the words, the program replaces the placeholders with the user's inputs.
5. Finally, the program prints out the new story with the replaced words for the user to read.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository or download the source code files.
3. Ensure you have a story template saved in a `.txt` file in the same directory as the program.
4. Run the `main.py` file using Python.
5. Follow the prompts to enter words for each placeholder in the story.
6. Once all words are entered, the program will print out the new story with the replaced words.

## Example

Suppose you have a story template saved in a file named `story.txt`. The interaction will go like this:

```
Enter an adjective: happy
Enter a noun: cat
Enter a name: Alice
Enter a place: magical
Enter an animal: dragon
Enter a noun: backpack
Enter an adjective: epic

Once upon a time, there was a happy cat named Alice. Alice lived in a magical place with their pet dragon. One day, Alice decided to go on an adventure. They packed their backpack and set off on their epic journey...
```

