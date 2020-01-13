def greedy(graph, possibilities):
    """
    Greedily assigns the lowest costing transmitters to the nodes of the graph.
    """
    for node in graph.nodes.values():
        # Retreive all valid possible values for a node.
        node_possibilities = node.get_possibilities(possibilities)

        # Sort them by value in ascending order.
        node_possibilities.sort(key=lambda x: x.value)

        # Assign the lowest value possibility to the node.
        node.set_value(node_possibilities[0])
