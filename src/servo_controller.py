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

def func1():
    servo1.move_servo(0)
    servo2.move_servo(180)

def func2():
    servo1.move_servo(180)
    servo2.move_servo(0)

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

# Example usage
if __name__ == "__main__":
    servo1 = ServoController(11)
    servo2 = ServoController(37)
    try:
        while True:
            t1.start()
            t2.start()
            t1.join()
            t2.join()
    except KeyboardInterrupt:
        del servo1
        del servo2
