import paho.mqtt.client as mqtt
from time import sleep
from RPi import GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)

def on_message(client, userdata, msg):
	print('received :',str(msg.payload.decode('utf-8')))
	data = msg.payload.decode("utf-8")
	print(data)
	if data == 'ON':
		GPIO.output(40, 1)	#turn on the bulb
	elif data == 'OFF':
		GPIO.output(40, 0)	#turn off the bulb
	
client = mqtt.Client("Client 2")
mqtt_broker = "localhost"
topic = "bulb"
while(1):
    #to connect with mqtt broker
    client.connect(mqtt_broker)
    client.loop_start()
    client.subscribe(topic)
    client.on_message=on_message
    sleep(1)
    client.loop_stop()

