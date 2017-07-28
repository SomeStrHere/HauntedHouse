class Character :
    """None AI player of the game."""

    def __init__(self, firstName, heightInFeet, age, fitnessLevel) : # The constructor
        self.firstName = firstName
        self.heightInFeet = heightInFeet
        self.age = age
        self.fitnessLevel = fitnessLevel
        self.inventory = []
        ## An array that includes items needed to finish the game.
        ## This stops opponents stealing items from this array.
        self.essentialItems = []
        self.hp = 80
        self.attack = 5

    def getItem(self, item) :
        self.inventory.append(item)

    def takeRandomItem(self) :
        takenItem = random.choice(self.inventory)
        self.inventory.remove(takenItem)
        return takenItem



            
