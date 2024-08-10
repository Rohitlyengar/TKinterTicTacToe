import sys
from graphics import Window
from grid import Grid

def main():
    width = int(sys.argv[1])
    height = int(sys.argv[2])

    win = Window(width, height)

    grid = Grid(win, width, height)
    grid.create_grid()

    win.wait_for_close()

if __name__ == '__main__':
    main()
