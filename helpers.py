# A file containing useful generic functions, such as for clearing the console.

import random

def clearConsole(wait) : #function to clear console on Linux or Windows
    """Clears console, with optional time delay.

    Will attempt to clear the console for Windows, should that fail it will attempt to clear the
    console for Linux.
    
    Args : wait (int or float) : A value representing how long time.sleep() should delay
           execution.
    
    """

    import time
    time.sleep(wait) 
    # produces a delay based on the argument given to clearConsole()
    
    import os

    try :
       os.system('cls') #clears console on Windows

    except :
       os.system('clear') #clears console on Linux

def sleep(wait) :
    """Delays program execution with the dealy given as 'wait'.
    
    Args : wait (int or float) : A value representing how long time.sleep() should delay
           execution.
    
    """
    import time 

    time.sleep(wait)


def coinToss() :

    coinFaces = ["Heads", "Tails"]

    index = random.randint(0,1) 

    return (coinFaces[index])
