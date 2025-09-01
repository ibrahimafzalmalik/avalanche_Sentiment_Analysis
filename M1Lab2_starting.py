# import packages
import streamlit as st
import pandas as pd
import os
import plotly.express as px
import openai
from dotenv import load_dotenv

#Title of the App
st.title("GenAI Sentiment Analysis Dashboard")

#Text for the App Intro
st.write("This is your GenAI powered data processing app")

col1, col2 = st.columns(2)

with col1:
    if st.button("Load Dataset"):
        pass
with col2:
    if st.button("Analyze Sentiments"):
        pass