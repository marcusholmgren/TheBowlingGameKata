class Game(object):
    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        total_score = 0
        first_in_frame = 0
        for frame in range(10):
            if self.is_strike(first_in_frame):
                total_score += 10 + self.next_two_balls_for_strike(first_in_frame)
                first_in_frame += 1
            elif self.is_spare(first_in_frame):
                total_score += 10 + self.next_ball_for_spare(first_in_frame)
                first_in_frame += 2
            elif first_in_frame + 1 < len(self.rolls):
                total_score += self.two_balls_in_frame(first_in_frame)
                first_in_frame += 2
        return total_score

    def is_spare(self, first_in_frame):
        if first_in_frame + 1 < len(self.rolls):
            return self.two_balls_in_frame(first_in_frame) == 10
        return False

    def two_balls_in_frame(self, first_in_frame):
        return self.rolls[first_in_frame] + self.rolls[first_in_frame + 1]

    def is_strike(self, first_in_frame):
        if first_in_frame + 1 < len(self.rolls):
            return self.rolls[first_in_frame] == 10
        return False

    def next_two_balls_for_strike(self, first_in_frame):
        return self.rolls[first_in_frame + 1] + self.rolls[first_in_frame + 2]

    def next_ball_for_spare(self, first_in_frame):
        return self.rolls[first_in_frame + 2]
