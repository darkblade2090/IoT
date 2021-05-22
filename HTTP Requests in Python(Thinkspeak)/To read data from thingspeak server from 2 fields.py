# To read data from thingspeak server
print("To Read data from thingspeak server")
import requests
import json

read_url = "https://api.thingspeak.com/channels/1377717/feeds.json?results=2"

while(1):
    r = requests.get(read_url)
    data1 = r.json()["feeds"][-1]["field1"]
    data2 = r.json()["feeds"][-1]["field2"]
    print("Field1 Data : ",data1)
    print("Field2 Data : ",data2)
    print("---------------------")
