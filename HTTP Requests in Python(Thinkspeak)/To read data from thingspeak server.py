# To read data from thingspeak server
print("To Read data from thingspeak server")
import requests
import json

read_url = "https://api.thingspeak.com/channels/1377717/feeds.json?results=2"

r = requests.get(read_url)
data = r.json()["feeds"][-1]["field1"]
print(data)
