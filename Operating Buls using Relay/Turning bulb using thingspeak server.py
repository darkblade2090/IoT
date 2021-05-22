from time import sleep
from RPi import GPIO
import requests
import json

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

readAPI = "https://api.thingspeak.com/channels/1383639/feeds.json?api_key=Y2LJMJL3TWZO363J&results=2"


while(1):
	
	r = requests.get(readAPI)
	data = r.json()['feeds'][-1]['field1']
	print("Web Response-",data)
	if data == '1':
		print("Bulb is Turned On")
		GPIO.output(40, 1)
	elif data == '0':
		print("Bulb is Turned Off")
		GPIO.output(40,0)
