from shapes import Point, Cross

class Game:
    def __init__(self, win, width, height):
        self.turn = True
        self.width = width
        self.height = height
        self.win = win

    def mouse_click(self, event):

        midpoint = Point()

        if event.y <= (self.height / 3):
            midpoint.y = (0 + (self.height / 3)) / 2

            if event.x <= (self.width / 3):
                print("Top Left")
                midpoint.x = 0 + (self.width / 3) / 2

            elif event.x <= (self.width * (2 / 3)):
                print("Top Middle")
                midpoint.x = (((self.width / 3) + (self.width * (2 / 3))) / 2)

            elif event.x <= self.width:
                print("Top Right")
                midpoint.x = (((self.width * (2 / 3)) + self.width) / 2)

        elif event.y <= (self.height * (2 / 3)):
            midpoint.y = ((self.height / 3) + (self.height * (2 / 3))) / 2

            if event.x <= (self.width / 3):
                print("Centre Left")
                midpoint.x = 0 + (self.width / 3) / 2

            elif event.x <= (self.width * (2 / 3)):
                print("Centre Middle")
                midpoint.x = (((self.width / 3) + (self.width * (2 / 3))) / 2)

            elif event.x <= self.width:
                print("Centre Right")
                midpoint.x = (((self.width * (2 / 3)) + self.width) / 2)

        elif event.y <= self.height:
            midpoint.y = ((self.height * (2 / 3)) + self.height) / 2

            if event.x <= (self.width / 3):
                print("Bottom Left")
                midpoint.x = 0 + (self.width / 3) / 2

            elif event.x <= (self.width * (2 / 3)):
                print("Bottom Middle")
                midpoint.x = (((self.width / 3) + (self.width * (2 / 3))) / 2)

            elif event.x <= self.width:
                print("Bottom Right")
                midpoint.x = (((self.width * (2 / 3)) + self.width) / 2)

        if self.turn:
            self.win.draw_cross(Cross(midpoint.x, midpoint.y), "black")
        else:
            self.win.draw_circle(midpoint.x, midpoint.y, "black")

        self.turn = False if self.turn else True
