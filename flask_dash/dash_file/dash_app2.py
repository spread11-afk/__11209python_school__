from dash import Dash, html
import pandas as pd
import dash_bootstrap_components as dbc

dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])

dash2.layout = html.Div([html.H1("H1!"),html.P("p!"),html.P("p2!")],className='container-lg',style={'backgroundColor':'#666'})


