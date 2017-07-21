class Character(object) :
    """None AI player of the game."""

    import random # Used to create a random character

    def __init__(self, firstName, heightInFeet, age, fitnessLevel) : # The constructor
        self.firstName = firstName
        self.heightInFeet = heightInFeet
        self.age = age
        self.fitnessLevel = fitnessLevel

    def createCharacter(self) :
        print('Please enter the following information to setup your character...\n')
        firstName = input('What is your first name? ')
        heightInFeet = float(input('What is your height in feet approx? '))
        age = int(input('What is your age in whole years? '))
        fitnessLevel = input('What is your fitness level (Poor, Okay, Great)? ')

    def createRandomCharacter(self) :
        firstNameData = ['Gareth', 'Dan', 'Rachel', 'Ethereal', 'Raby', 'Carrie', 'Erika',
                         'Nathan']
        heightInFeetData = [4.5, 5.3, 5.7, 5.7, 5.9, 5,11, 6, 6, 6.1, 6.2, 6.9]
        fitnessLevelData = ['Poor', 'Okay', 'Great']

        firstName = random.choice(firstNameData)
        age = random.randint(18, 55)
        heightInFeet = random.choice(heightInFeetData)
        fitnessLevel = random.choice(fitnessLevelData)
