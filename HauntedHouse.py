# A console based adventure game
# Created by https://github.com/SomeStrHere
# V: 0.2.0

import sys
from dice import *
from helpers import *
from asciiDrawings import *
from GameLevel import *
from Character import *

def main() :
    
    gameIntroduction()

    
def gameIntroduction() :

    clearConsole(0)
    
    #Character.createRandomCharacter()    # TODO add character generation to start of game
    #Character.createCharacter()          # TODO add character generation to start of game

    print('\n')
    print('Welcome to HAUNTED HOUSE, a text based adventure game.\n')
    # Delays in code execution to improve screen output and the user experience.
    #sleep(0.85) 
    print('You will be presented with numerous choices throughout the game and ' +
          'the choices you make\nwill influence your experience within the game.\n')
    #sleep(3.5)

    # Setting the scene for the start of the game.
    print('You\'ve arrived; the long drive to the house felt longer this evening, much ' +
          'longer, but it\'s late,\nand you\'ve had a few drinks, so you let it slide ' +
          'and collect your belongings from the trunk of the taxi...\nthe driver ' +
          'didn\'t even offer to help; and before anything was said, the driver ' +
          'was tearing off down the drive!\n'
          )

    print('Something doesn\'t feel quite right; unsure if it\'s just the drink and ' +
          'the 2am kebab you slip on your rucksak,\ngrab a holdhall in each hand and look up.')

    #sleep(5)

    print('\nThis isn\'t the house you remember...\n\n')

    #sleep(0.85)
         
    input('~ Press Enter to begin the adventure ~')

    # display the ASCII graphic of the outside of the house
    asciiHouse()

    # Descibre the weather, surroundings, the house and present the user the their first
    # options - TODO

    print('It\'s stormy and foggy; you\'re already soaked through with the rain. but ' +
          'you can tell this isn\'t your family home.\nBeing away travelling since ' +
          'finishing University you expected to see some changes, afterall you\'ve ' +
          'been away for\nalmost a year now... despite that, this is\'t your home...\n'
          )

    print('What it is though is shelter, if this truly isn\'t home; it\'s possible you ' +
          'have no idea where you are, you\'re still\na little drunk, freezing cold and ' +
          'it\'s now approaching 2:30am! What are you going to do...\n'
          )

    gameIntroductionMenu()

def gameIntroductionMenu() :

    varMenu = True

    while varMenu :
        print('Here are your options:\n')
        print('1) Walk up to the front door')
        print('2) Walk up to the garage door')
        print('3) Walk up to the garden gate, it appears to be open')
        print('4) Use your mobile phone')
        print('5) Run away, back down the drive (Exit the game)\n')

        userSelects = input('~ Please enter your (number) choice and press Enter ~\n')

        if userSelects == '1' :
            clearConsole(0)
            print('\nTesting - walk to front door')
            varMenu = False

        elif userSelects == '2' :
            clearConsole(0)
            print('\nTesting - walk to garage door')
            varMenu = False

        elif userSelects == '3' :
            clearConsole(0)
            print('\nTesting - walk to garden gate')
            varMenu = False

        elif userSelects == '4' :
            varMenu = False
            clearConsole(0)
            print('\nYou decide to use your phone and call for help.')

            print('\n# Dice Roll #')
            print('\nIf you roll 1-2... you left your phone in the taxi, doh!\n' +
                  '\nRolling a 3-4; your battery is flat\n' +
                  '\nRolling a 5, you call your friend.' +
                  '\n\nRolling a 6; you call your parents.')
                  #'who are worried about you, say they will try to find you at\n'
                  #'first light and they transfer 250 bit coins into your wallet.'

            input('\n~ Press Enter to roll ~\n')
            roll = diceRoll(6)

            print('\nYou rolled a {0}!\n'.format(roll))

            if roll == 1 or roll == 2 :
                print('Annoyed with yourself for leaving your phone in the taxi, you ' +
                      'walk up to the garage door looking for shelter.')
                # TO DO present user with new scene, options - OOP?

            elif roll == 3 or roll == 4 :
                print('You pull out your phone... and it\'s dead!\n' +
                      'Well that sucks! You quickly think about your options...\n\n' +
                      'You can\'t decide whether to knock on the door so early in the ' +
                      'morning, loaded down with bags and smelling of drink\nor to see if ' +
                      'there would be room to pitch your tent in the garden, and hope ' +
                      'the owners don\'t mind.\n'
                      )

                print('You decide to flip a coin; \'Heads\' you reluctantly knock on the door ' +
                      'and ask for help. If it\'s \'Tails\'; you go\n check out the garden ' +
                      'through what looks like an open gate.')

                input('\n~ Press Enter to flip a coin ~\n')

                coinFace = coinToss()

                print('\nIt\'s {0}!\n'.format(coinFace))

                if coinFace == 'Heads' :
                    print('You walk up to the front door and...')
                    print('TODO, OOP?') # TODO

                elif coinFace == 'Tails':
                    print('You walk up to the garden gate and...')
                    print('TODO, OOP?') # TODO
            
            elif roll == 5 :
                print('You pick up your phone and call a friend...')
                print('TODO, OOP? Remember phone conversation with friend') # TODO

            else : # You rolled a 6
                print('You pick up your phone and call your parents...')
                print('TODO, OOP? Remember to credit bitcoin wallet with 250') # TODO

        elif userSelects == '5' :
            varMenu = False
            clearConsole(0)
            print('\nYou realise you\'ve made a mistake, this doesn\'t feel right, despite ' +
                  'the weather you opt to chase after the taxi.\n'
                  )

            print('# Dice Roll #')
            print('\nIf you roll greater than a 1 on a 6 side dice, you run after the taxi ' +
                  'and the taxi driver notices and stops to\npick you up, which will exit ' +
                  'the game immediatley. If you roll a 1, the taxi driver doesn\'t see you ' +
                  'and\nthe game will exit in 10 seconds.\n'
                  )

            input('~ Press Enter to roll ~')
            roll = diceRoll(6)

            print('\nYou rolled a {0}!\n'.format(roll))

            if roll == 1 :
                print('Exiting game in...')
                diceDelayCountdown(1, 10, roll)

            else :
                sys.exit()
 
        else :
            #TODO implement ability to exit program after x number of errors are given here
            print('\nSorry; that was an invalid option, please try again\n')
            varMenu = True


if __name__ == "__main__" :
    main()
