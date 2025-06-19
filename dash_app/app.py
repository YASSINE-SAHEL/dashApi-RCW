import dash
from dash import html, dcc, Output, Input
import requests

app = dash.Dash(__name__, requests_pathname_prefix='/dashboard/')

app.layout = html.Div(children=[

    # Menu de navigation
    html.Div([
        html.A('Acceuil', href='/'),
        " | ",
        html.A('Logout', href='/logout'),
    ], style={'marginTop': 20}),

    html.H1(children="Example de Dashboard"),

    # Composant météo (mis à jour automatiquement)
    html.H2("📡 Données météo actuelles - Casablanca"),
    dcc.Interval(id='interval-refresh', interval=10*1000, n_intervals=0),
    html.Div(id='weather-box', style={
        'padding': '20px',
        'border': '2px solid #ccc',
        'borderRadius': '10px',
        'width': '300px',
        'marginTop': '20px',
        'backgroundColor': '#f0f8ff'
    }),

    # Bar Graph
    html.H2("**** Bar Graph ****"),
    dcc.Graph(
        id="exmpl_1",
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [6, 9, 4], "type": "bar", "name": "Example 1"},
                {"x": [7, 2, 5], "y": [3, 7, 1], "type": "bar", "name": "Example 2"}
            ]
        }
    ),

    # Line Graph
    html.H2("**** Line Graph ****"),
    dcc.Graph(
        id="exmpl_2",
        figure={
            "data": [
                {"x": [4, 3, 8], "y": [4, 9, 1], "type": "line", "name": "Example 3"},
                {"x": [2, 6, 8], "y": [9, 6, 11], "type": "line", "name": "Example 4"}
            ]
        }
    ),

    # Scatter Graph
    html.H2("**** Scatter Graph ****"),
    dcc.Graph(
        id="exmpl_3",
        figure={
            "data": [
                {"x": [4, 3, 8], "y": [4, 9, 1], "type": "scatter", "mode": "markers", "name": "Example 5"},
                {"x": [2, 6, 8], "y": [9, 6, 11], "type": "scatter", "mode": "markers", "name": "Example 6"}
            ]
        }
    ),

    # Pie Chart
    html.H2("**** Pie Chart Graph ****"),
    dcc.Graph(
        id="exmpl_4",
        figure={
            "data": [
                {"labels": ["A", "B", "C"], "values": [4, 9, 1], "type": "pie", "name": "Example 7"}
            ]
        }
    )
])

@app.callback(
    Output('weather-box', 'children'),
    Input('interval-refresh', 'n_intervals')
)
def update_weather(n):
    try:
        response = requests.get("https://weather-api-rcw-cwh8fhbkd2b7cxd8.canadaeast-01.azurewebsites.net/info")
        data = response.json()
        return [
            html.P(f"Date : {data['date']}"),
            html.P(f"Heure : {data['time']}"),
            html.P(f"Ville : {data['weather']['city']}"),
            html.P(f"Température : {data['weather']['tempreture']}°C"),
            html.P(f"Description : {data['weather']['description']}"),
        ]
    except Exception as e:
        return html.P("Erreur lors de la récupération des données météo.")

server = app.server
