GOOD_BLOCKS = [".", " "]
BAD_BLOCKS = ["="]
ENEMY_BLOCKS = ["F"]


class Pacman:
    def __init__(self, game_map, output_map, pacman_position, move, block):
        self.game_map = game_map
        self.output_map = output_map
        self.pacman_position = pacman_position
        self.move = move
        self.block = block
        self.lose = False

    @property
    def current_move_status(self):
        pacman_column = [l[self.pacman_position[1]] for l in self.output_map]
        pacman_line = self.output_map[self.pacman_position[0]]

        up_status = pacman_column[self.pacman_position[0] - 1]
        down_status = pacman_column[self.pacman_position[0] + 1]
        left_status = pacman_line[self.pacman_position[1] - 1]
        right_status = pacman_line[self.pacman_position[1] + 1]

        factory_status = {
            "up": up_status,
            "down": down_status,
            "left": left_status,
            "right": right_status
        }

        return factory_status.get(self.move)

    @property
    def next_pacman_position_location(self):
        next_up_position = [self.pacman_position[0] - 1, self.pacman_position[1]]
        next_down_position = [self.pacman_position[0] + 1, self.pacman_position[1]]
        next_left_position = [self.pacman_position[0], self.pacman_position[1] - 1]
        next_right_position = [self.pacman_position[0], self.pacman_position[1] + 1]

        factory_position = {
            "up": next_up_position,
            "down": next_down_position,
            "left": next_left_position,
            "right": next_right_position
        }

        return factory_position.get(self.move)

    def _validate_move(self):
        if self.current_move_status in BAD_BLOCKS:
            self.block = 2
            return False

        elif self.current_move_status in ENEMY_BLOCKS:
            self.lose = True
            return False

        elif self.current_move_status in GOOD_BLOCKS:
            return True

    def move_pacman(self):
        if self.block != 0:
            self.block -= 1
            response = (self.game_map, self.output_map, self.pacman_position, self.block, self.lose)
        else:
            if self._validate_move():
                self.game_map[self.pacman_position[0]][self.pacman_position[1]] = " "
                self.output_map[self.pacman_position[0]][self.pacman_position[1]] = " "
                self.output_map[self.next_pacman_position_location[0]][self.next_pacman_position_location[1]] = "P"

                response = (self.game_map, self.output_map, self.next_pacman_position_location, self.block, self.lose)

            else:
                response = (self.game_map, self.output_map, self.pacman_position, self.block, self.lose)

        return response
