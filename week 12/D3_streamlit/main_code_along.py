import pandas as pd
pd.DataFrame.iteritems = pd.DataFrame.items
import numpy as np
import plotly.express as px
import streamlit as st
import pickle
from streamlit_extras.add_vertical_space import add_vertical_space

### Default best practice structure when you have multiple cols:
# Define streamlit_element
# streamlit_element = st.columns, st.sidebar, st.tabs, etc. (see Layouts & Containers in docs)
# with streamlit_element:
    # Write some functions here that define what's inside
    # plotly_fig = px.line(data, x='col1', y='col2')
    # st.plotly_chart(plotly_fig)
    # st.markdown("Some markdown formatted text.")
    
### Goal for today: Build and deploy an EDA and ML tool
# Elements we need: data to analyze, some interesting charts, and some model
data = pd.read_csv("https://raw.githubusercontent.com/sabinagio/data-analytics/main/data/customer_churn.csv").dropna()

# Exploratory Data Analysis

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (0.01, 2, 0.1, 2, 0.01)
)


row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.columns(
    (0.01, 2, 0.1, 2, 0.01)
)

# open pickle files in main (reading the models)

# Add sidebar parameters

# Preprocessing data

# Create model magic


st.header("Customer Churn Analysis")
# Elements we need: data to analyze, some interesting charts, and some model
data = pd.read_csv("https://raw.githubusercontent.com/sabinagio/data-analytics/main/data/customer_churn.csv").dropna()
st.markdown("### Exploratory Data Analysis")
charges = st.selectbox("", ("MonthlyCharges", "TotalCharges"))
cat_var = st.selectbox("", data.select_dtypes("object").columns.drop("customerID"))
fig = px.histogram(data, x=charges, facet_row=cat_var)
st.plotly_chart(fig)