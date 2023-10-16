from src.HanoiGame import *
from src.Solver import *
from os import system
import time

class Runner:
    mode: int

    def __init__(self):
        self.run()


    def run(self):
        self.get_mode()
        run = self.get_process()


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
        process = input('Select the execution type\n\t( 1 ) User game\n\t( 2 ) Algorithm solution\n\t( 3 ) Optimized algorithm solution\nChoose you option: ')
        match process:
            case '1':
                return self.run_user_game()
            case '2':
                return self.run_algorithm()
            case '3':
                return self.run_optimized_algorithm()
        exit()


    def run_algorithm(self) -> None:
        print('\nRunning algorithm...')
        solver = Solver(''.join('1' for _ in range(self.mode)))

        start_time = time.time()
        solution = solver.solve()
        print(f'\nSolution: {solution}')
        print(f'Solved in {time.time() - start_time:.2f} s')


    def run_optimized_algorithm(self) -> None:
        print('\nRunning optimized algorithm...')
        solver = Solver(''.join('1' for _ in range(self.mode)))

        start_time = time.time()
        solution = solver.solve_optimized()
        print(f'\nSolution: {solution}')
        print(f'Solved in {time.time() - start_time:.2f} s')


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

