from dash import Dash, html,dash_table
import pandas as pd
import dash_bootstrap_components as dbc
from collections import OrderedDict

dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])

dash2.title = 'Youbike即時資料'

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ])

df = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)

dash2.layout = html.Div([dbc.Container([html.Div([html.Div([html.H1('Youbike即時資料')],className='col text-center')],className='row'),html.Div([html.Div([html.H1('顯示表格資料')],className='col text-center')],className='row',style={'pandingTop':'2rem'}),html.Div([html.Div([dash_table.DataTable(df.to_dict('records'),columns=[{'id':column,'name':column} for column in df.columns],
                        page_size=20
                    )],className="col text-center")],className="row",style={"paddingTop":'2rem'})])],className='container-lg')
