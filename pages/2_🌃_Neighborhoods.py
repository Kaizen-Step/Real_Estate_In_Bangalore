# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from geopy.geocoders import Nominatim
import streamlit.components.v1 as components

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title=' Neighborhoods - Real Estate In Bangalore',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌃 Neighborhoods')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache(allow_output_mutation=True)
def get_data(query):
    if query == 'Neighborhood_orginal':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/Neighborhoods/Neighborhood.csv')
    elif query == 'average_neighborhood':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/Neighborhoods/Average_neighborhood3.csv')
    elif query == 'Total_Neighborhood':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/Neighborhoods/total_neighborhood_averages.csv')
    elif query == 'Number_of_Luxuries_houses':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/Neighborhoods/Number_of_Luxuries_houses.csv')
    elif query == 'loc_bang':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/Locations/Bangalore_Locations3.csv')
    return None


Neighborhood_orginal = get_data('Neighborhood_orginal')
average_neighborhood = get_data('average_neighborhood')
Total_Neighborhood = get_data('Total_Neighborhood')
Number_of_Luxuries_houses = get_data('Number_of_Luxuries_houses')
loc_bang = get_data('loc_bang')

df = Neighborhood_orginal
df2 = average_neighborhood
df3 = Total_Neighborhood
df4 = Number_of_Luxuries_houses[(
    Number_of_Luxuries_houses['location'] != 'other')]
df5 = loc_bang

# Location Modification call locations less 15 repeatation as other
df.location = df.location.apply(lambda x: x.strip())
location_stats = df['location'].value_counts(ascending=False)
location_stats_less_than_15 = location_stats[location_stats <= 15]

df.location = df.location.apply(
    lambda x: 'other' if x in location_stats_less_than_15 else x)

st.map(df5)


#################################################################################################
st.write(""" ### Neighborhood Impact on Real Estates ##  """)

st.write("""
 Have you ever wondered why some neighborhoods have higher real estate prices than others? It turns out that the neighborhood you live in can have a significant impact on the value of your home. From the quality of schools to nearby amenities and even the crime rate, various factors can influence real estate prices. In this context, understanding how your neighborhood impacts your home's value can help you make informed decisions when buying or selling real estate.   

  """)


st.info(""" ##### In This Neighborhood Section you can find: ####

* Hollywood Yearly Gorss Revenue [USD]
* Hollywood Yearly Gross Change Rate
* Number of Movie Released in Hollywood each Year  
* Average Gross per Release   
* Each year, the top-selling movie [detailed table]



""")


#################################################################################################


#####################################################
st.write(""" ## Bangalore Total Neighborhoods """)

st.write("""  As of 2021, the population of Bangalore city is approximately 12.3 million. The area of Bangalore city is approximately 709 square kilometers (274 square miles). there are 1159 different neighborhoods in our data set, you can see the average price per square meter for each of these neighborhoods as following.

 """)

# Different Neighborhood price per square metere
fig = px.area((df3.sort_values(by='price_per_sqm', ascending=False)), x="location", y="price_per_sqm",
              title='Different Neighborhood Price per square meter [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Price per square meter [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    # Different Neighborhood Average Area
    fig = px.area((df3.sort_values(by='total_sqft', ascending=False)), x="location", y="total_sqft",
                  title='Different Neighborhood Average Area')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Total Area [Square Meter]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Different Neighborhood Average Area
    fig = px.area((df3.sort_values(by='Dollar_Price', ascending=False)), x="location", y="Dollar_Price",
                  title='Different Neighborhood Average Price [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Average Price [Square Meter]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Bangalore Neighborhood Zoom in """)

st.write("""  it is little bit hard to apprehend the information of 1159 different neighborhoods at one chart. So we focused on 159 neighborhoods that has the most number of building information in our data set. the first reason for this is talk about neiborhoods that we have enough information to talk about them accouratly. All the neighborhoods presented here have at least 15 individual building info in our data sets . offcourse all the optimum figures presented in this section are come from Bangalore total neighborhoods data frame. 

 """)


# Different Neighborhood price per square metere
fig = px.bar((df2.sort_values(by='price_per_sqm', ascending=False)), x="location", y="price_per_sqm", color="location",
             title='Different Neighborhood Price per square meter [USD]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Price per square meter [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    # Different Neighborhood Average Area
    fig = px.area((df3.sort_values(by="total_sqft", ascending=False)), x="location", y="total_sqft",
                  title='Different Neighborhood Average Area')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Total Area [Square Meter]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Different Neighborhood Average Area
    fig = px.area((df2.sort_values(by='Dollar_Price', ascending=False)), x="location", y="Dollar_Price",
                  title='Different Neighborhood Average Price [USD]')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Total Price [USD]')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" ## Number of Big luxarios house in each Neighborhoods""")

st.write("""  it is little bit hard to apprehend the information of 1159 different neighborhoods at one chart. So we focused on 159 neighborhoods that has the most number of building information in our data set. the first reason for this is talk about neiborhoods that we have enough information to talk about them accouratly. All the neighborhoods presented here have at least 15 individual building info in our data sets . offcourse all the optimum figures presented in this section are come from Bangalore total neighborhoods data frame. 

 """)

# Different Neighborhood Average Area
fig = px.bar((df4.sort_values(by='area_type', ascending=False)), x="location", y="area_type", color="location",
             title='Number of Big Luxuries Houses in each location')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Luxuries Houses')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* As a result of the COVID-19 pandemic, the Hollywood annual gross dropped from \$11.36 billion in 2019 to \$2.11 billion in 2020
* Annual gross has steadily increased, reaching nearly \$7.36 billion in 2022—a more than 112% increase in a single year.
* Since 2000, the number of movies released has continuously risen, with 2018 seeing a record-breaking 993 movies released in a single year
* The total gross fell by 82% in 2020 while the number of movies released fell by 44%.
* Each movie's average gross revenue rose from \$12 million in 2019 to \$14.84 million in 2022.

""")
