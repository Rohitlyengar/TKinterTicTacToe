from shapes import *
class Grid:
    def __init__(self, win, width, height):
        self.win = win
        self.width = width
        self.height = height

    def create_vertical_lines(self):

        p1_s = Point(self.width / 3, 0)
        p1_e = Point(self.width / 3, self.height)
        self.win.draw_line(Line(p1_s, p1_e), "black")

        p2_s = Point((self.width * 2) / 3, 0)
        p2_e = Point((self.width * 2) / 3, self.height)
        self.win.draw_line(Line(p2_s, p2_e), "black")

    def create_horizontal_lines(self):
        p1_s = Point(0, self.height / 3)
        p1_e = Point(self.width, self.height / 3)
        self.win.draw_line(Line(p1_s, p1_e), "black")

        p2_s = Point(0, (self.height * 2) / 3)
        p2_e = Point(self.width, (self.height * 2) / 3)
        self.win.draw_line(Line(p2_s, p2_e), "black")

    def create_grid(self):
        self.create_horizontal_lines()
        self.create_vertical_lines()

