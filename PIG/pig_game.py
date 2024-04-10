'''
    This program is used to simulate the game PIG. 
    
    The game of PIG is a multiplayer game where each player gets a turn to roll a dice, 
    the player can roll as many times until they choose to stop or roll a 1. If the player 
    rolls a 1, that players score is reset back to 0. Any other number that is rolled by 
    the player will be added to their total score.

    The first player to reach 50 points wins the game.
'''

import random

MAXSCORE = 50

# This function is used to simulate a dice roll using a random value from the range 1-6.
def roll():
    val = random.randrange(1,6)
    return val

# Error checking to make sure the user entered an acceptable value (int and between teh given range).
while True:
    numPlayers = input("How many players would like to play (2 - 4)? ")
    if numPlayers.isdigit():
        numPlayers = int(numPlayers)
        if 2 <= numPlayers <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input, try again.")

# This line is going to generate a list for the number of players and fill the index with the value 0.
playerScores = [0 for _ in range(numPlayers)]

# Loop through the code below until one of the players has has reached the max score of 50
while max(playerScores) < MAXSCORE:  
    '''
        For loop is used to simulate each players turn. 

        Until the while loop below is broken by a user selecting not to roll again, 
        it will keep asking if they want to roll.

        Everytime they choose to roll it updates the playerScore for that user.
    '''
    for idx in range(numPlayers):
        # Shows the users which players turn it is and shows them their total score at the moment their turn begins.
        print("\n#--- Player {}'s turn ---#\n".format(idx+1))
        print("Your total score is: {}\n".format(playerScores[idx]))

        # Used to keep track of the current rounds score.
        currentScore = 0

        '''
                While loop is used to ask the user if they want to roll. 
                If 'y' is entered, it simulates a roll using the roll() function. 
                
                If they enter 'n' then it skips past their turn and onto the next players.
        '''
        while True:
            rollBool = input("Would you like to roll (y) ? ")
            if rollBool.lower() != "y":
                break

            rollVal = roll()

            # If the player rolls a 1, it resets their score to 0 and breaks out of the while loop to go to next players turn.
            if rollVal == 1:
                playerScores[idx] = 0
                print("\n")
                print("\tYou rolled a 1! Turn done.\n")
                break
            else:
                currentScore += rollVal
                print("\n")
                print("\tYou rolled a {} \n".format(rollVal))
            
            # Display the total current rounds score for the player.
            print("\tYour current score for this round is: {}\n".format(currentScore))
        
        # Updates the players total score and shows them what they have.
        playerScores[idx] += currentScore
        print("\nYour total score is: {} \n".format(playerScores[idx]))

        # Checks to see if the player has reached the max score, if so alert the player and quit the program.
        if playerScores[idx] >= MAXSCORE:
            print("!!! PLAYER {} HAS WON THE GAME !!!".format(idx+1))
            quit()