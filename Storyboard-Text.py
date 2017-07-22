from helpers import *
from asciiDrawings import *
import random

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
# We could use the same statements for option 3 on start menu
# or create some new statements for this deviation


#
# Level = Start, player selects option 4 - dice roll result = 5
#
clearConsole(0)
print('\nYou pick up your phone and call a friend.\n')

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


#
# Level = Start, player selects option 4 - dice roll result = 6
#
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

# Add 200 bitcoins to characters balance
# Start patio level


#
# Level = Start, player selects option 5 - exit game
#
# Print outs for option 5 on the start menu are already included in HauntedHouse.py