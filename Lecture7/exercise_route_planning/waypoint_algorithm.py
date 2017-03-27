# Waypoint algorithm
import math

from export_kml import kmlclass

from utm import utmconv
from math import fabs

utm = utmconv();


# Plot dat' shit
kml_class = kmlclass()

# Open file
f = open("aqlogreader/coordinates_in_utm.txt", "r")

# Read Data
data_waypoints = []
for line in f:
    (easting, northing, height) = line.split(",");
    data_waypoints.append((float(easting), float(northing), float(height)))

new_waypoints = []
new_waypoints.append(0)
new_waypoints.append(len(data_waypoints)-1)

epsilon = 2
max_points = 32
stop_condition = False

while(len(new_waypoints) < max_points and not stop_condition):
    new_waypoints.sort()
    added_points = []
    stop_condition = True
    for i in range((len(new_waypoints) - 1)):
        first_point = data_waypoints[new_waypoints[i]]

        last_point = data_waypoints[new_waypoints[i+1]]

        a = first_point[1] - last_point[1] # y1 - y2
        b = last_point[0] - first_point[0] # x2 - x1
        c = (first_point[0] - last_point[0])*first_point[1] + (last_point[1] - first_point[1])*first_point[0] # (x1-x2)*y1 + (y2-y1)*x1
        denominator = math.sqrt(a**2 + b**2)
        furthest_away_waypoint = (0, 0) # Distance, index

        for index, current_waypoint in enumerate(data_waypoints[new_waypoints[i]:new_waypoints[i+1]]):
            distance = math.fabs(a*current_waypoint[0] + b * current_waypoint[1] + c)/denominator
            if furthest_away_waypoint[0] < distance:
                furthest_away_waypoint = (distance, index + new_waypoints[i])

        if furthest_away_waypoint[0] > epsilon:
            new_waypoints.append(furthest_away_waypoint[1])
            stop_condition = False

print "Number of waypoints found: ", len(new_waypoints)
kml_class.begin("Waypoints.kml", "Waypoints", "Waypoints", 3)
zone = 32
hemisphere = "N"
kml_class.trksegbegin("test","test2", "blue", "relativeToGround")
wpts = []
for index in new_waypoints:
	(lat, lon) = utm.utm_to_geodetic(hemisphere, zone, float(data_waypoints[index][0]), float(data_waypoints[index][1]))

	kml_class.trkpt(lat, lon, float(data_waypoints[index][2]))
	wpts.append( (lat, lon, float(data_waypoints[index][2])) )
kml_class.trksegend()
kml_class.end()



# qgc parameters
qgc_dunno = 0
qgc_frame_takeoff = 0 # 0 = abs 3 = relative
qgc_frame_wpt = 0 # 0 = abs 3 = relative
qgc_poi_heading = 3.14
qgc_vert_vmax = 1.0
qgc_radius = 3.5
qgc_loiter = 1
qgc_hori_vmax = 10
qgc_yaw = 3.14
qgc_dunno2 = 1



# qgc constants
MAV_CMD_NAV_WAYPOINT = 16
MAV_CMD_NAV_TAKEOFF = 22




# export to QGC waypoint list
f = open ('waypoints.txt', 'w')
f.write ('QGC WPL 120\n')
lat = wpts[0][0]
lon = wpts[0][1]
alt = wpts[0][2]

f.write ('%d\t%d\t%d\t%d\t%.2f\t%.0f\t%.2f\t%.2f\t%.8f\t%.8f\t%.3f\t%d\n' % (0, qgc_dunno, qgc_frame_takeoff, MAV_CMD_NAV_TAKEOFF, qgc_radius, qgc_loiter*1000, qgc_poi_heading, qgc_vert_vmax, lat, lon, alt, qgc_dunno2))

for wpt in wpts:
        f.write ('%d\t%d\t%d\t%d\t%.2f\t%.0f\t%.2f\t%.2f\t%.8f\t%.8f\t%.3f\t%d\n' % (i+1, qgc_dunno, qgc_frame_wpt, MAV_CMD_NAV_WAYPOINT, qgc_radius, qgc_loiter*1000, qgc_hori_vmax, qgc_yaw, wpt[0], wpt[1], wpt[2], qgc_dunno2))
f.close

