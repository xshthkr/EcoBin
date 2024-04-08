import time

import RPi.GPIO as GPIO

class Controller:
    def __init__(self):
        # Set GPIO mode
        GPIO.setmode(GPIO.BOARD)

        # Define GPIO pins
        self.pin1 = 11  # Replace with the GPIO pin connected to terminal 1 of the motor
        self.pin2 = 13  # Replace with the GPIO pin connected to terminal 2 of the motor

        # Set up GPIO pins
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)

        print("[ACTUATOR] >> Motor ready.")

    # Function to spin the motor clockwise
    def clockwise(self):
        print("[CONTROLLER] >> Rotating clockwise...")
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)

    # Function to spin the motor counterclockwise
    def counterclockwise(self):
        print("[CONTROLLER] >> Rotating counterclockwise...")
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)

    # Function to stop the motor
    def stop(self):
        print("[CONTROLLER] >> Stopping.")
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)

if __name__ == "__main__":
    try:
        controller = Controller()
        while True:
            # Spin clockwise for 3 seconds
            controller.clockwise()
            time.sleep(10)
            # Spin counterclockwise for 3 seconds
            controller.counterclockwise()
            time.sleep(10)
            # Stop for 1 second
            controller.stop()
            time.sleep(5)

    except KeyboardInterrupt:
        print("[ACTUATOR] >> Stopping motor...")
        controller.stop()
        GPIO.cleanup()
