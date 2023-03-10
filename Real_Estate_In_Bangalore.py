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
from PIL import Image

# Layout
st.set_page_config(page_title=' Real Estate In Bangalore',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Real Estate in Bangalore 🏛️')

st.text(" \n")


@st.cache(allow_output_mutation=True)
def get_data(query):
    if query == 'Bangalore_revised':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/finalized_Data_frame8.csv')
    elif query == 'loc_bang':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/Locations/Bangalore_Locations3.csv')
    return None


def readyn(x):
    if x == "Not Ready":
        return 0
    return 1


Bangalore_revised = get_data('Bangalore_revised')
loc_bang = get_data('loc_bang')


df2 = Bangalore_revised
df11 = loc_bang
####################################################################################
# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/housse4.jpg'))

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/House2.jpg'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/House3.jpg'))

st.write("""## Own Your Dream House ##

Imagine a house that is more than just a structure with four walls and a roof. A dream house is a place where you can escape from the chaos of everyday life and feel truly at home. It is a space where you can relax, unwind, and make memories that will last a lifetime. Your dream house is uniquely yours, tailored to your personal tastes and preferences. It is designed to meet your needs and cater to your lifestyle. Whether you prefer modern minimalism or a cozy cottage, your dream house reflects your individuality. Perhaps your dream house is perched on a hilltop with breathtaking views of the countryside. Maybe it's nestled among towering trees in a secluded forest. Or, it could be a sleek, urban high-rise with panoramic views of the city skyline. Inside, your dream house is a haven of comfort and luxury. It features the latest in technology and amenities, from state-of-the-art home automation systems to spa-like bathrooms and gourmet kitchens. Every detail has been carefully considered to create a space that is not only beautiful but functional. The living room is the heart of your dream house, where you can gather with family and friends to relax and entertain. It is warm and inviting, with plush seating, cozy blankets, and a fireplace to set the mood. The dining room is equally elegant, with a stunning table and chairs that are perfect for hosting dinner parties and holiday gatherings.
Acquiring your dream house can be a thrilling and rewarding experience. It takes a combination of planning, patience, and persistence to make your dream a reality. Whether it's saving up for a down payment, researching different neighborhoods, or working with a real estate agent, taking intentional steps towards your goal can help you find the perfect place to call home. With this dashboard, we've done our best to make your journey through your dream easier by employing sophisticated machine learning tools and a massive data set.









""")
######################################################

st.write("""
## Real Estate Price Prediction Application In Bangalore ##
Real Estate Price Prediction Application is a software tool that utilizes machine learning algorithms to forecast the future prices of properties in Bangalore, India. The application is designed to analyze various factors that influence the real estate market, such as location, area, number of bedrooms and Building type of the property, and provide accurate predictions of the property's future value. Bangalore is one of India's fastest-growing cities, with a thriving real estate market that attracts investors and homebuyers alike. By using this application, users can make informed decisions about buying or selling properties in Bangalore and maximize their returns on investment.
 """)
#####################################################################################
st.map(df11)
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


c1, c2 = st.columns(2)

with c2:

    st.write(""" ### Number of Bedrooms     """)
    Number_of_Bedrooms = st.slider('Please Choose the Number of Bedrooms',
                                   min_value=1, max_value=13, value=2, step=1)

    st.write(""" ### Number of Baths    """)
    bath = st.slider('Please Choose the Number of Baths',
                     min_value=1, max_value=15, value=1, step=1)

    st.write(""" ### Number of Balconies   """)
    balcony = st.slider('Please Choose the Number of Balconies',
                        min_value=0, max_value=4, value=1, step=1)

with c1:

    st.write(""" ### Locations     """)
    location = st.selectbox(
        'Please Choose the Neighborhood', options=locations_list, index=11)

    st.write(""" ### Buidling Type    """)
    building_type = st.selectbox('Please Choose Building Type [Apartment or House]', options=['Apartment', 'House']
                                 )

    st.write(""" ### Total Area in Square Meters    """)
    total_sqm = st.number_input('Please Enter Area number in Square meters ',
                                min_value=35, max_value=5000, value=110, step=1)


rready = 'Ready to Move'


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

round_predction = round(prediction, 2)

############################################################################################################
c1, c2, c3 = st.columns(3)


with c1:
    st.markdown(
        f""" ### 🔮 Your Dream House Price Would Be:  """)
    st.image(Image.open('Images/Codes2.jpg'))
# with c2:
#     st.text(" \n")
#     st.text(" \n")
#     st.text(" \n")
#     st.text(" \n")

#     st.image(Image.open('Images/ba.jpg'))


with c3:
    st.info(
        f""" ###       {round_predction}\$   """)

    if Apartment == 0:
        if round_predction > 500000:
            st.image(Image.open('Images/apartmentluxury.jpg'), width=500)
        elif round_predction > 400000:
            st.image(Image.open('Images/apartment2.jpg'), width=500)
        elif round_predction > 300000:
            st.image(Image.open('Images/apartment3.jpg'), width=500)
        elif round_predction > 200000:
            st.image(Image.open('Images/apartment4.jpg'), width=500)
        elif round_predction > 10000:
            st.image(Image.open('Images/apartment5.jpg'), width=500)
    elif Apartment == 1:
        if round_predction > 500000:
            st.image(Image.open('Images/houseluxury.jpg'), width=500)
        elif round_predction > 400000:
            st.image(Image.open('Images/h2.jpg'), width=500)
        elif round_predction > 300000:
            st.image(Image.open('Images/h3.jpg'), width=500)
        elif round_predction > 200000:
            st.image(Image.open('Images/h4.jpg'), width=500)
        elif round_predction > 10000:
            st.image(Image.open('Images/h5.jpg'), width=500)

##################################################################################################################


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")

with c2:
    st.info(
        '**Project Github:  [Real Estate In Bangalore](https://github.com/Kaizen-Step/Hollywood_Box_Office_Tragedy)**', icon="💻")
