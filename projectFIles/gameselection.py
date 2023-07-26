import higherlower
import headsortails
import guessnumber

#global variables keep track of total wins and losses
wins = 0
losses = 0

def gameSelection():
    print("Please select the game you would like to play by inputting the corresponding number.")

    #input validation, only allows for numbers 1-4 to be input, directs to respective games
    while True:
        selection = input("1. Higher Lower \n2. Heads or Tails\n3. Guess the Number\n4. Check Total Score\n")
        if selection == "1":
            higherlower.higherlower()
            break
        elif selection == "2":
            headsortails.headsortails()
            break
        elif selection == "3":
            guessnumber.guessnumber()
            break
        elif selection == "4":
            print("TOTAL SCORE:\nWINS: " + str(wins) + "\nLOSSES: " + str(losses))
            break
        else:
            print("Invalid input, please select the game you would like to play by inputting the corresponding number.")
    return