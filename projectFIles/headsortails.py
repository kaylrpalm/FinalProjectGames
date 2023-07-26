import randomizer
import gameselection

#function flips a coin by randomly generating 1 or 2
def coinflip():
    #coinflip
    coin = randomizer.randomizer(2)
    if coin == 1:
        coin = "H"
    else:
        coin = "T"    
    return coin

#runs the heads or tails game
def headsortails():
    print("\n/////////////////////\n\nWelcome to Heads or Tails.")
    tut = input("Would you like an explanation of the rules?(Y/N)\n")

    #input validation for tutorial prompt
    while True:
        if tut == "Y" or tut == "y":
            print("- In this game, you will start with 250 credits.\n- Each round you will bet an amount and guess if a flipped coin will land on head or tails.\n- The computer will also be playing with its own credits.\n- To win, reach 1000 credits before the computer. \n- If you or the computer reach 0 credits, the other wins automatically.\nHave fun!") 
            break
        elif tut == "N" or tut == "n":
            break
        else: 
             tut = input("Invalid input, please input Y/N.")

    #starting credits 
    playerCred = 250
    comCred = 250
    roundNum = 1 #keeps track of rounds played
    
    #game repeats until either player or computer has reached 0 or 1000 credits
    while (0 < playerCred < 1000) and (0 < comCred < 1000):
        print("\n////// ROUND " + str(roundNum) + " //////\n")
        print("You have " + str(playerCred) + " credits.")

        while True:  #makes sure players cannot bet more than they own
            playerBet = int(input("How many credits would you like to bet?\n"))
            if playerBet > playerCred:
                print("You cannot bet more credits than you have!")
            else:
                break
        
        #computer bets a random percentage of its credits
        comBet = round(comCred * randomizer.randomDecimal())

        print("You have bet " + str(playerBet) + " credits.\nThe computer has bet " + str(comBet) + " credits.\n")

        coinResult = coinflip()
        playerGuess = input("Heads or Tails?(H/T)\n")

        while True:
            # input validation & ensures that input is in uppercase for later equivalency comparisons 
            if playerGuess == "H" or playerGuess == "T":
                break
            elif playerGuess == "h":
                playerGuess = "H"
                break
            elif playerGuess == "t":
                playerGuess = "T"
                break
            else:
                playerGuess = input("Please input a valid value.(H/T)\n")

        #computer guess is randomly generated
        comGuess = coinflip()

        print("The coin has landed on...", end = "")
        if coinResult == "H":
            print ("HEADS!")
        else:
            print ("TAILS!")  

        #players gain credits for correct guesses and lose credits for incorrect ones   
        if playerGuess == coinResult:
            playerCred += playerBet
            print("\nYOU: CORRECT GUESS! Credits added to total.")
        else:
            playerCred -= playerBet
            print("\nYOU: INCORRECT GUESS! Credits subtracted from total.")
        if comGuess == coinResult:
            comCred += comBet
            print("\nCOM: CORRECT GUESS! Credits added to total.")
        else:
            comCred -= comBet
            print("\nCOM: INCORRECT GUESS! Credits subtracted total.")
        
        print("\n/////////////////////\n\nCredit Totals:\nYOU: " + str(playerCred) + "C\nCOM: " + str(comCred) + "C")
        roundNum += 1 #round number is iterated

    if comCred <= 0 or playerCred >= 1000:
        print("\n/////////////////////\n\nYOU WON!\nFinal Score:\nYOU: " +  str(playerCred) + " Credits \nCOM: " +  str(comCred) + " Credits")
        gameselection.wins += 1 #adds to win counter
    else:
        print("\n/////////////////////\n\nYOU LOST!\nFinal Score:\nYOU: " +  str(playerCred) + " Credits \nCOM: " +  str(comCred) + " Credits")
        gameselection.losses += 1 #adds to loss counter
        
    return