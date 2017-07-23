class Room :

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

    def setConnectedRooms(self, rooms) :
        self.connectedRooms = rooms

    def setProperties(self, properties) :
        self.properties = properties

    def setPropertyValue(self, property, value) :
        self.properties[property] = value

def createRooms() :
    rooms = []
    lobby = Room('Reception Area', 'hardwood floor', 'ceiling with chandeliers', 
                      True, '2 large chandeliers'
                      )

    basement = Room('Basement', 'bare earth floor with disturbed ground', 'floorboards', 
                         True, 'incandecent light fitting without a bulb'
                         )

    garage = Room('Garage', 'concrete floor', 'boarded ceiling',
                       True, 'fluorescent strip lighting'
                       )

    dinningRoom = Room('Dinning Room', 'polished wood floor', 'pattered wallpaper',
                            True, 'candles in holders'
                           )

    kitchen = Room('Kitchen', 'laminate flooring', 'white painted plaster', 
                            True, 'downlighters')

    utility = Room('Utility Room', 'stone tiles', 'white painted plaster', 
                            True, 'incandecent bulb')

    library = Room('Library', 'stained wood flooring', 'Dark painted plaster', 
                            True, 'floor lamps')

    masterBedroom = Room('Master Bedroom', 'carpet', 'white painted plaster', 
                                  True, 'incandecent bulb with shade')

    secondBedroom = Room('Second Bedroom', 'carpet', 'white painted plaster', 
                                  True, 'incandecent bulb with shade')

    nursery = Room('Nursery', 'carpet', 'white painted plaster', 
                            True, 'incandecent bulb with shade')

    landing = Room('Landing', 'carpet', 'white painted plaster',
                           True, 'incandecent bulb with shade')

    attick = Room('Attick', 'bare floorboards', 'bare brick', False, 'n/a')

    start = Room('Start Area', 'gravel drive', None, True, 'street lamp')

    patio = Room('The Patio', 'grass and paving stones', None, True, 'security light')

    garden = Room('The Rear Garden', 'grass', None, False, 'n/a')

    start.setConnectedRooms([garage, patio, lobby, patio, basement])
    patio.setConnectedRooms([lobby, garden])
    basement.setConnectedRooms([lobby])
    kitchen.setConnectedRooms([lobby, utility])
    landing.setConnectedRooms([attick, masterBedroom, secondBedroom, nursery])
    lobby.setConnectedRooms([patio, basement, kitchen, garage, dinningRoom, library])
    masterBedroom.setConnectedRooms([landing])
    secondBedroom.setConnectedRooms([landing])
    attick.setConnectedRooms([landing])
    utility.setConnectedRooms([kitchen])
    dinningRoom.setConnectedRooms([lobby, garden])
    nursery.setConnectedRooms([landing])
    garden.setConnectedRooms([[patio, dinningRoom]])
    library.setConnectedRooms([lobby])

    rooms.append(start)
    rooms.append(patio)
    rooms.append(basement)
    rooms.append(kitchen)
    rooms.append(landing)
    rooms.append(lobby)
    rooms.append(masterBedroom)
    rooms.append(secondBedroom)
    rooms.append(attick)
    rooms.append(utility)
    rooms.append(dinningRoom)
    rooms.append(nursery)
    rooms.append(garden)
    rooms.append(library)
    return rooms

