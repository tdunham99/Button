import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

yellow = 22
button = 6
button2 = 5
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.setup(button2, GPIO.IN)

while True:
	if GPIO.input(button) == False or GPIO.input(button2) == False:
		GPIO.output(yellow, True)
	elif GPIO.input(button) == True or GPIO.input(button2) == True:
		GPIO.output(yellow, False)

GPIO.cleanup()

