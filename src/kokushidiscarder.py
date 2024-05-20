import random
from jongsetting import tile_const

class KokushiDiscarder:
    def __init__(self):
        self.kokushi_tiles = tile_const.yaochu

    def discard(self, hand):
        tiles_discard_list = []

        for tile in hand:
            if tile not in self.kokushi_tiles:
                tiles_discard_list.append(tile)

        if tiles_discard_list:
            discard = random.choice(tiles_discard_list)
        else:
            tile_counts = {tile: hand.count(tile) for tile in hand}
            triplets = [tile for tile, count in tile_counts.items() if count >= 3]

            if triplets:
                discard = random.choice(triplets)
            else:
                pairs = [tile for tile, count in tile_counts.items() if count == 2]

                if pairs:
                    discard = random.choice(pairs)
                else:
                    discard = random.choice(hand)

        return discard