import random
from person import Person


class Enemy(Person):

    # function for generating coordinates of enemies
    def plant_enemies(self, e_arr, level):
        row_arr = [i for i in range(2, 31, 2)]
        col0 = [i for i in range(16, 61, 4)]
        col4 = [i for i in range(4, 61, 8)]
        col_n = [i for i in range(4, 61, 4)]
        if(level == 1):
            no = random.choice(range(2, 4))
        elif(level == 2):
            no = random.choice(range(4, 7))
        else:
            no = random.choice(range(8, 12))
        for i in range(no):
            row = random.choice(row_arr)
            if(row == 2):
                col = random.choice(col0)
            elif(row % 4 == 0):
                col = random.choice(col4)
            else:
                col = random.choice(col_n)
            e_arr.append((row, col))
        e_arr = list(set(e_arr))
        # print(e_arr[0])
        return e_arr

    # function for placing the enemies on the board array
    def place_enemies(self, final_board, e_arr):
        for i in e_arr:
            x = i[0]
            y = i[1]
            # print(e_arr)
            for j in range(x, x+2):
                for k in range(y, y+4):
                    final_board[j][k] = '\u001b[0;31mE\u001b[0m'
        return final_board

    # function for generating random movement for each enemy
    def move_enemy(self, final_board, e_arr, cord):
        arr = [1, 2, 3, 4]
        for index, i in enumerate(e_arr):
            direct = random.choice(arr)
            x = [i[0], i[1]]
            if(cord == x):
                for i in range(x[0], x[0]+2):
                    for j in range(x[1], x[1]+4):
                        print('cc')
                        final_board[i][j] = '\u001b[0;31mE\u001b[0m'
                return {'s': -1, 'f': final_board, 'e': e_arr}
            if(final_board[x[0]][x[1]] == '^'):
                e_arr.pop(index)
                continue
            flag = -1
            count = 0
            while flag == -1 and count < 4:
                if(direct == 1):
                    dic = self.move_right(final_board, x)
                    flag = dic['flag']
                    final_board = dic['final_board']
                    if(flag == 0):
                        i = (i[0], i[1] + 4)
                        e_arr[index] = i
                elif(direct == 2):
                    dic = self.move_down(final_board, x)
                    flag = dic['flag']
                    final_board = dic['final_board']
                    if(flag == 0):
                        i = (i[0] + 2, i[1])
                        e_arr[index] = i
                elif(direct == 3):
                    dic = self.move_left(final_board, x)
                    flag = dic['flag']
                    final_board = dic['final_board']
                    if(flag == 0):
                        i = (i[0], i[1] - 4)
                        e_arr[index] = i
                elif(direct == 4):
                    dic = self.move_up(final_board, x)
                    flag = dic['flag']
                    final_board = dic['final_board']
                    if(flag == 0):
                        i = (i[0] - 2, i[1])
                        e_arr[index] = i
                if(flag == -1):
                    direct = random.choice(arr)
                count += 1
            if(cord == [i[0], i[1]]):
                return {'s': -1, 'f': final_board, 'e': e_arr}
        return {'s': 0, 'f': final_board, 'e': e_arr}

    def move_right(self, final_board, x):
        if(final_board[x[0]][x[1]+4] == '\u001b[0;33mB\u001b[0m'):
            pass
        elif(final_board[x[0]][x[1]+4] != ' '):
            return {'flag': -1, 'final_board': final_board}
        for i in range(x[0], x[0]+2):
            for j in range(x[1]+4, x[1]+8):
                final_board[i][j] = '\u001b[0;31mE\u001b[0m'
                final_board[i][j-4] = ' '

        return {'flag': 0, 'final_board': final_board}

    def move_left(self, final_board, x):
        if(final_board[x[0]][x[1]-4] == '\u001b[0;33mB\u001b[0m'):
            pass
        elif(final_board[x[0]][x[1]-4] != ' '):
            return {'flag': -1, 'final_board': final_board}
        for i in range(x[0], x[0]+2):
            for j in range(x[1]-4, x[1]):
                final_board[i][j] = '\u001b[0;31mE\u001b[0m'
                final_board[i][j+4] = ' '

        return {'flag': 0, 'final_board': final_board}

    def move_up(self, final_board, x):
        if(final_board[x[0]-2][x[1]] == '\u001b[0;33mB\u001b[0m'):
            pass
        elif(final_board[x[0]-2][x[1]] != ' '):
            return {'flag': -1, 'final_board': final_board}
        for i in range(x[0]-2, x[0]):
            for j in range(x[1], x[1]+4):
                final_board[i][j] = '\u001b[0;31mE\u001b[0m'
                final_board[i+2][j] = ' '

        return {'flag': 0, 'final_board': final_board}

    def move_down(self, final_board, x):
        if(final_board[x[0]+2][x[1]] == '\u001b[0;33mB\u001b[0m'):
            pass
        elif(final_board[x[0]+2][x[1]] != ' '):
            return {'flag': -1, 'final_board': final_board}
        for i in range(x[0]+2, x[0]+4):
            for j in range(x[1], x[1]+4):
                final_board[i][j] = '\u001b[0;31mE\u001b[0m'
                final_board[i-2][j] = ' '

        return {'flag': 0,  'final_board': final_board}
