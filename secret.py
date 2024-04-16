import random

class NavalBattle:
    playing_field = [[0] * 10 for _ in range(10)]

    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def show():
        field = NavalBattle.playing_field
        field_copy = [['`'] * 10 for _ in range(10)]
        for i in range(len(field_copy)):
            for j in range(len(field_copy)):
                if field[i][j] != 0 and field[i][j] != 1:
                    field_copy[i][j] = field[i][j]

        for i in range(len(field)):
            print(*(field_copy[i]))

    def shot(self, x, y):
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
        status_4 = False
        status_3 = False
        status_2 = False
        status_1 = False

        field = [[0] * 10 for _ in range(10)]

        while not status_4:
            vert_hor = random.randint(1, 2)
            if vert_hor == 1:
                # hor
                point_x = random.randint(1, 10)
                point_y = random.randint(1, 10)

                field_x = point_x - 1
                field_y = point_y - 1

                if point_x >= 2 and point_x <= 9 and point_y >= 2 and point_y <= 6:
                    if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y + 4] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0 and \
                        field[field_x + 1][field_y + 4] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0 and \
                        field[field_x - 1][field_y + 3] == 0 and \
                        field[field_x - 1][field_y + 4] == 0:

                        field[field_x][field_y] = 1
                        field[field_x][field_y + 1] = 1
                        field[field_x][field_y + 2] = 1
                        field[field_x][field_y + 3] = 1
                        status_4 = True

                elif point_y >= 2 and point_y <= 6:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y + 4] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0 and \
                        field[field_x + 1][field_y + 4] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            field[field_x][field_y + 3] = 1
                            status_4 = True
                    
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y + 4] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0 and \
                        field[field_x - 1][field_y + 3] == 0 and \
                        field[field_x - 1][field_y + 4] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            field[field_x][field_y + 3] = 1
                            status_4 = True


                elif point_y == 1:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y + 4] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0 and \
                        field[field_x + 1][field_y + 4] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            field[field_x][field_y + 3] = 1
                            status_4 = True
                        
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x][field_y + 2] == 0 and \
                            field[field_x][field_y + 3] == 0 and \
                            field[field_x][field_y + 4] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x - 1][field_y + 2] == 0 and \
                            field[field_x - 1][field_y + 3] == 0 and \
                            field[field_x - 1][field_y + 4] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            field[field_x][field_y + 3] = 1
                            status_4 = True

                    else:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y + 4] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0 and \
                        field[field_x + 1][field_y + 4] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0 and \
                        field[field_x - 1][field_y + 3] == 0 and \
                        field[field_x - 1][field_y + 4] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            field[field_x][field_y + 3] = 1
                            status_4 = True

                elif point_y == 7:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0 and \
                        field[field_x + 1][field_y - 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            field[field_x][field_y + 3] = 1
                            status_4 = True

                            
                        
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x][field_y + 2] == 0 and \
                            field[field_x][field_y + 3] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x - 1][field_y + 2] == 0 and \
                            field[field_x - 1][field_y + 3] == 0 and \
                            field[field_x - 1][field_y - 1] == 0:
                                
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            field[field_x][field_y + 3] = 1
                            status_4 = True

                    else:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x][field_y + 2] == 0 and \
                            field[field_x][field_y + 3] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 1][field_y + 1] == 0 and \
                            field[field_x + 1][field_y + 2] == 0 and \
                            field[field_x + 1][field_y + 3] == 0 and \
                            field[field_x - 1][field_y - 1] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x - 2][field_y + 2] == 0 and \
                            field[field_x - 3][field_y + 3] == 0:
                                                        
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            field[field_x][field_y + 3] = 1
                            status_4 = True
            elif vert_hor == 2:
                # vert
                point_x = random.randint(1, 10)
                point_y = random.randint(1, 10)

                field_x = point_x - 1
                field_y = point_y - 1

                if point_x >= 2 and point_x <= 6 and point_y >= 2 and point_y <= 9:
                    if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x + 4][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0 and \
                        field[field_x + 4][field_y + 1] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0 and \
                        field[field_x + 3][field_y - 1] == 0 and \
                        field[field_x + 4][field_y - 1] == 0:

                        field[field_x][field_y] = 1
                        field[field_x + 1][field_y] = 1
                        field[field_x + 2][field_y] = 1
                        field[field_x + 3][field_y] = 1
                        status_4 = True

                elif point_x >= 2 and point_x <= 6:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x + 4][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0 and \
                        field[field_x + 4][field_y + 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            field[field_x + 3][field_y] = 1
                            status_4 = True
                    
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x + 4][field_y] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0 and \
                        field[field_x + 3][field_y - 1] == 0 and \
                        field[field_x + 4][field_y - 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            field[field_x + 3][field_y] = 1
                            status_4 = True

                        

                elif point_x == 1:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x + 4][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0 and \
                        field[field_x + 4][field_y + 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            field[field_x + 3][field_y] = 1
                            status_4 = True
                        
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 2][field_y] == 0 and \
                            field[field_x + 3][field_y] == 0 and \
                            field[field_x + 4][field_y] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x + 2][field_y - 1] == 0 and \
                            field[field_x + 3][field_y - 1] == 0 and \
                            field[field_x + 4][field_y - 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            field[field_x + 3][field_y] = 1
                            status_4 = True

                    else:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x + 4][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0 and \
                        field[field_x + 4][field_y + 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0 and \
                        field[field_x + 3][field_y - 1] == 0 and \
                        field[field_x + 4][field_y - 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            field[field_x + 3][field_y] = 1
                            status_4 = True

                elif point_x == 7:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            field[field_x + 3][field_y] = 1
                            status_4 = True

                            
                        
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 2][field_y] == 0 and \
                            field[field_x + 3][field_y] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x + 2][field_y - 1] == 0 and \
                            field[field_x + 3][field_y - 1] == 0 and \
                            field[field_x - 1][field_y - 1] == 0:
                                
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            field[field_x + 3][field_y] = 1
                            status_4 = True

                    else:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 2][field_y] == 0 and \
                            field[field_x + 3][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x + 1][field_y + 1] == 0 and \
                            field[field_x + 2][field_y + 1] == 0 and \
                            field[field_x + 3][field_y + 1] == 0 and \
                            field[field_x - 1][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x + 2][field_y - 1] == 0 and \
                            field[field_x + 3][field_y - 1] == 0:
                                                        
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            field[field_x + 3][field_y] = 1
                            status_4 = True

        count_3 = 0
        while not status_3:
            vert_hor = random.randint(1, 2)
            if vert_hor == 1:
                # hor
                point_x = random.randint(1, 10)
                point_y = random.randint(1, 10)

                field_x = point_x - 1
                field_y = point_y - 1

                if point_x >= 2 and point_x <= 9 and point_y >= 2 and point_y <= 7:
                    if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0 and \
                        field[field_x - 1][field_y + 3] == 0:

                        field[field_x][field_y] = 1
                        field[field_x][field_y + 1] = 1
                        field[field_x][field_y + 2] = 1
                        count_3 += 1

                elif point_y >= 2 and point_y <= 7:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            count_3 += 1
                    
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0 and \
                        field[field_x - 1][field_y + 3] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            count_3 += 1


                elif point_y == 1:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            count_3 += 1
                        
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x][field_y + 2] == 0 and \
                            field[field_x][field_y + 3] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x - 1][field_y + 2] == 0 and \
                            field[field_x - 1][field_y + 3] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            count_3 += 1

                    else:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 3] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 3] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0 and \
                        field[field_x - 1][field_y + 3] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            count_3 += 1

                elif point_y == 8:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x + 1][field_y - 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            count_3 += 1

                            
                        
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x][field_y + 2] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x - 1][field_y + 2] == 0 and \
                            field[field_x - 1][field_y - 1] == 0:
                                
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            count_3 += 1

                    else:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x][field_y + 2] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 1][field_y + 1] == 0 and \
                            field[field_x + 1][field_y + 2] == 0 and \
                            field[field_x - 1][field_y - 1] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x - 2][field_y + 2] == 0:
                                                        
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            field[field_x][field_y + 2] = 1
                            count_3 += 1
            elif vert_hor == 2:
                # vert
                point_x = random.randint(1, 10)
                point_y = random.randint(1, 10)

                field_x = point_x - 1
                field_y = point_y - 1

                if point_x >= 2 and point_x <= 7 and point_y >= 2 and point_y <= 9:
                    if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0 and \
                        field[field_x + 3][field_y - 1] == 0:

                        field[field_x][field_y] = 1
                        field[field_x + 1][field_y] = 1
                        field[field_x + 2][field_y] = 1
                        count_3 += 1

                elif point_x >= 2 and point_x <= 7:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            count_3 += 1
                    
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0 and \
                        field[field_x + 3][field_y - 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            count_3 += 1

                        

                elif point_x == 1:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            count_3 += 1
                        
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 2][field_y] == 0 and \
                            field[field_x + 3][field_y] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x + 2][field_y - 1] == 0 and \
                            field[field_x + 3][field_y - 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            count_3 += 1

                    else:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x + 3][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x + 3][field_y + 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0 and \
                        field[field_x + 3][field_y - 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            count_3 += 1

                elif point_x == 8:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            count_3 += 1

                            
                        
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 2][field_y] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x + 2][field_y - 1] == 0 and \
                            field[field_x - 1][field_y - 1] == 0:
                                
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            count_3 += 1

                    else:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 2][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x + 1][field_y + 1] == 0 and \
                            field[field_x + 2][field_y + 1] == 0 and \
                            field[field_x - 1][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x + 2][field_y - 1] == 0:
                                                        
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            field[field_x + 2][field_y] = 1
                            count_3 += 1
            if count_3 == 2:
                status_3 = True


        count_2 = 0
        while not status_2:
            vert_hor = random.randint(1, 2)
            if vert_hor == 1:
                # hor
                point_x = random.randint(1, 10)
                point_y = random.randint(1, 10)

                field_x = point_x - 1
                field_y = point_y - 1

                if point_x >= 2 and point_x <= 9 and point_y >= 2 and point_y <= 8:
                    if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0:

                        field[field_x][field_y] = 1
                        field[field_x][field_y + 1] = 1
                        count_2 += 1

                elif point_y >= 2 and point_y <= 8:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            count_2 += 1
                    
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            count_2 += 1


                elif point_y == 1:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            count_2 += 1
                        
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x][field_y + 2] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x - 1][field_y + 2] == 0:

                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            count_2 += 1

                    else:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y + 2] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 2] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 2] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            count_2 += 1

                elif point_y == 9:
                    if point_x == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            count_2 += 1

                            
                        
                    elif point_x == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x - 1][field_y - 1] == 0:
                                
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            count_2 += 1

                    else:
                        if field[field_x][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 1][field_y + 1] == 0 and \
                            field[field_x - 1][field_y - 1] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0:
                                                        
                            field[field_x][field_y] = 1
                            field[field_x][field_y + 1] = 1
                            count_2 += 1
            elif vert_hor == 2:
                # vert
                point_x = random.randint(1, 10)
                point_y = random.randint(1, 10)

                field_x = point_x - 1
                field_y = point_y - 1

                if point_x >= 2 and point_x <= 8 and point_y >= 2 and point_y <= 9:
                    if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0:

                        field[field_x][field_y] = 1
                        field[field_x + 1][field_y] = 1
                        count_2 += 1

                elif point_x >= 2 and point_x <= 8:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x - 1][field_y + 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            count_2 += 1
                    
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x - 1][field_y - 1] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            count_2 += 1  

                elif point_x == 1:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            count_2 += 1
                        
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x + 2][field_y] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x + 2][field_y - 1] == 0:

                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            count_2 += 1

                    else:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x + 2][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x + 2][field_y + 1] == 0 and \
                        field[field_x][field_y - 1] == 0 and \
                        field[field_x + 1][field_y - 1] == 0 and \
                        field[field_x + 2][field_y - 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            count_2 += 1

                elif point_x == 9:
                    if point_y == 1:
                        if field[field_x][field_y] == 0 and \
                        field[field_x + 1][field_y] == 0 and \
                        field[field_x - 1][field_y] == 0 and \
                        field[field_x][field_y + 1] == 0 and \
                        field[field_x + 1][field_y + 1] == 0 and \
                        field[field_x - 1][field_y + 1] == 0:
                            
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            count_2 += 1
                        
                    elif point_y == 10:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0 and \
                            field[field_x - 1][field_y - 1] == 0:
                                
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            count_2 += 1

                    else:
                        if field[field_x][field_y] == 0 and \
                            field[field_x + 1][field_y] == 0 and \
                            field[field_x][field_y + 1] == 0 and \
                            field[field_x + 1][field_y + 1] == 0 and \
                            field[field_x - 1][field_y - 1] == 0 and \
                            field[field_x - 1][field_y] == 0 and \
                            field[field_x - 1][field_y + 1] == 0 and \
                            field[field_x][field_y - 1] == 0 and \
                            field[field_x + 1][field_y - 1] == 0:
                                                        
                            field[field_x][field_y] = 1
                            field[field_x + 1][field_y] = 1
                            count_2 += 1

            if count_2 == 3:
                status_2 = True

        
        count_1 = 0
        while not status_1:

            point_x = random.randint(1, 10)
            point_y = random.randint(1, 10)

            field_x = point_x - 1
            field_y = point_y - 1

            if point_x >= 2 and point_x <= 9 and point_y >=2 and point_y <= 9:

                if field[field_x][field_y] == 0 and \
                    field[field_x][field_y + 1] == 0 and \
                    field[field_x + 1][field_y + 1] == 0 and \
                    field[field_x - 1][field_y - 1] == 0 and \
                    field[field_x][field_y - 1] == 0 and \
                    field[field_x + 1][field_y - 1] == 0 and \
                    field[field_x - 1][field_y] == 0 and \
                    field[field_x + 1][field_y] == 0 and \
                    field[field_x - 1][field_y + 1] == 0:

                    field[field_x][field_y] = 1
                    count_1 += 1
                
            elif point_x >= 2 and point_x <= 9:
                if point_y == 1:
                    if field[field_x][field_y] == 0 and \
                    field[field_x][field_y + 1] == 0 and \
                    field[field_x + 1][field_y + 1] == 0 and \
                    field[field_x - 1][field_y] == 0 and \
                    field[field_x + 1][field_y] == 0 and \
                    field[field_x - 1][field_y + 1] == 0:
                        
                        field[field_x][field_y] = 1
                        count_1 += 1

                elif point_y == 10:
                    if field[field_x][field_y] == 0 and \
                    field[field_x - 1][field_y - 1] == 0 and \
                    field[field_x][field_y - 1] == 0 and \
                    field[field_x + 1][field_y - 1] == 0 and \
                    field[field_x - 1][field_y] == 0 and \
                    field[field_x + 1][field_y] == 0:
                        
                        field[field_x][field_y] = 1
                        count_1 += 1

            
            elif point_y == 1:
                if point_x == 1:
                    if field[field_x][field_y] == 0 and \
                    field[field_x][field_y + 1] == 0 and \
                    field[field_x + 1][field_y + 1] == 0 and \
                    field[field_x + 1][field_y] == 0:
                        
                        field[field_x][field_y] = 1
                        count_1 += 1

                elif point_x == 10:
                    if field[field_x][field_y] == 0 and \
                    field[field_x][field_y + 1] == 0 and \
                    field[field_x - 1][field_y] == 0 and \
                    field[field_x - 1][field_y + 1] == 0:

                        field[field_x][field_y] = 1
                        count_1 += 1

            elif point_y == 10:
                if point_x == 1:
                    if field[field_x][field_y] == 0 and \
                    field[field_x][field_y - 1] == 0 and \
                    field[field_x + 1][field_y - 1] == 0 and \
                    field[field_x + 1][field_y] == 0:
                        
                        field[field_x][field_y] = 1
                        count_1 += 1

                elif point_x == 10:
                    if field[field_x][field_y] == 0 and \
                    field[field_x - 1][field_y - 1] == 0 and \
                    field[field_x][field_y - 1] == 0 and \
                    field[field_x - 1][field_y] == 0:
                        
                        field[field_x][field_y] = 1
                        count_1 += 1

            if count_1 == 4:
                status_1 = True


        NavalBattle.playing_field = field
        for i in field:
            print (i)



player1 = NavalBattle('#')
player1.shot(6, 2)
NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1,1)
player1.shot(1,1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)

    