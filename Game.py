"""
This module contains the logic for a bowling game.
"""

class Game(object):
    """
    Manages the state and scoring of a bowling game.
    """
    def __init__(self):
        """
        Initializes a new game.

        Sets up an empty list to store rolls and initializes the current roll counter.
        """
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins (int): The number of pins knocked down in the roll.
        """
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """
        Calculates the total score for the game.

        Returns:
            int: The total score.
        """
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
        """
        Checks if a frame is a spare.

        Args:
            first_in_frame (int): The index of the first roll in the frame.

        Returns:
            bool: True if the frame is a spare, False otherwise.
        """
        if first_in_frame + 1 < len(self.rolls):
            return self.two_balls_in_frame(first_in_frame) == 10
        return False

    def two_balls_in_frame(self, first_in_frame):
        """
        Calculates the sum of pins knocked down in a frame (two rolls).

        Args:
            first_in_frame (int): The index of the first roll in the frame.

        Returns:
            int: The sum of pins for the two rolls in the frame.
        """
        return self.rolls[first_in_frame] + self.rolls[first_in_frame + 1]

    def is_strike(self, first_in_frame):
        """
        Checks if a roll is a strike.

        Args:
            first_in_frame (int): The index of the roll to check.

        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        # A strike is when 10 pins are knocked down in the first roll of a frame.
        # The check for available rolls for bonus calculation should be handled by bonus calculation methods.
        if first_in_frame < len(self.rolls): # Ensure the roll itself exists
            return self.rolls[first_in_frame] == 10
        return False

    def next_two_balls_for_strike(self, first_in_frame):
        """
        Gets the scores of the next two balls after a strike.

        Args:
            first_in_frame (int): The index of the strike roll.

        Returns:
            int: The sum of pins for the next two balls.
        """
        return self.rolls[first_in_frame + 1] + self.rolls[first_in_frame + 2]

    def next_ball_for_spare(self, first_in_frame):
        """
        Gets the score of the next ball after a spare.

        Args:
            first_in_frame (int): The index of the first roll in the spare frame.

        Returns:
            int: The score of the next ball.
        """
        return self.rolls[first_in_frame + 2]
