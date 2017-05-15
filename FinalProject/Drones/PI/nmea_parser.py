import time
import serial
from crc16 import crc16
from slip_protocol import slip_protocol
from struct import pack
from utm import utmconv
from math import pi, cos, hypot, acos, sin

port_telemetry = serial.Serial("/dev/telemetry", baudrate=57600)
port_atmega = serial.Serial("/dev/ttyAMA0", baudrate=57600)

print "connected to: " + port_telemetry.portstr
print "connected to: " + port_atmega.portstr

slip = slip_protocol()
crc = crc16()

# RoboLab
lat_center = 55.3673034
lon_center = 10.4312593

# instantiate utmconv class
uc = utmconv()

# convert from geodetic to UTM
(hemisphere, zone, letter, easting, northing) = uc.geodetic_to_utm (lat_center,lon_center)

while True:
	try:
		rcv = port_telemetry.readline()
	except:
		rcv = ''
	

	line = rcv.rstrip().split(",")
	if line[0] == "$GTPOS":
		x = float(line[3])
		y = float(line[4])
		z = float(line[5])

		print "X: ",x, " Y:", y, " Z: ", z
	elif line[0] == "$GTERR":
		print "ERROR"
		continue

	elif line[0] == "$GTRSS":
		print "GTRSS"
		continue
	else:
		continue


	easting += x/1000.0
	northing += y/1000.0

	# convert back from UTM to geodetic
	(lat, lon) = uc.utm_to_geodetic (hemisphere, zone, easting, northing)
	print "Lat: ", lat, " lon: ", lon

	#Do GPS coordinate conversion
	# Extract data to x, y z, and q.
	vDOP = 1.0
	tDOP = 1.0
	nDOP = 1.0
	eDOP = 1.0

	msg_as_bytes = pack('ddfffff', lat, lon, z/1000.0, vDOP, tDOP, nDOP, eDOP)

	crc_result = crc.calc(msg_as_bytes)
	crc_out = chr(crc_result >> 8) + chr(crc_result & 0x00FF)

	msg_out = slip.encode(msg_as_bytes + crc_out)
	

	
	#print "-- Sending --"
	print "Packet length: ", len(msg_out)
	print "msg_out: ", (msg_as_bytes + crc_out).encode("hex")

	port_atmega.write(msg_out)
	rcv = port_atmega.readline()
	print "msg_rcv: ", rcv.encode("HEX")
	rcv = port_atmega.readline()
	print rcv.encode("utf-8")

	
