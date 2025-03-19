from window import Window
from cells import Line, Point, Cell
from maze import Maze


def main():

    win = Window(800, 600)

    maze = Maze(10, 5, 10, 10, 50, 50, win)
    maze.solve()
    
    
    win.wait_for_close()


main()