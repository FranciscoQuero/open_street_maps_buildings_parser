from connectors.open_street_maps_connector import OpenStreetMapConnector
from entities.map_boundaries import MapBoundaries


class DownloadMapFileUseCase(object):
    def __init__(self, minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude):
        self._boundaries = MapBoundaries(minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude)
        self._connector = OpenStreetMapConnector(self._boundaries)
        self._downloaded_map = None

    def run(self):
        self._downloaded_map = self._connector.get_map_in_boundaries()

    def get_downloaded_map(self):
        return self._downloaded_map
