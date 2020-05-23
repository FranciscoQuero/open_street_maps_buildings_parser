from use_cases.download_map_file_use_case import DownloadMapFileUseCase

if __name__ == '__main__':
    minimum_latitude = 37.1473
    minimum_longitude = -3.6097
    maximum_latitude = 37.1647
    maximum_longitude = -3.5875

    download_use_case = DownloadMapFileUseCase(minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude)
    download_use_case.run()
    map = download_use_case.get_downloaded_map()

