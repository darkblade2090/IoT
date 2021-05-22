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
    mailserver.sendmail(myemail , sendto, headers+"\r\n\r\n" , msg)
    print("Email Sent")
    mailserver.quit()


myemail = input("Enter your email : ")
password= input("ENter your password")
sendto  = input("Send To : ")
msg = input("Enter a message : ")
subject = "Header Section"
send_mail(myemail,password,sendto,subject,msg)
