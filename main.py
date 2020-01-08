from code.algorithms import randomize
from code.classes import graph
from code.visualisation import visualise as vis

if __name__ == '__main__':
    # Create a graph from our data
    test_graph = graph.Graph('data/US/states.csv', 'data/US/neighbours.csv')

    possibilities = ['red', 'green', 'blue', 'yellow', 'magenta']

    randomize.random_reassignment(test_graph, possibilities)

    violating_nodes = test_graph.get_violations()
    print(len(violating_nodes))

    print(test_graph.get_violations())

    vis.visualise(test_graph, "data/US/gz_2010_us_040_00_500k.json")
