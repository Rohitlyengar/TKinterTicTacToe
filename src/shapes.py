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

class Cross:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas, fill_color="black"):
        top_l = Point(self.x - 50, self.y - 50)
        top_r = Point(self.x + 50, self.y - 50)
        bot_l = Point(self.x - 50, self.y + 50)
        bot_r = Point(self.x + 50, self.y + 50)

        Line(top_l, bot_r).draw(canvas, fill_color)
        Line(top_r, bot_l).draw(canvas, fill_color)

