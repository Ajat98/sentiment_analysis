import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
import pandas as pd 
import plotly
import random
import plotly.graph_objs as pgo
from collections import deque

app = dash.Dash(__name__)
app.layout = html.Div(
   [
       html.H2('Live Twitter Sentiment'),
       dcc.Graph(id='live-graph', animate=True),
       dcc.Interval(
           id='graph-update',
           interval = 1*1000
       ),
   ]
)

@app.callback(Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')])

def update_graph_scatter():
    try:

        #Create conn here instead of above bc dash uses thread, will be issue with accessing cursor to perform actual operation
        #give connection every time
        conn = sqlite3.connect('twitter.db')
        c = conn.cursor()

        df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE '%crypto%' ORDER BY unix DESC LIMIT 1000", conn)
        df.sort_values('unix', inplace=True)
        df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
        df.dropna(inplace=True)

        X = df.unix.values[-100:]
        Y = df.sentiment_smoothed.values[-100:]

        data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode='lines+markers'
        )

        return {'data': [data], 'layout': pgo.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                    yaxis=dict(range=[min(Y),max(Y)]),)}
    
    except Exception as e:
        with open('errors.txt', 'a') as f:
            f.write(str(e))

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port=8080, debug=True)