# A console based adventure game
# Created by https://github.com/SomeStrHere
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
    
    gameIntroduction()
    
def gameIntroduction() :
    global locations, character

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

    isGameComplete()

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
            clearConsole(0)
            print('\nYou walk up to the front door...\n')
            walk()
            sleep(1.3)
            print('\nThe light from the lampost on the drive barley reaches the front door; you can make out ' +
            'the shape of the door,\nand windows but little more, the house is in darkness.\n')
            print('# Dice Roll #')
            print('Roll 1 - 4 = knock on the door.')
            print('Roll 5 = Try to open the door.')
            print('Roll 6 = ... sssh it\'s a surprise!')
            input('\n~ Press Enter to roll ~\n')
            roll = diceRoll(6)
            print('\nYou rolled a {0}!\n'.format(roll))
            if roll  <= 4 :
                print('Knock, Knock...')
                sleep(2)
                randomOption = random.randint(0,2)

                if randomOption == 0 :
                    print('Creeeeaaak')
                    print('The front door slowly opens!!!')
                    sleep(1)
                    print('You can only see darkness; and can\'t make anything out; ' +
                          'you step inside...')
                    locations[0].setAsVisited()
                    #TODO - start Lobby level
                    input() # Here to pause program execution during development

                elif randomOption == 1 :
                    print('What was that...?')
                    sleep(1)
                    print('There it is again... very faint; difficult to make out ' +
                          'but growing louder')
                    print('Whooooo gooooeesss theerrrrreeee?????')
                    sleep(2.5)
                    print('WTF!')
                    print('"This is certainly creepy"')
                    print('"How much did I have to drink...?"')
                    sleep(2.5)
                    print('\nYou try to introduce yourself and explain your situation, ' +
                          'but are interupted...')
                    print('If you want to come in here, you\'ll need the password')
                    sleep(1)
                    print('"The password!"')
                    sleep(0.3)
                    print('All you have to do is tell me the meaning of life?')
                    sleep(0.5)
                    print('"Well, I can\'t stay out here all night"')
                    meaningOfLife()                

                else :
                    print('No, answer; you try again')
                    print('Knock, Knock')
                    sleep(3)
                    print('There is no answer; try the garden gate')
                    StartToPatioGate()

            elif roll == 5 :
                print('You reach out for the door handle and tentatively turn it...')
                sleep(2)
                print('It\'s locked!')
                #TODO add facility to pick the lock

            else :
                print('Surprise!')
                print('You\'ve activated a trapdoor and find yourself in an underground room.')
                locations[0].setAsVisited()
                # TODO start basement level
                # TODO declare basement level as visited?

            varMenu = False

        elif userSelects == '2' :
            clearConsole(0)
            print('\nYou walk up to the garage door...\n')
            # Walk() will produce a series of strings using sleep(x) to delay each statement.
            walk()
            sleep(1.5)
            # Returns printout of ASCII drawing of front of closed garage door
            asciiClosedGarageFromStart()
            print('\nThe garage is attached to the house, and a thick hedge and fence ' +
                  'on the right side stops you from seeing past\nthe garage into the ' +
                  'back of the property.\n')
            print('# Dice Roll #')
            print('Roll a 1 - 8 = Walk to the front door.')
            print('Roll 9 - 11 = You try the other side of the property.')
            print('Roll double 6... and something else may happen')
            input('\n~ Press Enter to roll x2 D6 ~\n')
            roll = diceRoll(12)
            print('\nYou rolled a {0}!\n'.format(roll))
            if roll <= 8 :
                walk()
                doorOptions('all')
            elif roll >= 9 and roll <= 11 :
                print('The garage doesn\'t offer much help')
                sleep(0.5)
                print('You spot the garden gate at the other side of the property...')
                walk()
                sleep(1.3)
                print('You\'re in luck the gate as been left open')
                input('~ Press Enter to go through the gate ~')
                locations[0].setAsVisited()
                asciiPatioFromStart()
                # TODO start Patio level
            else :
                print('Lucky you; rolling that double 6!')
                print('You find a key in the darkness, and try it in the garage door')
                print('Wow! You\'r luck knows no bounds...')
                print('You open the garage door just enough to squeeze inside...')
                locations[0].setAsVisited()
                # TODO - start Garage level
            varMenu = False

        elif userSelects == '3' :
            clearConsole(0)
            print('\nYou walk to the garden gate...\n')
            walk()
            sleep(1.3)
            StartToPatioGate('')
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
                    print('Congratulations! You picked the lock and step inside...')
                    locations[0].setAsVisited()
                    # TODO - start Lobby level
                else :
                    print('Picking the lock failed...')
                    StartToPatioGate('Failed Pick Front Door')

            else : # You rolled a 6
                print('\nYou pick up your phone and call your parents...\n')

                # Number of dials is random int 1 to 3
                numberofDials = random.randint(1,3)

                for x in range(numberofDials) :
                    print('Dialing...')
                    # 0.5 second delay between each dial
                    sleep(0.5)

                characterName = "" # TODO
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
                # TODO - start Patio level

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
        locations[0].setAsVisited()
        #TODO - start Lobby level
                        
    else :
        print('Sorry, that\'s not correct')
        meaningOfLife()


