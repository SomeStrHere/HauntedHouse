# Collection of puzzles for the game

import random
from helpers import *

class Puzzle :
    """Puzzle class."""

    def questionsPuzzle() :

        passed = False
        questionPicker = random.randint(0,4)

        if questionPicker == 0 :
            print('What is the name of the 2 base number system used in computers?')
            answer = input().upper()

            if answer == 'BINARY' or answer == 'BINARY NUMBER SYSTEM' :
                passed = True

            else :
                passed = False

        elif questionPicker == 1 :
            print('Spell the real name of the actor who recently played Wonder Woman in 2017?')
            answer = input().upper()

            if answer == 'GAL GADOT' :
                passed = True

            else :
                passed = False

        elif questionPicker == 2 :
            print('In the computer security sector what does DoS stand for?')
            answer = input.upper()

            if answer == 'DENIAL OF SERVICE' :
                passed = True

            else :
                passed = False

        elif questionPicker == 3 :
            print('What year did Sega release the Sega Saturn console?')
            answer = input()

            if answer == '1995' or answer == '95' :
                passed = True

            else :
                passed = False

        else :
            print('Which INDIVIDUAL PERSON created the Apple 1 computer?')
            answer = input().upper()

            if answer == 'STEVE WOZNIAK' :
                passed = True

            else :
                passed = False

        return(passed)

    def riddlePuzzle() :

        passed = False
        riddlePicker = random.randint(0,4)

        if riddlePicker == 0 :
            print('What can you catch but not throw?')
            answer = input().upper()

            if answer == 'A COLD' or answer == 'COLD' :
                passed = True

            else :
                passed = False

        elif riddlePicker == 1 :
            print(' What is brown and sticky?')
            answer = input().upper()

            if answer == 'A STICK' or answer == 'STICK' :
                passed = True

            else :
                passed = False
                
        elif riddlePicker == 2 :
            print('Mr. Smith has 4 daughters. Each of his daughters has a brother.\n' +
                  'How many children does Mr. Smith have?')
            answer = input().upper()

            if answer == 'FIVE' or '5' :
                passed = True

            else :
                passed = False

        elif riddlePicker == 3 :
            print('During what month do people sleep the least?')
            answer = input().upper()

            if answer == 'FEBRUARY' :
                passed = True

            else :
                passed = False

        else :
            print('There is an ancient invention still used in some parts of the world today\n ' +
                 'that allows people to see through walls.What is it?')
            answer = input().upper()

            if answer == 'A WINDOW' or answer == 'WINDOW' :
                passed = True

            else :
                passed = False

        return(passed)
        
    def randomPuzzle() :

        puzzles = ['questionsPuzzle()', 'riddlePuzzle()']
        aPuzzle = random.choice(puzzles)

        return(aPuzzle)
