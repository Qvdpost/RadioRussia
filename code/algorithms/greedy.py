def greedy(graph, possibilities):
    """
    Greedily assigns the lowest costing transmitters to the nodes of the graph.
    """
    for node in graph.nodes.values():
        node_possibilities = node.get_possibilities(possibilities)

        node_possibilities.sort(key=lambda x: x.value)

        node.set_value(node_possibilities[0])
