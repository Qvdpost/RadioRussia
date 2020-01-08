import random


def random_assignment(graph, possibilities):
    for node in graph.nodes.values():
        node.set_value(random.choice(possibilities))

def random_reconfigure_nodes(graph, nodes, possibilities):
    for node in nodes:        
        graph.nodes[node].set_value(random.choice(possibilities))

def random_reassignment(graph, possibilities):
    randomize.random_assignment(test_graph, possibilities)

    violating_nodes = test_graph.get_violations()

    while(len(violating_nodes)):
        randomize.random_reconfigure_nodes(test_graph, violating_nodes, possibilities)

        violating_nodes = test_graph.get_violations()
