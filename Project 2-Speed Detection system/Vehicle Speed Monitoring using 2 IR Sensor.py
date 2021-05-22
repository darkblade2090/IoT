from RPi import GPIO
from time import sleep

ir1 = 40
ir2 = 38

GPIO.setmode(GPIO.BOARD) #10cm/1ms
GPIO.setup(ir1, GPIO.IN)
GPIO.setup(ir2, GPIO.IN)
Time = 0
distance = 13.0
fb_count= 0
bk_count= 0

#=====================requests congig.
import requests
import json

write_url = 'https://api.thingspeak.com/update?api_key=H35U76IS5ZOB11CU'

def write_data(speed,counts,dir_):
    main_url = write_url + '&field1=' + str(speed) + '&field2=' + str(counts) + '&field3=' + dir_
    print("Uploading Data...")
    r = requests.post(main_url)
    if r.json() ==0:
        while(r.json()==0):
            print('Retrying...')
            r = requests.post(main_url)
            sleep(1)
    print('data uploaded successfully!')
    

#=====================================
while(1):
    if GPIO.input(ir1) == 1:
        Time = 0
        fb_count +=1 #count detected objects
        while(GPIO.input(ir2)==0):
            Time=Time+1
            sleep(0.001)
            continue # wait till object reaches at ir2
        Time = Time/1000
        speed = distance/Time
        print("direction : To North")
        print("speed = ",int(speed),'cm/sec')
        print("Total objects detected : ",fb_count)
        write_data(speed , fb_count , 'to north')
        print("==============================")
        while(GPIO.input(ir2)==1):
            continue
        
    elif GPIO.input(ir2) == 1:
        Time = 0
        bk_count +=1 #count detected objects
        while(GPIO.input(ir1)==0):
            Time=Time+1
            sleep(0.001)
            continue # wait till object reaches at ir2
        Time = Time/1000
        speed = distance/Time
        print("direction : To South")
        print("speed = ",int(speed),'cm/sec')
        print("Total objects detected : ",bk_count)
        write_data(speed , bk_count , 'to south')
        print("==============================")
        while(GPIO.input(ir1)==1):
            continue
        
