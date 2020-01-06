class Node():
    def __init__(self, name, uid):
        self.name = name
        self.id = uid
        self.neighbours = {}
        self.value = None

    def add_neighbour(self, node):
        self.neighbours[node.id] = node
