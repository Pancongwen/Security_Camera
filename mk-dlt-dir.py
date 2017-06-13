#!/usr/bin/python
 
import datetime 
import shutil
import os

#define
today = datetime.date.today()
week_ago = today - datetime.timedelta(days=7)

#create a directory named by date
os.mkdir("/home/pi/Security_Camera/catch_pic/%s" % today);

#delete the directory a week ago
shutil.rmtree("/home/pi/Security_Camera/catch_pic/%s" % week_ago)




