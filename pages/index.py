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
        
            ## How will you be murdered?

            Have how you ever wondered how you would be murdered?  Will you be that 69% that will be killed with a gun or will you be that 31% that won't be? 

            This application will allow you to find out the answer to your question...  but do you really want to know?  

            """
        ),
        dcc.Link(dbc.Button('Predict murder weapon', color='primary'), href='/predictions')
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.Img(src='assets/murderpie.png', className='img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])