from dice import *

class Location :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        self.levelName = levelName
        self.floor = floor
        self.roof = roof
        self.lighting = lighting
        self.lightType = lightType

        self.connectedRooms = []
        self.properties = {'unlocked': True}

        self.visited = False

    def checkVisited(self) :
        return self.visited

    def setAsVisited(self) :
        self.visited = True;

    def setConnectedLocations(self, rooms) :
        self.connectedRooms = rooms

    def setProperties(self, properties) :
        self.properties = properties

    def setPropertyValue(self, property, value) :
        self.properties[property] = value

    def choiceToNextLocation(self) :
        print("Where do you want to go next?")
        locationNumber = 0;
        for location in self.connectedRooms :
            print(str(locationNumber) + ") " + location.levelName)
            locationNumber += 1

        userChoice = input("What is your choice? ")

        return self.connectedRooms[int(userChoice)]

    def getAttacked(self, character) :
        ## TODO

    def doPuzzle(self) :
        ##TODO

    def repairWeapons(self, character) :
        ## TODO


class Garage(Location) :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        super().__init__(levelName, floor, roof, lighting, lightType)

        ## Items that can be found in the garage
        self.itemsAvailable = []

    def doAction(self, diceRoll, character) :
        if(diceRoll == 1) :
            ## Go to new location
            self.choiceToNextLocation()
        elif(diceRoll == 2) :
            ## Find items
            self.searchLocation(character)
        elif(diceRoll == 3) :
            ## Get attacked by ghost etc
            self.getAttacked(character)
        elif(diceRoll == 4) :
            ## Repair all(?) weapons
            self.repairWeapons(character)
        elif(diceRoll == 5) :
            ## Be given a puzzle
            self.doPuzzle()
        elif(diceRoll == 6) :
            self.choiceToNextLocation()

    def searchLocation(self, character) :
        itemFound = random.choice(self.itemsAvailable)
        itemsAvailable.remove(itemFound)
        character.getItem(itemFound)
        

def createLocations() :
    locations = {}
    lobby = Location('Reception Area', 'hardwood floor', 'ceiling with chandeliers', 
                      True, '2 large chandeliers'
                      )

    basement = Location('Basement', 'bare earth floor with disturbed ground', 'floorboards', 
                         True, 'incandecent light fitting without a bulb'
                         )

    garage = Location('Garage', 'concrete floor', 'boarded ceiling',
                       True, 'fluorescent strip lighting'
                       )

    diningRoom = Location('Dinning Room', 'polished wood floor', 'pattered wallpaper',
                            True, 'candles in holders'
                           )

    kitchen = Location('Kitchen', 'laminate flooring', 'white painted plaster', 
                            True, 'downlighters')

    utility = Location('Utility Room', 'stone tiles', 'white painted plaster', 
                            True, 'incandecent bulb')

    library = Location('Library', 'stained wood flooring', 'Dark painted plaster', 
                            True, 'floor lamps')

    masterBedroom = Location('Master Bedroom', 'carpet', 'white painted plaster', 
                                  True, 'incandecent bulb with shade')

    secondBedroom = Location('Second Bedroom', 'carpet', 'white painted plaster', 
                                  True, 'incandecent bulb with shade')

    nursery = Location('Nursery', 'carpet', 'white painted plaster', 
                            True, 'incandecent bulb with shade')

    landing = Location('Landing', 'carpet', 'white painted plaster',
                           True, 'incandecent bulb with shade')

    attick = Location('Attick', 'bare floorboards', 'bare brick', False, 'n/a')

    start = Location('Start Area', 'gravel drive', None, True, 'street lamp')

    patio = Location('The Patio', 'grass and paving stones', None, True, 'security light')

    garden = Location('The Rear Garden', 'grass', None, False, 'n/a')

    start.setConnectedLocations([garage, patio, lobby, basement])
    patio.setConnectedLocations([lobby, garden])
    basement.setConnectedLocations([lobby])
    kitchen.setConnectedLocations([lobby, utility])
    landing.setConnectedLocations([attick, masterBedroom, secondBedroom, nursery])
    lobby.setConnectedLocations([patio, basement, kitchen, garage, diningRoom, library])
    masterBedroom.setConnectedLocations([landing])
    secondBedroom.setConnectedLocations([landing])
    attick.setConnectedLocations([landing])
    utility.setConnectedLocations([kitchen])
    diningRoom.setConnectedLocations([lobby, garden])
    nursery.setConnectedLocations([landing])
    garden.setConnectedLocations([[patio, diningRoom]])
    library.setConnectedLocations([lobby])

    patio.actions = [["You decide to go to a new location.", ]]

    locations['start'] = start
    locations['patio'] = patio
    locations['basement'] = basement
    locations['kitchen'] = kitchen
    locations['landing'] = landing
    locations['lobby'] = lobby
    locations['masterBedroom'] = masterBedroom
    locations['secondBedroom'] = secondBedroom
    locations['attick'] = attick
    locations['utility'] = utility
    locations['diningRoom'] = diningRoom
    locations['nursery'] = nursery
    locations['garden'] = garden
    locations['library'] = library
    return locations

