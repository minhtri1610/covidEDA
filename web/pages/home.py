import dash
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.H2('TÊN ĐỀ TÀI', className="app-header--title")
        ]
    ),
    html.Div(
        className="wapper-team",
        children=html.Div([
            html.H3('Nhóm 3TN'),
            html.P('Danh Sách Thành Viên'),
            html.H4('Trịnh Xuân Nam'),
            html.H4(' Lê Nguyễn Thiên Thanh'),
            html.H4('Lê Phước Trí'),
            html.H4(' Trần Minh Trí'),
        ])
    ),
    html.Div(
        className="wapper-nav",
        children=html.Div([
            dcc.Link('Phân Tích', href='/analytics', className="btn-nav btn-analy"),
            dcc.Link('Dự Báo', href='/predict', className="btn-nav btn-pre"),
        ])
    ),
    
], className="wapper-container bg-index")