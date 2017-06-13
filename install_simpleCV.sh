#!/bin/bash
#

cd Security_Camera/

#install simpleCV
sudo apt install -y ipython python-opencv python-scipy python-numpy python-setuptoolsls 
sudo pip install pyparaing svgwrite

#install drivers
wget http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc
sudo apt-key add ./lrkey.asc
echo “deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ wheezy main” >> /etc/apt/source.list
sudo apt update
sudo apt install -y uv4l uv4l-raspicam uv4l-raspicam-extras uv4l-server
sudo service uv4l_raspicam start

