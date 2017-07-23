import random
from Character import Character

class CharacterCreator :

    def createCharacter() :
        print('Please enter the following information to setup your character...\n')
        firstName = input('What is your first name? ')
        heightInFeet = float(input('What is your height in feet approx? '))
        age = int(input('What is your age in whole years? '))
        fitnessLevel = input('What is your fitness level (Poor, Okay, Great)? ')

        character = Character(firstName, heightInFeet, age, fitnessLevel)

        return(character)

    def createRandomCharacter() :
        firstNameData = ['Gareth', 'Dan', 'Rachel', 'Ethereal', 'Raby', 'Carrie', 'Erika',
                         'Nathan']
        heightInFeetData = [4.5, 5.3, 5.7, 5.7, 5.9, 5,11, 6, 6, 6.1, 6.2, 6.9]
        fitnessLevelData = ['Poor', 'Okay', 'Great']

        firstName = random.choice(firstNameData)
        age = random.randint(18, 55)
        heightInFeet = random.choice(heightInFeetData)
        fitnessLevel = random.choice(fitnessLevelData)

        # This method is called in HauntedHouse.py at the character creation.
        # You can access the object from there.
        randomCharacter = Character(firstName, age, heightInFeet, fitnessLevel)
        
        print("Name: " + firstName)
        print("Age: {0}".format(age))
        print("Height: {0} ft".format(heightInFeet))
        print("Fitness: " + fitnessLevel)
        print("")

        return(randomCharacter)
