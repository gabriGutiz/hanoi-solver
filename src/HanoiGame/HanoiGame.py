import logging as LOG
from collections import deque

from .Exceptions import InvalidModeException, InvalidMovementException
from .constants import StackA, StackB, StackC
from .Movement import Movement

class HanoiGame:
    stack_a = deque()
    stack_b = deque()
    stack_c = deque()

    mode: int
    game = {
        StackA: stack_a,
        StackB: stack_b,
        StackC: stack_c
    }
    movements: list[Movement]

    def __init__(self, mode: int=3):
        if not isinstance(mode, int):
            raise InvalidModeException('Mode must be of type int', mode)
        if mode < 3:
            raise InvalidModeException('Mode must be bigger or equals to 3', mode)

        self.mode = mode
        self.movements = []

        for i in range(0, mode):
            self.stack_a.append(mode-i)

    def make_movement(self, movement: Movement) -> None:
        if not self.movement_is_valid:
            raise InvalidMovementException(movement)

        self.game[movement.destiny_stack].append(self.game[movement.origin_stack].pop())
        self.movements.append(movement)

    def movement_is_valid(self, movement: Movement) -> bool:
        if self.game[movement.origin_stack].count == 0:
            return False
        if self.game[movement.origin_stack][-1] > self.game[movement.destiny_stack][-1]:
            return False
        return True

    def is_solved(self) -> bool:
        pass

    def __str__(self) -> str:
        response = 'Game:\n'
        for i in range(self.mode):
            for stack in self.game.values():
                response += '  '
                try:
                    val = list(stack)[self.mode - (i+1)]
                    response += str(val)
                except IndexError:
                    response += '|'
            response += '\n'

        response += ' ---------\n  A  B  C\n\nMovements: '
        for movement in self.movements:
            response += str(movement)
            response += ';'

        return response+'\n-----------------------'
