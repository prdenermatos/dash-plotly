from dash import Dash, html, dependencies, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


labels = ['Maçãs', 'Bananas', 'Laranjas']
values = [23, 17, 35]
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])





data_moc = {
    'x': [15, 16, 20 , 30 ],
    'y': [40, 50, 60, 90]
}


app = Dash(__name__)

app.layout = html.Div(
    children=[
    
    html.Div(
    children= [
       html.H1(children="Monitor de perspectiva no tempo"),  
        html.P("Esta é uma descrição resumida do gráfico"),
        dcc.Graph(
                id = "graph-lines" ,
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
    ),

    html.Div(
    children=[
        html.H1(children="Análise de Composição"),  
            html.P("Esta é uma descrição resumida do gráfico"),
            dcc.Graph(
                    id = "graph-boxplot" ,
                    figure={
                        "data": [
                            {
                                "y": data_moc["x"], 'type': 'box'  # o Type define o grafico  e cada um recebe uma forma de parâmetro
                            },
                            {
                                "y": data_moc["y"], 'type': 'box'  # o Type define o grafico  e cada um recebe uma forma de parâmetro
                            },
                        ],
                        "layout": {"title": "Boxplot"},
                    },
                ),
            ]
        ),

        html.Div(
        children=[
            html.H1(children="Análise de Composição"),  
                html.P("Pode ser usado para avaliar grandezas relacionadas"),
                dcc.Graph(
                        id = "graph-2-lines" ,
                        figure={
                    "data": [
                        {
                            "x": data_moc["x"],  
                            "y": data_moc["y"],
                            "type": "lines", 
                        },
                         {
                            "x": data_moc["y"],  
                            "y": data_moc["x"],
                            "type": "lines", 
                        },
                    ],
                    "layout": {"title": "Curvas com intercessão "},
                },
                    ),
        
        
                ]
        ),
        html.Div(
        children=[
            html.H1(children="Gráfico de Barras e Tendências"),  
                html.P("Pode ser usado para avaliar grandezas relacionadas"),
                dcc.Graph(
                        id = "graph-pie",
                        figure={
                    "data": [
                        {
                            "x": data_moc["x"],  
                            "y": data_moc["y"],
                            "type": "bar", 
                        },
                         {
                            "x": data_moc["x"],  
                            "y": data_moc["y"],
                            "type": "lines", 
                        },
                    ],
                    "layout": {"title": "Curvas com intercessão "},
                },
                    ),
                ]
        ),
         html.Div(
            children=[
            html.H1(children="Gráfico de Barras e Tendências"),  
                html.P("Pode ser usado para avaliar grandezas relacionadas"),
                dcc.Graph(
                        id = "graph-bar-lines" ,
                        figure=fig,

                       
                    ),
                dcc.Graph(
                        id = "graph-bar-lines2" ,
                        figure=fig2, 
                )
                ]
        ),

    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)

