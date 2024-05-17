import random

class RandomDiscarder:
    def __init__(self):
        pass

    def discard(self, hand):
        tile = random.choice(hand)
        return tile