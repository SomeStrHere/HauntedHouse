# A file containing useful functions related to dice

import random
from helpers import *

def diceRoll(maxInt) :
    """Returns a pseudo random dice roll of range 1 through x.

    Will generated a pseudo random dice roll based on the number of sides of the dice, given
    as x. The result will be returned as diceResult.
    
    Args : maxInt (int) : An int for the maximum range, i.e no. of sides of the dice, from which
                          a random number representing a dice roll will be generated..

    Returns : diceResult (int) : An int representing the result of rolling the dice.
    
    """

    diceResult = random.randint(1, maxInt)

    return(diceResult)

def diceDelayCountdown(diceNumber, delay, roll) :
    """Prints a countdown to the user with a corresponding execution delay.

    Prints a countdown to the user and pauses code execution between each count; the count
    and delay depends on the arguments given when called.
    
    Args : diceNumber (int) : An int representing the dice roll result which triggers the
                              countdown delay condition.

    Args : delay (int, float) : An int or float representing the length of the count and
                                corresponding delay; set at 1 second between count.

    Args : roll (int) : An int representing the result of previously called diceRoll()
    
    """

    if diceRoll(roll) == diceNumber :
        for x in range(delay) :
            print(x)
            sleep(1)
            x = (x + 1)
    else :
        pass
    

