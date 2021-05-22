import paho.mqtt.client as mqtt
from time import sleep

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("UTF-8")))

client = mqtt.Client("Client 2")
mqtt_broker = "192.168.0.116"
topic = "test"
while(1):
    #to connect with mqtt broker
    print('Connecting...')
    client.connect(mqtt_broker)
    print('Connected')
    client.loop_start()
    client.subscribe(topic)
    client.on_message=on_message
    sleep(1)
    client.loop_stop()
