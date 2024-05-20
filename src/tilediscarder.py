from randomdiscarder import RandomDiscarder
from kokushidiscarder import KokushiDiscarder
from sevensdiscarder import SevensDiscarder

class TileDiscarder:
    def __init__(self, mode):
        self.mode = mode
        self.random = RandomDiscarder()
        self.kokushi = KokushiDiscarder()
        self.sevens = SevensDiscarder()

    def discard_tile(self,hand):
        if self.mode == 0:
            discard = self.random.discard(hand)
        elif self.mode == 1:
            discard = self.kokushi.discard(hand)
        elif self.mode == 2:
            discard = self.sevens.discard(hand)
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
    hand = [1,9,11,19,21,29,31,32,33,34,5,1,37,36]
    discarder = TileDiscarder(1)
    hand_result = discarder.discard_tile(hand)
    print(hand_result)