import cv2
import numpy as np
import os

from jongsetting import detect_const
from jongsetting import cam_const

class TileDetector:
    def __init__(self):
        self.hand = []

    def detect_tiles(self):
        self.hand.clear()
        output_folder = 'oimg'

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        img = cv2.imread('simg/enhanced_img.jpg')
        output_img = img.copy()

        prev_detected_points = []

        for TILE in range(len(detect_const.filepath)):
            tilenum = len(self.hand)
            if tilenum < detect_const.handlen:
                template_folder = detect_const.filepath[TILE]
                piname = str(template_folder[5:9])
                detect_scale = False
                for i in range(12):
                    if not detect_scale:
                        template_path = os.path.join(template_folder, f'{piname}_{12-i}.jpg')
                        if not os.path.exists(template_path):
                            continue

                        template = cv2.imread(template_path)
                        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

                        threshold = detect_const.threshold[TILE]

                        loc = np.where(res >= threshold)

                        for pt in zip(*loc[::-1]):
                            skip_detection = False
                            for prev_pt in prev_detected_points:
                                if np.linalg.norm(np.array(pt) - np.array(prev_pt)) < detect_const.skippx:  
                                    skip_detection = True
                                    break

                            if not skip_detection:
                                color = detect_const.rectgbr[TILE]
                                cv2.rectangle(output_img, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), color, 5)
                                cv2.putText(output_img, f'{piname[0:4]}', (pt[0], pt[1] + 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 4)
                                cv2.putText(output_img, str(pt), (pt[0] - 10, pt[1] - 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 4)

                                self.hand.append((TILE, pt[0]))
                                prev_detected_points.append(pt)

                                print(f'Detected frame coordinates for {piname}_{i}: {pt}')
                            detect_scale = True

        output_path = os.path.join(output_folder, 'output_image_combined.jpg')

        cv2.imwrite(output_path, output_img)
        resized_img = cv2.resize(output_img,
                                       (cam_const.cam_ratio[0]*cam_const.cam_ratio[3], cam_const.cam_ratio[1]*cam_const.cam_ratio[3]))
        #cv2.imshow('detected_result', resized_img)

        self.hand.sort(key=lambda x: x[1], reverse=False)
        tiles = [row[0] for row in self.hand]
        
        return tiles

    def display_first_images(self):
        first_images = []
        for idx, (TILE, _) in enumerate(self.hand):
            piname = str(detect_const.filepath[TILE][5:9])
            first_image_path = os.path.join(detect_const.filepath[TILE], f'{piname}_0.jpg')
            first_image = cv2.imread(first_image_path)
            first_images.append(first_image)
        
        combined_image = np.concatenate(first_images, axis=1)
        resized_combined_image = cv2.resize(combined_image, (detect_const.hand_windowsize, 
                                            int(combined_image.shape[0] * (detect_const.hand_windowsize / combined_image.shape[1]))))
        cv2.imshow('Combined First Images', resized_combined_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = TileDetector()
    hand_result = detector.detect_tiles()
    detector.display_first_images()
    print(hand_result)
