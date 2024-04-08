from time import sleep
import threading

import RPi.GPIO as GPIO

class ServoController:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        self.p = GPIO.PWM(pin, 50)
        self.p.start(0)
        print("[ACTUATOR] >> Servo ready.")

    def __del__(self):
        print("[ACTUATOR] >> Stopping.")
        self.p.stop()
        GPIO.cleanup()

    def angle_to_duty_cycle(self, angle):
        duty_cycle = (angle / 18) + 2
        return duty_cycle

    def move_servo(self, angle):
        print(f"[ACTUATOR] >> Moving to {angle} degrees")
        duty_cycle = self.angle_to_duty_cycle(angle)
        self.p.ChangeDutyCycle(duty_cycle)
        sleep(1)


# PAIR 1
def servo1_spin_clockwise():
    servo1 = ServoController(11)
    servo1.move_servo(0)
    servo1.move_servo(90)
    del servo1
def servo2_spin_counterclockwise():
    servo2 = ServoController(37)
    servo2.move_servo(90)
    servo2.move_servo(0)
    del servo2

# PAIR 2
def servo1_spin_counterclockwise():
    servo1 = ServoController(11)
    servo1.move_servo(90)
    servo1.move_servo(0)
    del servo1
def servo2_spin_clockwise():
    servo2 = ServoController(37)
    servo2.move_servo(0)
    servo2.move_servo(90)
    del servo2


t1 = threading.Thread(target=servo1_spin_clockwise)
t2 = threading.Thread(target=servo2_spin_counterclockwise)

# Example usage
if __name__ == "__main__":

    t1.start()
    t2.start()
    t1.join()
    t2.join()
