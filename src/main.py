from image_capture import ImageCapture
from servo_controller import ServoController
from classification_2 import ImageClassifier

import os
import time

image_capture = ImageCapture()
path_to_image = image_capture.capture_image()

print(f"[ECOBIN] >> Path: {path_to_image}")

model = ImageClassifier()
model.load_training_data()
result = model.classify_image(path_to_image)

servo1 = ServoController(11)

if result == "O":
    print(f"[ECOBIN] >> Predicted Label: {result}")
    servo1.move_servo(0)
    time.sleep(5)
    servo1.move_servo(180)
    servo1.stop()

elif result == "R":
    print(f"[ECOBIN] >> Predicted Label: {result}")
    servo1.move_servo(180)
    time.sleep(5)
    servo1.move_servo(0) 
    servo1.stop()

else:
    print("[ECOBIN] >> Couldnt classify image.")    
