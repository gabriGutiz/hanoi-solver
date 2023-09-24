
class State:
    def __init__(self, game: str, last_state=None):
        self.last = last_state
        self.game = game


    def __str__(self):
        if self.last is None:
            return self.game
        return f'{self.last} -> {self.game}'

