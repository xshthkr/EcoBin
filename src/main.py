# MAIN

# This is the main script that integrates the image capture, classification, and actuation modules.
# It captures an image using the webcam, classifies the image using the KNN algorithm, and actuates the servo motors based on the classification result.
# The script is designed to run on the Raspberry Pi.

import os
import time
import threading

from image_capture import ImageCapture
from classification import ImageClassifier
from servo_controller_threaded import ServoController


image_capture = ImageCapture()
path_to_image = image_capture.capture_image()
image_capture.release()

train_folder = "/home/rpi/Downloads/DATASET_2/TRAIN"
model = ImageClassifier(train_folder)
model.load_training_data()
result = model.classify_image(path_to_image)

servo1 = ServoController(11)
servo2 = ServoController(37)


# PAIR 1
def servo1_spin_clockwise():
    servo1.move_servo(0)
    servo1.move_servo(90)


def servo2_spin_counterclockwise():
    servo2.move_servo(90)
    servo2.move_servo(0)

# PAIR 2
def servo1_spin_counterclockwise():
    servo1.move_servo(90)
    servo1.move_servo(0)


def servo2_spin_clockwise():
    servo2.move_servo(0)
    servo2.move_servo(90)


if result == "O":

    print(f"[ECOBIN] >> Predicted Label: {result}")

    # PAIR 1
    t1 = threading.Thread(target=servo1_spin_clockwise)
    t2 = threading.Thread(target=servo2_spin_counterclockwise)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

elif result == "R":

    print(f"[ECOBIN] >> Predicted Label: {result}")
    
    # PAIR 2
    t1 = threading.Thread(target=servo1_spin_counterclockwise)
    t2 = threading.Thread(target=servo2_spin_clockwise)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

else:
    
    print("[ECOBIN] >> Couldnt classify image.")

del servo1
del servo2
