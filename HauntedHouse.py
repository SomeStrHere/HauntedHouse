# A console based adventure game
# Created by https://github.com/SomeStrHere
# V: 0.0.1

import sys
from dice import diceRoll
from helpers import *

def main() :
    
    #pass #TODO
    welcomeScreen()


def welcomeScreen() :

    clearConsole(0)
    print("\n")
    print("                                               | |")
    print("                                              =====")
    print("                                              [   ]")
    print("                    __________________________[___]__________                               ")
    print("                   /                                         \\")
    print("                  /                                           \\")
    print("                 /                                             \\")
    print("                 ------------------------------------------------")
    print("                 |                                               |")


if __name__ == "__main__" :
    main()
