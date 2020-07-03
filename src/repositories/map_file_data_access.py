import json


FILE_NAME = 'map_json.osm'


class MapFileDataAccess(object):

    def __init__(self):
        pass

    @staticmethod
    def save_map_file(map_file):
        map_structure = json.loads(map_file.content)
        with open(FILE_NAME, 'w') as json_file:
            json.dump(map_structure, json_file)

    @staticmethod
    def load_map_file():
        with open(FILE_NAME, 'r') as json_file:
            map_file = json.load(json_file)

        return map_file
