import unittest
from gameplay import Game

class TestGrid(unittest.TestCase):
    def test_X_win_1(self):
        self.assertEqual(Game.check_X_winner([['X','X','X'], ['-','-','-'], ['-','-','-']]), True)
    def test_X_win_2(self):
        self.assertEqual(Game.check_X_winner([['-', '-', '-'], ['X', 'X', 'X'], ['-', '-', '-']]), True)
    def test_X_win_3(self):
        self.assertEqual(Game.check_X_winner([['-', '-', '-'], ['-', '-', '-'], ['X', 'X', 'X']]), True)
    def test_X_win_4(self):
        self.assertEqual(Game.check_X_winner([['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]), True)
    def test_X_win_5(self):
        self.assertEqual(Game.check_X_winner([['-', 'X', '-'], ['-', 'X', '-'], ['-', 'X', '-']]), True)
    def test_X_win_6(self):
        self.assertEqual(Game.check_X_winner([['X', '-', '-'], ['-', 'X', '-'], ['-', '-', 'X']]), True)
    def test_X_win_7(self):
        self.assertEqual(Game.check_X_winner([['X', '-', '-'], ['-', 'X', '-'], ['-', '-', 'X']]), True)
    def test_X_win_8(self):
        self.assertEqual(Game.check_X_winner([['-', '-', 'X'], ['-', 'X', '-'], ['X', '-', '-']]), True)


    def test_O_win_1(self):
        self.assertEqual(Game.check_O_winner([['O', 'O', 'O'], ['-', '-', '-'], ['-', '-', '-']]), True)
    def test_O_win_2(self):
        self.assertEqual(Game.check_O_winner([['-', '-', '-'], ['O', 'O', 'O'], ['-', '-', '-']]), True)
    def test_O_win_3(self):
        self.assertEqual(Game.check_O_winner([['-', '-', '-'], ['-', '-', '-'], ['O', 'O', 'O']]), True)
    def test_O_win_4(self):
        self.assertEqual(Game.check_O_winner([['O', '-', '-'], ['O', '-', '-'], ['O', '-', '-']]), True)
    def test_O_win_5(self):
        self.assertEqual(Game.check_O_winner([['-', 'O', '-'], ['-', 'O', '-'], ['-', 'O', '-']]), True)
    def test_O_win_6(self):
        self.assertEqual(Game.check_O_winner([['-', '-', 'O'], ['-', '-', 'O'], ['-', '-', 'O']]), True)
    def test_O_win_7(self):
        self.assertEqual(Game.check_O_winner([['O', '-', '-'], ['-', 'O', '-'], ['-', '-', 'O']]), True)
    def test_O_win_8(self):
        self.assertEqual(Game.check_O_winner([['-', '-', 'O'], ['-', 'O', '-'], ['O', '-', '-']]), True)

    def test_No_win_1(self):
        self.assertEqual(Game.check_X_winner([['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]), False)
        self.assertEqual(Game.check_O_winner([['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]), False)

    def test_No_win_2(self):
        self.assertEqual(Game.check_X_winner([['O', 'X', 'O'], ['X', 'X', 'O'], ['X', 'O', 'X']]), False)
        self.assertEqual(Game.check_O_winner([['O', 'X', 'O'], ['X', 'X', 'O'], ['X', 'O', 'X']]), False)

    def test_No_win_3(self):
        self.assertEqual(Game.check_X_winner([['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]), False)
        self.assertEqual(Game.check_O_winner([['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]), False)

    def test_No_win_4(self):
        self.assertEqual(Game.check_X_winner([['O', 'X', 'X'], ['X', 'O', 'O'], ['X', 'O', 'X']]), False)
        self.assertEqual(Game.check_O_winner([['O', 'X', 'X'], ['X', 'O', 'O'], ['X', 'O', 'X']]), False)

    def test_No_win_5(self):
        self.assertEqual(Game.check_X_winner([['X', 'O', 'O'], ['O', 'X', 'X'], ['X', 'X', 'O']]), False)
        self.assertEqual(Game.check_O_winner([['X', 'O', 'O'], ['O', 'X', 'X'], ['X', 'X', 'O']]), False)

    def test_No_win_6(self):
        self.assertEqual(Game.check_X_winner([['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'X']]), False)
        self.assertEqual(Game.check_O_winner([['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'X']]), False)

    def test_No_win_7(self):
        self.assertEqual(Game.check_X_winner([['O', 'X', 'O'], ['O', 'X', 'X'], ['X', 'O', 'X']]), False)
        self.assertEqual(Game.check_O_winner([['O', 'X', 'O'], ['O', 'X', 'X'], ['X', 'O', 'X']]), False)

    def test_win_1(self):
        self.assertEqual(Game.check_X_winner([['O', 'X', 'X'], ['X', 'O', 'X'], ['X', 'O', 'O']]), False)
        self.assertEqual(Game.check_O_winner([['O', 'X', 'X'], ['X', 'O', 'X'], ['X', 'O', 'O']]), True)

    def test_win_2(self):
        self.assertEqual(Game.check_X_winner([['X', 'O', 'O'], ['X', 'X', 'O'], ['O', 'X', 'X']]), True)
        self.assertEqual(Game.check_O_winner([['X', 'O', 'O'], ['X', 'X', 'O'], ['O', 'X', 'X']]), False)

    def test_win_3(self):
        self.assertEqual(Game.check_X_winner([['X', 'X', 'O'], ['O', 'X', 'X'], ['O', 'O', 'X']]), True)
        self.assertEqual(Game.check_O_winner([['X', 'X', 'O'], ['O', 'X', 'X'], ['O', 'O', 'X']]), False)


if __name__ == '__main__':
    unittest.main()
