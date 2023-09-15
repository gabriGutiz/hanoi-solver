from src.HanoiGame import *

class Runner:
    def __init__(self, mode: int=3):
        self.mode = mode
        self.run()

    def run(self):
        try:
            game = HanoiGame(self.mode)
            print(game)
            game.make_movement(Movement(StackA, StackB))
            print(game)
        except InvalidModeException as ex:
            print(ex)
