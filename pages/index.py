# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Why Predict Asteroids' Diameters?

            There has been heightened interest into predicting asteroid diameters due to the potential damage if these objects are to impact Earth. 
            
            This education app will help categorize potential threats to the planet as well as expand our knowledge of outer space. Big asteroids leave even bigger destruction so prepartion and accuracy is key.

            ✅ Asteroid Diameter Predictor is a prediction app that uses orbital parameters of an asteroid to accurately predict it's diameter (in kilometers) and compare those results to the actual diameter recorded.

            ✅ Asteroid Diameter Predictor has shown success in asteroid prediction. It can be implemented or scaled for comets, planets, and other objects in space for future applicaation and analysis.

            ✅ At the time of it's inception, Asteroid Diameter Predictor is the only intelligent prediction app that uses sophisticated machine learning algorithms to make statistical approximations on asteroids' diameters. 

            """
        ),
        dcc.Link(dbc.Button('Start Predicting!', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])