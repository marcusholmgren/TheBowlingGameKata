import unittest
from Game import Game


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.sut = Game()

    def test_can_roll(self):
        self.sut.roll(0)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
