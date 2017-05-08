# ------------------- Telemetry link --------------------
# Read data from socket, send data over serial device.

# Defines
GAMESON_PORT = 8888
BAUD_RATE  = 57600
PORT_NAME  = "/dev/ttyUSB0"
MSGLEN = 4
DATALEN = 2

# Import
import sys
import socket
import struct
import serial
from time import sleep
from crc16 import crc16
from slip_protocol import slip_protocol

# Connect to socket
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect(('127.0.0.1', 1337))
except Exception as error:
    print error
    print 'Failed to create socket'
    sys.exit()

# Create serial object
#telemetry = serial.Serial(PORT_NAME, BAUD_RATE)

# Packing variables
packet_format = 'dd'
packet_size = struct.calcsize(packet_format)

# Create CRC and slip
crc = crc16()
slip = slip_protocol()

loop = 1
while loop:

    data_msg = []
    bytes_recd = 0
    while bytes_recd < MSGLEN:
        data = socket.recv(DATALEN)
        if data == b'':
            print "Socket is broken - Closing program"
            break
        data_msg.append(float(data))
        bytes_recd = bytes_recd + len(data)

    print "-- Recieved --"
    print data_msg

    msg_as_bytes = struct.pack('dd', data_msg[0] , data_msg[1])

    crc_result = crc.calc(msg_as_bytes)
    crc_out = chr(crc_result >> 8) + chr(crc_result & 0x00ff)

    msg_out = slip.encode(msg_as_bytes + crc_out)

    print "-- Sending --"
    print type(msg_out)
    print "msg_out: ", msg_out
    print "crc: ",crc_out
    #telemetry.send(msg_out)

    print "-- Unpacked --"
    data_recv, crc_recv = msg_out[:MSGLEN], msg_out[MSGLEN:]
    print "Data: ", data_recv
    print "CRC: ", crc_recv
    msg_as_data = struct.unpack('dd', msg_out[:packet_size])
    print msg_as_data

    loop = loop - 1

print "Program Closing"
