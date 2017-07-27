# Details of the opponents a character may face within the game

import random
from helpers import *

class Opponent :
    """Opponent class."""

    def __init__(self, name, opponentType) : 
        self.name = name
        self.opponentType = opponentType


    def createRandomOpponent() :

        names = ['Refus', 'Red Shirt', 'Amelia', 'Howler', 'The Phantom', '01100111 01101000 01101111 01110011 01110100',
                'Dark Lord', 'Punisher', 'Reaper', 'Hitch', 'AntiSanta']
        name = random.choice(names)

        types =['Ghost', 'Bad Actor', 'Demon', 'Monster', 'Undead', 'Vampire']
        opponentType = random.choice(types)

        randomOpponent = Opponent(name, opponentType)
        return(randomOpponent)

    def combatAttack() :
        # Opponent makes a combat attack and you have to fight to survive/continue
        pass

    def fleeingAttack() :
        # Opponent makes an attack, and then flees
        print('\nphawack!')
        sleep(0.3)
        print('You\'re stuck hard across the head!')
        print('Dazed and confused, you struggle to regain your composure')
        sleep(3)
        print('Your attack as fled!')

    def itemAttack() :
        # Opponent forces you to answer questions or perform a task
        # for each question or task you get wrong, a random item is confiscated (maybe returned after a delay)
        pass

    def delayAttack() :
        # Player is fozen/stuck to the spont, and can't continue until a delay expires
        pass

    def randomAttack() :
        # Randomly selects one of the attack methods when called
        attacks = ['combatAttack()', 'fleeingAttack()', 'itemAttack()', 'delayAttack()', 'selectAttack()']
        attack = random.choice(attacks)

        return(attack)