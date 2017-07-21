class GameLevel(object):
    """A level within the game is a distinct area; seperate, yet connected to other game areas."""

    def __init__(self, levelDescription, floor, roof, light) : # The constructor
        self.levelDescription = levelDescription
        self.floor = floor
        self.roof = roof
        self.light = light
        #self.door = door
        #self.window = window
        #self.staircase = staircase

    # Instantiate game levels
        lobby = GameLevel('The Main Reception', 'Hardwood floor', 'Ceiling with Chandeliers', 
                          '2 large chandeliers'
                          )

        basement = GameLevel('The Basement', 'Earth floor with disturbed ground', 'Ceiling is floorboards', 
                             'Light fitting is missing a bulb'
                             )

        garage = GameLevel('A Large Cluttered Garage', 'Concrete floor', 'A boarded ceiling',
                           'Flurocent strip lighting'
                           )

        dinningRoom = GameLevel('The Dinning Room', 'Polished wood floor', 'Pattered wallpaper',
                                'An amount of candles in holders on and around the dinning table'
                               )

        #kitchen = GameLevel('', '', '')
    
        #utility = GameLevel('', '', '')

        #library = GameLevel('', '', '')

        #masterBedroom = GameLevel('', '', '')

        #secondBedroom = GameLevel('', '', '')

        #nursery = GameLevel('', '', '')

        #landing = GameLevel('', '', '')

        #attick = GameLevel('', '', '')


# Instantiate outdoor game sub levels
class OutsideLevel(GameLevel) : 
    """Sub class of GameLevel for outdoor levels of the game."""

    def __init__(self, levelDescription, floor) :
        super().__init__(levelDescription, floor)
        self.dayTime = dayTime

    start = OutsideLevel('Start Area', 'Gravel drive')

    patio = OutsideLevel('The Patio', 'Grass and paving stones')

    garden = OutsideLevel('The Rear Garden', 'Grass')
