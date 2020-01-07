import random


def random_assignment(graph, possibilities):
    for node in graph.nodes.values():
        node.set_value(random.choice(possibilities))

