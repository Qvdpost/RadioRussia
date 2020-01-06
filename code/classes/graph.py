import csv
from .node import Node


class Graph():
    def __init__(self, nodes_file, neighbours_file):
        self.nodes = self.load_nodes(nodes_file)
        self.load_neighbours(neighbours_file)

    def load_nodes(self, node_file):
        nodes = {}
        with open(node_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                nodes[row['id']] = Node(row['name'], row['id'])

        return nodes

    def load_neighbours(self, neighbour_file):
        with open(neighbour_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                neighbours = eval(row['neighbours'])
                node_id = row['state']
                for neighbour in neighbours:
                    neighbour = self.nodes[neighbour]
                    self.nodes[node_id].add_neighbour(neighbour)