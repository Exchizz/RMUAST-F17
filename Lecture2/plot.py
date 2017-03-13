#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time

LIPO_LOW  = 3
LIPO_HIGH = 4.2
LIPO_SPAN = LIPO_HIGH - LIPO_LOW

def CalculateSOC(voltage):
	voltage = float(voltage)
	return (voltage - LIPO_LOW)/LIPO_SPAN



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
x_voltage = []
y_soc = []

i =0
for dat in data:
	x = time.strptime(dat[1],'%H:%M:%S')
	x = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
	x_time.append( x )
	y_voltage.append( dat[11]  )


	x_voltage.append( dat[11] )
	y_soc.append( CalculateSOC(dat[11]) )

	i+=1

#x_time = x_time - x_time[0];
x_time[:] = [x - x_time[0] for x in x_time]

f, axarr = plt.subplots(2,  sharex=False )
axarr[0].scatter(x_time, y_voltage)
axarr[0].set_title('Voltage discharge')
axarr[0].set_xlabel("Time")
axarr[0].set_ylabel("Voltage")


axarr[1].scatter(x_voltage, y_soc)
axarr[1].set_title('SOC-Calculator')
axarr[1].set_xlabel("Voltage")
axarr[1].set_ylabel("SOC")


#plt.xlim(int(float(x_time[0])),int(float(x_time[-1])))

f.subplots_adjust(hspace=0.3)
plt.suptitle(filename, fontsize=20)
plt.show()

