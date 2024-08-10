from tkinter import *

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__root.title("Tic Tac Toe")
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def wait_for_close(self):
        self.__isRunning = True
        while self.__isRunning:
            self.__root.update_idletasks()
            self.__root.update()

    def close(self):
        self.__isRunning = False
        print("Closing window")
