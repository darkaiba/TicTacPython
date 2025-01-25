import re

class Human:
    def __init__(self, state, player):
        self.state = state
        self.player = player
        self.name = f"Human: {player}"

    def play(self):
        move_input = input("Move: ")
        move = self.parse_move(move_input)

        if move is None:
            print("Invalid move. Try again.")
            self.play()
        else:
            self.state[move.line][move.column] = self.player

    def parse_move(self, move):
        regex = re.compile(r"([a-c])([1-3])")
        match = regex.match(move)

        if not match:
            return None

        move_result = Move()
        move_result.column = ord(match.group(1)) - ord('a')
        move_result.line = int(match.group(2)) - 1

        return move_result

class Move:
    def __init__(self):
        self.line = 0
        self.column = 0
