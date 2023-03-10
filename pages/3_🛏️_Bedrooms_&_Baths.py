# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import matplotlib.pyplot as plt
import altair as alt
from vega_datasets import data

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title=' Bedrooms_&_Baths -  Real Estate In Bangalore',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🛏️ Bedrooms & Baths 🛁')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'bedrooms_bathroom_orginal':
        return pd.read_csv('Data/Bedrooms_Bathrooms/Bedrooms_Bathrooms.csv')
    elif query == 'Weekly_2022':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y22/Y22-Weekly.csv')
    elif query == 'table':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Domestic/Y22/Y22-Weekly2.csv')
    return None


bedrooms_bathroom_orginal = get_data('bedrooms_bathroom_orginal')
Weekly_2022 = get_data('Weekly_2022')
table = get_data('table')

df = bedrooms_bathroom_orginal
df2 = df[(df['Number_of_Bedrooms'] <= 3)]
df3 = df[(df['Number_of_Bedrooms'] >= 4)]
df4 = df3[(df3['Dollar_Price'] >= 500000)]


#################################################################################################
st.write(""" ### Number of Bedroom and Bathroom Impact on Real Estate ##  """)

st.write(""" When it comes to real estate, the number of bedrooms and bathrooms in a property can have a significant impact on its price. Properties with more bedrooms and bathrooms are typically more expensive than those with fewer, as they offer more space and amenities for residents. In this sense, the number of bedrooms and bathrooms in a property can be seen as a reflection of its overall size and desirability, and can be a major factor in determining its market value. Whether you are buying or selling a property, it is important to consider the impact that the number of bedrooms and bathrooms can have on its price, and to use this information to make informed decisions about your real estate investments.



  """)


st.info(""" ##### In This Bedroom & Bathroom Section you can find: ####

* Daily Top 10 Movie Grosss in 2022 [USD]
* Daily Number of Movie Released
* 2022 Weekly Figures
* Top First Sold Movie each Week [Detailed Table]



""")


#################################################################################################


#####################################################

st.write(""" ## All Houses""")

st.write(""" The highest top-10 grossing day in 2019 was 169 million, which fell to 57 million in 2020 and then rose to 128 million in 2021. This trend was expected to continue, and the record should have been broken in 2022. However, as you can see, there were days with a maximum of 99 million top ten grossings, and none of them were able to break "Spider-Man: No Way Home's" record in 2021. In 2022, there were seven days with more than 50 million top ten grossings, with other days tolerated between 20m and 45m on weekends and 2m to 14m on weekdays.
""")


source = df
chart = alt.Chart(source).mark_circle().encode(
    x='Dollar_Price',
    y='Number_of_Bedrooms',
    color='Dollar_Price',
).interactive()

st.altair_chart(chart, theme="streamlit", use_container_width=True)


st.write(""" ### Big Luxuries Houses  """)

st.write(""" The daily number of movies released increased steadily from 23 in the first week of January to 52 on September 17, before dropping to 24 on November 30. The Qatar 2022 World Cup might be a reason for this fall. Even though the number of movies that came out during this time period went down, the total gross didn't change much. Maybe theaters showing soccer matches were the reason for this.
""")


source = df4
chart = alt.Chart(source).mark_circle().encode(
    x='Dollar_Price',
    y='Number_of_Bedrooms',
    color='Dollar_Price',
).interactive()

st.altair_chart(chart, theme="streamlit", use_container_width=True)


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The highest top-10 grossing day in 2022 was only 99 million, falling short of 2021's record of 128 million
* In 2022, there were seven days with top 10 grossings of more than 50 million
* The amount of films released during the World Cup in Qatar decreased, but the overall box office didn't alter significantly
* After the summer, overall gross fell sharply, from a peak of 334 million on July 8–14 to a low of 58.7 million on September 9–15
* The quantity of movies released and the overall box office conflicted in the fall

""")
