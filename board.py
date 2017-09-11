

class Board():
    # function returns a 2-d empty array which serves as game board
    def make_board(self):
        game_board = []
        for i in range(34):
            game_board.append([])
        return game_board
