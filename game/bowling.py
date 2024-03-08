# game\bowling.py

class BowlingFrame:
    """Keeping the record of each bowling frame."""

    def __init__(self, max_roll=2):
        """Construct a frame."""
        self.pins = [0] * max_roll
        self.max_roll = max_roll
        self.next_roll = 0

    def roll(self, pins: int):
        """Roll the ball to knock down pins."""
        if self.next_roll < self.max_roll:
            self.pins[self.next_roll] = pins
            self.next_roll += 1

    def score(self):
        """Calculate the score of each frame."""
        return sum(self.pins)

    def is_spare(self):
        """Check if the frame is a spare."""
        return self.next_roll == self.max_roll and sum(self.pins) == 10

    def is_strike(self):
        """Check if the frame is a strike."""
        return self.pins[0] == 10


class BowlingFrame10(BowlingFrame):
    """Special handling for the 10th bowling frame."""

    def __init__(self):
        super().__init__(3)


class BowlingGame:
    """The Bowling Game."""

    def __init__(self):
        """Construct a BowlingGame object."""
        self.frames = [BowlingFrame() for _ in range(9)] + [BowlingFrame10()]
        self.cur_frame = 0

    def roll(self, num_of_pins: int):
        """Roll a bowling ball and knock down pins."""
        frame = self.frames[self.cur_frame]
        frame.roll(num_of_pins)
        
        if self.cur_frame < 9:
            if frame.is_strike() or frame.next_roll == frame.max_roll:
                self.cur_frame += 1
        else:
            if (frame.is_strike() or frame.is_spare()) and frame.next_roll == 3:
                self.cur_frame += 1
            elif not frame.is_strike() and not frame.is_spare() and frame.next_roll == 2:
                self.cur_frame += 1

    def score(self):
        """Calculate the current score of the game."""
        total = 0
        for i, frame in enumerate(self.frames):
            total += frame.score()
            if frame.is_spare() and i < 9:
                total += self.frames[i + 1].pins[0]
            elif frame.is_strike() and i < 9:
                next_frame = self.frames[i + 1]
                total += next_frame.score()
                if next_frame.is_strike() and i < 8:
                    total += self.frames[i + 2].pins[0]
        return total


# You can now use the updated classes in your game logic and testing.
