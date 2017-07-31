from dice import *
from Opponents import *
from puzzles import *
from asciiDrawings import *
from HauntedHouse import meaningOfLife
import random

class Location :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        ## Should be assigned in child class. dictKey must be the 
        ## same as the key value used for that object in the locations dictionary
        self.dictKey = ''
        self.levelName = levelName
        self.floor = floor
        self.roof = roof
        self.lighting = lighting
        self.lightType = lightType

        self.connectedRooms = []
        self.properties = {'unlocked': True}

        self.itemsAvailable = []

        self.visited = False
        self.gainedAccess = False

    def checkVisited(self) :
        return self.visited

    def setAsVisited(self) :
        self.visited = True; # Need to chang to entered ?

    def setConnectedLocations(self, rooms) :
        self.connectedRooms = rooms

    def setProperties(self, properties) :
        self.properties = properties

    def setPropertyValue(self, property, value) :
        self.properties[property] = value

    def choiceToNextLocation(self) :
        print("Where do you want to go next?")
        locationNumber = 0;
        for location in self.connectedRooms :
            print(str(locationNumber) + ") " + location.levelName)
            locationNumber += 1

        userChoice = input("What is your choice? ")

        return self.connectedRooms[int(userChoice)].dictKey

    def getAttacked(self, character) :
        attacker = Opponent.createRandomOpponent()
        print('# Attack #')
        sleep(0.3)
        print("You're being attacked by a {0} called {1}".format(attacker.opponentType, attacker.name))
        Opponent.randomAttack()

    def doPuzzle(self) :
        # Run a random puzzle from the Puzzle class
        Puzzle.randomPuzzle()

    def repairWeapons(self, character) :
        print('You spend some time repairing your weapons...')
        # Tools will randomly become broken after they have been used once
        # Using a broken tool will reduce success rate by 30%
        # repairing the tool will remove the decrease in success rate.
        ## TODO
        pass

    def searchLocation(self, character) :
        print('You search the location for items...')
        if(len(self.itemsAvailable) > 0):
            itemFound = random.choice(self.itemsAvailable)
            self.itemsAvailable.remove(itemFound)
            character.getItem(itemFound)
        else :
            print('No items found')


