from time import sleep

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

def servo1_spin():
    servo1 = ServoController(11)
    try:
        while True:
            servo1.move_servo(0)
            servo1.move_servo(180)
    except KeyboardInterrupt:
        del servo1

def servo2_spin():
    servo2 = ServoController(37)
    try:
        while True:
            servo2.move_servo(0)
            servo2.move_servo(180)
    except KeyboardInterrupt:
        del servo2

t1 = threading.Thread(target=servo1_spin)
t2 = threading.Thread(target=servo2_spin)

# Example usage
if __name__ == "__main__":
    servo1 = ServoController(11)
    servo2 = ServoController(37)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
