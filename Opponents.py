# Details of the opponents a character may face within the game

import random
from helpers import *

class Opponent :
    """Opponent class."""

    def __init__(self, name, opponentType, health, attack) : 
        self.name = name
        self.opponentType = opponentType
        self.health = health
        self.attack = attack

    def combatAttack(self, character) :
        # Opponent makes a combat attack and you have to fight to survive/continue
        pass

    def fleeingAttack(self, character) :
        # Opponent makes an attack, and then flees
        print('\nphawack!')
        sleep(0.3)
        print('You\'re stuck hard across the head!')
        print('Dazed and confused, you struggle to regain your composure')
        sleep(3)
        print('Your attack as fled!')

    def itemAttack(self, character) :
        # Opponent forces you to answer questions or perform a task
        # for each question or task you get wrong, a random item is confiscated (maybe returned after a delay)
        print("You are attacked by a " + self.opponentType + " called " + self.name + "!")
        print("It tells you that you must answer its question correctly or you will lose an item.")
        questionPair = getRandomQuestion()
        print("The question is...")
        print(questionPair['question'])
        answer = input("What is your answer? ")

        while((answer != questionPair['answer']) and (len(character.inventory) > 0)) :
            print("Wrong!")
            itemTaken = character.takeRandomItem()
            print("The " + self.opponentType + " takes your " + itemTaken + ".")
            answer = input('Guess again: ')
        
        if(answer == questionPair['answer']) :
            print('Well done! You guessed correctly.')
            print("The " + self.opponentType + " disappears.")
        else :
            print("You have no items left.")
            print("The " + self.opponentType + " disappears.")

    def delayAttack(self, character) :
        # Player is fozen/stuck to the spot, and can't continue until a delay expires
        pass

    def randomAttack() :
        # Randomly selects one of the attack methods when called
        attacks = ['combatAttack()', 'fleeingAttack()', 'itemAttack()', 'delayAttack()', 'selectAttack()']
        attack = random.choice(attacks)

        return(attack)

def createRandomOpponent() :

    names = ['Refus', 'Red Shirt', 'Amelia', 'Howler', 'The Phantom', '01100111 01101000 01101111 01110011 01110100',
            'Dark Lord', 'Punisher', 'Reaper', 'Hitch', 'AntiSanta']
    name = random.choice(names)

    types =['Ghost', 'Bad Actor', 'Demon', 'Monster', 'Undead', 'Vampire']
    opponentType = random.choice(types)

    healthOptions = [20, 25, 30, 35, 40]
    health = random.choice(healthOptions)

    attackOptions = [2, 4, 5, 7]
    attack = random.choice(attackOptions)

    randomOpponent = Opponent(name, opponentType, health, attack)
    return(randomOpponent)