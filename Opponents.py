# Details of the opponents a character may face within the game

class Opponent :
    """Opponent class."""

    def __init__(self, name, opponentType, typeDescription) : 
        self.name = name
        # opponent type can be used to vary interactions with use
        # could be ghost, demon, monster, vampire, etc
        self.opponentType = opponentType
        self.typeDescription = typeDescription

        names = ['Refus', 'Red Shirt', 'Amelia', 'Howler', 'The Phantom', '01100111 01101000 01101111 01110011 01110100 ',
                'Dark Lord', 'Punisher', 'Reaper', 'Hitch', 'AntiSanta']
        name = random.choice(names)

        # Dictionary so a sub description can be generated for each type of opponent,
        # which can be expanded upon in code when called.
        opponentDetails = {'Ghost' : 'TODO - Ghost description', 'Undead' : 'TODO - Undead description', 
                           'Demon' : 'TODO Demon description', 'Vampire' : 'TODO Vampire description', 
                           'Bad Actor' : 'TODO Bad Actor description'}


