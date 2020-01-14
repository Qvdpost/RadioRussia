
class Greedy:
    def __init__(self, graph, transmitters):
        self.graph = graph
        self.transmitters = transmitters

    def run(self):
        """
        Greedily assigns the lowest costing transmitters to the nodes of the graph.
        """
        for node in self.graph.nodes.values():
            # Retreive all valid possible values for a node.
            node_possibilities = node.get_possibilities(self.transmitters)

            # Sort them by value in ascending order.
            node_possibilities.sort(key=lambda node: node.get_value())

            # Assign the lowest value possibility to the node.
            node.set_value(node_possibilities[0])
