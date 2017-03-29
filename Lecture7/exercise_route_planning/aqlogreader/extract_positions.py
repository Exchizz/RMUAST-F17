from AQLogReader import aqLogReader
from utm import utmconv
from export_kml import kmlclass
from math import fabs

logreader = aqLogReader("../020-AQL.LOG");
#logreader.printChannelNames()
logreader.setChannels(['GPS_LAT', 'GPS_LON', 'GPS_HEIGHT'])
data = logreader.getData()

utm = utmconv();

kml_class = kmlclass()
kml_class.begin("original.kml", "Positions", "Positions", 3.0)

f = open('coordinates_in_utm.txt', 'w')
kml_class.trksegbegin("Original", "Original", "blue", "relativeToGround")

for pose in data:
	(lat, lon, height) = pose[0], pose[1], pose[2];
	if fabs(lat) > 0.1:
		(hemisphere, zone, zlet, easting, northing) = utm.geodetic_to_utm(lat, lon);

		f.write(str(easting) + ',' + str(northing) + "," + str(height) + str("\n"))
		kml_class.trkpt( lat, lon, height) # lon, lat
f.close();

kml_class.trksegend()
kml_class.end()
