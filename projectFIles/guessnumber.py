import randomizer
import gameselection

def guessnumber():
    print("\n/////////////////////\n\nWelcome to Guess the Number.")
    tut = input("Would you like an explanation of the rules?(Y/N)\n")

    #input validation for tutorial prompt
    while True:
        if tut == "Y" or tut == "y":
            print("- In this game, you will have to guess a number within a range you select.\n- You will be told if your guess is higher or lower than the value.\n- You can choose to play with a limited amount of guesses or not.\nHave fun!") 
            break
        elif tut == "N" or tut == "n":
            break
        else:
             tut = input("Invalid input, please input Y/N.\n")

    #allows user to play with unlimited guesses
    limitMode = input("Would you like to play with unlimited guesses?(Y/N)\n")

    while True:
        if limitMode == "Y" or limitMode == "y":
            #remainingGuess = 100
            limitMode = False
            break
        elif limitMode == "N" or limitMode == "n":
            limitMode = True
            print("You will be given 10 guesses.")
            break
        else:
            limitMode = input("Please enter a valid answer.(Y/N)\n")

    #upper is passed to randomizer so it can be used as an upper limit
    upper = input("Please enter the desired upper limit for number selection.\n")
    num = randomizer.randomizer(int(upper))
    guessCount = 0
    remainingGuess = 10

    #loops until number is guessed (for unlimited) or until number of guesses remaining = 0
    while remainingGuess > 0 or limitMode  == False:
        guess = int(input("Guess a number from 1 to " + str(upper) + ".\n"))
        guessCount += 1
        if guess > num:
            print("Your guess was higher than the number.")
        elif guess < num:
            print("Your guess was lower than the number.")
        else:
            print("YOU GUESSED THE CORRECT NUMBER!\nTotal Guesses: " + str(guessCount))
            gameselection.wins += 1
            break
        
        if limitMode == True:
            remainingGuess -= 1
            print("Remaining Guesses: " + str(remainingGuess) + "\n")
    if remainingGuess == 0:
        print("YOU LOST! The correct number was " + str(num) + ".")
        gameselection.losses += 1
    return