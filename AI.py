import math
from typing import List, Optional

class AI:
    def __init__(self, matriz: List[List[int]], player: int):
        self.matriz = matriz
        self.max_depth = 1
        self.player = player
        self.current_max_depth = 1
        self.name = f"AI: {player}"

    def get_matriz(self):
        return self.matriz

    def get_player(self):
        return self.player

    def set_matriz(self, matriz: List[List[int]]):
        self.matriz = matriz

    def set_difficulty(self, difficulty: int):
        self.max_depth = 1 + difficulty * 3

    def heuristic_value(self, line: List[int]) -> int:
        plus = line.count(1)
        minus = line.count(-1)

        if plus > 0 and minus > 0:
            return 0
        return plus - minus

    def heuristic(self, state: List[List[int]], depth: int, empty_size: int) -> Optional[int]:
        end = self.check_victory(state)

        if end is not None:
            return int(math.exp(10)) * end

        if depth < self.current_max_depth:
            return None

        res = 0

        d1 = [state[i][i] for i in range(3)]
        d2 = [state[i][2 - i] for i in range(3)]

        for i in range(3):
            linha = state[i]
            coluna = [state[j][i] for j in range(3)]

            res += self.heuristic_value(linha)
            res += self.heuristic_value(coluna)

        res += self.heuristic_value(d1)
        res += self.heuristic_value(d2)

        return res

    @staticmethod
    def check_victory(state: List[List[int]]) -> Optional[int]:
        d1 = sum(state[i][i] for i in range(3))
        d2 = sum(state[i][2 - i] for i in range(3))
        used = sum(cell != 0 for row in state for cell in row)

        for i in range(3):
            line = sum(state[i])
            column = sum(state[j][i] for j in range(3))

            if abs(line) == 3:
                return line // abs(line)
            if abs(column) == 3:
                return column // abs(column)

        if abs(d1) == 3:
            return d1 // abs(d1)
        if abs(d2) == 3:
            return d2 // abs(d2)

        if used == 9:
            return 0

        return None

    def max(self, state: List[List[int]], empty: List, player: int, alpha: int, beta: int, depth: int) -> int:
        result_n = self.heuristic(state, depth, len(empty))

        if result_n is not None:
            return self.player * result_n

        v = -math.inf

        for move in empty:
            new_state = [row[:] for row in state]
            new_state[move[0]][move[1]] = player

            empty_copy = empty[:]
            empty_copy.remove(move)

            nv = self.min(new_state, empty_copy, -player, alpha, beta, depth + 1)

            v = max(v, nv)
            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    def min(self, state: List[List[int]], empty: List, player: int, alpha: int, beta: int, depth: int) -> int:
        result_n = self.heuristic(state, depth, len(empty))

        if result_n is not None:
            return self.player * result_n

        v = math.inf

        for move in empty:
            new_state = [row[:] for row in state]
            new_state[move[0]][move[1]] = player

            empty_copy = empty[:]
            empty_copy.remove(move)

            nv = self.max(new_state, empty_copy, -player, alpha, beta, depth + 1)

            v = min(v, nv)
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v

    def get_best_move(self):
        empty = [(i, j) for i in range(3) for j in range(3) if self.matriz[i][j] == 0]
        state = [row[:] for row in self.matriz]

        self.current_max_depth = max(1, self.max_depth * len(empty) // 9)

        best_move = None
        v = -math.inf

        for move in empty:
            new_state = [row[:] for row in state]
            new_state[move[0]][move[1]] = self.player

            empty_copy = empty[:]
            empty_copy.remove(move)

            nv = self.min(new_state, empty_copy, -self.player, -math.inf, math.inf, 1)

            if nv > v:
                v = nv
                best_move = move

        return best_move

    def play(self):
        best_move = self.get_best_move()
        if best_move:
            self.matriz[best_move[0]][best_move[1]] = self.player