def StartToPatioGate(deviation) :
    # Function to set the scene for progressing the player from the Start level to the Patio level. 

    deviation = ''

    if deviation == 'Dead Phone' :
        randomDeviation = random.randint(0,1)

        if randomDeviation == 0:
            print('Lucky you! The gate is open afterall')
            print('~ Press Enter to go through the gate ~')
            clearConsole(1.5)
            locations[0].setAsVisited()
            asciiPatioFromStart()
           #TODO start Patio level

        else :
            if character.heightInFeet > 6 :
                print('Being tall as its advantages...')
                print('You grab hold of a hanging rope, climb up and over the hedge')
                clearConsole(1.5)
                locations[0].setAsVisited()
                asciiPatioFromStart()
                #TODO start Patio level
            elif character.heightInFeet < 4 :
                print('Being short as its advantages...')
                print('You find a small hole in the hedge and pull yourself through')
                clearConsole(1.5)
                locations[0].setAsVisited()
                asciiPatioFromStart()
            else :
                randomGateOptions(0)

    elif deviation == 'Failed Pick Front Door' :
        print('You walk back towards the garden gate')
        walk()
        print('As you approach the gate, you hear laughter, but can\'t identify the source...')
        print('hhehe, silly child; can\'t even pick a lock')
        sleep(1)
        print('Not sure if you\'ve passed out and are having a weird dream ' 
              ',\nyou hear the same voice again')
        print('Tell you what...')
        print('If you can tell guess my favorite super hero, I\'ll open the gate...' )
        superHero = input('~ Have a guess at the super hero and press Enter ~').upper()
        if superHero == 'BATMAN' :
            print('That\'s it!, come on in...')
            sleep(1)
            print('As nervous as ever, you step inside the now open gate')
            clearConsole()
            locations[0].setAsVisited()
            asciiPatioFromStart
            # TODO start Patio level
        else :
            print('Silly fool! mwaaaawhahahahahah')
            randomGateOptions()

    else : # If this isn't a deviation
        clearConsole(1)
        print('\nAt the  left hand side of the house, there is a very large hedge; and a fence behind that.')
        print('The hedge is too thick to climb through and too high for you to attempt to climb over.')
        sleep(1.5)
        print('\nLuckily')
        sleep(0.3)
        print('\n...or not')
        sleep(0.5)
        print('\nThere is an openning with a large gate.')
        sleep(0.5)
        print('If you could get through; you might be able to find shelter or get some help...')
        input('\n~ Press Enter to see what happens next ~')
        randomGateOptions(0)
   

