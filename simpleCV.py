#!/usr/bin/python 
from SimpleCV import *
import time
import os
import sys

cam = Camera()
display = Display((800,600))
threshold = 5.0

#define time
date = time.strftime("%Y-%m-%d")
current_time = time.strftime("%H:%M")
path = "/home/pi/Security_Camera/catch_pic/%s" % date

os.chdir(path)

while True:
    # Get Image from camera,
    img1 = cam.getImage().toGray()
    time.sleep(0.5)
    img2 = cam.getImage().toGray() 
    #compare two image
    diff = (img1 - img2).binarize(50).invert() 
    
    matrix = diff.getNumpy() 
    mean = matrix.mean()
    
    #find and highliht the objects
    blobs = diff.findBlobs()
    
    #check whether picture has changed,if change ,save image
    if mean >= threshold:
        i = 0
        while os.path.exists("%s-%s.jpg" % (current_time,i)):
            i += 1
        img2.save("%s-%s.jpg" % (current_time,i))
        print("Image Saved")
