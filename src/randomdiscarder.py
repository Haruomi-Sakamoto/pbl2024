import random

class RandomDiscarder:
    def __init__(self):
        pass

    def discard(self, hand):
        discard = random.choice(hand)
        return discard