#!/usr/bin/python
#
#catch picture 
from picamera import PiCamera
import time

#define date and time
date = time.strftime("%Y-%m-%d")
time = time.strftime("%H:%M")

#Pi_camera
camera = PiCamera() 
camera.resolution = (1920,1080)
camera.rotation = 180
path = "/home/pi/Security_Camera/catch_pic/%s/%s.jpg" % ( date, time )
camera.capture(path)

