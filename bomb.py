

class Bomb():

    # function to plant the bomb at given location
    def plant_bomb(self, final_board, c):
        if(final_board[c[0]][c[1]] == '\u001b[0;36mZ\u001b[0m'):
                return {'final_board': final_board, 'status': 1}
        else:
            for i in range(c[0], c[0]+2):
                for j in range(c[1], c[1]+4):
                    final_board[i][j] = '\u001b[0;36mZ\u001b[0m'
            return {'f_board': final_board, 'status': 0}

    # function to print remaining count on the bomb
    def p_count(self, final_board, coordinates, count):
        count = 2 - count
        st = '\u001b[0;36m%d\u001b[0m' % count
        for i in range(coordinates[0], coordinates[0]+2):
            for j in range(coordinates[1], coordinates[1]+4):
                final_board[i][j] = st
        return final_board

    # function to score the explosion and print it on board
    def explode_bomb(self, final_board, coordinates, e_arr):
        score = 0
        x = coordinates[0]
        y = coordinates[1]
        if(final_board[x][y+4] == '/'):
            score += 20
        if(final_board[x][y-4] == '/'):
            score += 20
        if(final_board[x-2][y] == '/'):
            score += 20
        if(final_board[x+2][y] == '/'):
            score += 20
        for index, i in enumerate(e_arr):
            if([x, y] == [i[0], i[1]]):
                e_arr.pop(index)
                score += 50
            elif([x-2, y] == [i[0], i[1]]):
                e_arr.pop(index)
                score += 50
            elif([x+2, y] == [i[0], i[1]]):
                e_arr.pop(index)
                score += 50
            elif([x, y-4] == [i[0], i[1]]):
                e_arr.pop(index)
                score += 50
            elif([x, y+4] == [i[0], i[1]]):
                e_arr.pop(index)
                score += 50
        for i in range(coordinates[0], coordinates[0]+2):
            for j in range(coordinates[1], coordinates[1]+4):
                final_board[i][j] = '^'
        if(final_board[coordinates[0]+2][coordinates[1]] != 'X'):
            for i in range(coordinates[0]+2, coordinates[0]+4):
                for j in range(coordinates[1], coordinates[1]+4):
                    final_board[i][j] = '^'
        if(final_board[coordinates[0]-2][coordinates[1]] != 'X'):
            for i in range(coordinates[0]-2, coordinates[0]):
                for j in range(coordinates[1], coordinates[1]+4):
                    final_board[i][j] = '^'
        if(final_board[coordinates[0]][coordinates[1]+4] != 'X'):
            for i in range(coordinates[0], coordinates[0]+2):
                for j in range(coordinates[1]+4, coordinates[1]+8):
                    final_board[i][j] = '^'
        if(final_board[coordinates[0]][coordinates[1]-4] != 'X'):
            for i in range(coordinates[0], coordinates[0]+2):
                for j in range(coordinates[1]-4, coordinates[1]):
                    final_board[i][j] = '^'
        return {'f_board': final_board, 'e_arr': e_arr, 'score': score}

    # clear space after explosion
    def clear_space(self, final_board, coordinates):
        for i in range(coordinates[0], coordinates[0]+2):
            for j in range(coordinates[1], coordinates[1]+4):
                final_board[i][j] = ' '
        if(final_board[coordinates[0]+2][coordinates[1]] == '^'):
            for i in range(coordinates[0]+2, coordinates[0]+4):
                for j in range(coordinates[1], coordinates[1]+4):
                    final_board[i][j] = ' '
        if(final_board[coordinates[0]-2][coordinates[1]] == '^'):
            for i in range(coordinates[0]-2, coordinates[0]):
                for j in range(coordinates[1], coordinates[1]+4):
                    final_board[i][j] = ' '
        if(final_board[coordinates[0]][coordinates[1]+4] == '^'):
            for i in range(coordinates[0], coordinates[0]+2):
                for j in range(coordinates[1]+4, coordinates[1]+8):
                    final_board[i][j] = ' '
        if(final_board[coordinates[0]][coordinates[1]-4] == '^'):
            for i in range(coordinates[0], coordinates[0]+2):
                for j in range(coordinates[1]-4, coordinates[1]):
                    final_board[i][j] = ' '
        return final_board
