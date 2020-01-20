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
        
            ## Process

            The process behind setting up Asteroid Diameter Predictor can be broken up into the following tasks: Start with finding useable data, run a pandas profiling report on the data, clean the data, and finally eliminate outliers in the target variable. 
            
            Step 1. Find the Data: This proved to be somewhat difficult when there are not a ton of clean, accessible datasets out there. This is especially true when dealing with space related content. 
            
             cleaning nightmare. The dataset was extremely large ( > 850,000 rows) so I had to perform some serious data condensing to upload my files to Github (check 'Conclusion' section for more info on how to circumvent Github's 25 MB upload limit) and use them on Google Colab. Running a pandas profiling report gave me some valuable insight on how to decrease the size, but also took 18 hours 🙃. I started with dropping repeated/highly correlated columns, dropping comet specific data (yes, there is a difference), eliminating outliers in highly skewed columns like the target 'diameter' variable, and dropping high cardinality categorical columns.


            """
        ),

    ],
)

layout = dbc.Row([column1])