#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

data = {}
#with open('pass.json') as f:
 # data = json.load(f)
# create message object instance

msg = MIMEMultipart()

 
message = "Hola soy Oziel, de clase de los Sabados a las 12pm."

 
msg['From'] = 'oziel.mendozacr@uanl.edu.mx'
receipents = ["ozielmdza@outlook.com"]
msg['To'] = ", ".join(receipents)
msg['Subject'] = 'Salu2!'

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()

server.login('oziel.mendozacr@uanl.edu.mx','Fisicomatematico12')

server.sendmail(msg['From'], receipents, msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))
