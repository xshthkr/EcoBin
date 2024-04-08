# IMAGE CAPTURE

# This is a module to capture images using the webcam of the Raspberry Pi.
# This script is used to capture an image from the webcam and display it.
# It saves the image in the specified path and displays it using matplotlib.

import cv2
import matplotlib.pyplot as plt


class ImageCapture:


    def __init__(self):
        # Open the first available webcam
        self.cap = cv2.VideoCapture(0)
        print("[WEBCAM] >> Ready")


    def capture_image(self):
        # Check if the webcam is opened correctly
        if not self.cap.isOpened():
            print("[WEBCAM] >> Error: Could not open webcam")
            return
        # Read a frame from the webcam
        print("[WEBCAM] >> Reading a frame from the webcam...")
        ret, frame = self.cap.read()
        # If frame is read correctly, save it
        if ret:
            path = "/home/rpi/Downloads/DATASET_2/TEST/test.jpg"
            cv2.imwrite(path, frame)
            print("[WEBCAM] >> Image captured successfully")
            print("[WEBCAM] >> Path:", path)

            plt.imshow(plt.imread(path))
            plt.title("Captured Image")
            plt.axis("off")
            plt.show()
            
            return path


    def release(self):
        # Release the webcam
        self.cap.release()


if __name__ == "__main__":
    # Create an instance of ImageCapture
    image_capture = ImageCapture()
    # Call the function to capture the image
    image_capture.capture_image()
    # Release the webcam
    image_capture.release()
