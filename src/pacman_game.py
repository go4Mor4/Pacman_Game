import os
import time
import keyboard
from src.pacman import Pacman
from src.ghost import Ghost
import copy

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
        self.output_map = None

    def __get_output_map(self):
        output_map = copy.deepcopy(self.game_map)

        output_map[self.pacman_position[0]][self.pacman_position[1]] = 'P'
        output_map[self.ghost_position[0]][self.ghost_position[1]] = 'F'

        return output_map

    def print_game(self):
        qnt_lines = len(self.output_map)
        qnt_columns = len(self.output_map[0])

        for i in range(qnt_lines):
            for j in range(qnt_columns):
                print(self.output_map[i][j], end=" ")
            print('\n')

        if self.block != 0:
            print(f"Movimento bloquado por {self.block} rodadas")

    def __check_victory(self):
        victory = True
        for line in self.game_map:
            if "." in line:
                victory = False
                break

        return victory

    def run(self):
        self.output_map = self.__get_output_map()
        while True:
            self.print_game()
            if not self.__check_victory():
                if keyboard.read_key() in move_dict.keys():
                    move = move_dict.get(keyboard.read_key())
                    game_map, output_map, pacman_position, block, lose = Pacman(self.game_map, self.output_map,
                                                                                self.pacman_position,
                                                                                move, self.block).move_pacman()

                    self.game_map = game_map
                    self.output_map = output_map
                    self.pacman_position = pacman_position
                    self.block = block

                    if lose:
                        print("VOCÊ PERDEU")
                        break

                    output_map, ghost_position, lose = Ghost(self.game_map,
                                                             self.output_map,
                                                             self.ghost_position).move_ghost()
                    self.output_map = output_map
                    self.ghost_position = ghost_position

            else:
                print("PARABENS VOCÊ VENCEU")
                break

            os.system('cls' if os.name == 'nt' else 'clear')
