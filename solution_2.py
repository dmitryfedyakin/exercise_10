class NavalBattle:
    '''
    Class represents a naval battle game with a playing field.

    Attributes:
        playing_field (list): A 10x10 list representing the playing field.
    '''

    playing_field = [[0] * 10 for _ in range(10)]

    def __init__(self, symbol):
        '''
        Initializes a player's choice with the specified symbol.

        :param symbol: A symbol representing a player's ship on the field.
        '''

        self.symbol = symbol

    @staticmethod
    def show():
        '''
        Display the current state of the playing field.
        '''

        field_copy = [['`'] * 10 for _ in range(10)]
        for i in range(len(field_copy)):
            for j in range(len(field_copy)):
                if NavalBattle.playing_field[i][j] != 0 and \
                NavalBattle.playing_field[i][j] != 1:
                    field_copy[i][j] = NavalBattle.playing_field[i][j]

        for i in range(len(NavalBattle.playing_field)):
            print(*(field_copy[i]))

    def shot(self, x, y):
        '''
        Makes a shot at the specified coordinates.

        :param x: x coordinate 
        :param y: y coordinate
        '''

        if NavalBattle.playing_field[y - 1][x - 1] == 1:
            print('попал')
            NavalBattle.playing_field[y - 1][x - 1] = self.symbol
        elif NavalBattle.playing_field[y - 1][x - 1] == 0:
            print('мимо')
            NavalBattle.playing_field[y - 1][x - 1] = 'o'