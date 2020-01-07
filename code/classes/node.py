class Node():
    def __init__(self, name, uid):
        self.name = name
        self.id = uid
        self.neighbours = {}
        self.value = None

    def add_neighbour(self, node):
        self.neighbours[node.id] = node

    def is_valid(self):
        for neighbour in self.neighbours.values():
            if neighbour.value == self.value:
                return False

        return True

    def set_value(self, value):
        self.value = value

    def __repr__(self):
        return self.id