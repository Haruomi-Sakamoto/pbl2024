import cv2
import os

from jongsetting import cam_const

class EnhancedContrast:
    def __init__(self):
        pass
        
    def enhance(self):
        original_image = cv2.imread('simg/saved_img.jpg', cv2.IMREAD_GRAYSCALE)
        median_filtered_image = cv2.medianBlur(original_image, 5)
        
        clahe = cv2.createCLAHE(clipLimit=cam_const.cliplimit, tileGridSize=(8,8))
        enhanced_image = clahe.apply(median_filtered_image)
        
        output_path = os.path.join('simg', 'enhanced_img.jpg')
        cv2.imwrite(output_path, enhanced_image)
        print("Enhanced image saved successfully.")

if __name__ == "__main__":
    contrast_enhancer = EnhancedContrast()
    enhanced_image = contrast_enhancer.enhance()
