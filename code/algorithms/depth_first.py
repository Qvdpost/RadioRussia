import copy


class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, graph, transmitters):
        self.graph = graph
        self.transmitters = transmitters

        self.states = [copy.deepcopy(self.graph)]

        self.best_solution = None
        self.best_value = float('inf')

    def get_next_state(self):
        return self.states.pop()

    def build_children(self, graph, node):
        # Retrieve all valid possible values for the node.
        values = node.get_possibilities(self.transmitters)

        # Add an instance of the graph to the stack, with each unique value assigned to the node.
        for value in values:
            new_graph = copy.deepcopy(graph)
            new_graph.nodes[node.id].set_value(value)
            self.states.append(new_graph)

    def check_solution(self, new_graph):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_graph.calculate_value()
        old_value = self.best_value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.best_solution = new_graph
            self.value = new_value

    def run(self):
        # Initialise the stack of graphs.
        stack = [copy.deepcopy(self.graph)]

        while len(stack) > 0:
            new_graph = self.get_next_state()

            # Retrieve the next empty node.
            node = new_graph.get_empty_node()
            if node is not None:
                self.build_children(new_graph, node)
            else:
                self.check_solution(new_graph)

        # Update the input graph with the best result found.
        self.graph = self.best_solution
