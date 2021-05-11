from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

r0=2
r1=3
r2=4
r3=9
row_pin=[ro,r1,r2,r3]

c0=17
c1=27
c2=22
c3=10

GPIO.setup(row_pin,GPIO.OUT)
GPIO.setup([c0,c1,c2,c3],GPIO.IN,GPIO.PUD_DOWN)

def row0():
    GPIO.output(row_pin,[0,0,0,1])
    data=[GPIO.input(c0),GPIO.input(c1),GPIO.input(c2),GPIO.input(c3)]

    if data==[0,0,0,1]:
        return('1')
    elif data==[0,0,1,0]:
        return('4')
    elif data==[0,1,0,0]:
        return('7')
    elif data==[1,0,0,0]:
        return('*')
    else:
        return('None')

def row1():
    GPIO.output(row_pin,[0,0,1,0])
    data=[GPIO.input(c0),GPIO.input(c1),GPIO.input(c2),GPIO.input(c3)]

    if data==[0,0,0,1]:
        return('2')
    elif data==[0,0,1,0]:
        return('5')
    elif data==[0,1,0,0]:
        return('8')
    elif data==[1,0,0,0]:
        return('0')
    else:
        return('None')

def row2():
    GPIO.output(row_pin,[0,1,0,0])
    data=[GPIO.input(c0),GPIO.input(c1),GPIO.input(c2),GPIO.input(c3)]

    if data==[0,0,0,1]:
        return('3')
    elif data==[0,0,1,0]:
        return('6')
    elif data==[0,1,0,0]:
        return('9')
    elif data==[1,0,0,0]:
        return('#')
    else:
        return('None')

def row3():
    GPIO.output(row_pin,[0,0,0,1])
    data=[GPIO.input(c0),GPIO.input(c1),GPIO.input(c2),GPIO.input(c3)]

    if data==[1,0,0,3]:
        return('A')
    elif data==[0,0,1,0]:
        return('B')
    elif data==[0,1,0,0]:
        return('C')
    elif data==[1,0,0,0]:
        return('D')
    else:
        return('None')

password=''              #Initializing password as string


#===============================================================================

import requests
import json

read_url=''     #Read API URL from thingspeak server

motor_pin=[19,26]                    #Motor to open/close door of bank locker
GPIO.setup(motor_pin,GPIO.OUT)
GPIO.output(motor_pin,[0,0])         #Initializing motor in stop state

while(1):
    sleep(0.2)
    d1=row0()
    if d1!='None':
        password+=d1
        print(password)

    d2=row1()
    if d2!='None':
        password+=d2
        print(password)

    d3=row2()
    if d3!='None':
        password+=d3
        print(password)

    d4=row3()
    if d4!='None':
        if d3=='D':
            #get true password from thingspeak
            d=requests.get(read_url)
            true_password=d.json()['feeds'][0]['field1']

            if true_password==password:
                print('Welcome')
                GPIO.output(motor_pin,[0,1])    #Motor start if password is right
                sleep(2)
                GPIO.output(motor_pin,[0,0])    #Motor stop

                password=''                     #Reset Password

            else:
                print("Incorrect password")
                password=''                     #Reset password


        else:
            password+=d4
            print(password)
    
