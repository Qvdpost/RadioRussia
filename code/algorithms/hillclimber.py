import copy

from .randomize import random_reconfigure_nodes
import random


class HillClimber:
    def __init__(self, graph, transmitters):
        if not graph.is_solution():
            raise Exception("Requires a complete solution.")

        self.graph = graph
        self.transmitters = transmitters

    def run(self, iterations):
        value = self.graph.calculate_value()
        for iteration in range(iterations):
            # Create a copy of the graph to simulate the change.
            new_graph = copy.deepcopy(self.graph)

            # Change the value of a random node with a random valid value.
            random_node = random.choice(list(self.graph.nodes.keys()))
            available_transmitters = self.graph.nodes[random_node].get_possibilities(self.transmitters)
            random_reconfigure_nodes(self.graph, [random_node], available_transmitters)

            # Check and accept a better solution.
            new_value = self.graph.calculate_value()
            if new_value <= value:
                value = new_value
                self.graph = new_graph
                print(iteration, value)
