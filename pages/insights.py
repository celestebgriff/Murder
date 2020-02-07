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



            """
        ),
        dcc.Markdown(
            """
        
            **My Baseline:**

            I first started by finding the majority class. This told me that gun was used the majority of the time.  I then guessed gun for each prediction and found the accuracy score. This gave me a majority class baseline of 69% for the accuracy of the model.

            **Linear Model:**

            For my first model, I choose a linear model.  The linear model I choose was a logistic regression cv model.  After running it found that it did better than the majority class baseline, earning a score of 72.6% for the validation set. This is a 3.6% increase.  I didn't feel that this was a high enough percentage so I continued. I felt like a tree-based model would be the next best model to try as it is more complex.
            
            **Tree-Based Model:**

            The tree-based model I choose to use was a random forest classifier.  It did better than the baseline and the linear model earning an accuracy score of 74%. This is an increase of 1.4%.  To increase the complexity once again I decided to do an XGBClassifier to see if I could improve the accuracy score further. 

            **XGBClassifier:**

            Using the XGBClassifer and got a validation score of 75%. This is an increase of 1%.  Since this was my best model I decided to use this to find my test accuracy.  The test accuracy turned out to be the same as the validation accuracy which was 75%.

            In the graph pictured below, I decided to do a partial dependence plot to show how the year impacted the model.  I was curious if the year would affect because of the large range in years, this also why I choose to do a random train test split.  I assumed that as time went on gun usage would increase but instead I found the opposite.  While the data is not extremely significant it shows that as the years progress a gun is less likely to be used as a murder weapon. 
            
            """
        ),
        html.Img(src='assets/yearpdp.png', className='img-fluid'),
        
        dcc.Markdown(
            """
        
            I was curious about how the number of perpetrators would affect the model.   I found that as the number of perpetrators increases there is a slight decrease in the chance that a gun will be used to commit the murder.

            """
        ),
        html.Img(src='assets/perpdp.png', className='img-fluid'),
        
        dcc.Markdown(
            """
        
            I was also curious about how the number of victims would affect the model.  I decided to create a partial dependence plot which is shown below. The plot shows that as the number of victims increases the more likely a gun will be used to commit the murder.

            """
        ),
        html.Img(src='assets/vicpdp.png', className='img-fluid'),
       
        dcc.Markdown(
            """
        
            I decided to do a partial dependence plot that directly compares how perpetrator count and victim count affect the model. It shows that as perpetrator count decreases and victim count increases, you're more likely to use a gun to commit a murder.  However, it also shows that victim count effects the model far greater than the perpetrator count.

            """
        ),
        html.Img(src='assets/vicperpdp.png', className='img-fluid'),
        
        dcc.Markdown(
            """
        
            A confusion matrix shows how a model performed it does this by showing how many times its predictions were correct or incorrect for each category. My confusion matrix shows that I correctly predicted that a gun was used 99,125 times and the category other was predicted correctly 14,127 times. Additionally, the other method was predicted 6,107 times when the murder weapon was committed with a gun.  The model also predicted a gun was used 31,957 times when the category other was used to commit the murder. From this, I can see that my model partially struggled with falsely predicted a gun, which is the second-highest number in my matrix.

            """
        ),
        html.Img(src='assets/murderconfusion.png', className='img-fluid'),
        
        dcc.Markdown(
            """
        
            It's interesting to see the ways that murder is committed especially in comparison to the ways that we see it on shows, news and in the movies.  While the majority of murders today are committed by guns, it is alarming to see the people are beginning more "creative" in their murders, using other methods more often than in past years. 
            
            """
        )
    ],
)

layout = dbc.Row([column1])