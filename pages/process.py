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

            ### Trust the Process
            The steps behind setting up Asteroid Diameter Predictor can be broken up into the following tasks: Begin with finding useable data, run a pandas profiling report on the data to garner insight on the variables, clean the data that is not useful for the project, and lastly eliminate outliers in the target variable for concise results. That completes the data cleaning process. Next, implementation of machine learning models were applied to the data in order to generate statistically backed predictions to real world data. Finally, results and accuracy were tested on the different models to find the best predictions.
    
            ### Step 1. Find the Data: 
            This proved to be somewhat difficult when there are not a great deal of clean, accessible datasets out there. This is especially true when dealing with space related content. The best place to find data relating to asteroids or comets can be found at JPL SSD Query(https://ssd.jpl.nasa.gov/sbdb_query.cgi#x). 

    
            ### Step 2. Run Pandas Profiling Report: 
            This may be a frivolous and time consuming process (my report gook 18 hours to execute), however, it gives incredible insight on the data being used. The pictures below help show the different utilities and information generated from the report. Here is an image of the Pandas Profiling Report:
            """
            html.Img(src='assets/pandas-profile.png', style={'width':'100%'})
           
            """
            Here is an image of the variable descriptions from the report:
            """

            html.Img(src='assets/variables.png', style={'width':'100%'})

            """
            Here is an image of the correlations generated via the report:
            """

            html.Img(src='assets/correlations.png', style={'width':'100%'})

            """
            ### Step 3. Clean the Data: 
            Once the profile report is generated there is all sorts of data cleaning to be done. This involves dropping highly correlated or repeated variables,dropping variables with large amounts of missing values, dropping irrelevant or empty variables, investigate types of variables, and lastly engineer new variables to help strengthen predicative powers.

            ### Step 4. Outlier Elimination: 
            This step is somewhat self-explanatory. The profiling report showed that the target variable was crazy skewed. Using the IQR I was able to get a much cleaner distribution of 'diameter' so that the target data was as concise as possible. There are before and after pictures shown below. Here is an image of the distribution of the target variable before and after outlier elimination:

            """
             html.Img(src='assets/before-dist-diameter.png', style={'width':'100%'})

            html.Img(src='assets/after-dist-diameter.png', style={'width':'100%'})

            """
            ### Step 5. Model Implementation:
            This step involves putting together the different models. The five core models were as follows: Baseline model, Linear Regression Model, Deceision Tree Regressor, Random Forest Regressor, and XGBoost Regressor. The best model after hyper-parameter optimization was the Random Forest Regressor. The snippet of code below shows the implementation of the model.
            """
            html.Img(src='assets/random-forest-regressor.png', style={'width':'100%'})

            """
            ### Step 6. Model Results:
            The results and errors are shown for each of the five models in the image below:
            """
            html.Img(src='assets/results.png', style={'width':'100%'})
        ),

    ],
)

layout = dbc.Row([column1])