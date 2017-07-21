class GameLevel(object) :
    """A level within the game is a distinct area; seperate, yet connected to other game areas."""

    def __init__(self, levelName, floor, roof, lighting, lightType) : # The constructor
        self.levelName = levelName
        self.floor = floor
        self.roof = roof
        self.lighting = lighting # Is there a light (appliance) in the room
        self.lightType = lightType


    # Instantiate game levels
        lobby = GameLevel('Reception Area', 'hardwood floor', 'ceiling with chandeliers', 
                          True, '2 large chandeliers'
                          )

        lobby.stairway = True

        basement = GameLevel('Basement', 'bare earth floor with disturbed ground', 'floorboards', 
                             True, 'incandecent light fitting without a bulb'
                             )

        basement.stairwway = True

        garage = GameLevel('Garage', 'concrete floor', 'boarded ceiling',
                           True, 'fluorescent strip lighting'
                           )

        dinningRoom = GameLevel('Dinning Room', 'polished wood floor', 'pattered wallpaper',
                                True, 'candles in holders'
                               )

        kitchen = GameLevel('Kitchen', 'laminate flooring', 'white painted plaster', 
                            True, 'downlighters')
    
        utility = GameLevel('Utility Room', 'stone tiles', 'white painted plaster', 
                            True, 'incandecent bulb')

        library = GameLevel('Library', 'stained wood flooring', 'Dark painted plaster', 
                            True, 'floor lamps')

        masterBedroom = GameLevel('Master Bedroom', 'carpet', 'white painted plaster', 
                                  True, 'incandecent bulb with shade')

        secondBedroom = GameLevel('Second Bedroom', 'carpet', 'white painted plaster', 
                                  True, 'incandecent bulb with shade')

        nursery = GameLevel('Nursery', 'carpet', 'white painted plaster', 
                            True, 'incandecent bulb with shade')

        landing = GameLevel('Landing', 'carpet', 'white painted plaster',
                           True, 'incandecent bulb with shade')

        landing.stairway = True

        attick = GameLevel('Attick', 'bare floorboards', 'bare brick', False, 'n/a')


# Instantiate outdoor game sub levels
class OutsideLevel(GameLevel) : 
    """Sub class of GameLevel for outdoor levels of the game."""

    def __init__(self, levelName, floor, lighting, lightType) :
        super().__init__(levelName, floor, lighting, lightType)

        start = OutsideLevel('Start Area', 'gravel drive', True, 'street lamp')

        patio = OutsideLevel('The Patio', 'grass and paving stones', True, 'security light')

        garden = OutsideLevel('The Rear Garden', 'grass', False, 'n/a')
