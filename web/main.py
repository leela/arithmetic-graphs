import os
import streamlit as st
import pandas as pd

df = pd.read_json(os.environ['NUMBERS_URL'])
df['A/2'] = df['A']/2
st.line_chart(df)
