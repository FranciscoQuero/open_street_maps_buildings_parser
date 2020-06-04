import json


class BuildingsDataAccess(object):
    def __init__(self):
        pass

    @staticmethod
    def save_buildings_file(buildings):
        buildings_dictionary = [element.to_dict() for element in buildings]
        with open('buildings_info.json', 'w') as f:
            json.dump(buildings_dictionary, f)
