import random

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
        
        field = NavalBattle.playing_field
        field_copy = [['`'] * 10 for _ in range(10)]
        for i in range(len(field_copy)):
            for j in range(len(field_copy)):
                if field[i][j] != 0 and field[i][j] != 1:
                    field_copy[i][j] = field[i][j]

        for i in range(len(field)):
            print(*(field_copy[i]))

    def shot(self, x, y):
        '''
        Makes a shot at the specified coordinates.

        :param x: x coordinate 
        :param y: y coordinate
        '''

        y_n = y - 1
        x_n = x - 1
        field = NavalBattle.playing_field

        if field == [[0] * 10 for _ in range(10)]:
            print('игровое поле не заполнено')

        else:
            if field[y_n][x_n] == 'o' or field[y_n][x_n] == self.symbol:
                print('ошибка')

            else:
                if field[y_n][x_n] == 1:
                    print('попал')
                    field[y_n][x_n] = self.symbol
                elif field[y_n][x_n] == 0:
                    print('мимо')
                    field[y_n][x_n] = 'o'

    def new_game():
        '''
        Makes new playing field.
        '''

        status_4 = False
        status_3 = False
        status_2 = False
        status_1 = False

        field = [[0] * 10 for _ in range(10)]

        size = 4

        count_3 = 0
        count_2 = 0
        count_1 = 0

        while not status_4 or not status_3 or not status_2 or not status_1:

            vert_hor = random.randint(1, 2)
            
            start_x = 0
            start_y = 0
            end_x = 0
            end_y = 0

            field_x = random.randint(0, 9)
            field_y = random.randint(0, 9)

            if vert_hor == 1:
                # hor
                status_hor = False

                if field_y == 0:
                    start_y = field_y
                else:
                    start_y = field_y - 1

                if field_y + size + 1 == 11:
                    end_y = field_y + size
                else:
                    end_y = field_y + size + 1

                if field_x == 0:
                    start_x = field_x
                else:
                    start_x = field_x - 1

                if field_x + 2 == 11:
                    end_x = field_x + 1
                else:
                    end_x = field_x + 2

                for x in range(start_x, end_x):
                    if x >= 10:
                        status_hor = False
                        break
                    else:
                        for y in range(start_y, end_y):
                            if y >= 10:
                                status_hor = False
                                break
                            else:
                                if field[x][y] == 0:
                                    status_hor = True
                                else:
                                    status_hor = False
                                    break
                        if not status_hor:
                            break
            
                if status_hor:
                    for j in range(size):
                        field[field_x][field_y + j] = 1

                    if size == 4:
                        status_4 = True
                        size = 3
                    elif size == 3:
                        count_3 += 1
                        if count_3 == 2:
                            status_3 = True
                            size = 2
                    elif size == 2:
                        count_2 += 1
                        if count_2 == 3:
                            status_2 = True
                            size = 1
                    elif size == 1:
                        count_1 += 1
                        if count_1 == 4:
                            status_1 = True

            if vert_hor == 2:
                # vert
                status_vert = False

                if field_x == 0:
                    start_x = field_x
                else:
                    start_x = field_x - 1

                if field_x + size + 1 == 11:
                    end_x = field_x + size 
                else:
                    end_x = field_x + size + 1

                if field_y == 0:
                    start_y = field_y
                else:
                    start_y = field_y - 1

                if field_y + 2 == 11:
                    end_y = field_y + 1
                else:
                    end_y = field_y + 2

                for y in range(start_y, end_y):
                    if y >= 10:
                        status_vert = False
                        break
                    else:
                        for x in range(start_x, end_x):
                            if x >= 10:
                                status_vert = False
                                break
                            else:
                                if field[x][y] == 0:
                                    status_vert = True
                                else:
                                    status_vert = False
                                    break
                        if not status_vert:
                            break
            
                if status_vert:
                    for j in range(size):
                        field[field_x + j][field_y] = 1

                    if size == 4:
                        status_4 = True
                        size = 3
                    elif size == 3:
                        count_3 += 1
                        if count_3 == 2:
                            status_3 = True
                            size = 2
                    elif size == 2:
                        count_2 += 1
                        if count_2 == 3:
                            status_2 = True
                            size = 1
                    elif size == 1:
                        count_1 += 1
                        if count_1 == 4:
                            status_1 = True
                    
        NavalBattle.playing_field = field
