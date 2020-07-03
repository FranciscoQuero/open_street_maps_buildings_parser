from src.repositories.map_file_data_access import MapFileDataAccess


class ReadMapFileUseCase(object):
    def __init__(self):
        self._data_access = MapFileDataAccess()
        self._map_file = None

    def run(self):
        self._map_file = self._data_access.load_map_file()

    def get_map_file(self):
        return self._map_file
