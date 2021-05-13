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
        self.block = 0

    def __setup_map(self):
        self.game_map[self.pacman_position[0]][self.pacman_position[1]] = 'P'
        self.game_map[self.ghost_position[0]][self.ghost_position[1]] = 'F'

    def write_game_map(self):
        qnt_lines = len(self.game_map)
        qnt_columns = len(self.game_map)

        for i in range(qnt_lines):
            for j in range(qnt_columns):
                print(self.game_map[i][j], end=" ")
            print('\n')

    def __check_victory(self):
        victory = True
        for line in self.game_map:
            if "." in line:
                victory = False
                break

        return victory


    def run(self):
        self.__setup_map()
        while True:
            self.write_game_map()
            if not self.__check_victory():
                if keyboard.read_key() in move_dict.keys():
                    move = move_dict.get(keyboard.read_key())
                    game_map, pacman_position, block = Pacman(self.game_map, self.pacman_position, move, self.block).move_pacman()
                    self.game_map = game_map
                    self.pacman_position = pacman_position
                    self.block = block

            else:
                break

            os.system('cls' if os.name == 'nt' else 'clear')

        print("PARABENS VOCÊ VENCEU")
