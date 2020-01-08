from code.algorithms import randomize
from code.classes import graph

if __name__ == '__main__':
    test_graph = graph.Graph('data/US/states.csv', 'data/US/neighbours.csv')

    possibilities = ['red', 'green', 'blue', 'yellow', 'cheese', 'strawberry']

    randomize.random_assignment(test_graph, possibilities)

    violating_nodes = test_graph.get_violations()
    print(len(violating_nodes))

