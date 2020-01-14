from code.algorithms import randomize
from code.algorithms import hillclimber as hc
from code.algorithms import depth_first as df
from code.algorithms import greedy as gr
from code.classes import graph, transmitters
from code.visualisation import visualise as vis

if __name__ == '__main__':
    source_folder = 'data/US'

    # Create a graph from our data
    test_graph = graph.Graph(f'{source_folder}/states.csv', f'{source_folder}/neighbours.csv')

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme('data/transmitters.csv')

    # # Random reassignment
    random_graph = randomize.random_reassignment(test_graph, transmitters.get_scheme(1))
    print(f"Value of the configuration after Randomized Assignment: {random_graph.calculate_value()}")

    # Greedy
    greedy = gr.Greedy(test_graph, transmitters.get_scheme((1)))
    greedy.run()

    print(f"Value of the configuration after Greedy: {greedy.graph.calculate_value()}")

    # Depth First
    depth = df.DepthFirst(test_graph, transmitters.get_scheme(1)[0:4])
    depth.run()

    print(f"Value of the configuration after DepthFirst: {depth.graph.calculate_value()}")

    # Hill Climber
    print("Setting up hillclimber...")
    climber = hc.HillClimber(greedy.graph, transmitters.get_scheme(1))

    print("Running hillclimber...")
    climber.run(2000)

    # Visualisation
    print(f"Value of the configuration after HillClimber: {climber.graph.calculate_value()}")
    vis.visualise(climber.graph, "data/US/gz_2010_us_040_00_500k.json")
