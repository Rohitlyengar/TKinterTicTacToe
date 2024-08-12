from shapes import Point, Cross

class Game:
    def __init__(self, win, width, height):
        self.turn = 'X'
        self.width = width
        self.height = height
        self.win = win

        self.grid = [['-', '-', '-'],
                    ['-', '-', '-'],
                    ['-', '-', '-']]

    @staticmethod
    def check_X_winner(grid):
        if grid[0][0] == 'X' and grid[0][1] == 'X' and grid[0][2] == 'X':
            return True
        elif grid[1][0] == 'X' and grid[1][1] == 'X' and grid[1][2] == 'X':
            return True
        elif grid[2][0] == 'X' and grid[2][1] == 'X' and grid[2][2] == 'X':
            return True
        elif grid[0][0] == 'X' and grid[1][0] == 'X' and grid[2][0] == 'X':
            return True
        elif grid[0][1] == 'X' and grid[1][1] == 'X' and grid[2][1] == 'X':
            return True
        elif grid[0][2] == 'X' and grid[1][2] == 'X' and grid[2][2] == 'X':
            return True
        elif grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X':
            return True
        elif grid[0][2] == 'X' and grid[1][1] == 'X' and grid[2][0] == 'X':
            return True
        return False

    @staticmethod
    def check_O_winner(grid):
        if grid[0][0] == 'O' and grid[0][1] == 'O' and grid[0][2] == 'O':
            return True
        elif grid[1][0] == 'O' and grid[1][1] == 'O' and grid[1][2] == 'O':
            return True
        elif grid[2][0] == 'O' and grid[2][1] == 'O' and grid[2][2] == 'O':
            return True
        elif grid[0][0] == 'O' and grid[1][0] == 'O' and grid[2][0] == 'O':
            return True
        elif grid[0][1] == 'O' and grid[1][1] == 'O' and grid[2][1] == 'O':
            return True
        elif grid[0][2] == 'O' and grid[1][2] == 'O' and grid[2][2] == 'O':
            return True
        elif grid[0][0] == 'O' and grid[1][1] == 'O' and grid[2][2] == 'O':
            return True
        elif grid[0][2] == 'O' and grid[1][1] == 'O' and grid[2][0] == 'O':
            return True
        return False

    def mouse_click(self, event):

        midpoint = Point()

        if event.y <= (self.height / 3):
            midpoint.y = (0 + (self.height / 3)) / 2

            if event.x <= (self.width / 3):
                if self.grid[0][0] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Top Left")
                midpoint.x = 0 + (self.width / 3) / 2
                self.grid[0][0] = self.turn

            elif event.x <= (self.width * (2 / 3)):
                if self.grid[0][1] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Top Middle")
                midpoint.x = (((self.width / 3) + (self.width * (2 / 3))) / 2)
                self.grid[0][1] = self.turn

            elif event.x <= self.width:
                if self.grid[0][2] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Top Right")
                midpoint.x = (((self.width * (2 / 3)) + self.width) / 2)
                self.grid[0][2] = self.turn

        elif event.y <= (self.height * (2 / 3)):
            midpoint.y = ((self.height / 3) + (self.height * (2 / 3))) / 2

            if event.x <= (self.width / 3):
                if self.grid[1][0] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Centre Left")
                midpoint.x = 0 + (self.width / 3) / 2
                self.grid[1][0] = self.turn

            elif event.x <= (self.width * (2 / 3)):
                if self.grid[1][1] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Centre Middle")
                midpoint.x = (((self.width / 3) + (self.width * (2 / 3))) / 2)
                self.grid[1][1] = self.turn

            elif event.x <= self.width:
                if self.grid[1][2] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Centre Right")
                midpoint.x = (((self.width * (2 / 3)) + self.width) / 2)
                self.grid[1][2] = self.turn

        elif event.y <= self.height:
            midpoint.y = ((self.height * (2 / 3)) + self.height) / 2

            if event.x <= (self.width / 3):
                if self.grid[2][0] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Bottom Left")
                midpoint.x = 0 + (self.width / 3) / 2
                self.grid[2][0] = self.turn

            elif event.x <= (self.width * (2 / 3)):
                if self.grid[2][1] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Bottom Middle")
                midpoint.x = (((self.width / 3) + (self.width * (2 / 3))) / 2)
                self.grid[2][1] = self.turn

            elif event.x <= self.width:
                if self.grid[2][2] != '-':
                    print("Cannot Place!\nTry Again!")
                    return
                print("Bottom Right")
                midpoint.x = (((self.width * (2 / 3)) + self.width) / 2)
                self.grid[2][2] = self.turn


        if self.turn == 'X':
            self.win.draw_cross(Cross(midpoint.x, midpoint.y), "black")
        else:
            self.win.draw_circle(midpoint.x, midpoint.y, "black")

        if self.check_X_winner(self.grid):
            print("X Wins!")
            return
        if self.check_O_winner(self.grid):
            print("O Wins!")
            return

        if self.turn == 'X':
            print("\nO's Turn!")
        else:
            print("\nX's Turn!")

        self.turn = 'O' if self.turn == 'X' else 'X'