import streamlit as st 
import pandas as pd

df_inf = pd.read_csv("inflasiyoy.csv", sep=";")

st.title("Inflasi dan Tingkat Pengangguran Terbuka di Indonesia")
st.dataframe(df_inf)