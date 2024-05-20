import random
from jongsetting import tile_const

class SevensDiscarder:
    def __init__(self):
        pass

    def discard(self, hand):
        # タイルの出現回数を数えるための辞書
        double_counts = {}

        # 手牌の中のタイルの数を数える
        for tile in hand:
            if tile in double_counts:
                double_counts[tile] += 1
            else:
                double_counts[tile] = 1

        # ペアでないタイルを tiles_discard_list に追加
        tiles_discard_list = [tile for tile, count in double_counts.items() if count % 2 != 0]

        if tiles_discard_list:
            discard = random.choice(tiles_discard_list)
        else:
            triple_counts = {tile: hand.count(tile) for tile in hand}
            triplets = [tile for tile, count in triple_counts.items() if count >= 3]

            if triplets:
                discard = random.choice(triplets)
            else:
                discard = random.choice(hand)

        return discard
