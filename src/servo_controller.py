# SERVO CONTROLLER

# This is a module to control servo motors using the Raspberry Pi.
# This script is used to test the servo motors.
# It moves the servos from 0 to 180 degrees and back to 0 degrees.
# The servos run alternately.

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


if __name__ == "__main__":

    # ServoController(pin, servo_number)
    servo1 = ServoController(11, 1)
    servo2 = ServoController(37, 2)

    try:
        while True:
            servo1.move_servo(0)
            servo1.move_servo(180)
            servo2.move_servo(0)
            servo2.move_servo(180)
    except KeyboardInterrupt:
        del servo1
        del servo2
