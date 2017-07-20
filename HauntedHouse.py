# A console based adventure game
# Created by https://github.com/SomeStrHere
# V: 0.0.1

import sys
from dice import diceRoll
from helpers import *
from asciiDrawings import *

def main() :
    
    startMenu()


def startMenu() :

    clearConsole(0)
    
    print('\n')
    print('Welcome to HAUNTED HOUSE, a text based adventure game.\n')
    # Delays in code execution to improve screen output and the user experience.
    sleep(0.85) 
    print('You will be presented with numerous choices throughout the game and ' +
          'the choices you make\nwill influence your experience within the game.\n')
    sleep(3.5)

    # Setting the scene for the start of the game.
    print('You\'ve arrived; the long drive to the house felt longer this evening, much ' +
          'longer, but it\'s late,\nand you\'ve had a few drinks, so you let it slide ' +
          'and collect your belongings from the trunk of the taxi...\nthe driver ' +
          'didn\'t even offer to help; and before anything was said, the driver ' +
          'was tearing off down the drive!\n'
          )

    print('Something doesn\'t feel quite right; unsure if it\'s just the drink and ' +
          'the 2am kebab you slip on your rucksak,\ngrab a holdhall in each hand and look up.')

    sleep(5)

    print('\nThis isn\'t the house you remember...\n\n')

    sleep(0.85)
         
    input('~ Press Enter to begin the adventure ~')

    # display the ASCII graphic of the outside of the house
    asciiHouse()

    # Descibre the weather, surroundings, the house and present the user the their first
    # options - TODO



if __name__ == "__main__" :
    main()
