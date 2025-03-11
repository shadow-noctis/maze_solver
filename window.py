from tkinter import Tk, BOTH, Canvas
from cells import Line

class Window:
    def __init__(self, width, height):
        root = Tk()
        self.__root = root
        root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_colour="black"):
        line.draw(self.__canvas, fill_colour)

        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.__running = False