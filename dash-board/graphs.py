from dash import Dash, html, dependencies, dcc



data_moc = {
    'x': [15, 16, 20 , 30 ],
    'y': [40, 50, 60, 90]
}


app = Dash(__name__)

app.layout = html.Div(
    children=[
    html.H1(children="Teste"),  
    html.P("Esta é uma descrição resumida do gráfico"),
   dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data_moc["x"],  # PAR ORDENADOS
                        "y": data_moc["y"],
                        "type": "lines",  #  TIPO DO GRÁFICO
                    },
                ],
                "layout": {"title": "Curva de Tendência"},
            },
        ),


    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)

# dash-table, dash-html-components, dash-core-components, tenacity, plotly, dash