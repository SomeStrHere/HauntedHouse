# A file containing useful functions related to dice

import random

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


