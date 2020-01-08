from code.algorithms import randomize
from code.classes import graph
from code.visualisation import visualise as vis

if __name__ == '__main__':
    test_graph = graph.Graph('data/US/states.csv', 'data/US/neighbours.csv')

    randomize.random_assignment(test_graph, ['red', 'green', 'blue'])

    print(test_graph.get_violations())

    vis.visualise(test_graph, "data/US/gz_2010_us_040_00_500k.json")
