import os
import time
import keyboard
from src.pacman import Pacman

move_dict = {
    'w': 'up',
    'a': 'left',
    's': 'down',
    'd': 'right',
}


class PacmanGame:
    def __init__(self, game_map, pacman_position, ghost_position):
        self.game_map = game_map
        self.pacman_position = pacman_position
        self.ghost_position = ghost_position

    def __setup_map(self):
        self.game_map[self.pacman_position[0]][self.pacman_position[1]] = 'PM'
        self.game_map[self.ghost_position[0]][self.ghost_position[1]] = 'F'

    def write_game_map(self):
        qnt_lines = len(self.game_map)
        qnt_columns = len(self.game_map)

        for i in range(qnt_lines):
            for j in range(qnt_columns):
                print(self.game_map[i][j], end=" ")
            print('\n')

    def run(self):
        while True:
            self.write_game_map()
            if keyboard.read_key() in move_dict.keys():
                move = move_dict.get(keyboard.read_key())
                game_map, pacman_position = Pacman(self.game_map, self.pacman_position, move).move_pacman()
                self.game_map = game_map
                self.pacman_position = pacman_position

            else:
                print("Tecla inválida")

            os.system('cls' if os.name == 'nt' else 'clear')
