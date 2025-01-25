class ActionIterator:
    def __init__(self, estado, vazios, player):
        self.estado = [row[:] for row in estado]  # Clone the 2D array
        self.vazios = vazios.copy()  # Copy the list
        self.player = player
        self.jogada = 0

    def next(self):
        self.jogada += 1
        return self.jogada < len(self.vazios)

    def get_vazios(self):
        ret = self.vazios.copy()
        ret.pop(self.jogada)
        return ret

    def get_estado(self):
        estado_clone = [row[:] for row in self.estado]  # Clone the 2D array
        p = self.vazios[self.jogada]
        estado_clone[p.line][p.column] = self.player
        return estado_clone

    def get_move(self):
        return self.vazios[self.jogada]

# Helper class for moves
class Move:
    def __init__(self, line, column):
        self.line = line
        self.column = column
