import cv2
import os
import time

from jongsetting import cam_const

class VideoStreamCapture:
    def __init__(self):
        self.url = cam_const.url
        self.cap = cv2.VideoCapture(cam_const.url)

    def capture_frames(self):
        cv2.namedWindow('Smartphone Webcam', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Smartphone Webcam',
                         cam_const.cam_ratio[0]*cam_const.cam_ratio[2], cam_const.cam_ratio[1]*cam_const.cam_ratio[2])

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to capture frame from IP camera")
                print("Wating connection",end="")
                while True:
                    print(".",end="")
                    time.sleep(1)
                    skey = cv2.waitKey(1)
                    if skey == ord('b'):
                        break
                break

            resized_frame = cv2.resize(frame,
                                       (cam_const.cam_ratio[0]*cam_const.cam_ratio[2], cam_const.cam_ratio[1]*cam_const.cam_ratio[2]))
            """
            grid_color = cam_const.gridcolor
            grid_thickness = 1
            for i in range(0, resized_frame.shape[1], 75): 
                cv2.line(resized_frame, (i, 0), (i, resized_frame.shape[0]), grid_color, grid_thickness)
            for j in range(0, resized_frame.shape[0], 100):
                cv2.line(resized_frame, (0, j), (resized_frame.shape[1], j), grid_color, grid_thickness)"""

            cv2.imshow('Smartphone Webcam', resized_frame)

            key = cv2.waitKey(1)
            if key == ord('s'):
                filename = f'saved_img.jpg'
                output_folder = 'simg'

                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                output_path = os.path.join(output_folder, filename)
                output_img = cv2.resize(frame,
                                       (cam_const.cam_ratio[0]*cam_const.cam_ratio[2], cam_const.cam_ratio[1]*cam_const.cam_ratio[2]))
                cv2.imwrite(output_path, frame)
                cv2.imshow('Saved_img', output_img)
                
                print(f"Frame saved as {filename}")

            elif key == ord('q'):
                break

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    video_capture = VideoStreamCapture()
    video_capture.capture_frames()
    video_capture.release()
