import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

yellow = 22
button = 12

GPIO.setup(12, RPIO.IN, pull_up_down = GPIO.PUD_UP)

if GPIO.input(button) == False:
	print("Working")

GPIO.cleanup()
