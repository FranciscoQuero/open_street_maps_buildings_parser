import requests


class OpenStreetMapConnector(object):
    MAP_URI = 'https://api.openstreetmap.org/api/0.6/map.json'

    def __init__(self, boundaries):
        self._boundaries = boundaries

    def get_map_in_boundaries(self):
        boundaries_box = self._get_boundaries_box()
        payload = {'bbox': boundaries_box}
        map_file = requests.get(self.MAP_URI, params=payload)
        return map_file

    def _get_boundaries_box(self):
        boundaries_list = [self._boundaries.minimum_longitude, self._boundaries.minimum_latitude,
                           self._boundaries.maximum_longitude, self._boundaries.maximum_latitude]
        boundaries_list_string = [str(element) for element in boundaries_list]
        return ','.join(boundaries_list_string)
