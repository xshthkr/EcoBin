# THREADED SERVO CONTROLLER

# This is a module to control servo motors using the Raspberry Pi in parallel
# This script is used to test the servo motors running in parallel.
# It moves the servos from 0 to 180 degrees and back to 0 degrees.
# The servos run parallelly.

import threading
from time import sleep
import RPi.GPIO as GPIO


class ServoController:


    def __init__(self, pin, servo_number):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        self.p = GPIO.PWM(pin, 50)
        self.p.start(0)
        self.number = servo_number
        print(f"[ACTUATOR {self.number}] >> Servo ready.")


    def __del__(self):
        print(f"[ACTUATOR {self.number}] >> Stopping.")
        self.p.stop()
        GPIO.cleanup()


    def angle_to_duty_cycle(self, angle):
        duty_cycle = (angle / 18) + 2
        return duty_cycle


    def move_servo(self, angle):
        print(f"[ACTUATOR {self.number}] >> Moving to {angle} degrees")
        duty_cycle = self.angle_to_duty_cycle(angle)
        self.p.ChangeDutyCycle(duty_cycle)
        sleep(1)


# ServoController(pin, servo_number)
servo1 = ServoController(11, 1)
servo2 = ServoController(37, 2)


# PAIR 1
def servo1_spin_clockwise():
    servo1.move_servo(45)
    servo1.move_servo(0)
def servo2_spin_counterclockwise():
    servo2.move_servo(45)
    servo2.move_servo(0)

# PAIR 2
def servo1_spin_counterclockwise():
    servo1.move_servo(0)
    servo1.move_servo(45)
def servo2_spin_clockwise():
    servo2.move_servo(0)
    servo2.move_servo(45)


# Example usage
if __name__ == "__main__":

    # PAIR 1
    t1 = threading.Thread(target=servo1_spin_clockwise)
    t2 = threading.Thread(target=servo2_spin_counterclockwise)

    # # PAIR 2
    # t3 = threading.Thread(target=servo1_spin_counterclockwise)
    # t4 = threading.Thread(target=servo2_spin_clockwise)

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    del servo1
    del servo2

    # sleep(2)

    # t3.start()
    # t4.start()
    # t3.join()
    # t4.join()
