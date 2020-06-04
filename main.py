from use_cases.download_map_file_use_case import DownloadMapFileUseCase
from use_cases.find_buildings_use_case import FindBuildingsUseCase
from use_cases.read_map_file_use_case import ReadMapFileUseCase
from use_cases.save_buildings_use_case import SaveBuildingsUseCase


def download_map():
    minimum_latitude = 37.1473
    minimum_longitude = -3.6097
    maximum_latitude = 37.1647
    maximum_longitude = -3.5875

    download_use_case = DownloadMapFileUseCase(minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude)
    download_use_case.run()


if __name__ == '__main__':
    read_map_use_case = ReadMapFileUseCase()
    read_map_use_case.run()
    map_structure = read_map_use_case.get_map_file()

    find_buildings_use_case = FindBuildingsUseCase(map_structure)
    find_buildings_use_case.run()

    buildings = find_buildings_use_case.get_buildings_map_elements()
    save_buildings_use_case = SaveBuildingsUseCase(buildings)
    save_buildings_use_case.run()
