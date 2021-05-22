#To publish data
from time import sleep
import paho.mqtt.client as mqtt

client = mqtt.Client("Client 1")
mqtt_broker = "192.168.0.116"
#broker.emqx.io
#to connect with broker
count = 0
print("Connecting...")
client.connect(mqtt_broker)
print("Connected")
while(1):
    topic = "test"
    message = input("Enter data : ")
    client.publish(topic , message)
    print("Data published-"+message)
