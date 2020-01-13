import copy
from code.visualisation import visualise as vis


class DepthFirst:
    def __init__(self, graph, transmitters):
        self.graph = graph
        self.transmitters = transmitters

    def run(self):
        stack = [copy.deepcopy(self.graph)]
        best = None
        best_value = float('inf')

        while len(stack) > 0:
            graph = stack.pop()

            node = graph.get_empty_node()
            if node is not None:

                values = node.get_possibilities(self.transmitters)

                for value in values:
                    new_graph = copy.deepcopy(graph)
                    new_graph.nodes[node.id].set_value(value)
                    stack.append(new_graph)
            else:
                graph_value = graph.calculate_value()
                if graph_value < best_value:
                    best = graph
                    best_value = graph_value

        self.graph.nodes = best.nodes
