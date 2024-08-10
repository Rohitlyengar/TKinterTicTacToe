from tkinter import *

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.minsize(self.width, self.height)
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__root.title("Tic Tac Toe")
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()

    def close(self):
        self.__isRunning = False
        print("Closing window")

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def create_vertical_lines(self):

        p1_s = Point(self.width / 3, 0)
        p1_e = Point(self.width / 3, self.height)
        self.draw_line(Line(p1_s, p1_e), "black")

        p2_s = Point((self.width * 2) / 3, 0)
        p2_e = Point((self.width * 2) / 3, self.height)
        self.draw_line(Line(p2_s, p2_e), "black")

    def create_horizontal_lines(self):
        p1_s = Point(0, self.height / 3)
        p1_e = Point(self.width, self.height / 3)
        self.draw_line(Line(p1_s, p1_e), "black")

        p2_s = Point(0, (self.height * 2) / 3)
        p2_e = Point(self.width, (self.height * 2) / 3)
        self.draw_line(Line(p2_s, p2_e), "black")

    def create_grid(self):
        self.create_horizontal_lines()
        self.create_vertical_lines()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.getX(), self.p1.getY(), self.p2.getX(), self.p2.getY(), fill=fill_color, width=2)
