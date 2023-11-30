import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

# 假設這是您的資料集
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 13, 18, 20]
}
df = pd.DataFrame(data)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('散點圖示例'),
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='x', y='y', title='散點圖')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
