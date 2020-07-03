from src.entities.map_element import MapElement


class FindBuildingsUseCase(object):
    def __init__(self, map_file):
        self._map = map_file
        self._map_elements = []

    def run(self):
        nodes_dictionary = self._get_nodes_dictionary_from_map()
        buildings = self._get_buildings_from_map()
        self._generate_map_elements_from_buildings(buildings, nodes_dictionary)

    def _get_nodes_dictionary_from_map(self):
        nodes = [element for element in self._map['elements'] if element['type'] == 'node']

        nodes_dictionary = {}
        for node in nodes:
            nodes_dictionary[node['id']] = node

        return nodes_dictionary

    def _get_buildings_from_map(self):
        elements_with_tags = [element for element in self._map['elements'] if 'tags' in element]

        buildings = []
        for element in elements_with_tags:
            if 'building' in element['tags']:
                buildings.append(element)

        return buildings

    def _generate_map_elements_from_buildings(self, buildings, nodes_dictionary):
        for building in buildings:
            if 'nodes' in building:
                latitude, longitude = self._calculate_mean_coordinates(building, nodes_dictionary)
                building_type = building['tags']['building']
                map_element = MapElement(latitude, longitude, building_type)
                self._map_elements.append(map_element)

    def _calculate_mean_coordinates(self, building, nodes_dictionary):
        latitudes = []
        longitudes = []
        for i in range(0, len(building['nodes'])):
            node_id = building['nodes'][i]
            node = nodes_dictionary[node_id]
            latitudes.append(node['lat'])
            longitudes.append(node['lon'])
        latitude = sum(latitudes) / len(latitudes)
        longitude = sum(longitudes) / len(longitudes)

        return latitude, longitude

    def get_buildings_map_elements(self):
        return self._map_elements
