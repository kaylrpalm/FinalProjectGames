import sys
import gameselection

def main():
    print("Welcome! ", end = "")
    #allows user to play games until N is input
    while True:
        #game selection menu
        gameselection.gameSelection()
        cont = input("\n/////////////////////\n\nWelcome back! Would you like to play another game?(Y/N)\n")
        if cont == "y" or cont == "Y":
            continue
        elif cont == "n" or cont =="N":
            print("Thank you for playing.")
            break
    return

if __name__ == '__main__':
    sys.exit(main())
