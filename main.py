import sys

from src.use_cases.download_map_file_use_case import DownloadMapFileUseCase
from src.use_cases.find_buildings_use_case import FindBuildingsUseCase
from src.use_cases.read_map_file_use_case import ReadMapFileUseCase
from src.use_cases.save_buildings_use_case import SaveBuildingsUseCase


def download_map(argv):
    minimum_latitude = argv[1]
    minimum_longitude = argv[2]
    maximum_latitude = argv[3]
    maximum_longitude = argv[4]

    download_use_case = DownloadMapFileUseCase(minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude)
    download_use_case.run()


def main():
    if len(sys.argv) > 1:
        download_map(sys.argv)

    read_map_use_case = ReadMapFileUseCase()
    read_map_use_case.run()
    map_structure = read_map_use_case.get_map_file()

    find_buildings_use_case = FindBuildingsUseCase(map_structure)
    find_buildings_use_case.run()

    buildings = find_buildings_use_case.get_buildings_map_elements()
    save_buildings_use_case = SaveBuildingsUseCase(buildings)
    save_buildings_use_case.run()


if __name__ == '__main__':
    main()
    print('Success! Social attractors were successfully identified. See the JSON file saved in this directory.')
