# Waypoint algorithm
import math

# Open file
f = open("aqlogreader/coordinates_in_utm.txt", "r")

# Read Data

data_waypoints = []
for line in f:
    (easting, northing) = line.split(",");
    data_waypoints.append((float(easting), float(northing)))

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

print new_waypoints


#for i in range(32):
