import time
from cells import Line, Cell
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_rows):
            cell_list = []
            for j in range(self._num_cols):
                cell_list.append(Cell(self._win))
            self._cells.append(cell_list)
        self._break_walls_r(0,0)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        x1 = self._x1 + (self._cell_size_x * i)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (self._cell_size_y * j)
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell._visited = True

        to_visit = []
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            
        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < len(self._cells) and 0 <= new_j < len(self._cells[0]):
                if not self._cells[new_i][new_j]._visited:
                    to_visit.append((new_i, new_j, di, dj))
            
        if not to_visit:
            return
                
        new_i, new_j, di, dj = random.choice(to_visit)    

        if dj == -1: #Up
            cell.has_top_wall = False
            self._cells[new_i][new_j].has_bottom_wall = False
        elif di == 1: #Right
            cell.has_right_wall = False
            self._cells[new_i][new_j].has_left_wall = False
        elif dj == 1: #Down
            cell.has_bottom_wall = False
            self._cells[new_i][new_j].has_top_wall = False
        elif di == -1: #Left
            cell.has_left_wall = False
            self._cells[new_i][new_j].has_right_wall = False

        self._break_walls_r(new_i, new_j)



    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)