#!/usr/bin/python
#/****************************************************************************
# exportKML
# Copyright (c) 2014-2015, Kjeld Jensen <kj@kjen.dk>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#****************************************************************************/
'''
2015-03-22 Kjeld Removed unnecessary trkptend() function
2015-11-18 Kjeld Added optional absolute altitude mode
'''
class kmlclass:

    def __init__(self):
        return

    def begin(self, fname, name, desc, width):
        self.f = open (fname, 'w')

	self.f.write ('	<?xml version="1.0" encoding="UTF-8"?>\n')
	self.f.write ('	<kml xmlns="http://www.opengis.net/kml/2.2">\n')
	self.f.write ('	  <Document>\n')
	self.f.write ('	    <name>Paths</name>\n')
	self.f.write ('	    <description>Examples of paths. Note that the tessellate tag is by default\n')
	self.f.write ('	      set to 0. If you want to create tessellated lines, they must be authored\n')
	self.f.write ('	      (or edited) directly in KML.</description>\n')
	self.f.write ('	    <Style id="yellowLineGreenPoly">\n')
	self.f.write ('	      <LineStyle>\n')
	self.f.write ('	        <color>7f00ffff</color>\n')
	self.f.write ('	        <width>4</width>\n')
	self.f.write ('	      </LineStyle>\n')
	self.f.write ('	      <PolyStyle>\n')
	self.f.write ('	        <color>7f00ff00</color>\n')
	self.f.write ('	      </PolyStyle>\n')
	self.f.write ('	    </Style>\n')
	self.f.write ('	    <Placemark>\n')
	self.f.write ('	      <name>Absolute Extruded</name>\n')
	self.f.write ('	      <description>Transparent green wall with yellow outlines</description>\n')
	self.f.write ('	      <styleUrl>#yellowLineGreenPoly</styleUrl>\n')
	self.f.write ('	      <LineString>\n')
	self.f.write ('	        <extrude>1</extrude>\n')
	self.f.write ('	        <tessellate>1</tessellate>\n')
	self.f.write ('	        <altitudeMode>absolute</altitudeMode>\n')
	self.f.write ('	        <coordinates>\n')


    def trkpt(self, lat, lon, ele):
        self.f.write ('%013.10f,%014.10f,%.3f\n' % (lon, lat, ele))
        return

    def end(self):
	self.f.write ('	        </coordinates>\n')
	self.f.write ('	      </LineString>\n')
	self.f.write ('	    </Placemark>\n')
	self.f.write ('	  </Document>\n')
	self.f.write ('	</kml>\n')
        self.f.close ()

