# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipeline = load('assets/pipeline.joblib')

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [

         dcc.Markdown(
            """
        
            ## Predictions

            Instructions: Picl the from the list of Asteroid's. User's can edit the following parameters: 'Number of Observations Used', 'Albedo', and 'Orbit Classification' to generate results

            """
        ),


        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Number of Observations Used'), 
        dcc.Slider(
            id='num_obs_used', 
            min=5, 
            max=4605, 
            step=50, 
            value=605, 
            marks={n: str(n) for n in range(100,4600,250)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Albedo (Proportion of the Light Reflected off Asteroid.)'), 
        dcc.Slider(
            id='albedo', 
            min=0, 
            max=1, 
            step=.1, 
            value=.10, 
            marks={n: str(n) for n in range(0,1,.10)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Orbit Classification'), 
        dcc.Dropdown(
            id='class', 
            options = [
                {'label': 'MBA', 'value': 'class_MBA'}, 
                {'label': 'IMB', 'value': 'class_IMB'}, 
                {'label': 'MCA', 'value': 'class_MCA'}, 
                {'label': 'APO', 'value': 'class_APO'}, 
                {'label': 'ATE', 'value': 'class_ATE'}, 
                {'label': 'OMB', 'value': 'class_OMB'}, 
                {'label': 'AMO', 'value': 'class_AMO'}, 
                {'label': 'TJN', 'value': 'class_TJN'}, 
                {'label': 'CEN', 'value': 'class_CEN'}, 
                {'label': 'AST', 'value': 'class_AST'}, 
                {'label': 'TNO', 'value': 'class_TNO'}, 
            ], 
            value = 'MBA', 
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Expected Lifespan', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')

        import pandas as pd

        @app.callback(
            Output('prediction-content', 'diameter'),
            [Input('year', 'value'), Input('continent', 'value')],      
                    ),

        def predict(year, continent):
        df = pd.DataFrame(
        columns=['year', 'continent'], 
        data=[[year, continent]]
                        ),

        y_pred = pipeline.predict(df)[0]
        return f'{y_pred:.0f} km'

    ]
)

layout = dbc.Row([column1, column2])





     