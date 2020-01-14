import copy

from .randomize import random_reconfigure_node
import random


class HillClimber:
    """
    The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, graph, transmitters):
        if not graph.is_solution():
            raise Exception("Requires a complete solution.")

        self.graph = graph
        self.value = graph.calculate_value()

        self.transmitters = transmitters

    def mutate_graph(self, new_graph):
        """
        Changes the value of a random node with a random valid value.
        """
        random_node = random.choice(list(new_graph.nodes.values()))
        available_transmitters = random_node.get_possibilities(self.transmitters)
        random_reconfigure_node(new_graph, random_node, available_transmitters)

    def check_solution(self, new_graph):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_graph.calculate_value()
        old_value = self.value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.graph = new_graph
            self.value = new_value

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        for iteration in range(iterations):
            print(f'Iteration {iteration}/{iterations}, current value: {self.value}')

            # Create a copy of the graph to simulate the change
            new_graph = copy.deepcopy(self.graph)

            self.mutate_graph(new_graph)

            # Accept it if it is better
            self.check_solution(new_graph)
