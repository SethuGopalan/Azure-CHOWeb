import dash
import dash_bootstrap_components as dbc
from dash import html,dcc



app=dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE])

app.layout=dbc.Container([

    dbc.Row([
        dbc.Col([
            html.H1("Welcome to CHO online")

        ])
    ])
])

if __name__=="__main__":
    app.run(debug=True)

    