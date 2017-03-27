from AQLogReader import aqLogReader
from utm import utmconv
from exportkml import kmlclass
from math import fabs

logreader = aqLogReader("../021-AQL.LOG");
#logreader.printChannelNames()
logreader.setChannels(['GPS_LAT', 'GPS_LON', 'GPS_HEIGHT'])
data = logreader.getData()

utm = utmconv();

kml_class = kmlclass()
kml_class.begin("test.kml", "somename", "some more text", 3.0)

f = open('coordinates_in_utm.txt', 'w')
for pose in data:
	(lat, lon, height) = pose[0], pose[1], pose[2];
	if fabs(lat) > 0.1:
		(hemisphere, zone, zlet, easting, northing) = utm.geodetic_to_utm(lat, lon);
#		print easting, northing
#		(lat, lon) = utm.utm_to_geodetic(hemisphere, zone, easting, northing)

		f.write(str(easting) + ',' + str(northing) + str("\n"))
		kml_class.trkpt( lat, lon, 2) # lon, lat
f.close();
kml_class.end()
