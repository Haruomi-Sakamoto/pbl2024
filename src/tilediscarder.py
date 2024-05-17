from randomdiscarder import RandomDiscarder
from kokushidiscarder import KokushiDiscarder

class TileDiscarder:
    def __init__(self, mode):
        self.mode = mode
        self.random = RandomDiscarder()
        self.kokushi = KokushiDiscarder()

    def discard_tile(self,hand):
        if self.mode == 0:
            discard = self.random.discard(hand)
        elif self.mode == 1:
            discard = self.kokushi.discard(hand)
            pass
        elif self.mode == 2:
            discard = 29
            pass
        elif self.mode == 3:
            discard = 11
            pass
        elif self.mode == 4:
            discard = 11
            pass
        
        index = self.find_value(hand, discard)

        return index  

    def find_value(self, matrix, target):
        for i in range(len(matrix)):
            if matrix[i] == target:
                return i
        return -1

if __name__ == "__main__":
    hand = [9,9,1,19,21,29,31,32,33,34,35,1,35,36]
    discarder = TileDiscarder(1)
    hand_result = discarder.discard_tile(hand)
    print(hand_result)