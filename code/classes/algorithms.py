import random
from graph import Graph


def random_assignment(graph, possibilities):
    print(graph.nodes)
    for node in graph.nodes.values():
        node.set_value(random.choice(possibilities))


if __name__ == '__main__':
    test_graph = Graph('../../data/Test/states.csv', '../../data/Test/neighbours.csv')

    random_assignment(test_graph, ['red', 'green', 'blue'])

    print(test_graph.get_violations())
