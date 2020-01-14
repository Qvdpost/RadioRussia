from code.algorithms import randomize
from code.algorithms import hillclimber as hc
from code.algorithms import depth_first as df
from code.algorithms import greedy
from code.classes import graph, transmitters
from code.visualisation import visualise as vis

if __name__ == '__main__':
    # Create a graph from our data
    test_graph = graph.Graph('data/US/states.csv', 'data/US/neighbours.csv')

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme('data/transmitters.csv')

    # Perform algorithm that keeps reassigning values until the case is solved
    # randomize.random_reassignment(test_graph, transmitters.get_scheme(1))

    # Example on how to get the nodes that have neighbours with the same value and print them
    # violating_nodes = test_graph.get_violations()
    #
    # print(len(violating_nodes))
    # print(test_graph.get_violations())
    # print(test_graph.calculate_value())

    print(transmitters.get_scheme(1)[2] == transmitters.get_scheme(1)[2])

    # Hill Climber
    print("Starting random assignment...")
    randomize.random_reassignment(test_graph, transmitters.get_scheme(1))

    print("Setting up hillclimber...")
    climber = hc.HillClimber(test_graph, transmitters.get_scheme(1))

    print("Running hillclimber...")
    climber.run(20000)

    # Depth First
    # depth = df.DepthFirst(test_graph, transmitters.get_scheme(1)[0:4])
    # depth.run()

    # Greedy
    # greed = greedy.greedy(test_graph, transmitters.get_scheme((1)))
    #
    # print(test_graph.calculate_value())
    # print(test_graph.get_violations())
    # vis.visualise(test_graph, "data/US/gz_2010_us_040_00_500k.json")
