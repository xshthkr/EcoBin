import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins
pin1 = 11  # Replace with the GPIO pin connected to terminal 1 of the motor
pin2 = 13  # Replace with the GPIO pin connected to terminal 2 of the motor

# Set up GPIO pins
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

# Function to spin the motor clockwise
def clockwise():
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)

# Function to spin the motor counterclockwise
def counterclockwise():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)

# Function to stop the motor
def stop():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)

if __name__ == "__main__":
    try:
        while True:
            # Spin clockwise for 3 seconds
                clockwise()
            time.sleep(10)
            # Spin counterclockwise for 3 seconds
            counterclockwise()
            time.sleep(10)
            # Stop for 1 second
            stop()
            time.sleep(5)

    except KeyboardInterrupt:
        print("Stopping motor...")
        stop()
        GPIO.cleanup()
