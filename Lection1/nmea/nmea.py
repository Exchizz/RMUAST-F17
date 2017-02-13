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
#filename="nmea_trimble_gnss_eduquad_flight.txt"
filename="nmea_ublox_neo_24h_static_gpgga.txt"
file = nmea.parse_nmea(filename)


kml_class = kmlclass()

i = 0
x_obs = []
y_sat = []
y_msl = []
y_hdop = []

kml_class.begin("test.kml", "somename", "some more text", 3.0)
for msg in file:
	try:
		# Convert from ddmm.mmmm  (degree minutes) to  dd (decimal degree)
		lat = int(float(msg[2])/100)
		degDec=(float(msg[2])-lat*100)/60;
		lat = lat + degDec;

		lon = int(float(msg[4])/100)
		degDec=(float(msg[4])-lon*100)/60;
		lon = lon + degDec;
	except:
		continue




	kml_class.trkpt( lat, lon, int(float(msg[9]))) # lon, lat

	y_sat.append(int(float(msg[7])))
	y_msl.append(int(float(msg[9])))
	x_obs.append(i)

	y_hdop.append(int(float(msg[8])))
	i+=1
kml_class.end()


f, axarr = plt.subplots(3,  sharex=True	)
axarr[0].scatter(x_obs, y_hdop)
axarr[0].set_title('HDOP')
axarr[0].set_xlabel("Observations")
axarr[0].set_ylabel("Horizontal accuracy")

axarr[1].scatter(x_obs,y_sat)
axarr[1].set_title('Number of sattelites')
axarr[1].set_xlabel("Observations")
axarr[1].set_ylabel("# of sattelites")

axarr[2].scatter(x_obs, y_msl)
axarr[2].set_title('Height (MSL)')
axarr[2].set_xlabel("Observations")
axarr[2].set_ylabel("Height [m]")


f.subplots_adjust(hspace=0.3)
plt.xlim(0,len(x_obs)-1)
plt.suptitle(filename, fontsize=20)
plt.show()
