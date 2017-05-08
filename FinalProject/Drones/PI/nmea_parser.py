import time
import serial

port = serial.Serial("/dev/ttyUSB0", baudrate=57600)

print "connected to: " + port.portstr

while True:
	try:
		rcv = port.readline()
	except:
		rcv = ''
	

	line = rcv.rstrip().split(",")
	if line[0] == "$GTPOS":
		x = line[3]
		y = line[4]
		z = line[5]

		print "X: ",x, " Y:", y, " Z: ", z
	if line[0] == "$GTERR":
		print "ERROR"
	if line[0] == "$GTRSS":
		print "GTRSS"
