import cv2
import time


class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def capture_photo(self, save_path):
        ret, frame = self.camera.read()
        timestamp = time.strftime('%Y%m%d%H%M%S')
        filename = f'image_{timestamp}.jpg'
        cv2.imwrite(save_path + '\\' + filename, frame)
        self.release()

    def release(self):
        if self.camera.isOpened():
            self.camera.release()


def main():
    save_path = r'C:\trayCamera\image'

    camera = Camera()
    camera.capture_photo(save_path)


if __name__ == '__main__':
    main()
