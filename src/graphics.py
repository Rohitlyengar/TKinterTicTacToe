from tkinter import *
from gameplay import Game

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game = Game(self, self.width, self.height)
        self.__root = Tk()
        self.__root.minsize(self.width, self.height)
        self.__root.title("Tic Tac Toe")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.bind("<Button-1>", self.game.mouse_click)
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__isRunning = False

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

    def draw_cross(self, cross, fill_color):
        cross.draw(self.__canvas, fill_color)

    def draw_circle(self, x, y, fill_color):
        self.__canvas.create_oval(x - 50, y - 50, x + 50, y + 50, outline=fill_color, width=2)

    def restart_game(self):
        self.__isRunning = False
