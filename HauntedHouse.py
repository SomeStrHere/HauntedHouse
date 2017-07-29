# A console based adventure game
# Created by https://github.com/SomeStrHere and https://github.com/kieranjen
# V: 0.3.0

import sys
import random
from CharacterCreator import *
from dice import *
from helpers import *
from asciiDrawings import *
from GameLevel import *
from Character import *
from Location import *

def main() :
    
    global interupt
    interupt = False
    gameIntroduction()
    
def gameIntroduction() :
    global locations, character, currentLocation

    clearConsole(0)
    welcomeGraphic()
    input('~ Press Enter to continue ~')
    clearConsole(0)
    # Delays in code execution to improve screen output and the user experience.
    #sleep(0.85) 
    print('\nYou will be presented with numerous choices throughout the game and ' +
          'the choices you make\nwill influence your experience within the game.\n')
    #sleep(3)

    # Setup a user or random generated character
    userCharacterOpt = input('Would you like to setup your own character or use a ' +
                             'randomly generated character?\n\n~ Yes) Character setup ~ ' +
                            '\n\n~ No) Random Character ~ ').upper()

    sleep(0.5)

    characterMenu = True
    while characterMenu :

        if userCharacterOpt == 'YES' or userCharacterOpt == 'Y' :
            characterMenu = False
            print('\n')
            character = CharacterCreator.createCharacter()

        elif userCharacterOpt == 'NO' or userCharacterOpt == 'N' :
            characterMenu = False
            print('\n')
            character = CharacterCreator.createRandomCharacter()

        else :
            print('Invalid  input, please try again')
            sleep(2)
            gameIntroduction()


    locations = createLocations()

    currentLocation = locations['start']

    ## isGameComplete()

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

    #newLocation = currentLocation.choiceToNextLocation()

    #print(newLocation.levelName)

    varMenu = True

    while varMenu :
        print('Here are your options:\n')
        print('1) Walk up to the front door')
        print('2) Walk up to the garage door')
        print('3) Walk up to the garden gate')
        print('4) Use your mobile phone')
        print('5) Run away, back down the drive (Exit the game)\n')

        userSelects = input('~ Please enter your (number) choice and press Enter ~\n')

        if userSelects == '1' :

            entered, nextLocation = locations['lobby'].locationIntroduction(character)

            if(entered == True) :
                locations['lobby'].setAsVisited()
                currentLocation = locations[nextLocation]
                entered, nextLocation = currentLocation.locationIntroduction(character, prevLocation = 'inside')
                currentLocation = locations[nextLocation]
                print(nextLocation)
                entered, nextLocation = currentLocation.locationIntroduction(character)

            else :
                if(nextLocation in locations) :
                    currentLocation = locations[nextLocation]
                else :
                    print("You could not enter the lobby area")
                    print()
                    print("Please choose a new location to visit.")
                    currentLocation.choiceToNextLocation()

            varMenu = False

        elif userSelects == '2' :
            entered, nextLocation = locations['garage'].locationIntroduction(character)

            if(entered == True) :
                locations['garage'].setAsVisited()
                currentLocation = locations['garage']
            else :
                if(nextLocation in locations) :
                    currentLocation = locations[nextLocation]
                else :
                    print("You could not enter the garage area.")
                    print()
                    print("Please choose a new location to visit.")
                    currentLocation.choiceToNextLocation()
            varMenu = False

        elif userSelects == '3' :

            ## Runs the patio introduction and returns whether access has been granted.
            entered, nextLocation = locations['patio'].locationIntroduction(character)

            ## If access is given above then enter the patio area
            if entered == True :
                locations['patio'].setAsVisited()
                currentLocation = locations['patio']

            ## If not given access to the patio area above make the user choose a new location. 
            ## Feel free if yu want to change this to teleport or something
            else :
                if(nextLocation in locations) :
                    currentLocation = locations[nextLocation]
                else :
                    print("You could not enter the patio area")
                    print()
                    print("Please choose a new location to visit.")
                    currentLocation.choiceToNextLocation()
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

            input('\n~ Press Enter to roll ~\n')
            roll = diceRoll(6)

            print('\nYou rolled a {0}!\n'.format(roll))

            if roll == 1 or roll == 2 :
                print('Annoyed with yourself for leaving your phone in the taxi, you ' +
                      'walk up to the garage door looking for some shelter.')
                walk()
                sleep(1.3)
                #TODO

            elif roll == 3 or roll == 4 :
                print('You pull out your phone... and it\'s dead!\n' +
                      'Well that sucks! You quickly think about your options...\n\n' +
                      'You can\'t decide whether to knock on the door so early in the ' +
                      'morning, loaded down with bags and smelling of drink\nor to see if ' +
                      'there would be room to pitch your tent in the garden, and hope ' +
                      'the owners don\'t mind.\n'
                      )

                print('You decide to flip a coin; \'Heads\' you reluctantly knock on the door ' +
                      'and ask for help. If it\'s \'Tails\'; you go\ncheck out the garden ' +
                      'through what looks like an open gate.')

                input('\n~ Press Enter to flip a coin ~\n')

                coinFace = coinToss()

                print('\nIt\'s {0}!\n'.format(coinFace))

                if coinFace == 'Heads' :
                    print('You walk up to the front door and...')
                    walk()
                    sleep(1.3)
                    # TODO
                    # We could use the same statements for option 1 on start menu
                    # or create some new statements for this deviation

                elif coinFace == 'Tails':
                    print('You walk up to the garden gate and...')
                    walk()
                    sleep(1.3)
                    StartToPatioGate('Dead Phone')
            
            elif roll == 5 :
                print('You pick up your phone and call a friend...')
                # Number of dials is random int 2 to 8
                numberofDials = random.randint(2,8)

                for x in range(numberofDials) :
                    print('Dialing...')
                    # 0.5 second delay between each dial
                    sleep(0.5)

                characterName = "" # TODO
                # Start conversation    
                print('Friend: Hello, wha\'s up?')
                sleep(0.3)
                print('{0}: Oh Hi, I need some help...'.format(characterName))
                print('{0}: I got invited to a party on the way back home from travelling...'.format(characterName))
                print('{0}: Looks like I got a little drunk and ended up getting dropped off at a strange house...'.format(characterName))
                print('{0}: Not sure where I am; can you help?'.format(characterName))
                sleep(1)
                print('Friend: That sucks... so you have no idea where you are?')
                sleep(0.3)
                print('{0}: No idea!'.format(characterName))
                sleep(0.3)
                print('Friend: How can I help you then; is anyone around, can you find out where you are?')
                sleep(0.3)
                print('{0}: There is no one around; just this creepy house, and I\'m freezing!'.format(characterName))
                sleep(0.3)
                print('Friend: Yeah; I heard about that crazy storm!')
                print('Friend: Well, you can\'t stay out all night, get some shelter, and I\'ll try and ' +
                     'find you when the storm breaks.')
                print('Friend: Don\'t forget you can pick the door open if you need to ' +
                     'just get some shelter')
                sleep(1)
                print('{0}: Hey yeah, forgot about my lockpicks!'.format(characterName))
                print('{0}: The house looks empty; so I\'ll try picking the lock'.format(characterName))
                sleep(0.3)
                print('Friend: Good plan; if that\'t doesn\'t work, better pitch your tent...')
                print('Friend: Stay safe, hopefully see you soon, bye!')
                sleep(0.3)
                print('{0}: Thanks, bye!'.format(characterName))
                print('\nPhone disconnects')

                print('# Attempt to pick the lock #')
                print('Roll 5+ on a D6 to sucessfully pick the lock and enter the house.')
                # If player doesn't role a 5+ send them to patio level 
                # (they'll need to pitch their tent or break in through the patio doors)

                roll = diceRoll(6)

                if roll >= 5 :
                    entered, nextLocation = locations['lobby'].locationIntroduction(character, deviation = 'Picked Front Door')
                    locations['lobby'].setAsVisited()
                    currentLocation = locations['lobby']
                    # TODO - start Lobby level
                else :
                    print('Picking the lock failed...')
                    ## TODO - What happens if failed?

            else : # You rolled a 6
                print('\nYou pick up your phone and call your parents...\n')

                # Number of dials is random int 1 to 3
                numberofDials = random.randint(1,3)

                for x in range(numberofDials) :
                    print('Dialing...')
                    # 0.5 second delay between each dial
                    sleep(0.5)

                characterName = character.firstName # TODO
                # Start conversation    
                print('Parents: Hello {0}, is everything alright; we expected you hours ago?'.format(characterName))
                sleep(0.3)
                print('{0}: I\'m sorry, I got a taxi after a party  on my way over...'.format(characterName))
                print('{0}: and the taxi dropped me off at a strange house in the middle of nowhere...'.format(characterName))
                print('{0}: Then the storm blew in.'.format(characterName))
                sleep(0.3)
                print('Parents: Oh no!')
                sleep(0.3)
                print('Parents: Are you okay?, we\'re a bit stranded by the storm ourselves...')
                print('Parents: We\'ll wire you some Bitcoins, in case you need them')
                print('Parents: Get shelter as best as you can, and we\'ll come pick you up once the storm breaks')
                sleep(0.3)
                print('{0}: Thank you, I\'ll get some shelter; looks like the house as a garden I can get into'.format(characterName))
                print('{0}: Bye for now'.format(characterName))
                print('Parents: Bye, take care')

                # TODO - Add 200 bitcoins to players bitcoin wallet/balance
                entered, nextLocation = locations['patio'].locationIntroduction(character)

                ## If access is given above then enter the patio area
                if entered == True :
                    locations['patio'].setAsVisited()
                    currentLocation = locations['patio']

                ## If not given access to the patio area above make the user choose a new location. 
                ## Feel free if yu want to change this to teleport or something
                else :
                    if(nextLocation in locations) :
                        currentLocation = locations[nextLocation]
                    else :
                        print("You could not enter the patio area")
                        print()
                        print("Please choose a new location to visit.")
                        currentLocation.choiceToNextLocation()
                varMenu = False

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

