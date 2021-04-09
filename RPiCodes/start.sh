#!/bin/sh
sudo uv4l -nopreview --auto-video_nr --driver raspicam --encoding mjpeg --width 640 --height 480 --framerate 10 --rotation 180 --server-option '--port=9090' --server-option '--max-queued-connections=30' --server-option '--max-streams=25' --server-option '--max-threads=100' --server-option '--admin-password=password'
python3 /home/pi/Monitor.py & ssh -A -R 10090:localhost:9090 root@ip "ssh -g -N -L 9090:localhost:10090 localhost" && fg
