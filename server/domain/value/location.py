from math import radians, cos, sin, asin, sqrt
class Location():
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, location):
        return haversine(self.latitude, self.longitude, location.latitude, location.longitude)

    def haversine(lat1, lon1, lat2, lon2):
        ''' Ty Rosetta Code <3 '''
	R = 6372.8 # Earth radius in kilometers

	dLat = radians(lat2 - lat1)
	dLon = radians(lon2 - lon1)
	lat1 = radians(lat1)
	lat2 = radians(lat2)

	a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
	c = 2*asin(sqrt(a))

	return R * c
