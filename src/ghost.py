from random import choice
import copy

GOOD_BLOCKS = [".", " "]
BAD_BLOCKS = ["="]
ENEMY_BLOCKS = ["P"]


class Ghost:
    def __init__(self, game_map, output_map, ghost_position):
        self.game_map = game_map
        self.output_map = output_map
        self.ghost_position = ghost_position
        self.lose = False

    def __get_ghost_move_possibilities(self):
        possibilities = []
        pacman_column = [l[self.ghost_position[1]] for l in self.output_map]
        pacman_line = self.output_map[self.ghost_position[0]]

        up_status = pacman_column[self.ghost_position[0] - 1]
        down_status = pacman_column[self.ghost_position[0] + 1]
        left_status = pacman_line[self.ghost_position[1] - 1]
        right_status = pacman_line[self.ghost_position[1] + 1]

        factory_status = {
            "up": up_status,
            "down": down_status,
            "left": left_status,
            "right": right_status
        }

        for possibility, possibility_value in zip(factory_status.keys(), factory_status.values()):
            if possibility_value in GOOD_BLOCKS:
                possibilities.append(possibility)

        return possibilities

    def get_move(self):
        return choice(self.__get_ghost_move_possibilities())

    def get_next_ghost_position_location(self):
        next_up_position = [self.ghost_position[0] - 1, self.ghost_position[1]]
        next_down_position = [self.ghost_position[0] + 1, self.ghost_position[1]]
        next_left_position = [self.ghost_position[0], self.ghost_position[1] - 1]
        next_right_position = [self.ghost_position[0], self.ghost_position[1] + 1]

        factory_position = {
            "up": next_up_position,
            "down": next_down_position,
            "left": next_left_position,
            "right": next_right_position
        }

        return factory_position.get(self.get_move())

    def move_ghost(self):
        next_ghost_position_location = self.get_next_ghost_position_location()
        if self.output_map[next_ghost_position_location[0]][next_ghost_position_location[1]] in ENEMY_BLOCKS:
            self.lose = True

        self.output_map[self.ghost_position[0]][self.ghost_position[1]] = copy.deepcopy(self.game_map[self.ghost_position[0]][self.ghost_position[1]])
        self.output_map[next_ghost_position_location[0]][next_ghost_position_location[1]] = "F"

        response = (self.output_map, next_ghost_position_location, self.lose)

        return response
