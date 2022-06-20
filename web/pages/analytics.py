from unicodedata import name
from matplotlib.pyplot import figure, xlabel
import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px
from pygments import highlight
import plotly.graph_objs as go

dash.register_page(__name__)

df = pd.read_csv('./data/covid_data.csv', header = 0, delimiter=',', encoding='unicode_escape')
groupedvalues_c = df.groupby('continent').sum().reset_index()
total_cases = sum(df['total_cases'])
total_deaths = sum(df['total_deaths'])
fig_1 = px.bar(groupedvalues_c, x='continent',y='total_cases',color='continent',labels={'total_cases': "Total Cases",'continent':'Continents'},width=720,height=480)
fig_2 = px.pie(groupedvalues_c, values='total_cases',names='continent', color='continent',labels={'total_cases': "Total Cases",'continent':'Continents'},width=720,height=480)
fig_3 = px.bar(groupedvalues_c, x='continent',y='total_deaths',color='continent',labels={'total_deaths': "Total Deaths",'continent':'Continents'},width=720,height=480)
fig_4 = px.pie(groupedvalues_c, values='total_deaths',names='continent', color='continent',labels={'total_deaths': "Total Deaths",'continent':'Continents'},width=720,height=480)

layout = html.Div([

    html.Div([
        html.Div([
            html.H2( print(total_cases))
        ])
    ]),

    html.Div([
        html.H2("Total number of infections", style={"margin-bottom": "0px", 'color': 'black','textAlign':"center"})
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
        html.H2("Total number of deaths", style={"margin-bottom": "0px", 'color': 'black','textAlign':"center"})
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
# pip install dash

# app = Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
