import copy


class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, graph, transmitters):
        self.graph = graph
        self.transmitters = transmitters

    def run(self):
        # Initialise the stack of graphs.
        stack = [copy.deepcopy(self.graph)]

        # Track best solution.
        best = None
        best_value = float('inf')

        while len(stack) > 0:
            graph = stack.pop()

            # Retrieve the next empty node.
            node = graph.get_empty_node()
            if node is not None:

                # Retrieve all valid possible values for the node.
                values = node.get_possibilities(self.transmitters)

                # Add an instance of the graph to the stack, with each unique value assigned to the node.
                for value in values:
                    new_graph = copy.deepcopy(graph)
                    new_graph.nodes[node.id].set_value(value)
                    stack.append(new_graph)
            else:
                # If there are no more empty nodes. The solution is completed.
                graph_value = graph.calculate_value()
                if graph_value < best_value:
                    best = graph
                    best_value = graph_value

        # Update the input graph with the best result found.
        self.graph.nodes = best.nodes
