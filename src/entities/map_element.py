class MapElement(object):
    def __init__(self, latitude, longitude, type):
        self.latitude = latitude
        self.longitude = longitude
        self.type = type

    def to_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "type": self.type,
        }
