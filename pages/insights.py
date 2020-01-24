# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ### Feature Importance Table

            The feature importance table is shown below created via the Eli5 library. These correspond to how important each feature is to the prediction of the asteroid's diameter.

            """     ),

        html.Img(src='assets/feature-importance.png', className='img-fluid'),

        dcc.Markdown( """
        Note features with ‘class_###’ or ‘producer_###’ are OneHot Encoded columns for class and producer features. This helps the predictor understand categorical features that may have some cardinality to them.
        """

        ),
    ],
    md=5,
)

column2 = dbc.Col(
    [   
        dcc.Markdown("""
            ### PDP Plot
            The PDP plot below shows the relationship between n_obs_used and the diameter. As shown to the left, 'n_obs_used' or the Number of Observations Used has the largest impact on the prediction of the asteroid's diameter. In this particular relationship, as the observations increase the diameter increases which is interesting to note. This could be due to the fact that the larger the asteroid the more times it can be observed and documented.
            """         ),

        html.Img(src='assets/pdp-plot.png', className='img-fluid'),
        html.Img(src='assets/pdp_albedo.png', className='img-fluid'),



        dcc.Markdown("""
        PDP plots are a great tool for visualizing the impact a feature has on the desired target variable as that feature is increased in value. Some variables produce negative sloping PDP plots like albedo above, resulting in a decrease to the predicted size in diameter. This is interesting to note becuase the higher the albedo means the higher proportion of light reflected through. Thus higher levels of light means the asteroid itself is smaller, which intuitvely makes sense. 
        
        """),
    ],
                )


column3 = dbc.Col(
    [
        dcc.Markdown("""
        ### 2-D PDP Plot
        
        This 2-D PDP plot shows the relationship between the number of observations used in recording the asteroid and the albedo. These are the two most important features from the dataset and show a very clean relationship in the plot. Albedo is defined as “the amount of light reflected from a celestial body”. This is in the form of value between 0 to 1, in which 0 represents total absorption and 1 represents total reflection. These characteristics go hand in hand because the larger the asteroid, the more observations recorded as well as more absorption of light. The more an asteroid allows light through the smaller it is in diameter and thus harder to observe.
        """
                    ),

        html.Img(src='assets/pdp-2-d.png', style={'width':'100%'}),

        dcc.Markdown("""
        ### Shapely Plots

        The Shapely plots are super useful and a great visual aid in understanding how a model makes predictions. The summary plot in the Shapely library gives an overview of the most impactful features on the model outputs.
        """
                    ),

        html.Img(src='assets/shapely-summary.png', style={'width':'100%'}),

        dcc.Markdown("""
     
        The red color is associated with increasing the model predictions as opposed to those in the blue color, which lower the model’s prediction.
         """
                    ),
    ],
     
                )


layout = html.Div(
    [
        dbc.Row([column1, column2]),
        dbc.Row(column3)
    ]
)