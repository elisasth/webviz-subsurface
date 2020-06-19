import dash_html_components as html
from dash.dependencies import Input, Output
from dash import Dash

from webviz_config import WebvizPluginABC
import pandas as pd

df = pd.read_csv ('silicon.txt', header = None)
df.columns = ['Angle','Intensity']
df.to_csv ('silicon.csv', index=None)


class MinimalPlugin(WebvizPluginABC):
    def __init__(self, app: Dash, title: str):
        super().__init__()

        self.title = title

        self.set_callbacks(app)

    @property
    def layout(self) -> html.Div:
        return html.Div(
            [
            html.H1(self.title),
            html.Div([
                dcc.Graph(
                    id='life-exp-vs-gdp',
                    figure={
                        'data': [
                            dict(
                                x=df[df['Angle'] == i]['gdp per capita'],
                                y=df[df['Intensity'] == i]['life expectancy'],
                                text=df[df['continent'] == i]['country'],
                                mode='markers',
                                opacity=0.7,
                                marker={
                                    'size': 15,
                                    'line': {'width': 0.5, 'color': 'white'}
                    },
                )
            ],
        }
    )
])
])

