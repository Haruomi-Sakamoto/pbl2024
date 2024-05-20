from ipwebcam import VideoStreamCapture
from enhancer import EnhancedContrast
from tiledetector import TileDetector
from tilecluclator import TileCluclator
from tilediscarder import TileDiscarder

#video_capture = VideoStreamCapture()
detector = TileDetector()
enhancer = EnhancedContrast()
cluclator = TileCluclator()
discarder = TileDiscarder(0)#Mode 0:Random, 1:Kokushi, 2:Sevens, 3:Nomal

myturn = False
victory = False

if __name__ == "__main__":
    while not victory: 
        #myturnかチェック
        myturn = True
        if myturn:
            #video_capture.capture_frames()
            #video_capture.release()

            enhanced_image = enhancer.enhance()

            hand_result = detector.detect_tiles()
            #detector.display_first_images()
            print(hand_result)
            victory = cluclator.check_victory(hand_result)
            if victory:
                #ロンする
                pass
            else:
                discard = discarder.discard_tile(hand_result)
                print(discard)
                #捨て牌
                myturn = False