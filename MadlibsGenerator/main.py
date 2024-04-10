'''
    By using the 'with open()' function. It sets a context for this program so that we can do normal operations 
    and the program knows we are reading from the story.txt file. When we go outside of the indentation, the 
    program will automatically clean up the file and set everything back as it was. By using the "r" argument 
    we are setting 'read-only' permissions.

    Noun = a person, place, action, or thing. eg. cake, shoes, school bus, Joshua Patton, singing.
    Adjective = used to describe a noun. eg. fluffy (noun: cake), Basketball (noun: shoes).


'''
with open("story.txt", "r") as f:
    story = f.read()

words = set()
startOfWord = -1

targetStart = "<"
targetEnd = ">"

# Loop through the story to find all the words that will be swapped with user's input.
for i, character in enumerate(story):
    # This is locating the opening angle bracket "<" and setting the startOfWord equal to that index.
    if character == targetStart:
        startOfWord = i

    # This is locating the closing angle bracket ">" and making sure that the matching startOfWord (opening angle bracket) was found.
    if character == targetEnd and startOfWord != -1:
        # This line is splicing the targeted word out of the story so that we can save it to a list.
        word = story[startOfWord: i + 1]
        # Adding the target word into our list of words to be replaced.
        words.add(word)
        # Resetting the startOfWord variable to -1 to find the next word.
        startOfWord = -1

# Dict to store all the users input for the word to be replaced.
answers = {}

# Loops through the words and allows the user to input a value for the matching word.
for word in words:
    answer = input("Enter a word for {}: ".format(word))
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

# Prints the story with the words replaced by user's input.
print("\n")
print(story)