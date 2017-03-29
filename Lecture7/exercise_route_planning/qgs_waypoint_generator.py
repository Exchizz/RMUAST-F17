class GQCGenerator:
    # qgc constants
    MAV_CMD_NAV_WAYPOINT = 16
    MAV_CMD_NAV_TAKEOFF = 22

    def __enter__(self):
        return self;

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()

    # qgc parameters
    def __init__(self, filename = "waypoints.txt", qgc_frame_takeoff = 0, qgc_frame_wpt = 0, qgc_poi_heading = 3.14, qgc_vert_vmax = 1.0, qgc_radius = 3.5,qgc_loiter = 1, qgc_hori_vmax = 10):
        self.qgc_frame_takeoff = qgc_frame_takeoff # 0 = abs 3 = relative
        self.qgc_dunno = 0
        self.qgc_frame_wpt = qgc_frame_wpt # 0 = abs 3 = relative
        self.qgc_poi_heading = qgc_poi_heading
        self.qgc_vert_vmax = qgc_vert_vmax
        self.qgc_radius = qgc_radius
        self.qgc_loiter = qgc_loiter
        self.qgc_hori_vmax = qgc_hori_vmax
        self.qgc_dunno2 = 1
        self.i = 0

        self.f = open (filename, 'w')
        self.f.write ('QGC WPL 120\n')

    def AddWaypoint(self, lat, lon, alt, yaw):
        self.f.write ('%d\t%d\t%d\t%d\t%.2f\t%.0f\t%.2f\t%.2f\t%.8f\t%.8f\t%.3f\t%d\n' % (self.i+1, self.qgc_dunno, self.qgc_frame_wpt, self.MAV_CMD_NAV_WAYPOINT, self.qgc_radius, self.qgc_loiter*1000, self.qgc_hori_vmax, yaw, lat, lon, alt, self.qgc_dunno2))
        self.i+=1

    def AddTakeOff(self, lat, lon, alt, yaw):
        self.f.write ('%d\t%d\t%d\t%d\t%.2f\t%.0f\t%.2f\t%.2f\t%.8f\t%.8f\t%.3f\t%d\n' % (self.i+1, self.qgc_dunno, self.qgc_frame_wpt, self.MAV_CMD_NAV_TAKEOFF, self.qgc_radius, self.qgc_loiter*1000, self.qgc_hori_vmax, yaw, lat, lon, alt, self.qgc_dunno2))
        self.i+=1
