from src.connectors.open_street_maps_connector import OpenStreetMapConnector
from src.entities.map_boundaries import MapBoundaries
from src.repositories.map_file_data_access import MapFileDataAccess


class DownloadMapFileUseCase(object):
    def __init__(self, minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude):
        self._boundaries = MapBoundaries(minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude)
        self._connector = OpenStreetMapConnector(self._boundaries)
        self._downloaded_map = None

    def run(self):
        self._downloaded_map = self._connector.get_map_in_boundaries()
        data_access = MapFileDataAccess()
        data_access.save_map_file(self._downloaded_map)

    def get_downloaded_map(self):
        return self._downloaded_map
