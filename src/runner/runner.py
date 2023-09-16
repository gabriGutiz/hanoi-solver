from src.HanoiGame import *
from os import system

class Runner:
    mode: int

    def __init__(self):
        self.run()

    def run(self):
        self.get_mode()
        run = self.get_process()
        run()

    def get_mode(self) -> None:
        while True:
            self._clear_terminal()
            size = input('Size of the game (>=3): ')
            if not size.isnumeric():
                continue

            self.mode = int(size)
            break

    def get_process(self) -> callable:
        self._clear_terminal()
        process = input('Select the execution type\n\t( 1 ) User game\n\t( 2 ) Algorithm solution\nChoose you option: ')
        if process == '1':
            return self.run_user_game
        elif process == '2':
            return self.run_algorithm
        exit()

    def run_algorithm(self) -> None:
        print('Running algorithm')
        pass

    def run_user_game(self) -> None:
        try:
            game = HanoiGame(self.mode)
            while not game.is_solved():
                self._clear_terminal()
                print(game)
                while True:
                    move: Movement
                    try:
                        movement = input('Desired movement (A-B): ').upper().split('-')
                        move = Movement(movement[0][0], movement[-1][0])
                    except Exception as ex:
                        print(ex)
                        print('Invalid stack')
                        continue
                    break
                try:
                    game.make_movement(move)
                except InvalidMovementException as ex:
                    print('Invalid movement')

        except InvalidModeException as ex:
            print(ex)

        print(f'Game solved with {game.movements_quantity()} movements!')

    @staticmethod
    def _clear_terminal() -> None:
        system('cls || clear')
