import sys
from graphics import *

def main():
    width = int(sys.argv[1])
    height = int(sys.argv[2])

    win = Window(width, height)
    win.create_grid()

    win.wait_for_close()

if __name__ == '__main__':
    main()
