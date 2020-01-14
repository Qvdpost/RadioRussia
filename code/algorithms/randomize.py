import random


def random_assignment(graph, possibilities):
    """
    Randomly assign each node with one of the possibilities.
    """
    for node in graph.nodes.values():
        node.set_value(random.choice(possibilities))


def random_reconfigure_nodes(graph, nodes, possibilities):
    """
    Takes a list of node ids and assigns each node with one of the possibilities.
    """
    for node in nodes:
        graph.nodes[node].set_value(random.choice(possibilities))


def random_reassignment(graph, possibilities):
    """
    Algorithm that reassigns nodes that are invalid until each node is valid.

    CAUTION: may run indefinitely.
    """

    random_assignment(graph, possibilities)
    print(graph.nodes['AL'].value.name)
    print(graph.nodes['HI'].is_valid())

    violating_nodes = graph.get_violations()
    print(violating_nodes)

    while len(violating_nodes):
        # print(len(violating_nodes))
        random_reconfigure_nodes(graph, violating_nodes, possibilities)

        violating_nodes = graph.get_violations()
