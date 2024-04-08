from image_capture import ImageCapture
from servo_controller_threaded import ServoController
from classification_2 import ImageClassifier

import os
import time
import threading

image_capture = ImageCapture()
path_to_image = image_capture.capture_image()

print(f"[ECOBIN] >> Path: {path_to_image}")

train_folder = "/home/rpi/Downloads/DATASET_2/TRAIN"
model = ImageClassifier(train_folder)
model.load_training_data()
result = model.classify_image(path_to_image)

servo1 = ServoController(11)

def servo1_spin_clockwise():
    servo1 = ServoController(11)
    servo1.move_servo(0)
    servo1.move_servo(180)
    del servo1

def servo1_spin_counterclockwise():
    servo1 = ServoController(11)
    servo1.move_servo(180)
    servo1.move_servo(0)
    del servo1

def servo2_spin_clockwise():
    servo2 = ServoController(37)
    servo2.move_servo(180)
    servo2.move_servo(0)
    del servo2

def servo2_spin_counterclockwise():
    servo2 = ServoController(37)
    servo2.move_servo(0)
    servo2.move_servo(180)
    del servo2


if result == "O":
    print(f"[ECOBIN] >> Predicted Label: {result}")


elif result == "R":
    print(f"[ECOBIN] >> Predicted Label: {result}")
    t1 = threading.Thread(target=servo1_spin_clockwise)
    t2 = threading.Thread(target=servo2_spin_counterclockwise)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

else:
    print("[ECOBIN] >> Couldnt classify image.")    
    t1 = threading.Thread(target=servo1_spin_counterclockwise)
    t2 = threading.Thread(target=servo2_spin_clockwise)
    t1.start()
    t2.start()
    t1.join()
    t2.join()