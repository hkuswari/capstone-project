import streamlit as st 
import pandas as pd

df_inf = pd.read_csv("inflasiyoy.csv", sep=";", parse_dates=['Bulan'], index_col=['Bulan'])
df_tpt = pd.read_csv("tpt.csv", sep=";", parse_dates=['Tahun'], index_col=['Tahun'])

st.title("Inflasi dan Tingkat Pengangguran Terbuka di Indonesia")
st.write("Saat ini inflasi di Indonesia sedang mengalami peningkatan. Pada bulan September tahun 2022\
    tingkat inflasi IHK di Indonesia mencapai 5,95%. Berdasarkan hal ini maka akan dilihat hubungan dari\
    tingkat Inflasi dan Tingkat Pengangguran Terbuka (TPT) di Indonesia. ")

st.caption("Sumber: Bank Indonesia")
st.line_chart(df_inf)
st.caption("Sumber: BPS")
st.line_chart(df_tpt)
