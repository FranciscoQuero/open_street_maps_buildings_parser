from entities.map_element import MapElement


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
                node_id = building['nodes'][0]
                node = nodes_dictionary[node_id]
                latitude = node['lat']
                longitude = node['lon']
                type = building['tags']['building']
                map_element = MapElement(latitude, longitude, type)
                self._map_elements.append(map_element)

    def get_buildings_map_elements(self):
        return self._map_elements
