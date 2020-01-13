import json

from bokeh.io import show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure


def visualise(graph, geo_file):
    """
    Visualisation code that uses bokeh and geometry data from a JSON file
    to represent a coloured graph.
    """

    with open(geo_file, 'r') as geo_file:
        data = json.load(geo_file)

    # Dict comprehension that creates a dictionary with a lowercase name for the
    # node if it has at least one neighbour
    states = {node.name.lower(): node for node in graph.nodes.values() if len(node.neighbours) != 0}

    # Take the features of the states that have at least one neighbour
    for i in range(len(data['features'])):
        data['features'] = [feature for feature in data['features'] if
                            feature['properties']['NAME'].lower().replace(' ', '') in states]

    # Get the colour of the states from the corresponding nodes
    for feature in data['features']:
        if states[feature['properties']['NAME'].lower().replace(' ', '')].get_value() is not None:
            feature['properties']['colour'] = states[
                feature['properties']['NAME'].lower().replace(' ', '')].get_value().colour.get_web()

            feature['properties']['cost'] = states[
                feature['properties']['NAME'].lower().replace(' ', '')].get_value().value
            feature['properties']['transmitter'] = states[
                feature['properties']['NAME'].lower().replace(' ', '')].get_value().name
        else:
            feature['properties']['colour'] = 'grey'
            feature['properties']['cost'] = 0
            feature['properties']['transmitter'] = "None"

    geo_source = GeoJSONDataSource(geojson=json.dumps(data))

    # Set the bokeh tooltips
    TOOLTIPS = [
        ("(x,y)", "($x, $y)"),
        ("State", "@NAME"),
        ("Transmitter", "@transmitter"),
        ("Cost", "@cost")
    ]

    p = figure(background_fill_color="lightgrey", tooltips=TOOLTIPS)
    p.sizing_mode = 'scale_height'
    p.patches(xs='xs', ys='ys', fill_color='colour', line_color='black', line_width=0.2, source=geo_source)

    show(p)
