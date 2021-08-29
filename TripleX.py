import sys
import random
from datetime import datetime

def PrintIntroduction(Difficulty):
    print("\n\nYou are a secret agent breaking into a level " + str(Difficulty) + " secure server room...")
    print("You need to enter the correct codes to continue...\n\n")

def PlayGame(Difficulty):
    PrintIntroduction(Difficulty)

    # Note that {random.randint(0,sys.maxsize)} gets a random integer
    # between 0 and a really large number that is meant to be like infinity

    CodeA = random.randint(0,sys.maxsize) % Difficulty + Difficulty
    CodeB = random.randint(0,sys.maxsize) % Difficulty + Difficulty
    CodeC = random.randint(0,sys.maxsize) % Difficulty + Difficulty

    CodeSum = CodeA + CodeB + CodeC
    CodeProduct = CodeA * CodeB * CodeC

    # Print CodeSum and CodeProduct to the terminal
    print("+ There are 3 numbers in the code")
    print("+ The code add-up to: " + str(CodeSum))
    print("+ The code multiply to give: " + str(CodeProduct))

    # Store player guess
    ListGuess = input().split()

    if len(ListGuess) == 3: #Check if the lenght of the user input equal to 3
        GuessA, GuessB, GuessC = ListGuess
        GuessSum = 0
        GuessProduct = 0
        
        if GuessA.isnumeric() and GuessB.isnumeric() and GuessC.isnumeric(): # Check if player typed numbers
            GuessSum = int(GuessA) + int(GuessB) + int(GuessC)
            GuessProduct = int(GuessA) * int(GuessB) * int(GuessC)
            
            if GuessSum == CodeSum and GuessProduct == CodeProduct: # Check if player guess is correct
                print("\n*** Well done agent! You have extracted a file! Keep going! ***")
                return True
            
            else:
                print("\n*** You entered the wrong code! Careful agent! Try again! ***")
                return False
        
        else:
            print( "\n*** Careful agent! You should enter only numbers not characters ***")        
            return False
    else:
        print("\nInvalid input. Please write your input in form X X X and be sure to use only numbers")
    

random.seed(datetime.now().timestamp()) # Create new random sequence based on time of day
LevelDifficulty = 1
MaxDifficulty = 5

while LevelDifficulty <= MaxDifficulty: # Loop the game until all levels are completed
    bLevelComplete = PlayGame(LevelDifficulty)
    if bLevelComplete:
        LevelDifficulty += 1

print("\n*** Great work agent! You got all the files! Now get out of there! ***\n")