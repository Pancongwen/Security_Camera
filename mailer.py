#!/user/bin/python
#
#send email by using smtplib

import os
import smtplib
from email.mime.text import MIMEText
import time
from email.mime.application import MIMEApplication  
from email.MIMEBase import MIMEBase
from email import Encoders 
from email.MIMEMultipart import MIMEMultipart


#set date
date =  time.strftime("%Y-%m-%d")

#set email From_addr and To_addr
From   = "1227398402@qq.com"
Passwd = "wqqitjcleljfhajj"
To     = "1227398402@qq.com"

#email part
msg = MIMEMultipart()
msg.attach( MIMEText(
    "This is a email from you security camera."
    "Here are some pictures or videos catched in %s." % date) )
msg["Subject"] = "Security Camera(%s)" % date
msg["From"]    = From
msg["To"]      = To

#attach part
path = "/home/pi/Security_Camera/catch_pic/%s" % date 
for filename in os.listdir(path):
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(os.path.join(path, filename),"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)
    msg.attach(part) 

#test part
try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(From, Passwd)
    s.sendmail(From, To, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e 
