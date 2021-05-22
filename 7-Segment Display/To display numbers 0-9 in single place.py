#======================================================Import libraries
from RPi import GPIO
from time import sleep
#======================================================GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#======================================================Sensor Configuration
sensor_pin = 8
GPIO.setup(sensor_pin , GPIO.IN)
count = 0
#======================================================SSD Pin Configuration
ssd_pins = [31 , 33 , 35 , 37 , 40 , 38 , 36]
GPIO.setup(ssd_pins , GPIO.OUT)
#======================================================SSD digit code for Common cathode
#         g,f,d,e,c,b,a
digit = [[0,1,1,1,1,1,1], #0
         [0,0,0,0,1,1,0], #1
         [1,0,1,1,0,1,1], #2
         [1,0,0,1,1,1,1], #3
         [1,1,0,0,1,1,0], #4
         [1,1,0,1,1,0,1], #5
         [1,1,1,1,1,0,1], #6
         [0,0,0,0,1,1,1], #7
         [1,1,1,1,1,1,1], #8
         [1,1,0,1,1,1,1]] #9
#======================================================Main Code
while(True):
	if GPIO.input(sensor_pin)==1 :
		count=count+1
		print(count)
		while(GPIO.input(sensor_pin)==1):
			continue
	GPIO.output(ssd_pins , digit[count%10])


