
# <----------------------------------------------------------------------------------------------------------------------------------------------------------> #
#                                                           PATENT SIMILARITY IMPLEMENTATION N.F.                                                              #
# <----------------------------------------------------------------------------------------------------------------------------------------------------------> #

import pickle

infile = open("data_network.p",'rb')
data_network = pickle.load(infile)
infile.close()

nodes_ = data_network[1]
edges_ = data_network[2]

#%% Dash
import dash
import dash_cytoscape as cyto
import dash_html_components as html
from dash.dependencies import Input, Output

#####Cyto Code
        
app = dash.Dash(__name__)

# define layout
default_stylesheet = [
    {
        "selector": 'node',
        "style":{
                "label": "data(id)"
        }
    },
    {
        'selector': '.followerNode',
        'style': {
            'background-color': '#00AAD9'
        }
    }
]

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-event-callbacks-2',
        style={'width': '100%', 'height': '900px'},
        layout = {'name': 'cose'},
        elements = edges_ + nodes_,
        stylesheet=default_stylesheet
        ),
        html.P(id='cytoscape-tapNodeData-output'),
    ])

@app.callback(Output('cytoscape-tapNodeData-output', 'children'),
                Input('cytoscape-event-callbacks-2', 'tapNodeData'))
def displayTapNodeData(data):
    if data:
        return data['label']


if __name__ == '__main__':
    app.run_server(debug=False)