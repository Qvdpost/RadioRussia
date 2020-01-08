from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
import json


def visualise(graph, geo_file):
    with open(geo_file, 'r') as geo_file:
        data = json.load(geo_file)

    states = {node.name.lower(): node for node in graph.nodes.values() if len(node.neighbours) != 0}

    for i in range(len(data['features'])):
        data['features'] = [feature for feature in data['features'] if feature['properties']['NAME'].lower().replace(' ', '') in states]

    for feature in data['features']:
        feature['properties']['colour'] = states[feature['properties']['NAME'].lower().replace(' ', '')].value

    geo_source = GeoJSONDataSource(geojson=json.dumps(data))

    p = figure(background_fill_color="lightgrey")
    p.patches(xs='xs', ys='ys', fill_color='colour', source=geo_source)

    show(p)
