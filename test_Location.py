from Location import *
from Character import *
import mock

class TestLocation :

    def test_checkVisited(self) :
        testLocation = Location('tester', 'test floor', None, True, 'testLight')

        assert(testLocation.checkVisited() == False)

    def test_GarageIntro(self) :
        testGarage = Garage('garage', 'concrete', None, True, 'window light')
        testCharacter = Character('Kieran', 6.0, 18, 'Great')

        with mock.patch('builtins.input', side_effect=[0]):
            entered, nextLocation = testGarage.locationIntroduction(testCharacter)

        assert(entered == True or entered == False)

        if entered :
            assert(nextLocation == 'garage')
        else :
            nextLocation in ['lobby', 'patio']

    def test_LobbyIntro(self) :
        testLobby = Lobby('lobby', 'carpet', None, True, 'lamp')
        testCharacter = Character('Kieran', 6.0, 18, 'Great')

        with mock.patch('builtins.input', side_effect=[0, '42']):
            entered, nextLocation = testLobby.locationIntroduction(testCharacter)

        assert(entered == True or entered == False)

        if entered :
            assert(nextLocation == 'lobby')
        else :
            nextLocation in ['basement', 'patio']

    def test_DinningRoomIntro(self) :
        testDR = DinningRoom('DR', 'carpet', None, True, 'lamp')
        testCharacter = Character('Kieran', 6.0, 18, 'Great')

        with mock.patch('builtins.input', side_effect=[0]):
            entered, nextLocation = testDR.locationIntroduction(testCharacter)

        assert(entered == True or entered == False)

        if entered :
            assert(nextLocation == 'diningRoom')
        else :
            nextLocation in ['patio']

    def test_BasementIntro(self) :
        testBasement = Basement('basement', 'carpet', None, True, 'lamp')
        testCharacter = Character('Kieran', 6.0, 18, 'Great')

        with mock.patch('builtins.input', side_effect=[0,0]):
            entered, nextLocation = testBasement.locationIntroduction(testCharacter)

        assert(entered == True or entered == False)

        if entered :
            assert(nextLocation == 'basement')
        else :
            nextLocation in []