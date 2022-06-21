from unicodedata import name
from matplotlib.pyplot import figure, xlabel
import pandas as pd
import dash
import plotly.express as px
from pygments import highlight
from dash import html, dcc, callback, Input, Output
import plotly.graph_objs as go

dash.register_page(__name__)

df = pd.read_csv('./data/covid_data.csv', header = 0, delimiter=',', encoding='unicode_escape')
groupedvalues_c = df.groupby('continent').sum().reset_index()
df_d = df.sort_values(by='total_deaths', ascending=False)
df_d = df_d.head(10)
df_c = df.sort_values(by='total_cases', ascending=False)
df_c = df_c.head(10)
df_o = df.sort_values(by='aged_70_older', ascending=False)
df_o = df_o.head(10)

fig_1 = px.bar(groupedvalues_c.sort_values(by='total_cases', ascending=False), x='continent',y='total_cases',color='continent',labels={'total_cases': "Total Cases",'continent':'Continents'},width=720,height=480)
fig_2 = px.pie(groupedvalues_c, values='total_cases',names='continent', color='continent',labels={'total_cases': "Total Cases",'continent':'Continents'},width=720,height=480)
fig_3 = px.bar(groupedvalues_c.sort_values(by='total_deaths', ascending=False), x='continent',y='total_deaths',color='continent',labels={'total_deaths': "Total Deaths",'continent':'Continents'},width=720,height=480)
fig_4 = px.pie(groupedvalues_c, values='total_deaths',names='continent', color='continent',labels={'total_deaths': "Total Deaths",'continent':'Continents'},width=720,height=480)

fig_5 = px.bar(df_d, x='location',y='total_deaths',color='continent',labels={'total_deaths': "Total Deaths",'continent':'Continents'},width=720,height=480)
fig_6 = px.bar(df_c, x='location',y='total_cases',color='continent',labels={'total_cases': "Total Cases",'continent':'Continents'},width=720,height=480)
fig_7 = px.bar(df_o, x='location',y='aged_70_older',color='continent',labels={'aged_70_older': "Aged 70 older",'continent':'Continents'},width=720,height=480)

layout = html.Div([

    html.Div([
        html.Div([
            html.H2("113,863,086 COVID Cases", id="total_cases"),
            html.H2("2,532,633 COVID Deaths" ,id="total_deaths")
        ], className="wapper-top-cases")
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
    ],className="row flex-display"),

    html.Div([
        html.H2('TOP 10 countries with the highest number of deaths', className="text-center"),
        html.Div([
            dcc.Graph(id='my_graph_5',figure=fig_5),
        ], className = 'one-half column'),
        html.H2('TOP 10 countries with the highest number of infections', className="text-center"),
        html.Div([
            dcc.Graph(id='my_graph_6',figure=fig_6),
        ], className = 'one-half column'),
    ],className="row flex-display"),
    
    html.Div([
        html.H2('TOP 10 countries with the highest percentage of population over 70', className="text-center"),
        html.Div([
            dcc.Graph(id='my_graph_7',figure=fig_7),
        ], className = 'one-half column')
    ],className="row flex-display")

    ,html.Div(
        className="wapper-nav",
        children=html.Div([
            dcc.Link('< Home Page', href='/home', className="btn-nav btn-pre"),
            dcc.Link('Predict Page >', href='/predict', className="btn-nav btn-analy")
            
        ])
    )
])


# @callback(
#     Output(component_id='total_cases', component_property='children'),
#     Input('total_cases', 'value')
# )
# def cal_total_cases():
#     total_cases = sum(df['total_cases'])
#     return total_cases

# @callback(
#     Output(component_id='total_deaths', component_property='children'),
#     Input('total_deaths', 'value')
# )
# def cal_total_deaths():
#     total_deaths = sum(df['total_deaths'])
#     return total_deaths
# pip install dash

# app = Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
