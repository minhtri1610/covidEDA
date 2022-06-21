import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.H2('Covid 19 Pandemic: Data, Analysis & Visualization', className="app-header--title")
        ]
    ),
    html.Div(
        className="wapper-team",
        children=html.Div([
            html.H3('3TN team'),
            html.P('List members'),
            html.H4('Trinh Xuan Nam'),
            html.H4('Le Nguyen Thien Thanh'),
            html.H4('Le Phuoc Tri'),
            html.H4('Tran Minh Tri'),
        ])
    ),
    html.Div(
        className="wapper-nav",
        children=html.Div([
            dcc.Link('Analytics', href='/analytics', className="btn-nav btn-analy"),
            dcc.Link('Predict', href='/predict', className="btn-nav btn-pre"),
        ])
    ),
    
], className="wapper-container bg-index")