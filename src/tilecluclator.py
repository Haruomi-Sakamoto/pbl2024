from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld
from mahjong.constants import EAST, SOUTH, WEST, NORTH

class TileCluclator:
    def __init__(self):
        self.calcuator = HandCalculator()
        self.game = False

    def convert_to_numerical(self,tiles):
        if tiles:
            man = ''.join(str(int(tile) - 0) for tile in tiles if 1 <= int(tile) <= 9)
            pin = ''.join(str(int(tile) - 10) for tile in tiles if 11 <= int(tile) <= 19)
            sou = ''.join(str(int(tile) - 20) for tile in tiles if 21 <= int(tile) <= 29)
            honors = ''.join(str(int(tile) - 30) for tile in tiles if 31 <= int(tile) <= 36)
        
            return man, pin, sou, honors

    def calc_yaku(self, man_, pin_, sou_, honors_, win_):
        tiles = TilesConverter.string_to_136_array(man=str(man_), pin=str(pin_), sou=str(sou_), honors=str(honors_))

        if win_ < 10:
            win_tile = TilesConverter.string_to_136_array(man=str(win_))[0]
        elif 10 <= win_ < 20:
            win_tile = TilesConverter.string_to_136_array(pin=str((win_ - 10)))[0]
        elif 20 <= win_ < 30:
            win_tile = TilesConverter.string_to_136_array(sou=str((win_ - 20)))[0]
        elif win_ >= 30:
            win_tile = TilesConverter.string_to_136_array(honors=str((win_ - 30)))[0]

        melds = None

        dora_indicators = None
        """dora_indicators = [
            TilesConverter.string_to_136_array(pin='7')[0],
            TilesConverter.string_to_136_array(sou='9')[0],
        ]"""

        config = HandConfig(is_tsumo=True, options=OptionalRules(has_aka_dora=False))

        result = self.calcuator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
        self.game = self.check_hand_result(result)
        return self.game

    def check_hand_result(self, hand_result):
        if hand_result.han != None:
            print(hand_result.han, hand_result.fu)
            print(hand_result.cost['main'], hand_result.cost['additional'])
            print(hand_result.yaku)
            for fu_item in hand_result.fu_details:
                print(fu_item)
            print('')
            return True
        else:
            #print("役無")
            return False
        
    def check_victory(self, tiles):
        win = tiles[13]
        man, pin, sou, honors = self.convert_to_numerical(tiles)

        vic = self.calc_yaku(man, pin, sou, honors, win)

        return vic

if __name__ == "__main__":
    pass

"""
akadora=0
win: man0~9=0~9, pin0~9=10~19, sou0~9=20~29, wind=31~34, honors=35~37
"""