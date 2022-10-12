import streamlit as st 
import pandas as pd

df_inf = pd.read_csv("inflasiyoy.csv", sep=";", parse_dates=['Bulan'], index_col=['Bulan'])

st.title("Inflasi dan Tingkat Pengangguran Terbuka di Indonesia")
st.write("Saat ini inflasi di Indonesia sedang mengalami peningkatan. Pada bulan September tahun 2022\
    tingkat inflasi IHK di Indonesia mencapai 5,95%.")
st.line_chart(df_inf)
st.caption("Sumber: Bank Indonesia")
