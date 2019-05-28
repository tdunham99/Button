import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
yellow = 22
button = 12

# Setup the pin that the LED is connected to
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

buttonPress = True
LEDstate = False


print("Press the button homie!")
buttonPress = GPIO.input(button)
if buttonPress == False and LEDstate == False:
	GPIO.output(yellow, True)
	print("LED ON")
	LEDstate = True
	sleep(2)
elif buttonPress == True and LEDstate == True:
	GPIO.output(yellow, False)
	print("LED OFF")
	LEDstate = False
	sleep(2)
GPIO.cleanup()                              