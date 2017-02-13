#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

def parser(filename):
                array = []
                with open(filename, "r") as ins:
                        for line in ins:
                                array.append( line.rstrip().split("\t") )
                return array



filename="log-2016-01-14.txt"
data = parser(filename)


x_time = []
y_voltage = []

i =0
for dat in data:
#	print dat[4]
	print dat[11]

#	x_time.append( dat[4]  )
#	x_time.append( i )
	x = time.strptime(dat[1],'%H:%M:%S')
	x = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
	x_time.append( x )
	y_voltage.append( dat[11]  )
	i+=1

#x_time = x_time - x_time[0];
x_time[:] = [x - x_time[0] for x in x_time]

f, axarr = plt.subplots(3,  sharex=True )
axarr[0].scatter(x_time, y_voltage)
axarr[0].set_title('HDOP')
axarr[0].set_xlabel("Time")
axarr[0].set_ylabel("Voltage")



f.subplots_adjust(hspace=0.3)
plt.xlim(int(float(x_time[0])),int(float(x_time[-1])))
plt.suptitle(filename, fontsize=20)
plt.show()

