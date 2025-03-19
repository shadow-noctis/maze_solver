import time
from cells import Line, Cell
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_rows):
            cell_list = []
            for j in range(self._num_cols):
                cell_list.append(Cell(self._win))
            self._cells.append(cell_list)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if i == 0 and j == 0:
            self._cells[i][j].has_top_wall = False
        elif i == len(self._cells) -1 and j == len(self._cells[i]) -1:
            self._cells[i][j].has_bottom_wall = False
        cell = self._cells[i][j]
        x1 = self._x1 + (self._cell_size_x * i)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (self._cell_size_y * j)
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell._visited = True

        while True:
            to_visit = []
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < len(self._cells) and 0 <= new_j < len(self._cells[0]):
                    if not self._cells[new_i][new_j]._visited:
                        to_visit.append((new_i, new_j, di, dj))
                
            if not to_visit:
                self._draw_cell(i,j)
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

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j]._visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True
        if i == len(self._cells) -1 and j == len(self._cells[i]) -1:
            return True
        #Up
        if j - 1 >= 0:
            if self._cells[i][j -1].has_bottom_wall == False and self._cells[i][j -1]._visited == False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        #Right
        if i + 1 <= len(self._cells) -1:
            if self._cells[i +1][j].has_left_wall == False and self._cells[i+1][j]._visited == False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                if self._solve_r(i +1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        #Bottom
        if j + 1 <= len(self._cells[i]) -1:
            if self._cells[i][j + 1].has_top_wall == False and self._cells[i][j+1]._visited == False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                if self._solve_r(i, j +1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        #Left
        if i - 1 >= 0:
            if self._cells[i - 1][j].has_right_wall == False and self._cells[i - 1][j]._visited == False:
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                if self._solve_r(i -1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        return False

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)