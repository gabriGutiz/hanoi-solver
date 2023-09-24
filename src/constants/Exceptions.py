from typing import Any
from src.HanoiGame import Movement

class InvalidMovementException(Exception):
    def __init__(self, moviment: Movement):
        self.moviment = moviment

class InvalidModeException(Exception):
    def __init__(self, message: str, mode: Any):
        self.message = message
        self.mode = mode
