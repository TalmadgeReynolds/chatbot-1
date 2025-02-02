{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import json\
\
# Page Configuration\
st.set_page_config(page_title="Interactive Dashboard", layout="wide")\
\
# Load datasets\
@st.cache_data\
def load_data():\
    with open("ADDL_Categories.json") as file:\
        addl_categories = json.load(file)\
    with open("updated_unified_datasets.json") as file:\
        unified_data = json.load(file)\
    with open("cleaned_Media_Sentiment_Analysis_cleaned.json") as file:\
        media_sentiment = json.load(file)\
    with open("news_sentiment_trends.json") as file:\
        news_sentiments = json.load(file)\
    return addl_categories, unified_data, media_sentiment, news_sentiments\
\
# Load Data\
addl_categories, unified_data, media_sentiment, news_sentiments = load_data()\
\
# Centered Search Pane Styling\
st.markdown(\
    """\
    <style>\
        .centered-search \{\
            display: flex;\
            justify-content: center;\
            align-items: center;\
            height: 70vh;\
        \}\
        .search-bar \{\
            background-color: #f0f2f6;\
            border: 2px solid #4CAF50;\
            border-radius: 15px;\
            padding: 20px;\
            text-align: center;\
            width: 50%;\
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);\
        \}\
        .search-bar input \{\
            font-size: 18px;\
            text-align: center;\
        \}\
    </style>\
    <div class="centered-search">\
        <div class="search-bar">\
            <h2 style="color:#4CAF50;">Enter a Politician or Company Name</h2>\
        </div>\
    </div>\
    """,\
    unsafe_allow_html=True,\
)\
\
# User Input\
st.markdown("### Search Input")\
user_query = st.text_input("Enter your query:", "", key="search_input")\
\
# Results Section\
if user_query:\
    st.subheader(f"### Generating Report for: \{user_query\}")\
    \
    # Placeholder for Overview\
    st.markdown("#### \uc0\u55357 \u56541  Overview")\
    st.info(f"This is a placeholder for an overview report on **\{user_query\}**.")\
\
    # Placeholder for Media Sentiment\
    st.markdown("#### \uc0\u55357 \u56522  Media Sentiment Analysis")\
    st.warning(f"Sentiment data for **\{user_query\}** will appear here.")\
\
    # Placeholder for Connections\
    st.markdown("#### \uc0\u55357 \u56599  Policy/Corporate Connections")\
    st.success(f"Connections related to **\{user_query\}** will be displayed here.")\
\
    # Placeholder for News Trends\
    st.markdown("#### \uc0\u55357 \u56560  News Trends")\
    st.error(f"News headlines and trends related to **\{user_query\}** will show up here.")\
\
else:\
    st.write("Please enter a politician or company name to generate the report.")\
\
# Footer\
st.markdown("---")\
st.caption("Powered by Streamlit and custom global insight datasets.")\
}