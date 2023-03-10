# Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title='Future Worl -  Real Estate In Bangalore',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔥 Future Work')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


###################################################################################

st.write(""" ### Limitatioin on Certain Features in Data Set ##  """)

st.write(""" Amenities play a significant role in determining the value of real estate. Properties located near desirable amenities such as schools, parks, shopping centers, and transportation hubs are typically priced higher than those that are not. The lack of data related to amenities was really a big issue with this data set. Also, each property's latitude and longitude could help the prediction and suggestion applications. For future projects, it is needed to provide some information related to the outside appearance of the house or features that provide for more up-to-date buildings like a pool or gym. In the section that follows, we provide a list of several ideas that can be used in the upcoming project that will use a comprehensive data set.
  """)


st.info(""" ##### For future work: ####

* If data set had specified the Latitude and Longitude of  properties, the map in the price prediction section may display homes that were most relevant to the user criteria   
* Take into account the influence of inflation on real estate prices  
* provide a thorough analysis of the city in addition to price prediction application  
* Employ more complex models with greater depth to get greater accuracy (a large data set with greater detail is required)   
* Based on user information, the AI system could suggest many alternatives and advise the optimal one  



""")


##############################################################################################


#####################################################
