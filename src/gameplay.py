from shapes import *

class Game:
    def __init__(self, win, width, height):
        self.turn = True
        self.width = width
        self.height = height
        self.win = win

    def mouse_click(self, event):

        if event.y <= (self.height / 3):
            if event.x <= (self.width / 3):
                print("Top Left")
            elif event.x <= (self.width * (2 / 3)):
                print("Top Middle")
            elif event.x <= self.width:
                print("Top Right")

        elif event.y <= (self.height * (2 / 3)):
            if event.x <= (self.width / 3):
                print("Centre Left")
            elif event.x <= (self.width * (2 / 3)):
                print("Centre Middle")
            elif event.x <= self.width:
                print("Centre Right")

        elif event.y <= self.height:
            if event.x <= (self.width / 3):
                print("Bottom Left")
            elif event.x <= (self.width * (2 / 3)):
                print("Bottom Middle")
            elif event.x <= self.width:
                print("Bottom Right")

        cross = Cross(event.x, event.y)
        self.win.draw_cross(cross, "black")
