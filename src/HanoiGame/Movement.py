from src.constants import AllowedStacks

class Movement:
    origin_stack: AllowedStacks
    destiny_stack: AllowedStacks

    def __init__(self, origin: AllowedStacks, destiny: AllowedStacks):
        self.origin_stack = origin
        self.destiny_stack = destiny

    def __str__(self):
        return f'{self.origin_stack} -> {self.destiny_stack}'
