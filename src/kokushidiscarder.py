import random
from jongsetting import tile_const

class KokushiDiscarder:
    def __init__(self):
        self.kokushi_tiles = tile_const.yaochu

    def discard(self, hand):
        tiles_to_discard = []

        tile_count = {}
        kokushi_twice_count = 0
        kokushi_twice_tiles = set()

        for tile in hand:
            if tile in tile_count:
                tile_count[tile] += 1
            else:
                tile_count[tile] = 1
        
        for tile, count in tile_count.items():
            if tile in self.kokushi_tiles:
                if count == 2:
                    kokushi_twice_count += 1
                    kokushi_twice_tiles.add(tile)
        
        if kokushi_twice_count >= 2:
            for tile, count in tile_count.items():
                if tile in self.kokushi_tiles:
                    if count >= 3:
                        tiles_to_discard.extend([tile] * (count - 2))
            
            if tiles_to_discard:
                return random.choice(tiles_to_discard)
            else:
                return random.choice(hand)
        else:
            # If there's only one or fewer types of Kokushi tiles appearing twice,
            # we need to decide which one to discard
            return random.choice(list(kokushi_twice_tiles))


