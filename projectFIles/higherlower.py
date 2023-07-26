import randomizer
import gameselection

def higherlower():
    print("\n/////////////////////\nWelcome to Higher Lower.")
    tut = input("Would you like an explanation of the rules?(Y/N)\n")

    #input validation for tutorial prompt
    while True: 
        if tut == "Y" or tut == "y":
            print("- A number between 1 and a number of your choice will be randomly generated.\n- This number will be revealed to you.\n- After this number is revealed, a second number will be generated.\n- In order to gain a point, you must guess if this unknown second number is higher or lower than the first number.\n- If you guess incorrectly, the computer gains a point.\n- The first to reach 5 points wins.\n Have fun!") 
            break
        elif tut == "N" or tut == "n":
            break
        else: #input validation
             tut = input("Invalid input, please input Y/N.")

    #upper is used to randomize number
    upper = input("Please enter the desired upper limit for number selection.\n")
    userPoints = 0
    cpuPoints = 0
    roundNum = 1
    
    while userPoints < 5 and cpuPoints < 5:
        num1 = randomizer.randomizer(int(upper))
        num2 = randomizer.randomizer(int(upper))

        while True:
            if num1 > num2:
                result = "L"
                break
            elif num1 < num2:
                result = "H"
                break
            else: #generated numbers are the same, loops until they are different
                num2 = randomizer.randomizer(int(upper))
        
        print("\n////// ROUND " + str(roundNum) + " //////\n")
        print("The number is " + str(num1) + ".")
        guess = input("Do you think the next number is higher or lower than the first?(H/L)\n")
        
        # ensures that input is in uppercase for later equivalency comparisons
        if guess == "h":
            guess = "H"
        if guess == "l":
            guess = "L"
        
        if guess == result:
            userPoints += 1
            print("You were correct! The first number was " + str(num1) + " and the second number was " + str(num2) + "." )
        else:
            cpuPoints +- 1
            print("You were incorrect! The first number was " + str(num1) + " and the second number was " + str(num2) + "." )

        print("Points: " + str(userPoints))
        roundNum += 1

    if userPoints == 5:
        print("YOU WON!\nScore: " +  str(userPoints) + " - " + str(cpuPoints))
        gameselection.wins += 1
    else: 
        print("YOU LOST!\nScore: " +  str(userPoints) + " - " + str(cpuPoints))
        gameselection.losses += 1
    return