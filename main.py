from window import Window
from cells import Line, Point, Cell
from maze_class import Maze


def main():

    win = Window(800, 600)

    maze = Maze(10, 5, 5, 5, 50, 50, win)
    
    
    
    #cell1 = Cell(win)
    #cell1.has_right_wall = False
    #cell1.draw(10, 10, 60, 60)

    #cell2 = Cell(win)
    #cell2.has_left_wall=False
    #cell2.draw(70, 50, 120, 100)

    #cell1.draw_move(cell2)



    #cell = Cell(win)
    #cell.has_top_wall = False
    #cell.draw(110, 110, 200, 200)

    #cell = Cell(win)
    #cell.has_bottom_wall = False
    #cell.draw(210, 210, 300, 300)

    #cell = Cell(win)
    #cell.has_left_wall = False
    #cell.draw(310, 310, 400, 400)

    #cell = Cell(win)
    #cell.has_right_wall = False
    #cell.draw(410, 410, 500, 500)

    win.wait_for_close()


main()