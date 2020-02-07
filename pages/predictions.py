# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
from joblib import load
import shap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy
from numpy import arange
import numpy as np

# Imports from this application
from app import app

from joblib import load
pipeline = load('assets/pipeline.joblib')
df = pd.read_csv('assets/top_asteroids.csv') #this will be exported ten asteroids with proper columns

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [

         dcc.Markdown(""" 
         ### Instructions: 
            This predictor will use the information associated with a particular asteroid selected from the drop down menu on the right. However, in an effort to make the app more interactive to the user, one can edit the following parameters: 'Number of Observations Used', 'Albedo', and 'Orbit Classification'. This will override the values for the given asteroid and generate a new prediction, but be careful this could totally throw off the accuracy of the prediction!! After selecting your inputs and asteroid, you will see the predicted diameter value  versus the actual diameter of the asteroid in question with the given parameters. These will be accompanied by a shapely plot to give a rundown on why the diameter was predicted to be that specific size. Hope you enjoy and have fun!

            """
        ),


        dcc.Markdown('## User Inputs', className='mb-5'), 
        dcc.Markdown('#### Number of Observations Used'), 
        dcc.Slider(
            id='n_obs_used', 
            min=100, 
            max=1500, 
            step=100, 
            value=605, #when someone selects asteroid what will happen with slider update?
            marks={n: str(n) for n in range(100,1500,100)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('#### Albedo (Proportion of the Light Reflected off Asteroid)'), 
        dcc.Slider(
            id='albedo', 
            min=0, 
            max=1, 
            step=.10, 
            value=.10, 
            marks={n: str(n) for n in np.linspace(0,1,num=9)}, 
            className='mb-5', 
        ), 

        dcc.Markdown('''
        ### Orbit Classification 
        For more info on orbit classifications use this link:
        [Click Here](https://pdssbn.astro.umd.edu/data_other/objclass.shtml)
        '''), 


        dcc.Dropdown(
            id='classes', 
            options = [
                {'label': 'Main Belt Asteroid', 'value': 'MBA'}, #mba write out for label
                {'label': 'Inner Main-Belt Asteroid', 'value': 'IMB'}, 
                {'label': 'Mars-Crossing Asteroid', 'value': 'MCA'}, 
                {'label': 'Apollo', 'value': 'APO'}, 
                {'label': 'Aten', 'value': 'ATE'}, 
                {'label': 'Outer Main-Belt Asteroid', 'value': 'OMB'}, 
                {'label': 'Amor', 'value': 'AMO'}, 
                {'label': 'Jupiter Trojan', 'value': 'TJN'}, 
                {'label': 'Centaur', 'value': 'CEN'}, 
                {'label': 'Asteroid (no matches)', 'value': 'AST'}, 
                {'label': 'TransNeptunian Object', 'value': 'TNO'}, 
            ], 
            value = 'MBA', 
            className='mb-5', 
        ), 
    ],
    md=6,
)

#select asteroid here in a dropdown !!!!!!!!!!
column2 = dbc.Col(
    [
        dcc.Markdown('#### Asteroids'), 
        dcc.Dropdown(
            id='asteroid', 
            options = [
                {'label': 'Agathe', 'value': '   228 Agathe'}, 
                {'label': 'Bruna', 'value': '   290 Bruna'}, 
                {'label': 'Phaetusa', 'value': '   296 Phaetusa'}, 
                {'label': 'Constantia', 'value': '   315 Constantia'}, 
                {'label': 'Adalberta', 'value': '   330 Adalberta (A910 CB)'},
                {'label': 'Hungaria', 'value': '   434 Hungaria (1898 DR)'}, 
                {'label': 'Adelaide', 'value': '   525 Adelaide (1908 EKa)'}, 
                {'label': 'Kundry', 'value': '   553 Kundry (1904 PP)'}, 
                {'label': 'Reginhild', 'value': '   574 Reginhild (1905 RD)'}, 
                {'label': 'Mireille', 'value': '   594 Mireille (1906 TW)'}, 
                {'label': 'Agnes', 'value': '   641 Agnes (1907 ZX)'}, 
                {'label': 'Kastalia', 'value': '   646 Kastalia (1907 AC)'}, 
                {'label': 'Adelgunde', 'value': '   647 Adelgunde (1907 AD)'}, 
                {'label': 'Josefa', 'value': '   649 Josefa (1907 AF)'}, 
                {'label': 'Noemi', 'value': '   703 Noemi (1910 KT)'}, 
            ], 
            value = 'Kastalia', 
            className='mb-5', 
        ), 

        #html.Img(src='assets/galaxy.jpg', style={'width':'100%'}),

    ],
)

#### Want to have shapely plot here
column3 = dbc.Col(
    [
        html.H2('Predicted Diameter:', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        #html.Button('Explain Prediction', id='explain-btn'),
        #html.Div([html.Img(id='shap-img', height=200, width=1000)])
    ],
)

layout = html.Div(
    [
        dbc.Row([column1, column2]),
        dbc.Row(column3)
    ],
)


####BRUNO NOTES#####

def fig_to_uri(in_fig, close_all=True, **save_args):
    """
    Save a figure as a URI
    :param in_fig:
    :return:
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)

@app.callback(
    Output('prediction-content', 'children'),
    [Input('n_obs_used', 'value'), 
     Input('albedo', 'value'),
     Input('classes', 'value'),
     Input('asteroid', 'value')],
)

def predict(n_obs_used, albedo, classes, asteroids):

    #conver input to dataframe
    pred_df = df[df.full_name == asteroids]
    pred_df = pred_df[['orbit_id', 'e', 'a', 'i', 'om', 'w', 'ma', 'n', 'tp', 'moid',
       'moid_jup', 'classes', 'producer', 'data_arc', 'n_obs_used', 'rms',
       'albedo', 'diameter_sigma', 'first_year_obs', 'first_month_obs',
       'last_obs_year', 'last_obs_month']]

    if pred_df.n_obs_used.values[0] != 605:
        pred_df.at[int(pred_df.index.values[0]), 'n_obs_used'] = n_obs_used
    if pred_df.albedo.values[0] != .10:
        pred_df.at[int(pred_df.index.values[0]), 'albedo'] = albedo
    if pred_df.classes.values[0] != 'MBA':
        pred_df.at[int(pred_df.index.values[0]), 'classes'] = classes
    y_pred = pipeline.predict(pred_df)[0]
    return (f'{y_pred:.4f} km')
    

# SHAP INPUT UNCOMMENT ONCE DONE GETTING RUN




# @app.callback(
#     Output('shap-img', 'src'),
#     [Input('explain-btn','n_clicks')],
#     [State('n_obs_used', 'value'), 
#      State('albedo', 'value'),
#      State('classes', 'value'),
#      State('asteroid', 'value')],
# )


# #should arguments be alll the different columns for this as well???
# def explain_png(n_clicks, loan_amnt, int_rate, term, fico_range_high, annual_inc, home_ownership):
    
#     #conver input to dataframe
#     pred_df = df[df.full_name == asteroids]

#     if n_obs_used is not None:
#         pred_df = pred_df.iloc[:,'n_obs_used'] = n_obs_used #google how to overwrite single value in df
#     if albedo is not None:
#         pred_df = pred_df.iloc[:,'albedo'] = albedo
#     if classes is not None:
#         pred_df = pred_df.iloc[:,'classes'] = classes #change class in df to classes b4 train model in pipelin
    

#     # Get steps from pipeline and transform
#     model = pipeline.named_steps['xgbclassifier']
#     encoder = pipeline.named_steps['ordinalencoder']
#     df_processed = encoder.transform(df)
    
#     # Get shapley additive explanations
#     explainer = shap.TreeExplainer(model)
#     shap_values = explainer.shap_values(df_processed)

#     # Plot shapley and save matplotlib plot to base64 encoded buffer for rendering
#     fig = shap.force_plot(
#         base_value=explainer.expected_value, 
#         shap_values=shap_values, 
#         features=df_processed, 
#         show=False,
#         matplotlib=True)
    
#     out_url = fig_to_uri(fig)

#     # Return image
#     return out_url



     