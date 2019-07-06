# -*- coding: utf-8 -*-

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_bootstrap_components import themes


def sankey_graph(node_labels, node_links):
    return dcc.Graph(
        figure={
            'data': [{
                'type': 'sankey',
                'node': {
                    'label': node_labels,
                },
                'link': {
                    "source": [node_labels.index(l[0]) for l in node_links],
                    "target": [node_labels.index(l[1]) for l in node_links],
                    "value": [l[2] for l in node_links],
                }
            }],
        },
    )


labels = [
    "net import",
    "uk produced",
    "all",
    "non-packaging waste",
    "packaging waste",
    "stock",
    "recycled",
    "recycled in uk",
    "recycled via export",
    "non-recycled",
    "unaccounted",
]
links = [
    ("net import", "all", 4.6),
    ("uk produced", "all", 1.3),
    ("all", "non-packaging waste", 1.5),
    ("all", "packaging waste", 2.2),
    ("all", "stock", 1.2),
    ("all", "unaccounted", 1.0),
    ("non-packaging waste", "recycled", 0.2),
    ("non-packaging waste", "non-recycled", 1.3),
    ("packaging waste", "recycled in uk", 0.4),
    ("packaging waste", "recycled via export", 0.65),
    ("packaging waste", "non-recycled", 1.15),
    ("recycled in uk", "recycled", 0.4),
    ("recycled via export", "recycled", 0.65),
]

app = dash.Dash(__name__, external_stylesheets=[themes.BOOTSTRAP])

app.layout = html.Div(className="container-fluid", children=[
    sankey_graph(labels, links)
])

if __name__ == '__main__':
    app.run_server(debug=True)
