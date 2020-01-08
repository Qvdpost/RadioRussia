import random


def random_assignment(graph, possibilities):
    for node in graph.nodes.values():
        node.set_value(random.choice(possibilities))


def random_reconfigure_nodes(graph, nodes, possibilities):
    for node in nodes:
        graph.nodes[node].set_value(random.choice(possibilities))


def random_reassignment(graph, possibilities):
    random_assignment(graph, possibilities)

    violating_nodes = graph.get_violations()

    while len(violating_nodes):
        random_reconfigure_nodes(graph, violating_nodes, possibilities)

        violating_nodes = graph.get_violations()
