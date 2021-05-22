import smtplib
def send_mail(myemail, password, sendto,subject, msg):
    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    headers = ["From: " + myemail, "Subject: " + subject, "To: " + sendto,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    print("Connecting...")
    mailserver.starttls()
    print("Logging In...")
    mailserver.login(myemail , password)
    print("Sending Email...")
    mailserver.sendmail(myemail , sendto, msg)
    print("Email Sent")
    mailserver.quit()

myemail = ''
password= '6'
sendto  = ''
msg = "Hello,\r\nObject Detected!!!"
subject = "Alert from Raspberry Pi"
from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40 , GPIO.IN)
while(1):
	if GPIO.input(40) == 1:
		print("Object Detected!!!")
		send_mail(myemail,password,sendto,subject,msg)
	
