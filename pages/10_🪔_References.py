# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image


# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='References -Real Estate In Bangalore',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 References')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# SQL Codes
st.write(""" ## Acknowledgement ## """)

st.write("""
We are grateful to all who helped us develop this project, especially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with a comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And we are thankful for (https://codebasics.io/) tutorial on cleaning data and the linear regression model develpment, and also ****Kaggle**** with its massive database, and last but not least, ****MetricsDao**** which is the reason behind this project.


""")

st.text(" \n")
st.text(" \n")

# Sources
st.write(""" ## Sources ## """)

st.write("""
Here are the reference numbers for all of the sources used in this project:
  


""")

st.write("""
 1.https://codebasics.io/      
        2.https://www.shutterstock.com/search/bangalore-house    
        3.https://www.prestigeprimrosehills.gen.in/blog/top-luxury-apartments-in-bangalore.html    
        4.https://www.sobha.com/city/bengaluru/    
        5.https://www.justdial.com/Bangalore/RNR-Apartment-ISKCON-Temple-Mahalakshmi-Layout/080PXX80-XX80-180214130417-F2B1_BZDET   
        

""")
