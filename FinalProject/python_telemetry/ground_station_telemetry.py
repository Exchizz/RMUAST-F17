# ------------------- Telemetry link --------------------
# Read data from socket, send data over serial device.

# Defines
GAMESON_PORT = 8888
BAUD_RATE  = 57600
PORT_NAME  = "/dev/ttyUSB0"

# Import
import sys
import socket
import struct
import serial
from time import sleep
from crc16 import crc16

# Connect to socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1337))
except Exception as error:
    print error
    print 'Failed to create socket'
    sys.exit()

# Create serial object
telemetry = serial.Serial(PORT_NAME, BAUD_RATE)

# Create CRC object
crc = crc16()

while True:
    data = s.recv(1)
    print data

	#asbytes = struct.pack('ddff', lat,lon,height,dop)
	#msg = asbytes;

	#result = crc.calc(msg)
	#crc_out = chr(result >> 8) + chr(result & 0x00ff)

	#out = msg + crc_out
	#print type(out)
	#s.sendto(out, ("Drone1.local", 8888))
	#print "out: ", out
