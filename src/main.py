from image_capture import ImageCapture
from servo_controller import ServoController
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

def func1():
    servo1.move_servo(0)
    servo2.move_servo(180)

def func2():
    servo1.move_servo(180)
    servo2.move_servo(0)

def func3():
    servo1.move_servo(180)
    servo2.move_servo(0)

def func4():
    servo1.move_servo(0)
    servo2.move_servo(180)

if result == "O":
    print(f"[ECOBIN] >> Predicted Label: {result}")


elif result == "R":
    print(f"[ECOBIN] >> Predicted Label: {result}")
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

else:
    print("[ECOBIN] >> Couldnt classify image.")    
    t1 = threading.Thread(target=func3)
    t2 = threading.Thread(target=func4)
    t1.start()
    t2.start()
    t1.join()
    t2.join()