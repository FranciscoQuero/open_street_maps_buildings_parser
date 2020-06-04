import json


class MapFileDataAccess(object):
    def __init__(self):
        pass

    @staticmethod
    def save_map_file(map_file):
        map_structure = json.loads(map_file.content)
        with open('map.osm', 'w') as f:
            json.dump(map_structure, f)

    @staticmethod
    def load_map_file():
        with open('map.osm', 'r') as json_file:
            map_file = json.load(json_file)

        return map_file
