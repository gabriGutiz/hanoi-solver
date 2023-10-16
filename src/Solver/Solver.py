from src.constants import InvalidModeException
from .State import State


class Solver:
    def __init__(self, game: str):
        if self.game_is_valid(game):
            self.initial_state = State(game)
            self.states = [State(game)]
            self.state_op = State(''.join(['1' for i in range(len(game))]))


    @staticmethod
    def game_is_valid(game: str) -> bool:
        if len(game) < 3:
            raise InvalidModeException('Mode must be bigger or equals to 3', 3)
        return True


    @staticmethod
    def possible_movements(state: State) -> list[State]:
        movements = []
        for i, char in enumerate(state.game):
            if state.game[:i].find(char) != -1:
                continue
            for j in range(1, len(state.game)+1):
                if str(j) == char or state.game[:i].find(str(j)) != -1:
                    continue
                new_game = list(state.game)
                new_game[i] = str(j)
                movements.append(State(''.join(new_game), state))
        return movements


    @staticmethod
    def is_solved(state: State) -> bool:
        solved = ''.join(['3' for _ in range(len(state.game))])
        return state.game == solved


    def solve_optimized(self):
        self._solve_optimized(len(self.state_op.game), '1', '3', '2')
        return self.state_op


    def _solve_optimized(self, n, from_rod, to_rod, aux_rod):
        if n == 0:
            return
        self._solve_optimized(n-1, from_rod, aux_rod, to_rod)

        state = self.state_op.game
        new_game = list(state)
        new_game[n-1] = to_rod

        new_state = State(''.join(new_game), self.state_op)
        self.state_op = new_state

        self._solve_optimized(n-1, aux_rod, to_rod, from_rod)


    def solve(self) -> State:
        new_states = []
        for state in self.states:
            for move in self.possible_movements(state):
                if self.is_solved(move):
                    return move
                if state.last and move.game == state.last.game:
                    continue
                new_states.append(move)
        self.states = new_states
        return self.solve()

