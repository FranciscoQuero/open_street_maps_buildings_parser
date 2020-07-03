from src.repositories.buildings_data_access import BuildingsDataAccess


class SaveBuildingsUseCase(object):
    def __init__(self, buildings):
        self._data_access = BuildingsDataAccess()
        self._buildings = buildings

    def run(self):
        self._data_access.save_buildings_file(self._buildings)