def meaningOfLife() :
    print('Now... what\'s the meaning of life? Hmmm')
    answer = input('~ Enter your guess ~ ')
    
    if answer == '42' :
        print('That\'s it!')
        print('Now, you may enter...')
        print('\nYou step inside...')
        locations['start'].setAsVisited()
        currentLocation = locations['lobby']
        #TODO - start Lobby level
                        
    else :
        print('Sorry, that\'s not correct')
        meaningOfLife()


def doorOptions(option) :

    # Argument (option) determines which set of random 
    # diaologues and options are returned to the player
    minInt = 0
    maxInt = 9

    if option == 'all' :
        randomNumber = random.randint(minInt, maxInt)

    elif option == 'locked' :
        randomNumber = random.randint(minInt, 3)

    elif option == 'unlocked' :
        randomNumber = random.randint(4, 7)

    elif option == 'other' :
        randomNumber = random.randint(8, maxInt)

    # The dialogue and options for players to pass through doorways
    # Locked option 1
    if randomNumber == 0 :
       print('The door is locked with a very sophisticated lock\nthere is no way ' +
             'for you - or anyone! to pick this lock; it simply won\'t happen!')
       sleep(1.5)
       print('You take another look at the door...')
       print('While the lock does indeed look formidable; the door and door frame ' +
       'appears\nto only be made out of plywood!')
       sleep(2)
       print('If you\'re big and fit enough you can break through the door!')
       
       if character.heightInFeet >= 4.5 and character.fitnessLevel == 'Great' :
           print('\nSmash!')
           sleep(0.5)
           print('Crash')
           sleep(0.5)
           currentLocation.setAsVisited()
           print('/nYou\'ve done it, you\'ve smashed through the door!')

       else :
            Print('There is no getting through this door; the lock is unbreakable, and a ' +
                  'weakling like you can\'t break through the door either, pathetic!')
            # TODO - finish
            print('You\'d better try another way')
            return(doorOptions('Other'))
            
       
    # Locked option 2
    elif randomNumber >= 1 and randomNumber <= 3 :
        print('This door is locked, but it looks pickable')
        print('Do you have lockpicks?')
        input('~ Press Enter to check if you have lockpicks ~')

        # TODO - how can we check if character is in possession of lockpicks?

        currentLocation.setAsVisited()

    # Unlocked option 1
    elif randomNumber >= 4 and randomNumber <= 7 :
        print('In the darkness, what you mustook for a door,')
        print('was in fact just a curtain.')
        currentLocation.setAsVisited()
        print('You step inside...')

    # Other options
    else :
        print('You walk towards the doorway...')
        sleep(2.5)
        print('Flash!')
        print('A blinding light, explodes around the edges of the door!')
        print('# Dice Roll #')
        #print('Roll a 1-2, you turn away in fright!')
        #print('Roll a 3-4, you kickin the door regardless!')
        #print('Roll a 5-6, you open the door and...')
        roll = diceRoll(6)
        if roll >= 1 <= 2 :
            currentLocation.setAsVisited()
            print('You turn away in fright!')
        elif roll >= 3 <= 4 :
            currentLocation.setAsVisited()
            print('You kick the door in regardless!')
        else :
            currentLocation.setAsVisited()
            print('You open the door and...')


def isGameComplete() :

    # Check if all locations have been visited.
    
    LocationsVistedCounter = 0

    # Loop through each location in list of locations
    for location in locations : 

        # Check if locations as been visited
        if location.checkVisited() == True :
            # Increment counter if location as been visited
            LocationsVistedCounter = LocationsVistedCounter + 1

    # Determine if all locations have been visited
    if LocationsVistedCounter == len(locations) :
        return(gameComplete())

def gameComplete() :

       clearConsole(0)
       # Displays ASCII graphic for finishing the game
       gameFinished()

       # A to start a new game, X to quit
       completeMenu = input().upper()

       if completeMenu == 'A' :
           gameIntroduction()

       elif completeMenu == 'X' :
           sys.exit()

       else :
           clearConsole(0)
           gameComplete()

def delayedAttack(mins, string) :
    pass

if __name__ == "__main__" :
    main()
