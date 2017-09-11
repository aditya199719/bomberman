from game import Game

final = Game()
a = final.start_game(1)
if(a == 1):
    b = final.start_game(2)
    if(b == 1):
        final.start_game(3)
