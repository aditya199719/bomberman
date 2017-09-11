import os
import tty
import termios
import random
import time
import sys
from wall import Wall
from board import Board
from bricks import Bricks
from bomb import Bomb
from enemies import Enemy


class Game(Board, Wall, Bricks, Bomb, Enemy):

    def start_game(self, level):
        key = 0
        bomb_stat = 0
        self.__lives = 2
        self.__score = 0
        self.__c = [2, 4]
        print("a")
        self.__e = super(Bomb, self).plant_enemies(self.__e, level)
        board = super(Game, self).make_board()
        wall_board = super(Board, self).make_walls(board)
        game_board = super(Wall, self).generate_bricks(wall_board)
        f_board = super(Enemy, self).make_person(game_board, self.__c)
        f_board = super(Bomb, self).place_enemies(f_board, self.__e)
        self.print_board(f_board, level)
        while True:
            if(bomb_stat == -1):
                if(count <= 2):
                    f_board = super(Bricks, self).p_count(f_board, arr, count)
                    self.print_board(f_board, level)
                    count += 1
                elif(count > 2):
                    if(dic_b['status'] == 0):
                        f_board = self.print_explosion(f_board, arr, level)
                        count = 0
                        bomb_stat = 0
            if(not self.__e):
                if(level != 3):
                    print("level complete...next level in 3 sec")
                    time.sleep(3)
                else:
                    print("Game complete", end="\r\n")
                return 1
            if(self.__stat == -1 and self.__lives <= 0):
                return 0
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                key = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd,  termios.TCSADRAIN,  old_settings)
            if(key == 'd'):
                dic = super(Enemy, self).move_right(f_board, self.__c)
                f_board = dic['f_board']
                self.__c = dic['coordinates']
            elif(key == 'w'):
                dic = super(Enemy, self).move_up(f_board, self.__c)
                f_board = dic['f_board']
                self.__c = dic['coordinates']
            elif(key == 's'):
                dic = super(Enemy, self).move_down(f_board, self.__c)
                f_board = dic['f_board']
                self.__c = dic['coordinates']
            elif(key == 'a'):
                dic = super(Enemy, self).move_left(f_board, self.__c)
                f_board = dic['f_board']
                self.__c = dic['coordinates']
            elif(key == 'b'):
                if(bomb_stat == 0):
                    dic_b = super(Bricks, self).plant_bomb(f_board, self.__c)
                    bomb_stat = -1
                    f_board = dic_b['f_board']
                    count = 0
                    arr = [self.__c[0], self.__c[1]]
            elif(key == 'q'):
                return 0
            dic2 = super(Bomb, self).move_enemy(f_board, self.__e, self.__c)
            f_board = dic2['f']
            self.__stat = dic2['s']
            self.__e = dic2['e']
            self.print_board(f_board, level)
            if(self.__stat == -1):
                if(self.__lives <= 0):
                    print("Game over \n Score:%d" % self.__score)
                    return 0
                else:
                    if(bomb_stat == -1):
                        arr = super(Enemy, self).clear(f_board, arr)
                        bomb_stat = 0
                    time.sleep(0.5)
                    self.restore_person(f_board, level)
        return 0

    def print_explosion(self, f_board, c_b, level):
        x = c_b[0]
        y = c_b[1]
        dic = super(Bricks, self).explode_bomb(f_board, c_b, self.__e)
        f_board = dic['f_board']
        self.__score += dic['score']
        self.__e = dic['e_arr']
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(sys.stdin)
        self.print_board(f_board, level)
        if([x, y]==self.__c or  [x-2, y]==self.__c or [x+2, y]==self.__c or [x, y-4]==self.__c or [x, y+4]==self.__c):
            self.__stat = -1
        time.sleep(0.5)
        f_board = super(Bricks, self).clear_space(f_board, c_b)
        self.print_board(f_board, level)
        if(self.__stat == -1):
            if(self.__lives <= 0):
                self.__lives -= 1
                print("Game over \n Score:%d" % self.__score)
            else:
                self.restore_person(f_board, level)
        termios.tcsetattr(fd,  termios.TCSADRAIN,  old_settings)
        return f_board

    def print_board(self, f_board, level):
        os.system("clear")
        print('                               BOMBERMAN', end='\r\n')
        print("Score:%d                         Level:%d                    Lives:%d\n" %(self.__score, level, self.__lives), end ='\r\n')
        for i in range(34):
            print(''.join(f_board[i]), end='\r\n')

    def restore_person(self, f_board, level):
        self.__lives -= 1
        self.__c = [2, 4]
        f_board = super(Enemy, self).make_person(f_board, self.__c)
        self.print_board(f_board, level)
        self.__stat = 0
        return f_board

    def __init__(self):
        self.__c = [2, 4]
        self.__stat = 0
        self.__e = []
        self.__score = 0
        self.__lives = 2
