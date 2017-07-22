from helpers import *
from asciiDrawings import *

# This file contains story board text segments for use within the game.
# Currently setup here as a place holder so text segments can be moved to correct place when required.

#
# Level = Start, player selects option 1 - walk up to the front door
# 
print('\nYou walk up to the front door...\n')
print('The light from the lampost on the drive barley reaches the front door; you can make out ' +
      'the shape of the door, and windows but little more, the house is in darkness.\n')
# Progress into moving the player through to another level
print('# Dice Roll #')
print('Roll 1 - 4 = knock on the door.')
print('Roll 5 = Try to open the door.')
# Start basement level
print('Roll 6 = The doormat is a trapdoor and you fall linto the basement.')
input('\n~ Press Enter to roll ~\n')


#
# Level = Start, player selects option 2 - walk to garage door
#
print('\nYou walk to garage door...\n')
sleep(2)
# Returns printout of ASCII drawing of front of closed garage door
asciiClosedGarageFromStart()
print('\nThe garage is attached to the house, and a thick hedge and fence ' +
      'on the right side stops you from seeing past the garage into the ' +
      'back of the property.\n')
print('# Dice Roll #')
print('Roll a 1 - 8 = Walk to the front door.')
print('Roll 8+ = Walk through the open garden gate.')
input('\n~ Press Enter to roll x2 D6 ~\n')


#
# Level = Start, player selects option 3 - walk to garden gate
#
print('\nYou walk to the garden gate...\n')
print('\nThere is an openning in a large thick hedge with an open gate.\n')
input('\n~ Press Enter to walk through the open gate ~\n')
# Start patio level
clearConsole(0)
# Returns printout of ASCII drawing of front of closed garage door
asciiPatioFromStart()


#
# Level = Start, player selects option 4 - player opts to use mobile phone to call for help
#
# Print outs for option 4 on the start menu are already included in HauntedHouse.py
print('\nYou decide to use your phone and call for help.')
            #elif roll == 3 or roll == 4 :
            #    print('You pull out your phone... and it\'s dead!\n' +
            #          'Well that sucks! You quickly think about your options...\n\n' +
            #          'You can\'t decide whether to knock on the door so early in the ' +
            #          'morning, loaded down with bags and smelling of drink\nor to see if ' +
            #          'there would be room to pitch your tent in the garden, and hope ' +
            #          'the owners don\'t mind.\n'
            #          )

            #    print('You decide to flip a coin; \'Heads\' you reluctantly knock on the door ' +
            #          'and ask for help. If it\'s \'Tails\'; you go\n check out the garden ' +
            #          'through what looks like an open gate.')

# If coin flip result is Heads
('\nYou walk up to the front door and...\n') 
# We could use the same statements for option 1 on start menu
# or create some new statements for this deviation

# If coin flip result is Tails
print('\nYou walk up to the garden gate and...\n')


#
# Level = Start, player selects option 4 - dice roll result = 5
#
print('\nYou pick up your phone and call a friend...\n')


#
# Level = Start, player selects option 4 - dice roll result = 6
#
print('\nYou pick up your phone and call your parents...\n')


#
# Level = Start, player selects option 5 - exit game
#
# Print outs for option 5 on the start menu are already included in HauntedHouse.py