class Garage(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'garage'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
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
                entered = False
                nextLocation = 'lobby'
                # TODO need to actually start the code for entering the front door here
                # How do we call it?
            elif roll >= 9 and roll <= 11 :
                print('The garage doesn\'t offer much help')
                sleep(0.5)
                print('You spot the garden gate at the other side of the property...\n')
                entered = False
                nextLocation = 'patio'
            else :
                print('Lucky you; rolling that double 6!')
                print('You find a key in the darkness, and try it in the garage door')
                print('Wow! You\'r luck knows no bounds...')
                print('You open the garage door just enough to squeeze inside...')
                entered = True
                nextLocation = 'garage'

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif self.visited == False and self.gainedAccess == True :
            ## When inside call this. Set visited as true after called.

            self.visited = True

        else :
            print("You return to the garage.")

        return entered, nextLocation


class Patio(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'patio'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def randomGateOptions(self) :

        print('')
        minInt = 0
        maxInt = 7
        access = True

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
            self.randomGateOptions()

        elif randomNumber == 1 or randomNumber == 2:
            print('The gate as an unusual lock; a riddle lock!?')
            print('Pressing the button marked "Riddle", you hear a voice... although it doesn\'t ' +
                  'appear to be coming from the speaker on the lock')
            print('Answer this simple riddle and the gate will open...')
            sleep(2)
            riddleAnswer = input('What loses its head in the morning and gets it back at night?').upper()
            if riddleAnswer == 'A PILLOW' or riddleAnswer == 'PILLOW' :
                print('That\'s correct... come on in')
                print('What else could you do... you step inside...')
                clearConsole(0)
                asciiPatioFromStart()
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
                asciiPatioFromStart()
                # TODO start Patio level

        elif randomNumber == 3 or randomNumber == 4 :
            print('As you approach the gate, you notice a piece of paper taped to it\n')
            print('It reads\n')
            print('All you have to do to unlock the gate and enter our patio ' +
                  'is\nanswer this simple question')
            noOfWheels = input('"If you have the money to buy any vehicle in the world; how many ' +
                  'wheels will your dream vehicle have?" ')
            if  noOfWheels == '2' :
                print('Click!')
                print('The gate opens and you step inside...')
                clearConsole(2)
                asciiPatioFromStart()
                # TODO start Patio level
            else :
                access = False
                ## Execute your below code in HauntedHouse if the locationIntroduction returns false.
                ## Maybe use a random number to decide what to do.

                ## print('What kind of animal are you1?!')
                ## print('For that answer; we will have to randomly generate a new character for you!\n')
                ## newcharacter = CharacterCreator.createRandomCharacter()
                ## print('\nNow you can enter...')
                ## clearConsole(3)
                ## asciiPatioFromStart()
                # TODO start Patio level

        elif randomNumber >= 5 and randomNumber <= maxInt :
            print('After looking around, you have discovered that this large gate is unlocked.')
            print('Nervously, you open the gate and state inside...')
            sleep(2)
            print('...')
            clearConsole(1.5)
            asciiPatioFromStart()
            #TODO start Patio level

        return access

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'
        ## Only display the introduction stuff if you have not visited before
        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('\nYou walk to the garden gate...\n')
            walk()
            print()
            sleep(1.3)
            allowRoll = diceRoll(6)
            allowedAccess = False
            if(allowRoll >= 1 and allowRoll <=4) :
                allowedAccess = True
            else :
                allowedAccess = False

            if allowedAccess :
                randomDeviation = random.randint(0,1)

                if randomDeviation == 0:
                    print("You attempt to pick the lock of the garden gate...")
                    print()
                    sleep(1.3)
                    print('You manage to pick the lock!')
                    enterCon()
                    clearConsole(1.5)
                    nextLocation = 'patio'

                else :
                    if character.heightInFeet > 6 :
                        print('Being tall as its advantages...')
                        print('You grab hold of a hanging rope, climb up and over the hedge')
                        enterCon()
                        clearConsole(1.5)
                        entered = True
                        nextLocation = 'patio'
                    elif character.heightInFeet < 4 :
                        print('Being short as its advantages...')
                        print('You find a small hole in the hedge and pull yourself through')
                        enterCon()
                        clearConsole(1.5)
                        entered = True
                        nextLocation = 'patio'
                    else :
                        ## Execute the gate options method and decide whther you are given access
                        entered = self.randomGateOptions()

            else :
                print("You attempt to pick the lock of the garden gate...")
                sleep(1.5)
                print("You fail to pick the lock.")
                print()
                print('You hear laughter, but can\'t identify the source...')
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
                    asciiPatioFromStart()
                    entered = True
                    nextLocation = 'patio'
                    # TODO start Patio level
                else :
                    print('Silly fool! mwaaaawhahahahahah')
                    entered = self.randomGateOptions()

            if entered :
                self.gainedAccess = True

        elif self.visited == False and self.gainedAccess == True :
            ## Equivalent to the old 'inside'. Use this to assign visited as True

            self.visited = True

        else :
            ## Simple message if you have been in the patio area already
            print("You've returned to the patio area")

        return entered, nextLocation

    

class Lobby(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'lobby'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
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
                    entered = True
                    nextLocation = 'lobby'

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
                    entered = meaningOfLife()
                    nextLocation = 'lobby'                

                else :
                    print('No, answer; you try again')
                    print('Knock, Knock')
                    sleep(3)
                    print('There is no answer; try the garden gate')
                    nextLocation = 'patio'
                    entered = False

            elif roll == 5 :
                print('You reach out for the door handle and tentatively turn it...')
                sleep(2)
                print('It\'s locked!')
                #TODO add facility to pick the lock

            else :
                print('Surprise!')
                print('You\'ve activated a trapdoor and find yourself in an underground room.')
                enterCon()
                nextLocation = 'basement'
                entered = False
                # TODO start basement level

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :
            print('You are in the lobby.')
            self.visited = True

        else :
            print("You have returned to the lobby area.")

        return entered, nextLocation


class DinningRoom(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'diningRoom'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('\nYou walk towards the dining room....\n')

            # Generate random to determine which type of progression the player
            # makes into the Dinning Room.

            # Decided to not annouce like a dice roll here, because I'd like to keep
            # the player guessing and be surprised.
            progression = random.randint(0,6)

            if (progression == 0) :
                self.lighting = False
                print('Peering inside, with your faced pressed tightly agains the glass; there is little to see\n' +
                      'the place is in total darkness.')
                print('You spot the candle holders, reflecting the moonlight through the storm cloud; it\'s about\n' +
                      'all you can see. Still unsure if this place is abandoned, or at least vacant for the night\n ' +
                      'or sheltering a family, asleep upstairs, you decide to make the best of what shelter you ' +
                      'have with you, your tent.') 
                entered = False
                nextLocation = 'patio'

            elif (progression >= 1 and progression <= 3) :
                self.lighting = True
                light = self.lighting
                print('The room is somewhat iluminated by {0}, but, you can\'t see anyone.'.format(light))
                doorLocked = random.choice['open', 'locked']
                print('Urged on by the storm, you try the door and find it {0}'.format(doorLocked))

                if doorLocked == 'open' :
                    print('Tentatively, you slowly open the door, and prepared to be confronted at any moment, ' +
                          'you step inside... you\'re far too tired, and far too cold\n' +
                          'to wait outside and hope someone finds you before you freeze to death.')

                if doorLocked == 'locked' :
                    print('Not relishing the idea of pitching up your tent on an unknown property, and\n ' +
                          'being so cold, you could audition for Snowman! you knock on the door...\n')
                    print('Knock')
                    sleep(0.5)
                    print('Knock')
                    sleep(1)

                    print('# Dice Roll #')
                    print('Roll = 1-2; all seems well') # door opens on it's own, attack is triggered after time delay
                    print('Roll = 3-4; someone lets you in') # ghost, vampire... unknown to player straight away
                    print('Roll = 5+; something unexpected') # falls unconcious, awakes 1 minute later, etc
                    input('\n~ Press Enter to roll\n')
                    roll = diceRoll(6)

                    if roll == 1 or roll == 2 :
                        print('The lights flicker, as if someone is walking beside them...')
                        print('but, you see no one')
                        sleep(1)
                        print('Click')
                        sleep(0.5)
                        print('The door opens, as if on its own')
                        print('You step inside...')
                        entered = True
                        nextLocation = 'diningRoom'

                        ##timeout(1, attackString)

                        ##attackString = (
                            ##'Insert details of the attack here' # TODO
                            ##)

                        opponent = createRandomOpponent()
                        opponent.itemAttack(character)

                        # Execute hidden delay, can't use time.sleep as I want the delay to be in the background.
                        # I'm researching how best to do the above.
                        # Trigger attack after hidden delay expires.
                        
                    elif roll == 3 or roll == 4 :
                        print('The air grows cold, you shiver and your spine tingles')
                        print('The candles are out, and the thin smoke moves as if to dance')
                        sleep(1)
                        print('A shadow grows larger as it approaches the door')
                        sleep(0.5)
                        print('You can feel the hairs on the back of your neck standing up')
                        print('Relieved and terrified in equal measure, you\'re frozen to the spot')
                        sleep(1)
                        print('In the darkness something reaches towards the door... difficult to see')
                        sleep(0.3)
                        print('Click')
                        sleep(0.3)
                        print('Now unlocked the door swings open')
                        print('The darkness retreats from the doorway, as if to beckon you inside')
                        sleep(0.5)
                        print('You step inside')
                        sleep(0.3)
                        print('Sharply, the door; as if on its own, slams shut behind you')
                        print('Click!')
                        print('You\'re inside now!')
                        print('You glance over to the lights which are now again lit')
                        print('Looking back, whomever opened the door for you, as gone; you appear to be alone')
                        entered = True
                        nextLocation = 'diningRoom'

                    else :
                        print('...?')
                        sleep(2)
                        if self.lighting == True :
                            print('Despite, signs the house is occupied, your knocking appears to go unasnwered')
                        else :
                            print('Despite, the {0}, being lit, your knocking appears to go unanswered'.format(self.lightType))
                        print('then...')
                        sleep(0.5)
                        print('POOF!')
                        sleep(0.3)
                        print('FLASH!')
                        sleep(0.3)
                        print('Dazed and confused you take stock of your surroundings...')
                        print('You\'re surrounded by fog, you can\'t make anything out')
                        sleep(1)
                        print('Then, a voice breaks the silence')
                        sleep(0.5)
                        print('Earthling!')
                        print('Thou shalt not pass... unless')
                        print('You master our little challenge')
                        sleep(1)
                        print('Let the challenge begin!')
                        passed = Puzzle.riddlePuzzle() # TODO - Is this correct; I want this option to be just riddles

                        if passed :
                            print('Congratulations!')
                            print('You have passed our challenge')
                            sleep(1)
                            print('The fog slowly fades; you\'re back, facing the patio doors')
                            print('Swinging open, the doors now out of your way')
                            sleep(0.5)
                            print('You step inside...')
                            entered = True
                            nextLocation = 'diningRoom'
                        else :
                            print('Pity!')
                            sleep(0.5)
                            print('We would have had fun with you...')
                            print('But...')
                            sleep(0.5)
                            print('Rules are rules')
                            print('You can\'t enter here, at least not yet')
                            sleep(0.5)
                            print('Exasperated and still freezing, you step back from the patio doors')
                            entered = False
                            nextLocation = 'patio'
                    
            elif (progression == 3 or progression == 4) :
                print('You can feel the warm eminating from the room; even with no one insight\n' + 
                      'it is a dam sight more welcoming than the freezing cold stormy night outside on the patio!')
                sleep(1)
                print('The doors are locked, but you\'ve made up your mind')
                print('You have little choice... you\'re going to kick your way through the patio doors!')
                sleep(1)
                print('You lunge forward with all your might and...')

                kicksRequired = 0
                
                if character.fitnessLevel == 'Poor' :
                    kicksRequired = 5
                
                elif character.fitnessLevel == 'Okay' :
                    kicksRequired = 4

                else :
                    kicksRequired = 2

                for steps in range(kicksRequired) :
                    print('\nKick!')
                    print('...')
                    sleep(1.5) # Delay between kicks

                print('You\'re through')
                print('No alarms sounded, no one rushed to see what you were doing')
                print('All is well... or is it?\n')
                entered = True
                nextLocation = 'diningRoom'

            else :
                print('You can feel the warm eminating from the room; even with no one insight\n' + 
                      'it is a dam sight more welcoming than the freezing cold stormy night outside on the patio!')
                sleep(1)
                print('A sound, a movement... something makes you look up')
                print('It\'s a window, an open window')
                sleep(1.5)
                print('You\'re far too cold and tired to be pleasent about things, you\'re going inside!')
                print('Stepping back, you take a quick run up and leap for the open window')

                if (character.heightInFeet < 4.5 and character.fitnessLevel == 'Poor') :
                    print('...')
                    sleep(1)
                    print('You give it your best effort, but you\'re not able to pull youself up to where you can\n' +
                          'enter the window.')
                    print('Annoyed, with yourself; you feel defeanted')
                    sleep(0.5)
                    print('What now...')
                    entered = False
                    nextLocation = 'patio'

                else :
                    print('...')
                    sleep(1)
                    print('Got it!')
                    print('You\'ve managed it!')
                    print('Despite the freezing cold and torrential rain, you\'ve managed it!')
                    sleep(1)
                    print('Holding on to the window ledge, you pull yourself up')
                    print('...and through the window you go.')
                    print('You\'re inside...')
                    entered = True
                    nextLocation = 'diningRoom'

                ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True
            
        elif (self.visited == False and self.gainedAccess == True) :
            clearConsole(0)
            print('\nYou walk up to the door...\n') # Entering the dinning room from inside the house

            indoorProgression = random.randint(0,6)

            if (indoorProgression == 0) :
                print('and it swings open in front of you')
                print('You can hear faint chuckling as you step inside, and feel a cool breeze blow across your face')
                print('as if someone left a window open')
                entered = True
                nextLocation = 'Dinning Room'

            elif (indoorProgression >= 1 and indoorProgression <= 3) :
                print('Being mindful of your predicament; being inside a house, which is not your own...')
                print('your nervously knock on the door')
                sleep(0.5)
                print('Knock')
                sleep(0.3)
                print('Knock')
                sleep(0.3)
                print('You hear a voice from inside the room')
                print('"Enter"')
                print('Unsure of what\'s to come, you open the door and step inside')
                print('Looking around the room, you can\'t see anyone... who was it beckoned you in...?')
                entered = True
                nextLocation = 'diningRoom'

            else :
                print('You reach out to grab the handle, and it disapears in front of you; melting into the door!')
                sleep(0.5)
                print('Laughter seems to be all around you')
                sleep(0.5)
                print('You shake you head, as if to see if you\'re dreaming')
                sleep(0.5)
                print('Looking back, the door handle is there oncemore')
                sleep(0.5)
                print('Grabbing the handle, you attempt to open the door')
                print('The handle won\'t turn, the door won\'t open, and worse still...')
                print('You can\'t let go of the door handle, you\'re stuck!')
                sleep(1)
                print('Panic begins to set in... shit!, shit!')
                sleep(0.5)
                print('A "chuckle" can be heard, as if coming from inside the room')
                sleep(0.3)
                print('You like my little tric, huh?')
                print('You\'re too stunned to answer')
                sleep(0.5)
                print('Answer my riddle and you will be free...')
                print('...you don\'t seem to have much choice\n')

                riddleResult = Puzzle.riddlePuzzle()

                if riddleResult :
                    print('Oh, well done; I knew you had it in you')
                    sleep(1)
                    print('Definatley, after first making sure your hand is free; you open the door')
                    print('and step inside...')
                    entered = True
                    nextLocation = 'diningRoom'

                elif riddleResult :
                    print('Oh, that is a shame... "laughter grows louder and louder"')
                    print('Looks like you won\'t be going anywhere')
                    sleep(1)
                    print('Then silence, deadly silence... and you still can\'t remove your hand or open the door')
                    sleep(30)
                    sleep('"hehe')
                    sleep(30)
                    print('"bored now"')
                    print('Flash!')
                    sleep(0.3)
                    print('Your hand is released from the door, and you fall to the ground in a heap!')
                    print('\n~ Are you sure you want to visit the Dinning Room? Y/N ~')
                    userAnswer = input().upper()

                    if userAnswer == 'Y' :
                        sleep(1)
                        print('\nThe door swings open slowly')
                        print('Cautiously, yet determined you enter the Dinning Room')
                        entered = True
                        nextLocation = 'Dinning Room'

                    else :
                        print('You turn away back into the Lobby')
                        print('The door swings ajar and shuts again')
                        print('Doing so repeatedly, as if to mock you\n')
                        entered = False
                        nextLocation = 'lobby'

            self.visited = True

        else :
            print("You have returned to the dinning room.")

        return entered, nextLocation

class Basement(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'basement'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
            # TODO - we need to connect this 'outside' version to the Lobby locationIntroduction
            # So that it runs after the trapdoor is activated.
            clearConsole(0)
            print('Thud!')
            sleep(1)
            print('You hit the floor, and disperse a layer of dust into the air')
            sleep(2)
            print('You pick yourself up and dust yourself down')
            print('It\'s dark, you spin around trying to regain your bearings')
            sleep(2)
            print('Oww!')
            print('^ You found the light fitting!')
            print('It\'s very dark down here, you feel around for the light switch...')
            print('\n# Dice Roll #\n')
            print('Let\'s see if you find the light switch')
            enterCon()
            findSwitch = random.randint(0,1)

            if findSwitch == 0 :
                print('Found it!')
                print('That\'s a rlief, huh')
                print('Click')
                print('1')
                sleep(1)
                print('2...')
                sleep(1)
                print('3..?')
                sleep(1)
                print('WTF!, then you realize... the light doesn\'t have a bulb! doh!')
                print('Now what?')
                enterCon()

            else :
                print('Nothing!')
                sleep(1)
                print('sih!')
                print('You\'re eyes start to adjust to the darkness; but you still can\'t see much')
                print('Now what?')
                enterCon()

            entered = True
            nextLocation = 'basement'

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :
            ## You are INSIDE the location for the first time 
            

            self.visited = True

        else :
            print('You have returned to the basement')

        return entered, nextLocation


class Kitchen(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'kitchen'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'
        #('Kitchen', 'laminate flooring', 'white painted plaster', True, 'downlighters')
        #ConnectedLocations([lobby, utility])

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('Approaching the open doorway, you\'re alert to the sounds and smells of a busy working kitchen,' +
                  'you could be in a restaurant')
            print('About to walk in...')
            sleep(1.5)
            print('The room suddenly becomes silent, as if everyone is now alert to your presence!')
            print('The lights flicker out; the rooms in darkness now, and the silence is deafenning')
            print('You step inside...')
            enterCon()

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :

            ## At the end set visited to true
            self.visited = True
        else :
            print('You have returned to the kitchen')

        return entered, nextLocation

class Utility(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'utility'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'
        #('Utility Room', 'stone tiles', 'white painted plaster', True, 'incandecent bulb')
        #ConnectedLocations([kitchen])

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('You grab the handle of the utility door and try to slide it open')
            print('It\'s very stiff, as if it hasn\'t been used in a long time')
            fitness = character.fitnessLevel
            pulls = 0

            if fitness == 'Poor' :
                pulls = 8
            elif fitness == 'Okay' :
                pulls = 5
            else :
                pulls = 2

            print('Grasping the door handle firmly, you pull!')
            for x in range(pulls) :
                print('and pull...')
                sleep(1)

            print('Finally!')
            print('You manage to slide the door open enough so you can step inside')
            enterCon()

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :

            ## Set visited to true at the end of the call
            self.visited = True
        else :
            print('You have returned to the utility rom')

        return entered, nextLocation

class Library(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'library'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('') # TODO

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :
            clearConsole(0)
            print('') # TODO
            self.visited = True

        else :
            print('You have returned to the library')

        return entered, nextLocation


class MasterBedroom(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'masterBedroom'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('') # TODO

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :

            ## Set visited to true at the end of the method
            self.visited = True

        else :
            print('You have returned to the master bedroom')

        return entered, nextLocation


class SecondBedroom(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'secondBedroom'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('') # TODO

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :

            ## Set visited to true at the end of the method call
            self.visited = True

        else :
            print('You have returned to the second bedroom')

        return entered, nextLocation


class Nursery(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'nursery'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('') # TODO

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :

            ## Set visited to true at the end. This part should only run once.
            self.visited = True

        else :
            print('You have returned to the master nursery')

        return entered, nextLocation


class Landing(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'landing'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('') # TODO

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :

            ## Set visited to true at the end of the method call
            self.visited = True

        else :
            print('You have returned to the landing')

        return entered, nextLocation


class Attick(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'attick'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) :
            clearConsole(0)
            print('') # TODO

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :

            ## Set visited to true at the end of the method call
            self.visited = True

        else :
            print('You have returned to the attick')

        return entered, nextLocation


class Garden(Location) : # Rear garden

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)
        self.dictKey = 'garden'

    def doAction(self, diceRoll, character) :
        changedLocation = False
        nextLocation = ''
        if(diceRoll == 1) :
            ## Go to new location
            nextLocation = self.choiceToNextLocation()
            changedLocation = True
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            nextLocation = self.choiceToNextLocation()
            changedLocation = True

        return changedLocation, nextLocation

    def locationIntroduction(self, character, deviation = '') :
        entered = True
        nextLocation = 'random'

        if(self.visited == False and self.gainedAccess != True) : # User falls throuhg trapdoor from lobby
            clearConsole(0)
            print('') # TODO

            ## Keep at the end of the first if statement
            if(entered == True) :
                self.gainedAccess = True

        elif(self.visited == False and self.gainedAccess == True) :
            clearConsole(0)
            print('') # TODO
            self.visited = True

        else :
            print('You have returned to the garden')

        return entered, nextLocation


def createLocations() :
    locations = {}
    lobby = Lobby('Reception Area', 'hardwood floor', 'ceiling with chandeliers', 
                      True, '2 large chandeliers'
                      )

    basement = Basement('Basement', 'bare earth floor with disturbed ground', 'floorboards', 
                         True, 'incandecent light fitting without a bulb'
                         )

    garage = Garage('Garage', 'concrete floor', 'boarded ceiling',
                       True, 'fluorescent strip lighting'
                       )

    diningRoom = DinningRoom('Dinning Room', 'polished wood floor', 'pattered wallpaper',
                            True, 'candles in holders'
                           )

    kitchen = Kitchen('Kitchen', 'laminate flooring', 'white painted plaster', 
                            True, 'downlighters')

    utility = Utility('Utility Room', 'stone tiles', 'white painted plaster', 
                            True, 'incandecent bulb')

    library = Library('Library', 'stained wood flooring', 'Dark painted plaster', 
                            True, 'floor lamps')

    masterBedroom = MasterBedroom('Master Bedroom', 'carpet', 'white painted plaster', 
                                  True, 'incandecent bulb with shade')

    secondBedroom = SecondBedroom('Second Bedroom', 'carpet', 'white painted plaster', 
                                  True, 'incandecent bulb with shade')

    nursery = Nursery('Nursery', 'carpet', 'white painted plaster', 
                            True, 'incandecent bulb with shade')

    landing = Landing('Landing', 'carpet', 'white painted plaster',
                           True, 'incandecent bulb with shade')

    attick = Attick('Attick', 'bare floorboards', 'bare brick', False, 'n/a')

    start = Location('Start Area', 'gravel drive', None, True, 'street lamp')

    patio = Patio('The Patio', 'grass and paving stones', None, True, 'security light')

    garden = Garden('The Rear Garden', 'grass', None, False, 'n/a')

    start.setConnectedLocations([garage, patio, lobby, basement])
    patio.setConnectedLocations([lobby, garden])
    basement.setConnectedLocations([lobby])
    kitchen.setConnectedLocations([lobby, utility])
    landing.setConnectedLocations([attick, masterBedroom, secondBedroom, nursery])
    lobby.setConnectedLocations([patio, basement, kitchen, garage, diningRoom, library])
    masterBedroom.setConnectedLocations([landing])
    secondBedroom.setConnectedLocations([landing])
    attick.setConnectedLocations([landing])
    utility.setConnectedLocations([kitchen])
    diningRoom.setConnectedLocations([lobby, garden])
    nursery.setConnectedLocations([landing])
    garden.setConnectedLocations([[patio, diningRoom]])
    library.setConnectedLocations([lobby])

    patio.actions = [["You decide to go to a new location.", ]]

    locations['start'] = start
    locations['patio'] = patio
    locations['basement'] = basement
    locations['garage'] = garage
    locations['kitchen'] = kitchen
    locations['landing'] = landing
    locations['lobby'] = lobby
    locations['masterBedroom'] = masterBedroom
    locations['secondBedroom'] = secondBedroom
    locations['attick'] = attick
    locations['utility'] = utility
    locations['diningRoom'] = diningRoom
    locations['nursery'] = nursery
    locations['garden'] = garden
    locations['library'] = library
    return locations

