from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

motor_1_pin = [38,40]
forword = [0,1]
backword= [1,0]
stop    = [0,0]

GPIO.setup(motor_1_pin , GPIO.OUT)

GPIO.output(motor_1_pin , forword)
sleep(2)
GPIO.output(motor_1_pin , stop)
sleep(2)
GPIO.output(motor_1_pin , backword)
sleep(2)
GPIO.output(motor_1_pin , stop)
