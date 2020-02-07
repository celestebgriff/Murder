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

            **The Question:**

            In today's day and age, murder has become more involved in our daily lives we see it in the news, crime shows, documentaries, etc. I admit that I have found a love for these crime shows. But it leads me to question, how many people are murdered by guns as we see in the news every day or by the more "creative" ways that we all see on the crime shows? Which one is more accurately showing how real people are murdered? The question I choose to look at is:  **Will a murder committed with a gun?**

            **What was my target?**

            When looking through the data I found, I choose to focus on the murder weapon specifically spitting the data into "Gun" or "Other".  For the gun, this includes all types of guns, but interestingly 50% of all murders were committed with Handguns.  Other, of course, is a large category that ranges greatly.  Below I have added all the possible other categories:
            
            -Blunt Object

            -Strangulation

            -Knife

            -Fall

            -Drowning

            -Suffocation

            -Explosives

            -Fire

            -Drugs

            -Poison

            **Regression or classification?**

            I used classification for the data since this data is categorical.  I can't use a regression model since this type of model requires numerical data.


            **Why I decided to predict accuracy:**

            Upon exploring my data set I found that the gun was the majority class, occurring 69.5% of the time.  Because this number falls between the range of 50%-70% I choose to use accuracy as my evaluation metric. When a number falls outside the range 50%-70%, the accuracy can become increasingly misleading. 
                
            **Baseline:**

            A baseline is the result of simple summary statistics, simple models, or randomness.  From this, we can establish a starting point for our evaluation metric, in this case: accuracy.  From the baseline, you'll want to build more and more complex models to improve your evaluation metric score. For this case, I choose the majority case baseline because I had already chosen to find accuracy and these two are closely linked as mentioned in the accuracy section.

            **Why is it useful?**

            This application could be used for somebody who studies the psychology of murders as it depicts the factors that could affect how perpetrator choices their method of murder.  I chose this model because I thought it would be fun since I love true crime shows.


            """
        ),

    ],
)

layout = dbc.Row([column1])