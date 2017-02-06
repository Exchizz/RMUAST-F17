#!/usr/bin/python

from exportkml import kmlclass
import numpy as np
import matplotlib.pyplot as plt

class NMEA:
	def parse_nmea(self,filename):
		array = []
		with open(filename, "r") as ins:
			for line in ins:
				array.append( line.rstrip().split(",") )
		return array

nmea = NMEA()
#file = nmea.parse_nmea("nmea_trimble_gnss_eduquad_flight.txt")
file = nmea.parse_nmea("nmea_ublox_neo_24h_static_gpgga.txt")


kml_class = kmlclass()

i = 0
x_sat = []
y_sat = []
y_msl = []
y_hdop = []
kml_class.begin("test.kml", "somename", "some more text", 3.0)
for msg in file:
	if msg[0] == "":
		continue
	try:
		float(msg[4])
		print msg[2], ", ", msg[4], ", ", msg[9], ", ", len(msg)
	except:
		continue



	lat = int(float(msg[2])/100)
	degDec=(float(msg[2])-lat*100)/60;
	lat = lat + degDec;



	lon = int(float(msg[4])/100)
	degDec=(float(msg[4])-lon*100)/60;
	lon = lon + degDec;

	kml_class.trkpt( lat, lon, int(float(msg[9]))) # lon, lat

	y_sat.append(int(float(msg[7])))
	y_msl.append(int(float(msg[9])))
	x_sat.append(i)

	y_hdop.append(int(float(msg[8])))
	i+=1
kml_class.end()

# Create plt with HDOP
plt.scatter(x_sat, y_hdop)
plt.show()


# Create plt with MSL
plt.scatter(x_sat, y_msl)
plt.show()


# Create one plt of sattelittes
plt.scatter(x_sat, y_sat)
plt.show()
