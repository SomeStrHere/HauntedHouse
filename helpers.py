# A file containing useful generic functions, such as for clearing the console.

import random

def clearConsole(wait=0) : #function to clear console on Linux or Windows
    """Clears console, with optional time delay.

    Will attempt to clear the console for Windows, should that fail it will attempt to clear the
    console for Linux.
    
    Args : wait (int or float) : A value representing how long time.sleep() should delay
           execution.
    
    """

    import time
    import platform
    time.sleep(wait) 
    # produces a delay based on the argument given to clearConsole()
    
    import os

    operatingSystem = platform.system()

    if(operatingSystem == 'Windows') :
       os.system('cls') #clears console on Windows

    else :
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


def walk() :
    """Creates slow scrolling txt to describe walking."""
    sleep(0.5)
    print('Walk...')
    sleep(0.5)
    print('......Walk...')
    sleep(0.5)
    print('............Walk')


def timeout(mins, string):
    """Executes code after a given delay, in a seperate thread to main code.
    
    Args : mins (int) : A value representing how long the timer will wait before
                        executing code in the timer thread.

           string (string) : A given string to be printed after the delay.
    
    """
    # The below executes after timeout expires
    # Source for feature = https://stackoverflow.com/questions/18406165/creating-a-timer-in-python
    print(string)

    from threading import Timer
    import time

    # duration is in seconds
    t = Timer(mins * 60, timeout)
    t.start()

def getRandomQuestion() :
    questions = [{'question': 'What is the number 5 in binary?', 'answer': '101'}]

    return random.choice(questions)

