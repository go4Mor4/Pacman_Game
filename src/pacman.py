GOOD_BLOCKS = [".", " "]
BAD_BLOCKS = ["="]


class Pacman:
    def __init__(self, game_map, pacman_position, move, block=0):
        self.game_map = game_map
        self.pacman_position = pacman_position
        self.move = move
        self.block = block

    @property
    def current_move_status(self):
        pacman_column = [l[self.pacman_position[1]] for l in self.game_map]
        pacman_line = self.game_map[self.pacman_position[0]]

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
        next_left_postion = [self.pacman_position[0], self.pacman_position[1] - 1]
        next_right_postion = [self.pacman_position[0], self.pacman_position[1] + 1]

        factory_position = {
            "up": next_up_position,
            "down": next_down_position,
            "left": next_left_postion,
            "right": next_right_postion
        }

        return factory_position.get(self.move)

    def _validate_move(self):
        if self.current_move_status in BAD_BLOCKS:
            self.block = 2
            return False

        elif self.current_move_status in GOOD_BLOCKS:
            return True

    def move_pacman(self):
        if self._validate_move():
            self.game_map[self.pacman_position[0]][self.pacman_position[1]] = " "
            self.game_map[self.next_pacman_position_location[0]][self.next_pacman_position_location[1]] = "PM"

            response = (self.game_map, self.next_pacman_position_location)

        return response
