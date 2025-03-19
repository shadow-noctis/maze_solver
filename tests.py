import unittest
import random

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_cells(self):
        num_rows = 100
        num_cols = 80
        m2 = Maze(0,0, num_rows, num_cols, 5, 5)
        self.assertEqual(len(m2._cells), num_rows)
        self.assertEqual(len(m2._cells[0]), num_cols)

    def test_maze_cell(self):
        num_rows = 1
        num_cols = 1
        m3 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m3._cells), num_cols)
        self.assertEqual(len(m3._cells[0]), num_rows)


    def test_visisted_func(self):
        num_rows = 15
        num_cols = 15
        m4 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(m4._cells[2][5]._visited, False)

    def test_visited_reset(self):
        num_rows = 10
        num_cols = 16
        m5 = Maze(0,0, num_rows, num_cols, 5, 5)
        i = random.randrange(len(m5._cells))
        j = random.randrange(len(m5._cells[i]))
        self.assertEqual(m5._cells[i][j]._visited, False)


if __name__ == "__main__":
    unittest.main()