# Details of the opponents a character may face within the game

import random

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


