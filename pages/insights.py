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
        
            ## Insights

            The feature importance table is shown below created via the Eli5 library. These correspond to how important each feature is to the prediction of the asteroid's diameter.
            
            html.Img(src='assets/feature-importance.png', className='img-fluid')

            The PDP plot below shows the relationship between n_obs_used and the diameter. As the observations increase the diameter increases which is interesting to note. This could be due to the fact that the larger the asteroid the more times it can be observed and documented.

            html.Img(src='assets/pdp-plot.png', className='img-fluid')

            """
        ),
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

 column2 = dbc.Col(
     [
     dcc.Markdown(
         """


        This 2-D PDP plot shows the relationship between the number of observations used in recording the asteroid and the albedo. These are the two most important features from the dataset and show a very clean relationship in the plot. Albedo is defined as “the amount of light reflected from a celestial body”. This is in the form of value between 0 to 1, in which 0 represents total absorption and 1 represents total reflection. These characteristics go hand in hand because the larger the asteroid, the more observations recorded as well as more absorption of light. The more an asteroid allows light through the smaller it is in diameter and thus harder to observe.
    
        html.Img(src='assets/pdp-2-d.png', className='img-fluid')

        The Shapely plots are super useful and a great visual aid in understanding how a model makes predictions. The summary plot in the Shapely library gives an overview of the most impactful features on the model outputs.

        html.Img(src='assets/shapely-summary', className='img-fluid')

        The red color is associated with increasing the model predictions as opposed to those in the blue color, which lower the model’s prediction.

    
            """),
     ],
     md=4,
 )

layout = dbc.Row([column1, column2])