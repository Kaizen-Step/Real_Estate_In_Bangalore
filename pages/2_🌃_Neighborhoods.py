# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import altair as alt

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
    elif query == 'bedrooms_bathroom_orginal':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/Bedrooms_Bathrooms/Bedrooms_Bathrooms.csv')
    return None


Neighborhood_orginal = get_data('Neighborhood_orginal')
average_neighborhood = get_data('average_neighborhood')
Total_Neighborhood = get_data('Total_Neighborhood')
Number_of_Luxuries_houses = get_data('Number_of_Luxuries_houses')
loc_bang = get_data('loc_bang')
bedrooms_bathroom_orginal = get_data('bedrooms_bathroom_orginal')


df = Neighborhood_orginal
df2 = average_neighborhood
df3 = Total_Neighborhood
df4 = Number_of_Luxuries_houses[(
    Number_of_Luxuries_houses['location'] != 'other')]
df5 = loc_bang

df11 = bedrooms_bathroom_orginal
df12 = df11[(df11['Number_of_Bedrooms'] <= 3)]
df13 = df11[(df11['Number_of_Bedrooms'] >= 4)]
df14 = df13[(df13['Dollar_Price'] >= 500000)]

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

* Bangalore Total Neighborhoods
* Top 159 Neighborhoods based on number of available properties  
* Ordinary Neighborhoods Number of bedrooms to house price Scatter Plot  
* Number of Big luxarios house in each Neighborhoods  
* Luxuries Houses Scatter Plot




""")


#################################################################################################


#####################################################
st.write(""" ## Bangalore Total Neighborhoods """)

st.write("""  Bangalore, also known as Bengaluru, is the capital city of the southern Indian state of Karnataka. With a population of over 12 million people, it is the third-most populous city in India. The city covers an area of approximately 741 square kilometers and is divided into various neighborhoods or localities, such as Koramangala, Indiranagar, Jayanagar, Malleshwaram, and Whitefield. Each neighborhood has its own unique culture and vibe, making Bangalore a diverse and vibrant city. you can see the average price per square meter for each of these neighborhoods as following. Raghuvanahalli ranked first in price per square meter, Raghuvanahalli is a quiet and peaceful residential neighborhood located in South Bangalore. It is situated near the Kanakapura Main Road, which provides easy access to the city's major hubs. The area is known for its greenery and is surrounded by several parks and open spaces, making it a popular destination for morning walks and jogging.

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

st.write(""" ## Ordinary Neighborhoods Number of bedrooms to house price Scatter Plot """)

st.write(""" The scatter plot showing the number of bedrooms in each neighborhood in relation to its price is shown. as well as the distribution of bedrooms across the property. The most popular properties in Bangalore are those with four and three rooms. the most expensive property in region worth 3.5 million dollar which has 4 bedrooms and located in Indiranagar neighborhood.
""")


source = df11
chart = alt.Chart(source).mark_circle().encode(
    x='Dollar_Price',
    y='Number_of_Bedrooms',
    color='Dollar_Price',
).interactive()

st.altair_chart(chart, theme="streamlit", use_container_width=True)


st.write(""" ## Number of Big luxarios house in each Neighborhoods""")

st.write("""  Bangalore, is home to some of the most luxurious neighborhoods in India. One such neighborhood is the upscale area of Indiranagar. Located in the heart of the city, Indiranagar is known for its tree-lined streets, beautiful parks, and high-end boutiques. It is a popular destination for the city's elite and affluent residents. Indiranagar boasts a range of luxurious properties, from sprawling mansions to modern apartments with state-of-the-art amenities. The area is also home to a number of fine dining restaurants, trendy bars, and upscale shopping destinations.  
In this dashboard, luxurious houses are those that cost more than half a million dollars and have more than four bedrooms. 
you can see whitefield ranked first among neighboorhood with more than 20 ,Whitefield is a bustling neighborhood located in the eastern part of Bangalore,Once a quaint settlement on the outskirts of the city, Whitefield has now transformed into a major IT hub and residential area, attracting people from all over the world. The area is home to several multinational corporations, including IT giants such as IBM, Oracle, and Dell. 

 """)

# Different Neighborhood Average Area
fig = px.bar((df4.sort_values(by='area_type', ascending=False)), x="location", y="area_type", color="location",
             title='Number of Big Luxuries Houses in each location')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Luxuries Houses')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Big Luxuries Houses  """)

st.write(""" Bangalore is home to some of the most luxurious houses in India. These houses are equipped with state-of-the-art amenities and are designed with modern architecture. Many of these houses are located in prime locations and offer breathtaking views of the city. The interiors of these houses are designed with opulent furnishings and modern fixtures. Some of the features that are commonly found in these houses include private pools, spacious balconies, and lush gardens. Many of these houses also come equipped with home theaters, gyms, and game rooms. It's remarkable that homes with more than 10 bedrooms may be found in a variety of neighborhoods, some of which are inexpensive and have values significantly lower than homes with 4 bedrooms in the uptown area.
""")


source = df14
chart = alt.Chart(source).mark_circle().encode(
    x='Dollar_Price',
    y='Number_of_Bedrooms',
    color='Dollar_Price',
).interactive()

st.altair_chart(chart, theme="streamlit", use_container_width=True)


##########################################################################
