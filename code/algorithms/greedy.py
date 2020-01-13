def greedy(graph, transmitters):
    for node in graph.nodes.values():
        possibilities = node.get_possibilities(transmitters)

        possibilities.sort(key=lambda x: x.value)

        node.set_value(possibilities[0])
