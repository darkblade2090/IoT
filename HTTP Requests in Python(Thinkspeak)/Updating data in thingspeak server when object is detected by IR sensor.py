from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensor_pin = 37
GPIO.setup(sensor_pin , GPIO.IN)
count = 0

import requests
import json
write_api = "https://api.thingspeak.com/update?api_key=6DPPAQDZGFNEAMZP&field1="
count = 0
while(1):
	sensor_data = GPIO.input(sensor_pin)
	if sensor_data == 1:
		count+=1
		print("Object Detected")
		while(sensor_data == 1):
			sensor_data = GPIO.input(sensor_pin)
			continue
		r = requests.post(write_api+str(count))
		print("Uploading Data")
		print("No Object")
		print("Total Counts : ",count)
        if sensor_data == 1:
                count+=1
                print("Object Detected")
                while(sensor_data == 1):
                        sensor_data = GPIO.input(sensor_pin)
                        continue
                print("No Object Detected")
                r = requests.post(write_api+str(count))

