class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y

    def draw(self, canvas, fill_colour="black"):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_colour, width=2)


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall == True:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line)
        if self.has_right_wall == True:
            line = Line(Point(self._x2, self._y2), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_top_wall == True:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line)
        if self.has_bottom_wall == True:
            line = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            colour = "red"
        elif undo:
            colour = "gray"
        from_cell_x = self._x1 + (self._x2 - self._x1) / 2
        from_cell_y = self._y2 + (self._y1 - self._y2) / 2
        to_cell_x = to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2
        to_cell_y = to_cell._y2 + (to_cell._y1 - to_cell._y2) / 2
        line = Line(Point(from_cell_x, from_cell_y), Point(to_cell_x, to_cell_y))
        self._win.draw_line(line, fill_colour=colour)
        
