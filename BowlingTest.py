import unittest
from Game import Game


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.sut = Game()

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.sut.score())

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.sut.score())

    def test_one_spare(self):
        self.roll_spare()
        self.sut.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(16, self.sut.score())

    def test_one_strike(self):
        self.roll_strike()
        self.sut.roll(3)
        self.sut.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.sut.score())

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(300, self.sut.score())

    def roll_strike(self):
        self.sut.roll(10)

    def roll_spare(self):
        self.sut.roll(5)
        self.sut.roll(5)

    def roll_many(self, n, pins):
        for i in range(n):
            self.sut.roll(pins)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
