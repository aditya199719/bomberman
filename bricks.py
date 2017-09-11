import random


class Bricks():

    """the function generates a random no of bricks
    and adds the brick symbols to the game board"""
    def generate_bricks(self, game_board):
        no_bricks = [i for i in range(10, 31)]
        row_arr = [i for i in range(2, 31, 2)]
        col0 = [i for i in range(16, 61, 4)]
        col4 = [i for i in range(4, 61, 8)]
        col_n = [i for i in range(4, 61, 4)]
        no = random.choice(no_bricks)
        for i in range(no):
            row = random.choice(row_arr)
            if(row == 2):
                col = random.choice(col0)
            elif(row % 4 == 0):
                col = random.choice(col4)
            else:
                col = random.choice(col_n)
            for k in range(row, row+2):
                for l in range(col, col+4):
                    game_board[k][l] = '/'
        return game_board
