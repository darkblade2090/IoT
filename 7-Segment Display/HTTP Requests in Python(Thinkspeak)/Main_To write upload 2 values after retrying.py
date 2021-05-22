from time import sleep
import requests
import json
def write_request(d1 , d2):
    i = 0
    while(i<3):
        url = "https://api.thingspeak.com/update?api_key="
        #thingspeak write API key (To be changed)
        wr_api = "6DPPAQDZGFNEAMZP"
        #=========================
        data1 = "&field1=" + d1
        data2 = "&field2=" + d2
        main_url = url + wr_api + data1 + data2
        #=========================
        r = requests.post(main_url)
        res = r.json()
        print(type(res))
        if res == 0:
            if i==2:
                print("Server Error")
                break
            print("Retrying...",i)
            i+=1
            sleep(5)
            continue
        elif res>0:
            print("Upload Done!!!")
            break 
        
while(1):
    a = input("Enter 1st value : ")
    b = input("Enter 2nd value : ")

    write_request(a,b)
