# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image
# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='Methodology - Real Estate In Bangalore',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🗺️ Methodology')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Data Sources


@st.cache()
def get_data(query):
    if query == 'Original_Bangalore':
        return pd.read_csv('Bangalore Data frame/Bengaluru_House_Data.csv')
    return None

# Convert square feet to square meter


def convert_sqft_to_sqm(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0])+float(tokens[1]))/2*0.092903
    try:
        return (float(x)*0.092903)
    except:
        return None

# Neighberhood


def neighborhood(x):
    if x > 887.802859:
        return 'Tier 1'
    elif x > 688.224046:
        return 'Tier 2'
    elif x > 551.693267:
        return 'Tier 3'
    return 'Tier 4'

# Ready or Not Ready


def ready(x):
    if x == 'Ready To Move':
        return x
    return 'Not Ready'


Original_Bangalore = get_data('Original_Bangalore')
Original_Bangalore = Original_Bangalore.drop(['society'], axis='columns')


df = Original_Bangalore.dropna()
df['Number_of_Bedrooms'] = df['size'].apply(lambda x: int(x.split(' ')[0]))
df2 = df.copy()
df2['total_sqm'] = df2['total_sqft'].apply(convert_sqft_to_sqm)
df2['Dollar_Price'] = df2['price'].apply(lambda x: float(x)*1223.80)
df2['price_per_sqm'] = df2['Dollar_Price']/df2['total_sqm']
df2 = df2.drop(['size'], axis='columns')


#################################################################################################
# OutLiners

#
df3 = df2[~(df2['total_sqm']/df2['Number_of_Bedrooms'] < 30)]
df3['neighborhood'] = df3['price_per_sqm'].apply(neighborhood)
df3['availability'] = df3['availability'].apply(ready)


#################################################################################################

st.write("""
We have a strong interest in anything involving machine learning, and the independent project gave us the chance to learn more about it and restate our enthusiasm for it. The ability to produce hypotheses, forecasts, and give machines the capacity to learn on their own is powerful and has an infinite number of potential applications.   
 we have chosen Bangalore Real Estate Forecast as our approach. The goal was to estimate the cost of a particular property using market pricing while taking into account other "features" that would be defined in the following sections. 
  """)
st.info(""" ##### In This Methodology Section you can find: ####

* Data Cleansing
* Machine Learning Model
* Glossary
""")


#################################################################################################

st.write(""" ## Data Cleansing
""")

st.write(""" The statistics were collected from the property prices in Bangalore [Dataset](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) on Kaggle with 13,147 number of properties collected from 2017 to 2020. The information includes many variables such as area_type, availability, location, BHK, society,total_sqft, balconies, bathroom, and price. The cleansing process started with the elimination of null values.As you can see in the image below, 41% of the values for the property society were null, hence the entire column was removed.
""")
st.image(Image.open('Images/society_null.jpg'))

st.write(""" then, cleared all the properties data which some informations were missed and came to 11,841 row with no null value. There some rows with range in area , and some with achre or other units presented. the values with range were replaced with average value ((Start + End)/2) and other units were erased. the price value presented in lakh (100,000 indian rupee) which we convert it to USD price with 1223.80 exchange rate to have better sense of price. The total square feet also converted to square meter.     
we devide the bangalore neighborhoods to 4 equal sections based on price per square meter.(the numbers came from describe command).   
  def neighborhood(x):
    if x > 887.802859:
        return 'Tier 1'
    elif x > 688.224046:
        return 'Tier 2'
    elif x > 551.693267:
        return 'Tier 3'
    return 'Tier 4')  
the whole cleansing and modeling ideas are deprived from https://codebasics.io/. with some little changes in details.

""")
#####################################################
st.write(""" ## Machine Learning Model
""")

st.write(""" The data obtained will be utilized in a machine learning model. We will use K-fold Cross-Validation and the GridSearchCV approach to determine the best method and parameters for the model. to evaluate this we use following model selection based on grid search which deprived from https://codebasics.io/. For this  The linear regression model has been discovered to yield the most favorable outcomes for our data, with a score exceeding 80%, which is quite good. 
""")
st.image(Image.open('Images/best_model_selection.jpg'))

st.write(""" ## Glossary
""")

st.write(""" #### Linear Regression
""")
st.write(""" Linear regression is a machine learning technique that estimates the value of a dependent variable (Y) based on a given independent variable (X). This method creates a relationship between the input (X) and the output (Y) values. Linear regression is a widely recognized and comprehended algorithm in machine learning. There are various models of linear regression, including simple linear regression, ordinary least squares, Gradient Descent, and Regularization.
""")


######################################################
st.write(""" ####  Decision Tree Regression
""")
st.write("""  A tool is used to train a model with a tree structure to make predictions about future data and give meaningful continuous output. The key principles of decision trees, including Maximizing Information Gain, Classification trees, and Regression trees, are involved in the decision tree regression process. The fundamental concept of decision trees is that they are created by repeatedly dividing nodes into child nodes, starting with the parent node or root node. These child nodes can then become parent nodes for their own offspring nodes. To optimize the tree learning method, an objective function is established by identifying the nodes with informative features that maximize information gain.

""")


##########################################################
st.write(""" ####  Regression Tree
""")
st.write(""" The capability of handling both continuous and categorical input variables is a feature of regression trees. Among various machine learning algorithms for regression, the Decision Tree method has the lowest loss and is highly regarded. With an R-Squared value of 0.998, the Decision Tree is considered an excellent model. To accomplish web development, the Decision Tree was utilized.
""")


##########################################################################
st.write(""" ####   Random Forest Regression
""")
st.write(""" Generating a vast number of decision trees is a crucial technique for both classification and regression in machine learning. The fundamentals of decision trees are widely used for a range of machine learning tasks. Using decision trees is essential for data mining, as it remains consistent despite changes in scaling or other factors. To learn complex patterns effectively, the trees are grown to a great depth. Random forest, which involves training multiple deep decision trees on different portions of the same dataset and averaging the results, is a method used to improve accuracy, but it does come with a slight increase in bias and some interoperability issues.
""")
#########################################################################################
