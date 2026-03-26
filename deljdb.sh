#!/bin/bash


LOG_DIR="/home/pi/Desktop/Journal"

find "$LOG_DIR" -type f -mtime +30 -exec rm -f {} \;   #-mmin +1





