from RPi import GPIO
from time import sleep
from int2bool import convert
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#=========================Pin Configuration
rs = 21
rw = 20
en = 16
	    #d7 , d6 , d5 , d4 , d3 , d2 , d1 , d0
data_pins = [14 , 15 , 18 , 23 , 24 , 25 ,  8 ,  7]
GPIO.setup([rs , rw , en] , GPIO.OUT)
GPIO.setup(data_pins , GPIO.OUT)

#GPIO initialization
GPIO.output([rs , rw , en] , GPIO.LOW )
GPIO.output(data_pins , GPIO.LOW)

def lcdcmd(cmd): 	#lcd command function
	GPIO.output(rs , 0)	#set command mode
	GPIO.output(rw , 0)	#set write mode
	GPIO.output(data_pins , convert(cmd)) #data_pins = enable command
	GPIO.output(en , 1)	#clock high
	sleep(0.010)
	GPIO.output(en , 0)	#clock low

def lcddat(data):	#lcd data function
	GPIO.output(rs , 1)     #set command mode
	GPIO.output(rw , 0)     #set write mode
	GPIO.output(data_pins , convert(ord(data))) #data_pins = enable command
	GPIO.output(en , 1)     #clock high
	sleep(0.0001)
	GPIO.output(en , 0)     #clock low
def lcd_print(str_):
	for x in str_:
		lcddat(x)

lcdcmd(0x0c)	#lcd enable command
lcdcmd(0x01)	#lcd clear command
lcdcmd(0x38)	#lcd 2 line mode
#==============================================
import json
import requests
read_url = "xyz"   #thingspeak read url
while(1):
	r = requests.get(read_url)
	data1 = r.json()["feeds"][-1]["field1"]
	data2 = r.json()["feeds"][-1]["field2"]
	lcdcmd(0x01)	#clear lcd
	lcdcmd(0x80)	#1st line 1st position
	lcd_print(data1)
	lcdcmd(0xc0)	#2nd line 1st position
	lcd_print(data2)
	sleep(1)
