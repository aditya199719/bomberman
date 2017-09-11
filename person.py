

class Person():

    # generates person at top left corner of the board
    def make_person(self, game_board, c):
        x = c[0]
        y = c[1]
        for i in range(x, x+2):
            for j in range(y, y+4):
                game_board[i][j] = '\u001b[0;33mB\u001b[0m'
        return game_board

    # function for moving right
    def move_right(self, final_board, c):
        if(final_board[c[0]][c[1]+4] == '\u001b[0;31mE\u001b[0m'):
            pass
        elif(final_board[c[0]][c[1]+4] != ' '):
            return {'coordinates': c, 'f_board': final_board}

        if(final_board[c[0]][c[1]] == '\u001b[0;36m2\u001b[0m'):
            clear_board = self.clear_bomb(final_board, c)
        else:
            clear_board = self.clear(final_board, c)
        c[1] += 4
        game_board = self.make_person(clear_board, c)
        return {'coordinates': c, 'f_board': game_board}

    # function for moving left
    def move_left(self, final_board, c):
        if(final_board[c[0]][c[1]-4] == '\u001b[0;31mE\u001b[0m'):
            pass
        elif(final_board[c[0]][c[1]-4] != ' '):
            return {'coordinates': c, 'f_board': final_board}
        if(final_board[c[0]][c[1]] == '\u001b[0;36m2\u001b[0m'):
            clear_board = self.clear_bomb(final_board, c)
        else:
            clear_board = self.clear(final_board, c)
        c[1] -= 4
        game_board = self.make_person(clear_board, c)
        return {'coordinates': c, 'f_board': game_board}

    # function for moving upwards
    def move_up(self, final_board, c):
        if(final_board[c[0]-2][c[1]] == '\u001b[0;31mE\u001b[0m'):
            pass
        elif(final_board[c[0]-2][c[1]] != ' '):
            return {'coordinates': c, 'f_board': final_board}
        if(final_board[c[0]][c[1]] == '\u001b[0;36m2\u001b[0m'):
            clear_board = self.clear_bomb(final_board, c)
        else:
            clear_board = self.clear(final_board, c)
        c[0] -= 2
        game_board = self.make_person(clear_board, c)
        return {'coordinates': c, 'f_board': game_board}

    # function for moving downwards
    def move_down(self, final_board, c):
        if(final_board[c[0]+2][c[1]] == '\u001b[0;31mE\u001b[0m'):
            pass
        elif(final_board[c[0]+2][c[1]] != ' '):
            return {'coordinates': c, 'f_board': final_board}
        if(final_board[c[0]][c[1]] == '\u001b[0;36m2\u001b[0m'):
            clear_board = self.clear_bomb(final_board, c)
        else:
            clear_board = self.clear(final_board, c)
        c[0] += 2
        game_board = self.make_person(clear_board, c)
        return {'coordinates': c, 'f_board': game_board}

    # function for clearing the previous position of the person
    def clear(self, final_board, c):
        x = c[0]
        y = c[1]
        for i in range(x, x+2):
            for j in range(y, y+4):
                final_board[i][j] = ' '
        return final_board

    # function for clearing pevious position after planting bomb
    def clear_bomb(self, final_board, c):
        x = c[0]
        y = c[1]
        for i in range(x, x+2):
            for j in range(y, y+4):
                final_board[i][j] = '\u001b[0;36m2\u001b[0m'
        return final_board
