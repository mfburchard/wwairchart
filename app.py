import pandas as pd
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

data = pd.read_csv('https://datamfburchaws.s3.us-east-2.amazonaws.com/airdata_cities.csv')

app = dash.Dash()

server = app.server

app.layout = html.Div([     
    dcc.Graph(
        id='MedianPM25',
        figure={
            'data': [
                go.Scatter(
                    x=data[data['City'] == i]['Date'],
                    y=data[data['City'] == i]['median'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 5,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in data.City.unique()
            ],

            'layout': go.Layout(
                xaxis={'title': 'Date'},
                yaxis={'title': 'PM2.5'},
                margin={'l': 50, 'b': 30, 't': 10, 'r': 0},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
   
])

if __name__ == '__main__':
    app.run_server(debug=True)
 