import random
from jongsetting import tile_const

class RandomDiscarder:
    def __init__(self, wind):
        self.wind = tile_const.wind
        self.yakupai = tile_const.sangen
        for i in range (len(wind)):
            self.yakupai.append(wind[i])
            self.wind.remove(wind[i])
        pass

    def discard(self, hand):
        print(self.wind)
        print(self.yakupai)

wind = [31,33]
r = RandomDiscarder(wind)
r.discard(2)
