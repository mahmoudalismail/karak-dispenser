#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def forward():
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(18, GPIO.LOW)
	time.sleep(0.02)

def backward():
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.010)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.010)

def center():
	GPIO.output(18, GPIO.HIGH)
        time.sleep(0.0015)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.0185)

def fullPWM(pwm):
	pwm.start(100)

def forwardPWM(pwm):
	pwm.start(5)

def backwardPWM(pwm):
	pwm.start(10)

def runServo(total_time):
	start_time = time.time()
	while True:
		backward()
		if time.time() - start_time > total_time:
			break

if __name__ == "__main__":
	total_time = 5
	if len(sys.argv) > 1:
		total_time = int(sys.argv[1])
	print "Running for %d seconds..."%(total_time)
	pwm = GPIO.PWM(18,50)
	start = time.time()
	while True:
		backward()

		if time.time() - start > total_time:
			break
