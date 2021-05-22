import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    
def read_message(mqttBroker):
    client = mqtt.Client("ravi")
    client.connect(mqttBroker) 

    client.loop_start()

    client.subscribe("temp")
    client.on_message=on_message 

    time.sleep(1)
    client.loop_stop()
mqttBroker ="broker.emqx.io"
message = 0
while(1):
    read_message(mqttBroker)
    
