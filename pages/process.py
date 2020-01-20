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
        
            ### Process
            
            ## Trust the Process
            The steps behind setting up Asteroid Diameter Predictor can be broken up into the following tasks: Begin with finding useable data, run a pandas profiling report on the data to garner insight on the variables, clean the data that is not useful for the project, and finally eliminate outliers in the target variable for concise results. Once the data cleaning process is complete the implementation of machine learning models were applied to the data in order to generate statistically backed predictions to real world data.
    
            ## Step 1. Find the Data: 
            This proved to be somewhat difficult when there are not a great deal of clean, accessible datasets out there. This is especially true when dealing with space related content. The best place to find data relating to asteroids or comets can be found at [JPL SSD Query](https://ssd.jpl.nasa.gov/sbdb_query.cgi#x). 

    
            ## Step 2. Run Pandas Profiling Report: 
            This may be a frivolous and time consuming process (my report gook 18 hours to execute), however, it gives incredible insight on the data being used. The pictures below help show the different utilities and information generated from the report.

            Here is an image of the Pandas Profiling Report:
            ![Pandas Profile Report](/Images/pandas-profiling.png)

            Here is an image of the variable descriptions from the report:
            ![Variables](/Images/variables.png)

            Here is an image of the correlations generated via the report:
            ![Correlation](/Images/correlations)

            ## Step 3. Clean the Data: 
            Once the profile report is generated there is all sorts of data cleaning to be done. This involves dropping highly correlated or repeated variables,dropping variables with large amounts of missing values, dropping irrelevant or empty variables, investigate types of variables, and lastly engineer new variables to help strengthen predicative powers.

            ## Step 4. Outlier Elimination: 
            This step is somewhat self-explanatory. The profiling report showed that the target variable was crazy skewed. Using the IQR I was able to get a much cleaner distribution of 'diameter' so that the target data was as concise as possible. There are before and after pictures shown below.

             Here is an image of the Pandas Profiling Report:
            ![Before Outlier Removal](/Images/before-dist-diameter.png)

            Here is an image of the variable descriptions from the report:
            ![After Outlier Removal](/Images/after-dist-diameter.png)


            """
        ),

    ],
)

layout = dbc.Row([column1])