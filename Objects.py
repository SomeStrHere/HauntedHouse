# Do we also need a subclass for money and a subclass for weapons

class Objects(object) :
    """A class to store data and functions related to in game objects"""

    def __init__(self, name, description, canBePickedUp, canBeCarried, canBePossessed, 
                 twoHandedCarry, itemType, foundLocation, 
                 foundLevel, currentLocation, currentLevel) : # The constructor
        self.name = name
        self.description = description
        self.canBePickedUp = canBePickedUp
        self.twoHandedCarry = twoHandedCarry # Does it need two hands to carry it
        self.canBeCarried = canBeCarried
        self.canBePossessed = canBePossessed
        self.itemType = itemType
        self.foundLocation = foundLocation
        self.currentLocation = currentLocation

        itemType = ['Clothing', 'Furniture', 'Ornament', 'Weapon', 'Shelter', 'Food', 'Drink', 'Fuel', 'Money', 'Tool']
        # An example of a tool would be lockpicks or matches




class Possesions(Objects) :
    """A subclass of Objects to store data and functions related to character possesions"""

    def __init__(self, name, description, canBePickedUp, canBeCarried, canBePossessed, 
                 twoHandedCarry, itemType, foundLocation, foundLevel, 
                 beingCarried, location) :
        super().__init__(name, description, canBePickedUp, canBeCarried, canBePossessed, 
                 twoHandedCarry, itemType, foundLocation, foundLevel)

        self.beingCarried = beingCarried
        self.location = location 

        # Location in this context means where abouts on the person is the item stored, i.e pocket or rucksack
        tent = Possesions('Tent', 'A tent to provide shelter', True, True, True, False, 'Shelter', 'Rucksack', 'Start', True, 'Rucksack')
        lockpicks = Possesions('Lockpicks', 'Lockpicks to pick locks', True, True, True, False, 'Tool', 'Pocket', 'Start', True, 'Pocket')

    #[storage] location, i.e trouser pocket, holdhall 1, holdhall 2, rucksack
    # left hand, right hand

    # Not used currentLocation and currentLevel here because if the players possesses them,
    # then the possessions location will be where the player is.

class Weapons(Objects) :
    """A class to store data and functions related to in game weapons"""

    def __init__(self, name, description, canBePickedUp, canBeCarried, canBePossessed, 
                 twoHandedCarry, itemType, foundLocation, 
                 foundLevel, currentLocation, currentLevel, weaponType) : 
        super().__init__(name, description, canBePickedUp, canBeCarried, canBePossessed, 
                 twoHandedCarry, itemType, foundLocation, foundLevel, 
                 currentLocation, currentLevel)

        self.weaponType = weaponType

