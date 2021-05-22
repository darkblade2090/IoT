# to write data at thingspeak server
print("To write data at thingspeak server")
import requests
import json
write_url = "http://api.thingspeak.com/update?api_key=6DPPAQDZGFNEAMZP&field1="

data = input("Enter a value : ")

r = requests.post(write_url+data)

print(r.json())
