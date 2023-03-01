import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Criando os dados para os gráficos
df = px.data.gapminder()
fig1 = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent', title='Gráfico 1')
fig2 = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent', title='Gráfico 2')
fig3 = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent', title='Gráfico 3')

# Criando o layout do app
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.Div(children=[
        dcc.Graph(id='fig1', figure=fig1),
    ], style={'width': '33%', 'display': 'inline-block'}),
    html.Div(children=[
        dcc.Graph(id='fig2', figure=fig2),
    ], style={'width': '33%', 'display': 'inline-block'}),
    html.Div(children=[
        dcc.Graph(id='fig3', figure=fig3),
    ], style={'width': '33%', 'display': 'inline-block'}),
])

if __name__ == '__main__':
    app.run_server()
