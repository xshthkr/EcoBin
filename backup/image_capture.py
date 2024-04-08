import cv2

def capture_image():
    # Open the first available webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Read a frame from the webcam
    ret, frame = cap.read()

    # If frame is read correctly, save it
    if ret:
        cv2.imwrite("/home/rpi/Downloads/DATASET_2/TEST/test.jpg", frame)
        print("Image captured successfully")

    # Release the webcam
    cap.release()

if __name__ == "__main_":

    # Call the function to capture the image
    capture_image()
