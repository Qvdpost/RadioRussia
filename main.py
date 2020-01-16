from code.classes import graph, transmitters

from code.algorithms import randomize
from code.algorithms import greedy as gr
from code.algorithms import depth_first as df
from code.algorithms import hillclimber as hc
from code.algorithms import simulatedannealing as sa

from code.visualisation import visualise as vis

if __name__ == '__main__':
    source_folder = 'data/US'

    # Create a graph from our data
    test_graph = graph.Graph(f'{source_folder}/states.csv', f'{source_folder}/neighbours.csv')

    # Create the transmitter cost schemes
    transmitters = transmitters.CostScheme('data/transmitters.csv')

    # --------------------------- Random reassignment --------------------------
    random_graph = randomize.random_reassignment(test_graph, transmitters.get_scheme(1))
    print(f"Value of the configuration after Randomized Assignment: {random_graph.calculate_value()}")

    # --------------------------- Greedy ---------------------------------------
    greedy = gr.Greedy(test_graph, transmitters.get_scheme((1)))
    greedy.run()

    print(f"Value of the configuration after Greedy: {greedy.graph.calculate_value()}")

    # --------------------------- Depth First ----------------------------------
    # depth = df.DepthFirst(test_graph, transmitters.get_scheme(1)[0:4])
    # depth.run()
    #
    # print(f"Value of the configuration after DepthFirst: {depth.graph.calculate_value()}")

    # --------------------------- Hill Climber ---------------------------------
    print("Setting up Hill Climber...")
    climber = hc.HillClimber(random_graph, transmitters.get_scheme(1))

    print("Running Hill Climber...")
    climber.run(2000, verbose=True)

    print(f"Value of the configuration after Hill Climber: {climber.graph.calculate_value()}")

    # --------------------------- Simulated Annealing --------------------------
    # Het is lastig om een goede starttemperatuur te vinden. Een goede vuistregel is de maximale
    # scoreverandering die plaats kan vinden. In ons geval is dat 19, want we veranderen
    # iedere keer maar 1 transmitter, en het waardeverschil tussen de duurste en de goedkoopste
    # in column 1 is 19.

    print("Setting up Simulated Annealing...")
    simanneal = sa.SimulatedAnnealing(random_graph, transmitters.get_scheme(1), temperature=19)

    print("Running Simulated Annealing...")
    simanneal.run(2000, verbose=True)

    print(f"Value of the configuration after Simulated Annealing: {simanneal.graph.calculate_value()}")

    # --------------------------- Visualisation --------------------------------
    vis.visualise(simanneal.graph, "data/US/gz_2010_us_040_00_500k.json")
