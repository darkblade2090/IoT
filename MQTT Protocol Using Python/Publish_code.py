import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

mqttBroker ="broker.emqx.io" 

client = mqtt.Client("abhi")
client.connect(mqttBroker) 
count = 0
while True:
    client.publish("temp", count)
    print("Sent - " + str(count))
    time.sleep(5)
    count+=1
