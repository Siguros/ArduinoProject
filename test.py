#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# for 1st Motor on ENA
ENA = 33
IN1 = 35
IN2 = 37
def main():
    GPIO.setmode(GPIO.BOARD)
    # initialize
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    try:
        while True:
            time.sleep(1)
            # Toggle the output every second
            print("Outputting {} to pin {}".format(GPIO.HIGH, IN1))
            print("Outputting {} to pin {}".format(GPIO.LOW, IN2))
            GPIO.output(IN1, GPIO.HIGH)
            GPIO.output(IN2, GPIO.LOW)
            time.sleep(1)
            print("Outputting {} to pin {}".format(GPIO.HIGH, IN2))
            print("Outputting {} to pin {}".format(GPIO.LOW, IN1))
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)

    finally:
        GPIO.cleanup

if __name__ == '__main__':
    main()
