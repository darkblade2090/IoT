#===========================MQTT Setup
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
#=====================================

from tkinter import *
from tkinter import font
box = Tk()
box.geometry("600x600")

def b1_fun():
    print("Bulb is Turned ON")
    topic = "bulb"
    message = "ON"
    client.publish(topic , message)
    
def b2_fun():
    print("Bulb is Turned OFF")
    topic = "bulb"
    message = "OFF"
    client.publish(topic , message)


l = Label(box,
          text = "HOME AUTOMATION",
          font = 30)
b1 = Button(box,
           text = "ON",
           font = 20,
           command = b1_fun(),
            activeforeground = "pink",
            activebackground = "green",
            bg = "red",
            height = 10,
            width = 10,
            padx = -10,
            pady = 1)
b2 = Button(box,
           text = "OFF",
           font = 20,
           command = b2_fun(),
            activeforeground = "pink",
            activebackground = "green",
            bg = "blue",
            height = 10,
            width = 10)

l.pack()
b1.pack()
b2.pack()
box.mainloop()
