import numpy as np
from ui import UI

class Board:

    def __init__(self, ui: UI):
        self.grid = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
        self.ui = ui

    def eval(self, turn, depth, max_depth):
        player = turn % 2 + 1

        if self.check_victory():
            if player == 1:
                return -1
            else:
                return 1
        elif turn > max_depth:
            return 0
        elif depth >= max_depth:
            return 0
        else:
            return None
            
        
    def test_eval(self, turn, depth, max_depth):
        player = turn % 2 + 1 

        if self.check_victory():
            if player == 1:
                return -10000
            else:
                return 10000

        if depth >= max_depth:
            return self.calculate_heuristic(player)
        
        return None
        
    def calculate_heuristic(self, player):
        reward = 0
        addreward = 0

        # Horizontal alignment check
        for line in range(6):
            for horizontal_shift in range(4):
                if self.grid[horizontal_shift][line] == self.grid[horizontal_shift + 1][line] != 0:
                    addreward += 1
                    if self.grid[horizontal_shift + 1][line] == self.grid[horizontal_shift + 2][line] != 0:
                        addreward += 10
                        if self.grid[horizontal_shift + 2][line] == self.grid[horizontal_shift + 3][line] != 0:
                            addreward += 1000
        reward += addreward
        addreward = 0
        # Vertical alignment check
        for column in range(7):
            for vertical_shift in range(3):
                if self.grid[column][vertical_shift] == self.grid[column][vertical_shift + 1] != 0:
                    addreward += 1
                    if self.grid[column][vertical_shift + 1] == self.grid[column][vertical_shift + 2] != 0:
                        addreward += 10
                        if self.grid[column][vertical_shift + 2] == self.grid[column][vertical_shift + 3] != 0:
                            addreward += 1000

        reward += addreward
        addreward = 0
        # Diagonal alignment check
        for horizontal_shift in range(4):
            for vertical_shift in range(3):
                if self.grid[horizontal_shift][vertical_shift] == self.grid[horizontal_shift + 1][vertical_shift + 1] != 0:
                    addreward += 1
                    if self.grid[horizontal_shift + 1][vertical_shift + 1] == self.grid[horizontal_shift + 2][vertical_shift + 2] != 0:
                        addreward += 10
                        if self.grid[horizontal_shift + 2][vertical_shift + 2] == self.grid[horizontal_shift + 3][vertical_shift + 3] != 0:
                            addreward += 1000
                elif self.grid[horizontal_shift][5 - vertical_shift] == self.grid[horizontal_shift + 1][4 - vertical_shift] != 0:
                    addreward += 1
                    if self.grid[horizontal_shift + 1][4 - vertical_shift] == self.grid[horizontal_shift + 2][3 - vertical_shift] != 0:
                        addreward += 10
                        if self.grid[horizontal_shift + 2][3 - vertical_shift] == self.grid[horizontal_shift + 3][2 - vertical_shift] != 0:
                            addreward += 1000
        reward += addreward

        #bonus center
        center_column = self.grid[3]
        center_count = np.count_nonzero(center_column == player)
        reward += center_count * 3

        if player == 1:
            return -reward
        else:
            return reward

    def copy(self):
        new_board = Board(self.ui)
        new_board.grid = np.array(self.grid, copy=True)
        return new_board

    def reinit(self):
        self.grid.fill(0)
        for i in range(7):
            for j in range(6):
                self.ui.canvas.itemconfig(self.ui.disks[i][j], fill=self.ui.disk_color[0])

    def get_possible_moves(self):
        possible_moves = list()
        if self.grid[3][5] == 0:
            possible_moves.append(3)
        for shift_from_center in range(1, 4):
            if self.grid[3 + shift_from_center][5] == 0:
                possible_moves.append(3 + shift_from_center)
            if self.grid[3 - shift_from_center][5] == 0:
                possible_moves.append(3 - shift_from_center)
        return possible_moves

    def add_disk(self, column, player, update_display=True):
        for j in range(6):
            if self.grid[column][j] == 0:
                break
        self.grid[column][j] = player
        if update_display:
            self.ui.canvas.itemconfig(self.ui.disks[column][j], fill=self.ui.disk_color[player])

    def column_filled(self, column):
        return self.grid[column][5] != 0

    def check_victory(self):
        # Horizontal alignment check
        for line in range(6):
            for horizontal_shift in range(4):
                if self.grid[horizontal_shift][line] == self.grid[horizontal_shift + 1][line] == self.grid[horizontal_shift + 2][line] == self.grid[horizontal_shift + 3][line] != 0:
                    return True
        # Vertical alignment check
        for column in range(7):
            for vertical_shift in range(3):
                if self.grid[column][vertical_shift] == self.grid[column][vertical_shift + 1] == \
                        self.grid[column][vertical_shift + 2] == self.grid[column][vertical_shift + 3] != 0:
                    return True
        # Diagonal alignment check
        for horizontal_shift in range(4):
            for vertical_shift in range(3):
                if self.grid[horizontal_shift][vertical_shift] == self.grid[horizontal_shift + 1][vertical_shift + 1] ==\
                        self.grid[horizontal_shift + 2][vertical_shift + 2] == self.grid[horizontal_shift + 3][vertical_shift + 3] != 0:
                    return True
                elif self.grid[horizontal_shift][5 - vertical_shift] == self.grid[horizontal_shift + 1][4 - vertical_shift] ==\
                        self.grid[horizontal_shift + 2][3 - vertical_shift] == self.grid[horizontal_shift + 3][2 - vertical_shift] != 0:
                    return True
        return False