def randomGateOptions(skipInt) :

    print('')
    skipInt = 0
    minInt = 0
    maxInt = 9

    # TODO - This commented out code block bellow is designed to stop a user
    # from randomly generating the "wait 20 seconds" option back to back (buggy atm)

    #while skipInt != 1 :
    #    randomNumber = random.randint(minInt, maxInt)
    #randomNumber = random.randint(1, maxInt)

    randomNumber = random.randint(minInt, maxInt)

    if randomNumber == 0 :
        print('Woahhh')
        print('You appear to be stuck within the space time continum!')
        print('It\'ll take you 20 seconds to become unstuck...')
        for x in range(20) :
            print(x)
            sleep(1)
            x = (x + 1)
        print('You\'re still outside the gate.. let\'s try again...')
        randomGateOptions(1)

    elif randomNumber == 1 or randomNumber == 2:
        print('The gate as an unussual lock; a riddle lock!?')
        print('Pressing the button marked "Riddle", you hear a voice... although it doesn\'t ' +
              'appear to be coming from the speaker on the lock')
        print('Answer this simple riddle and the gate will open...')
        sleep(2)
        riddleAnswer = input('What loses its head in the morning and gets it back at night?').upper()
        if riddleAnswer == 'A PILLOW' or riddleAnswer == 'PILLOW' :
            print('That\'s correct... come on in')
            print('What else could you do... you step inside...')
            clearConsole(0)
            locations[0].setAsVisited()
            asciiPatioFromStart
            # TODO start Patio level
        else :
            print('Thou shalt not pass!')
            sleep(2)
            print('Kidding... wait for 1 minute... only then can you enter!')
            sleep(15)
            print('...')
            sleep(15)
            print('...time ain\'t up yet...')
            sleep(30)
            print('...???')
            sleep(60)
            print('Oops; actually forgot about you there...')
            print('Thou shalt pass!')
            clearConsole(0)
            locations[0].setAsVisited()
            asciiPatioFromStart
            # TODO start Patio level

    elif randomNumber == 3 or randomNumber == 4 :
        print('As you approach the gate, you notice a piece of paper taped to it\n')
        print('It reads\n')
        print('All you have to do to unlock the gate and enter our patio ' +
              'is\nanswer this simple question')
        noOfWheels = input('"If you have the money to buy any car in the world; how many ' +
              'wheels will your dream vehicle have?" ')
        if  noOfWheels == '2' :
            print('Click!')
            print('The gate opens and you step inside...')
            clearConsole(2)
            locations[0].setAsVisited()
            asciiPatioFromStart()
            # TODO start Patio level
        else :
            print('What kind of animal are you1?!')
            print('For that answer; we will have to randomly generate a new character for you!\n')
            newcharacter = CharacterCreator.createRandomCharacter()
            print('\nNow you can enter...')
            clearConsole(3)
            locations[0].setAsVisited()
            asciiPatioFromStart()
            # TODO start Patio level
            
    elif randomNumber >=5 and randomNumber <= 7 :
        # TODO - something else
        print('As you start looking at the gate at the side of the house; you notice a shiny coin ' +
              'on the floor and pick it up')
        print('The coin as "Teleportation Coin" written on it... so you give it a toss')
        headsOrTails = coinToss()
        if headsOrTails == 'Heads' :
            locations[0].setAsVisited()
            print('Woooooooooooooooooooooooossssshhhh')
            print('You\'re not outside anymore!')
            print('You\'ve been teleported to...')
            sleep(2)
            print('A nursery!')
            # TODO start Nursery level
            input() # Development / Testing

        else :
            locations[0].setAsVisited()
            print('Shiiiiiiiiiiiiiiiiiiiiiittttttt!!!')
            print('You\'re not outside anymore!')
            print('You\'ve been teleported to...')
            sleep(2)
            print('hmmmm... you have no idea!')
            # TODO start Attick level

    elif randomNumber >= 8 and randomNumber <= maxInt :
        print('After looking around, you have discovered that this large gate is unlocked.')
        print('Nervously, you open the gate and state inside...')
        sleep(2)
        print('...')
        clearConsole(1.5)
        locations[0].setAsVisited()
        asciiPatioFromStart()
        #TODO start Patio level


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
           locations[0].setAsVisited()
           return(print('/nYou\'ve done it, you\'ve smashed through the door!'))

       else :
            Print('There is no getting through this door; the lock is unbreakable, and a ' +
                  'weakling like you can\'t break through the door either, pathetic!')
            # TODO - finish
            locations[0].setAsVisited()
       
    # Locked option 2
    elif randomNumber >= 1 and randomNumber <= 3 :
        print('Testing - Locked option 2')
        locations[0].setAsVisited()

    # Unlocked option 1
    elif randomNumber >= 4 and randomNumber <= 7 :
        print('Testing - Unlocked option 1')
        locations[0].setAsVisited()

    # Other options
    else :
        print('Testing - Other options')
        locations[0].setAsVisited()


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


if __name__ == "__main__" :
    main()
