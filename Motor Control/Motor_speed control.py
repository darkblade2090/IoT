from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

motor_pin = [38 , 40]
GPIO.setup(motor_pin , GPIO.OUT)

def motor_control(dir , d_cycle , t):	#(direction , duty_cycle , time)
	direction = [not(dir) , dir]	#direction Control
	total_delay = 0.010
	on_delay = (d_cycle*total_delay)/100
	off_delay= total_delay - on_delay 
	#print(on_delay,off_delay)
	for x in range(t*100):
                #Total time = 10ms (0.010 sec)
                GPIO.output(motor_pin , direction)
                sleep(on_delay)            #on time delay
                GPIO.output(motor_pin , [0,0])
                sleep(off_delay)            #off time delay
                # % d_cycle = (on_delay/total_delay)*100
	GPIO.output(motor_pin , [0,0])	#stop motor
while(True):
	motor_control(0 , 70 , 5)
	sleep(2)
	motor_control(1 , 70 , 5)
	sleep(2)
