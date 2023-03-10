# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import matplotlib.pyplot as plt
from sklearn import datasets

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='🏗️ Building Type - Real Estate In Bangalore',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🏗️ Building Type')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'bedrooms_bathroom_orginal':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Real_Estate_In_Bangalore/main/Data/Building_Type/Building_type.csv')
    elif query == 'Number_of_Release':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Geners/Genre-Total2.csv')
    elif query == 'average_per_release':
        return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Geners/Genre-Total3.csv')
    return None


Total_Genre = get_data('Total_Genre')
Number_of_Release = get_data('Number_of_Release')
average_per_release = get_data('average_per_release')


df = Total_Genre
df2 = Number_of_Release
df3 = average_per_release
#################################################################################################
st.write(""" ### Building Type Impact ##  """)

st.write("""
The choice between buying an apartment or a house can have a significant impact on real estate prices. Generally, apartments tend to be more affordable than houses, but this can vary depending on factors such as location, size, and amenities. For example, apartments in highly desirable areas or those with luxury amenities may command higher prices than smaller houses in less desirable locations. Ultimately, the decision between an apartment or a house will depend on individual preferences, lifestyle, and budget, all of which can affect the value of real estate in the market.

   

  """)


st.info(""" ##### In This Genre Section you can find: ####

* Top 7 Genre Based on All time Total Gross
* Top 7 Genre Based on Number of Release
* Top 7 Genre Based on Average Gross per Release



""")


#################################################################################################


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The adoption genre is currently the most profitable of all time, with gross sales of 74 billion dollars
* Foreign language and documentaries were the categories with the most number of releases
* The category deserving of attention is IMAX, with 153 million in average box office receipts per movie
* The average gross per release was insufficient because there weren't many releases in some genres
  

""")
