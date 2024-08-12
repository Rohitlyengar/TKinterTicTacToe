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
            if event.x <= (self.width / 3):
                print("Top Left")
                midpoint = Point((self.width / 3) / 2, (self.height / 3)/2)
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

        if self.turn:
            self.win.draw_cross(Cross(midpoint.x, midpoint.y), "black")
        else:
            self.win.draw_circle(midpoint.x, midpoint.y, "black")

        self.turn = False if self.turn else True
