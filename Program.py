import re
from AI import AI
from Human import Human

class Game:
    def __init__(self):
        self.state = [[0 for _ in range(3)] for _ in range(3)]

    def render(self):
        print()
        print("   a   b   c")

        for i in range(len(self.state)):
            print(f"{i + 1}   {self.get_symbol(self.state[i][0])}", end="")

            for j in range(1, len(self.state[i])):
                print(f"|  {self.get_symbol(self.state[i][j])} ", end="")
            print()

            if i < 2:
                print("   -----------")
        print()

    def get_symbol(self, val):
        if val < 0:
            return 'O'
        elif val == 0:
            return ' '
        else:
            return 'X'

    @staticmethod
    def main():
        game = Game()
        game.render()
        print("Jogo da Velha!")
        print("======================")

        difficulty = -1
        while difficulty < 0 or difficulty > 3:
            print("Escolha a Dificuldade")
            print("0 - Eu quero minha mãe")
            print("1 - Ainda mijo na cama:")
            print("2 - I'm Batman!")
            print("3 - Birl! Chuck Norris!")
            print()
            difficulty = int(input("Difficulty: "))

        print("======================")
        print()

        turn = -1
        while turn < 0 or turn > 1:
            turn = int(input("Se você quer iniciar digite 0, senão 1: "))

        print("======================")
        print()

        ai = AI(game.state, -1)
        ai.set_difficulty(difficulty)
        ai2 = AI(game.state, 1)
        ai2.set_difficulty(difficulty)

        players = [None, None]
        if turn == 1:
            players[1] = Human(game.state, 1)
            players[0] = ai
        else:
            players[0] = Human(game.state, 1)
            players[1] = ai

        i = 0
        status = None

        while (status := AI.check_victory(game.state)) is None:
            game.render()
            players[i].play()
            i = (i + 1) % 2

        if status == -1:
            print("Game Over, Patinho!")

        elif status == 1:
            print("You Won!")

        elif status == 0:
            print("Draw!")

if __name__ == "__main__":
    Game.main()
