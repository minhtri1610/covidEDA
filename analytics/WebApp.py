
from unicodedata import name
from matplotlib.pyplot import figure, xlabel
import pandas as pd
from dash import Dash,html,dcc
import plotly.express as px
from pygments import highlight
import plotly.graph_objs as go
# pip install dash

app = Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

df = pd.read_csv('covid_data.csv', header = 0, delimiter=',', encoding='unicode_escape')
groupedvalues_c = df.groupby('continent').sum().reset_index()
fig_1 = px.bar(groupedvalues_c, x='continent',y='total_cases',color='continent',labels={'total_cases': "Total Cases",'continent':'Continents'},width=720,height=480)
fig_2 = px.pie(groupedvalues_c, values='total_cases',names='continent', color='continent',labels={'total_cases': "Total Cases",'continent':'Continents'},width=720,height=480)
fig_3 = px.bar(groupedvalues_c, x='continent',y='total_deaths',color='continent',labels={'total_deaths': "Total Deaths",'continent':'Continents'},width=720,height=480)
fig_4 = px.pie(groupedvalues_c, values='total_deaths',names='continent', color='continent',labels={'total_deaths': "Total Deaths",'continent':'Continents'},width=720,height=480)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('corona-logo-1.jpg'),
                     id='corona-image',
                     style={
                         "height": "150px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
                     )
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H1("Covid - 19", style={"margin-bottom": "0px", 'color': 'black'}),
                html.H2("Track Covid - 19 Cases", style={"margin-top": "0px", 'color': 'black'}),
            ])
        ], className="one-half column", id="title"),

        html.Div([
            html.H4('Presented by gourp 3TN',
                    style={'color': 'orange'}),

        ], className="one-third column", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        html.H3("THE TOTAL CASES", style={"margin-bottom": "0px", 'color': 'black','textAlign':"center"})
    ]),

    html.Div([

        html.Div([
            dcc.Graph(id='my_graph_1',figure=fig_1),
        ], className = 'one-half column'),

        html.Div([
            dcc.Graph(id='my_graph_2',figure=fig_2),
        ], className = 'one-half column'),
     ],className="row flex-display"),

       html.Div([
        html.H3("THE TOTAL DEATHS", style={"margin-bottom": "0px", 'color': 'black','textAlign':"center"})
    ]),

     html.Div([
        html.Div([
            dcc.Graph(id='my_graph_3',figure=fig_3),
        ], className = 'one-half column'),

        html.Div([
            dcc.Graph(id='my_graph_4',figure=fig_4),
        ], className = 'one-half column'),
     ],className="row flex-display")
])



if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
    