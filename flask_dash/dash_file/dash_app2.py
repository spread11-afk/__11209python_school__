from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

dash2 = Dash(requests_pathname_prefix="/dash/app2/")

dash2.layout = html.Div([
    html.H1(children='Dash Layout', style={'textAlign':'center'}),
    ])


