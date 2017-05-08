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
from slip_protocol import slip_protocol

# Connect to server
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('127.0.0.1', 1337))
except Exception as error:
    print error
    print 'Failed to connect'
    sys.exit()

# Variables
# We want X, Y, and Z position with a quality in percentage
x = 0.0
y = 0.0
z = 0.0
q = 0       # Quality

# Create serial object
#telemetry = serial.Serial(PORT_NAME, BAUD_RATE)

# Packing variables
packet_format = 'dddi'
packet_size = struct.calcsize(packet_format)

# Create slip
slip = slip_protocol()

while True:
    data_msg = []
    bytes_recd = 0
    while bytes_recd < MSGLEN:
        data = server.recv(DATALEN)
        if data == b'':
            print "Socket is broken - Closing program"
            break
        data_msg.append(float(data))
        bytes_recd = bytes_recd + len(data)

    print "-- Recieved --"
    print data_msg

    # Extract data to x, y z, and q.
    x = 1
    y = 2
    z = 3
    q = 4

    msg_as_bytes = struct.pack('dddi', x, y, z, q)

    msg_out = slip.encode(msg_as_bytes)

    print "-- Sending --"
    print type(msg_out)
    print "msg_out: ", msg_out
    #telemetry.send(msg_out)

    # ---- RECEIVING END ------
    print "-- Unpacked --"
    data_recv = msg_out;
    msg_recv = []
    started = False
    escaped = False

    for byte in data_recv:
        # If message has been started.
        if started:
            # Check for ESC.
            if byte == slip.SLIP_ESC:
                escaped = True

            # When ESC was just received, append according to next byte.
            if escaped:
                if byte == slip.SLIP_ESC_ESC:
                    msg_recv.append(slip.SLIP_ESC)
                elif byte == slip.SLIP_ESC_END:
                    msg_recv.append(slip.SLIP_END)
                escaped = False

            # Check for END.
            elif byte == slip.SLIP_END:
                started = False

            # Otherwise just append the byte.
            else:
                msg_recv.append(byte)

        # Start or stop message when END is received.
        elif byte == slip.SLIP_END:
                started = True

    print msg_recv

    msg_recv_unpacked = struct.unpack('dddi', ''.join(msg_recv))

    print msg_recv_unpacked

    #msg_as_data = struct.unpack('dddi', msg_out[:packet_size])
    #print msg_as_data

print "Program Closing"
