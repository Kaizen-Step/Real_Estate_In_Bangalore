# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor


# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='🦾 Price prediction - Real Estate In Bangalore',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🦾 Price prediction ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache(allow_output_mutation=True)
def get_data(query):
    if query == 'Bangalore_revised':
        return pd.read_csv('Data/finalized_Data_frame8.csv')
    return None


def readyn(x):
    if x == "Not Ready":
        return 0
    return 1


Bangalore_revised = get_data('Bangalore_revised')

df2 = Bangalore_revised

###################################################################

# Location Modification call locations less 15 repeatation as other
df2.location = df2.location.apply(lambda x: x.strip())
location_stats = df2['location'].value_counts(ascending=False)
location_stats_less_than_15 = location_stats[location_stats <= 15]

df2.location = df2.location.apply(
    lambda x: 'other' if x in location_stats_less_than_15 else x)

###################################################################

# Availability Modified


df2['availability'] = df2['availability'].apply(readyn)

###################################################################

# Apartment or House

df2['Apartment'] = df2.area_type.apply(
    lambda x: 0 if x == 'Plot  Area' else 1)

#############################################################
# Outliers
# Price Per Square Meter Outlier remover


def Price_per_square_outliers_remover(df):
    df_out = pd.DataFrame()
    for key, subdf in df.groupby('location'):
        m = np.mean(subdf.price_per_sqm)
        st = np.std(subdf.price_per_sqm)
        reduced_df = subdf[(subdf.price_per_sqm > (m-st))
                           & (subdf.price_per_sqm <= (m+st))]
        df_out = pd.concat([df_out, reduced_df], ignore_index=True)
    return df_out


df3 = Price_per_square_outliers_remover(df2)
print(df3.shape)
##############################################################################################
# Make Location Dummies

dummies = pd.get_dummies(df3.location)
df4 = pd.concat([df3, dummies.drop('other', axis='columns')], axis='columns')
df5 = df4.drop('location', axis='columns')

##########################################################

# X and Y defination for Model

X = df5.drop(['price', 'area_type', 'total_sqft', 'price_per_sqm', 'neighborhood',
             'Dollar_Price'], axis='columns')
print(X)

Y = df5.Dollar_Price

#######################################################################

# Linear Regression Model Features

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=10)

Bangalore_Model = LinearRegression()
Bangalore_Model.fit(X_train, Y_train)
Bangalore_Model.score(X_test, Y_test)
cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
cross_val_score(LinearRegression(), X, Y, cv=cv)

print(cross_val_score(LinearRegression(), X, Y, cv=cv))

#############################################################################################
# Interactive wiht User


locations_list = []
for index, value in df2.location.items():
    if value not in locations_list:
        locations_list.append(value)


st.write(""" ## Locations     """)
location = st.selectbox(
    'Please Choose the Neighborhood', options=locations_list)

c1, c2 = st.columns(2)

with c1:

    st.write(""" ## Number of Bedrooms     """)
    Number_of_Bedrooms = st.slider('Please Choose the Number of Bedrooms',
                                   min_value=1, max_value=13, value=2, step=1)

    st.write(""" ## Number of Baths    """)
    bath = st.slider('Please Choose the Number of Baths',
                     min_value=1, max_value=15, value=1, step=1)

    st.write(""" ## Number of Balconies   """)
    balcony = st.slider('Please Choose the Number of Balconies',
                        min_value=0, max_value=4, value=1, step=1)

with c2:
    st.write(""" ## Buidling Type    """)
    building_type = st.selectbox('Please Choose Building Type [Apartment or House]', options=['Apartment', 'House']
                                 )

    st.write(""" ## Total Area in Square Meters    """)
    total_sqm = st.number_input('Please Enter Area number in Square meters ',
                                min_value=35, max_value=5000, value=110, step=1)
    st.write(""" ## Availability      """)
    rready = st.selectbox('Please Choose is the builing availability', options=['Ready to Move', 'Will be Ready Less than 2 Month']
                          )


def convert_apartment(building_type):
    if building_type == 'Apartment':
        return 0
    return 1


def convert_availability(rready):
    if rready == "Ready to Move":
        return 1
    return 0


Apartment = convert_apartment(building_type)

availability = convert_availability(rready)


#################################################################################################

# Predict Function


def predict_price(location, availability, bath, balcony, Number_of_Bedrooms, total_sqm, Apartment):
    loc_index = np.where(X.columns == location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = availability
    x[1] = bath
    x[2] = balcony
    x[3] = Number_of_Bedrooms
    x[4] = total_sqm
    x[5] = Apartment
    if loc_index >= 0:
        x[loc_index] = 1

    return Bangalore_Model.predict([x])[0]


prediction = predict_price(location, availability, bath,
                           balcony, Number_of_Bedrooms, total_sqm, Apartment)

st.write(round(prediction, 2))
###################################################################################################
