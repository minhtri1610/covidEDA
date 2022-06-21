import dash
import pickle
import numpy as np
from dash import html, dcc, callback, Input, Output
from dash.exceptions import PreventUpdate

dash.register_page(__name__)

mymodel = pickle.load(open('./data/mymodel.sav','rb')) 

layout = html.Div([
    html.Img(src="assets/imgs/pre-img.png"),
    html.H1('Number of deaths in prediction'),
    html.P(children='Number of positive cases', className="title"),
	html.Div([

        dcc.Input(
            id="input_positive",
            type="number",
            placeholder="Number of positive cases",
        )
    ]),
    html.P(children='Population', className="title"),
	html.Div([

        dcc.Input(
            id="input_population",
            type="number",
            placeholder="Population",
        )
    ]),
    html.P(children='Number of people older than 70', className="title"),
	html.Div([

        dcc.Input(
            id="input_older70",
            type="number",
            placeholder="Number of people older than 70",
        )
    ]),

    html.Div([
        html.Button('Predict', id='submit')
    ]),
    html.Div(id='output_deaths'),

    html.Div(
        className="wapper-nav",
        children=html.Div([
            dcc.Link('< Home Page', href='/home', className="btn-nav btn-pre"),
            dcc.Link('Analytics Page >', href='/analytics', className="btn-nav btn-analy")
            
        ])
    )
], className='wapper_predict')



@callback(
    Output(component_id='output_deaths', component_property='children'),
    Input(component_id='input_positive', component_property='value'),
    Input(component_id='input_population', component_property='value'),
    Input(component_id='input_older70', component_property='value'),
    Input(component_id='submit', component_property='n_clicks'),
)
def update_city_selected(input_positive, input_population, input_older70, n_clicks):
    if n_clicks is None:
        return f'Deaths Prediction: 0'
    else:
        if input_positive is not None and input_population is not None and input_older70 is not None :
            predicted_Die = np.round(mymodel.predict([[input_positive, input_population, input_older70]]))
            return f'Deaths Prediction: {predicted_Die}'
        else:
            return f'Deaths Prediction: 0'
        
        