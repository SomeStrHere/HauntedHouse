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
    print("                    __________________________[   ]__________")
    print("                   /                                         \\")
    print("                  /                                           \\")
    print("                 /                                             \\")
    print("                 ------------------------------------------------")
    print("                 |                                               |")
    print("                 |   __________        _____         __________  |")
    print("                 |   |         |       |   |         |        |  |")
    print("                 |   |         |       |   |         |        |  |")
    print("                 |   |         |       |   |         |        |  |")
    print("                 |   |         |       =====         |        |  |")
    print("                 |   ===========                     ==========  |")
    print("                 |                                               |_________________________")
    print("                 |                                               |                        \\")
    print("                 |   ________________                _________   |                         \\")
    print("~~~~~~~~~~~~~~~~~|   |              |    ________    |       |   |                           |")

if __name__ == "__main__" :
    main()
