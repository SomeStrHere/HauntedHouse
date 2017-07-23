class Location :

    def __init__(self, levelName, floor, roof, lighting, lightType) :
        self.levelName = levelName
        self.floor = floor
        self.roof = roof
        self.lighting = lighting
        self.lightType = lightType

        self.connectedRooms = []
        self.properties = {}

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

def createLocations() :
    locations = []
    lobby = Location('Reception Area', 'hardwood floor', 'ceiling with chandeliers', 
                      True, '2 large chandeliers'
                      )

    basement = Location('Basement', 'bare earth floor with disturbed ground', 'floorboards', 
                         True, 'incandecent light fitting without a bulb'
                         )

    garage = Location('Garage', 'concrete floor', 'boarded ceiling',
                       True, 'fluorescent strip lighting'
                       )

    dinningRoom = Location('Dinning Room', 'polished wood floor', 'pattered wallpaper',
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

    start.setConnectedLocations([garage, patio, lobby, patio, basement])
    patio.setConnectedLocations([lobby, garden])
    basement.setConnectedLocations([lobby])
    kitchen.setConnectedLocations([lobby, utility])
    landing.setConnectedLocations([attick, masterBedroom, secondBedroom, nursery])
    lobby.setConnectedLocations([patio, basement, kitchen, garage, dinningRoom, library])
    masterBedroom.setConnectedLocations([landing])
    secondBedroom.setConnectedLocations([landing])
    attick.setConnectedLocations([landing])
    utility.setConnectedLocations([kitchen])
    dinningRoom.setConnectedLocations([lobby, garden])
    nursery.setConnectedLocations([landing])
    garden.setConnectedLocations([[patio, dinningRoom]])
    library.setConnectedLocations([lobby])

    locations.append(start)
    locations.append(patio)
    locations.append(basement)
    locations.append(kitchen)
    locations.append(landing)
    locations.append(lobby)
    locations.append(masterBedroom)
    locations.append(secondBedroom)
    locations.append(attick)
    locations.append(utility)
    locations.append(dinningRoom)
    locations.append(nursery)
    locations.append(garden)
    locations.append(library)
    return locations
