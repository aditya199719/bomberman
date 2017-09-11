

class Wall():

    # function adds boundary walls and walls blocks inside the board
    def make_walls(self, game_board):
        for i in range(2):
            for j in range(68):
                game_board[i]. append('X')
                game_board[33 - i]. append('X')
        for i in range(2, 32):
            if(i % 4 == 2 or i % 4 == 3):
                for j in range(4):
                    game_board[i].append('X')
                for j in range(60):
                    game_board[i].append(' ')
                for j in range(4):
                    game_board[i].append('X')
            else:
                for j in range(0, 65, 4):
                    q = j / 4
                    if(q % 2 == 0):
                        for k in range(4):
                            game_board[i]. append('X')
                    else:
                        for k in range(4):
                            game_board[i]. append(' ')
        return game_board
