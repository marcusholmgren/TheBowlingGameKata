class Game(object):
    def __init__(self):
        self.current_score = 0

    def roll(self, pins):
        self.current_score = self.current_score + pins

    def score(self):
        return self.current_score
