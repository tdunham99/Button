import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

yellow = 22
button = 12

while wait_for_press():
	if button.is_pressed:
		print("On")
		yellow.on()
	else:
		print("Off")
		yellow.off()

GPIO.cleanup()
