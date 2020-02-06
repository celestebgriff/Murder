# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
import pandas as pd
# Imports from this application
from app import app

# Load pipeline
from joblib import load
pipeline = load('assets/pipeline.joblib')
print('Pipeline loaded!')

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Year', 'value'),
     Input('VictimAge', 'value'),
     Input('VictimCount', 'value'),
     Input('PerpetratorCount', 'value'),
     Input('AgencyType', 'value'),
     Input('State', 'value'),
     Input('Month', 'value'),
     Input('CrimeSolved', 'value'),
     Input('VictimSex', 'value'),
     Input('VictimRace', 'value'),
     Input('VictimEthnicity', 'value'),
     Input('PerpetratorSex', 'value'),
     Input('PerpetratorRace', 'value'),
     Input('PerpetratorEthnicity', 'value'),
     Input('Relationship', 'value'),],
)
def predict(Year, VictimAge, VictimCount, PerpetratorCount, AgencyType,
State, Month, CrimeSolved, VictimSex, VictimRace,
VictimEthnicity, PerpetratorSex, PerpetratorRace, PerpetratorEthnicity, Relationship):
    df = pd.DataFrame(
        columns=['Year', 'VictimAge', 'VictimCount', 'PerpetratorCount',
        'AgencyType', 'State', 'Month', 'CrimeSolved',
        'VictimSex', 'VictimRace', 'VictimEthnicity', 'PerpetratorSex',
        'PerpetratorRace', 'PerpetratorEthnicity', 'Relationship'], 
        data=[[Year, VictimAge, VictimCount, PerpetratorCount, AgencyType,
        State, Month, CrimeSolved, VictimSex, VictimRace,
        VictimEthnicity, PerpetratorSex, PerpetratorRace, PerpetratorEthnicity, Relationship]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f}'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
    dcc.Markdown('Year'),
    dcc.Slider(
        id='Year',
        min=1980,
        max=2014,
         marks={
        1980: '1980',
        1985: '1985',
        1990: '1990',
        1995: '1995',
        2000: '2000',
        2005: '2005',
        2010: '2010',
        },
        value=1990
    ),
    dcc.Markdown('Victim Age'),
    dcc.Slider(
        id='VictimAge',
        min=1,
        max=100,
        marks={
        10: '10',
        20: '20',
        30: '30',
        40: '40',
        50: '50',
        60: '60',
        70: '70',
        80: '80',
        90: '90',
        100: '100'
        },
        value=50
    ),
    dcc.Markdown('Victim Count'),
    dcc.Slider(
        id='VictimCount',
        min=1,
        max=10,
        marks={i: '{}'.format(i) for i in range(11)},
        value=5
    ),
    dcc.Markdown('Perpetrator Count'),
    dcc.Slider(
        id='PerpetratorCount',
        min=1,
        max=10,
        marks={i: '{}'.format(i) for i in range(11)},
        value=5
    ),
    dcc.Markdown('Agency Type'),
    dcc.Dropdown(
        id='AgencyType',
        options=[
            {'label': 'Municipal Police', 'value': 'Municipal Police'},
            {'label': 'Sheriff', 'value': 'Sheriff'},
            {'label': 'State Police', 'value': 'State Police'},
            {'label': 'Special Police', 'value': 'Special Police'},
            {'label': 'Tribal Police', 'value': 'Tribal Police'},
            {'label': 'Regional Police', 'value': 'Regional Police'},
            {'label': 'County Police', 'value': 'County Police'}
        ],
        value='State Police'
    ), 
    dcc.Markdown('State'),
    dcc.Dropdown(
        id='State',
        options=[
            {'label': 'Alabama', 'value': 'Alabama'},
            {'label': 'West Virginia', 'value': 'West Virginia'},
            {'label': 'California', 'value': 'California'},
            {'label': 'North Carolina', 'value': 'North Carolina'},
            {'label': 'Illinois', 'value': 'Illinois'},
            {'label': 'Wisconsin', 'value': 'Wisconsin'},
            {'label': 'Florida', 'value': 'Florida'},
            {'label': 'Texas', 'value': 'Texas'},
            {'label': 'New York', 'value': 'New York'},
            {'label': 'Virginia', 'value': 'Virginia'},
            {'label': 'District of Columbia', 'value': 'District of Columbia'},
            {'label': 'Pennsylvania', 'value': 'Pennsylvania'},
            {'label': 'Ohio', 'value': 'Ohio'},
            {'label': 'Connecticut', 'value': 'Connecticut'},
            {'label': 'Oklahoma', 'value': 'Oklahoma'},
            {'label': 'Maryland', 'value': 'Maryland'},
            {'label': 'Georgia', 'value': 'Georgia'},
            {'label': 'Louisiana', 'value': 'Louisiana'},
            {'label': 'Indiana', 'value': 'Indiana'},
            {'label': 'Washington', 'value': 'Washington'},
            {'label': 'Michigan', 'value': 'Michigan'},
            {'label': 'New Jersey', 'value': 'New Jersey'},
            {'label': 'Montana', 'value': 'Montana'},
            {'label': 'South Carolina', 'value': 'South Carolina'},
            {'label': 'Alaska', 'value': 'Alaska'},
            {'label': 'Tennessee', 'value': 'Tennessee'},
            {'label': 'Missouri', 'value': 'Missouri'},
            {'label': 'Mississippi', 'value': 'Mississippi'},
            {'label': 'Arizona', 'value': 'Arizona'},
            {'label': 'Nevada', 'value': 'Nevada'},
            {'label': 'Colorado', 'value': 'Colorado'},
            {'label': 'Kentucky', 'value': 'Kentucky'},
            {'label': 'Maine', 'value': 'Maine'},
            {'label': 'Arkansas', 'value': 'Arkansas'},
            {'label': 'Massachusetts', 'value': 'Massachusetts'},
            {'label': 'Delaware', 'value': 'Delaware'},
            {'label': 'Oregon', 'value': 'Oregon'},
            {'label': 'Minnesota', 'value': 'Minnesota'},
            {'label': 'Idaho', 'value': 'Idaho'},
            {'label': 'Iowa', 'value': 'Iowa'},
            {'label': 'New Mexico', 'value': 'New Mexico'},
            {'label': 'New Hampshire', 'value': 'New Hampshire'},
            {'label': 'Vermont', 'value': 'Vermont'},
            {'label': 'Hawaii', 'value': 'Hawaii'},
            {'label': 'Utah', 'value': 'Utah'},
            {'label': 'Kansas', 'value': 'Kansas'},
            {'label': 'Nebraska', 'value': 'Nebraska'},
            {'label': 'South Dakota', 'value': 'South Dakota'},
            {'label': 'Rhode Island', 'value': 'Rhodes Island'},
            {'label': 'Wyoming', 'value': 'Wyoming'},
            {'label': 'North Dakota', 'value': 'North Dakota'}

        ],
        value='Alabama'
    ),
    dcc.Markdown('Month'),
    dcc.Dropdown(
        id='Month',
        options=[
            {'label': 'January', 'value': 'January'},
            {'label': 'February', 'value': 'February'},
            {'label': 'March', 'value': 'March'},
            {'label': 'April', 'value': 'April'},
            {'label': 'May', 'value': 'May'},
            {'label': 'June', 'value': 'June'},
            {'label': 'July', 'value': 'July'},
            {'label': 'August', 'value': 'August'},
            {'label': 'September', 'value': 'September'},
            {'label': 'October', 'value': 'October'},
            {'label': 'November', 'value': 'November'},
            {'label': 'December', 'value': 'December'}
        ],
        value='May'
    ),

    dcc.Markdown('Crime Solved'),
    dcc.Dropdown(
        id='CrimeSolved',
        options=[
            {'label': 'Yes', 'value': 'Yes'},
            {'label': 'No', 'value': 'No'}
        ],
        value='Yes'
    ), 


    dcc.Markdown('Victim Sex'),
    dcc.Dropdown(
        id='VictimSex',
        options=[
            {'label': 'Male', 'value': 'Male'},
            {'label': 'Female', 'value': 'Female'}
        ],
        value='Male'
    ),
    dcc.Markdown('Victim Race'),
    dcc.Dropdown(
        id='VictimRace',
        options=[
            {'label': 'White', 'value': 'White'},
            {'label': 'Black', 'value': 'Black'},
            {'label': 'Asian/Pacific Islander', 'value': 'Asian/Pacific Islander'},
            {'label': 'Native American/Alaska Native', 'value': 'Native American/Alaska Native'}
        ],
        value='White'
    ),
    dcc.Markdown('Victim Ethnicity'),
    dcc.Dropdown(
        id='VictimEthnicity',
        options=[
            {'label': 'Not Hispanic', 'value': 'Not Hispanic'},
            {'label': 'Hispanic', 'value': 'Hispanic'}
        ],
        value='Not Hispanic'
    ),
    dcc.Markdown('Perpetrator Sex'),
    dcc.Dropdown(
        id='PerpetratorSex',
        options=[
            {'label': 'Male', 'value': 'Male'},
            {'label': 'Female', 'value': 'Female'}
        ],
        value='Male'
    ),
    dcc.Markdown('Perpetrator Race'),
    dcc.Dropdown(
        id='PerpetratorRace',
        options=[
            {'label': 'White', 'value': 'White'},
            {'label': 'Black', 'value': 'Black'},
            {'label': 'Asian/Pacific Islander', 'value': 'Asian/Pacific Islander'},
            {'label': 'Native American/Alaska Native', 'value': 'Native American/Alaska Native'}
        ],
        value='White'
    ),
    dcc.Markdown('Perpetrator Ethnicity'),
    dcc.Dropdown(
        id='PerpetratorEthnicity',
        options=[
            {'label': 'Not Hispanic', 'value': 'Not Hispanic'},
            {'label': 'Hispanic', 'value': 'Hispanic'}
        ],
        value='Not Hispanic'
    ),
    dcc.Markdown('Relationship'),
    dcc.Dropdown(
        id='Relationship',
        options=[
            {'label': 'Girlfriend', 'value': 'Girlfriend'},
            {'label': 'Husband', 'value': 'Husband'},
            {'label': 'Friend', 'value': 'Friend'},
            {'label': 'Acquaintance', 'value': 'Acquaintance'},
            {'label': 'Stranger', 'value': 'Stranger'},
            {'label': 'Family', 'value': 'Family'},
            {'label': 'Boyfriend', 'value': 'Boyfriend'},
            {'label': 'Sister', 'value': 'Sister'},
            {'label': 'Daughter', 'value': 'Daughter'},
            {'label': 'Son', 'value': 'Son'},
            {'label': 'Common-Law Husband', 'value': 'Common-Law Husband'},
            {'label': 'Wife', 'value': 'Wife'},
            {'label': 'Father', 'value': 'Father'},
            {'label': 'Ex-Wife', 'value': 'Ex-Wife'},
            {'label': 'Brother', 'value': 'Brother'},
            {'label': 'Neighbor', 'value': 'Neighbor'},
            {'label': 'Employee', 'value': 'Employee'},
            {'label': 'In-Law', 'value': 'In-Law'},
            {'label': 'Employer', 'value': 'Employer'},
            {'label': 'Stepson', 'value': 'Stepson'},
            {'label': 'Common-Law Wife', 'value': 'Common-Law Wife'},
            {'label': 'Stepfather', 'value': 'Stepfather'},
            {'label': 'Boyfriend/Girlfriend', 'value': 'Boyfriend/Girlfriend'},
            {'label': 'Ex-Husband', 'value': 'Ex-Husband'},
            {'label': 'Stepdaughter', 'value': 'Stepdaughter'},
            {'label': 'Mother', 'value': 'Mother'},
            {'label': 'Stepmother', 'value': 'Stepmother'}
        ],
        value='Friend'
    )

    ],
    md=6,
)

column2 = dbc.Col(
[
        html.H2('Murder Weapon', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])