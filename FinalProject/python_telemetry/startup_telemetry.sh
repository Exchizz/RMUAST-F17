#!/bin/bash

sudo chmod 666 /dev/ttyUSB0
stty -F /dev/ttyUSB0 57600
while true; do echo "$GTPOS,12931,Drone,1,2,3" > /dev/ttyUSB0; sleep 0.1; done;
