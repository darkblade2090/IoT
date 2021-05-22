from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

bulb = 40
GPIO.setup(bulb , GPIO.OUT)

while(True):
	a = input("Enter Bulb State(\"ON\" or \"OFF\") : ")
	if a == "ON":
		print("Bulb is ON")
		GPIO.output(bulb , GPIO.HIGH)
	elif a == "OFF":
		print("Nolb is OFF")
		GPIO.output(bulb , GPIO.LOW)
	else:
		print("Enter correct choice!!!")
