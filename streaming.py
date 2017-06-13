#!/usr/bin/python 
from SimpleCV import *

cam = Camera()
display = Display((800,600))

#port 8000
streaming = JpegStreamer("0.0.0.0:8000")

while True:
    img = cam.getImage()
    img.save(streaming)
