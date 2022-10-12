from cgitb import text
import streamlit as st 
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

df_inf = pd.read_csv("inflasiyoy.csv", sep=";", parse_dates=['Bulan'], index_col=['Bulan'])
df_tpt = pd.read_csv("tpt.csv", sep=";", parse_dates=['Tahun'], index_col=['Tahun'])
df_inftahunan = pd.read_csv("inflasitahunan.csv", sep=";", parse_dates=['Tahun'], index_col=['Tahun'])
df_gini = pd.read_csv("gini.csv", sep=";", parse_dates=['Tahun'], index_col=['Tahun'])

st.title("Indeks Gini, Inflasi dan Tingkat Pengangguran Terbuka di Indonesia") 
with st.container():
    st.write("""
            Kemiskinan adalah konsep multidimensi yang dapat didefinisikan secara absolut dan relatif. 
            United Nation (1995) menegaskan bahwa 'kemiskinan absolut didefinisikan sebagai suatu kondisi yang ditandai dengan 
            perampasan serius kebutuhan dasar manusia yang meliputi: kesehatan, pendidikan, tempat tinggal, air minum yang aman, 
            makanan, fasilitas sanitasi, dan informasi'. Sedangkan kemiskinan relatif didefinisikan sebagai keadaan di mana seorang 
            individu tidak memiliki jumlah pendapatan minimum yang akan memungkinkannya untuk memiliki standar hidup yang 
            dibutuhkan dalam masyarakat (Lipton & Ravallion, 1995).
            """)
    st.write("""
            Banyak penelitian yang telah dilakukan untuk menjelaskan kemiskinan, baik di Indonesia maupun di Dunia. 
            Berdasarkan beberapa penelitian tersebut dan fenomena yang terjadi saat ini yakni meningkatnya inflasi di Indonesia. Maka dalam
            Capstone Project ini akan dibahas secara singkat bagaimana hubungan variabel-variabel yang dapat menunjukkan kemiskinan
            di Indonesia. Variabel-variabel yang akan dianalisis hubungannya secara singkat disini adalah Indeks Gini, Inflasi dan 
            Tingkat Pengangguran Terbuka.
            """)
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.header("Indeks Gini")
        st.write("""
                Indeks Gini menurut World Bank merupakan suatu ukuran ketimpangan dari distribusi pendapatan atau pengeluaran konsumsi
                antar individu atau rumah tangga dalam suatu perekonomian. Indeksi Gini bernilai antara 0 sampai dengan 1. Nilai
                indeks gini mendekati satu memiliki arti bahwa perekonomian semakin timpang. Pada tahun 2022
            """)
        fig_gini = go.Figure()
        fig_gini.add_trace(go.Scatter(y=df_gini["IndeksGini"], x=df_gini.index,
                                mode='lines+markers',
                                name='lines+markers'))
        fig_gini.update_layout(title=go.layout.Title(
                                        text="Indeks Gini Indonesia per Tahun <br><sup>Sumber: WDI</sup>",
                                        xref="paper",
                                        x=0
                                    ),
                            xaxis_title='Tahun',
                            yaxis_title='Indeks Gini')
        fig_gini.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig_gini, use_container_width=True)

    with col2:
        st.header("Inflasi")
        st.write("""
                Inflasi dapat diartikan sebagai kenaikan harga barang dan jasa secara umum dan terus menerus dalam jangka waktu tertentu.
                Saat ini Inflasi di Indonesia sedang mengalami peningkatan yang cukup tinggi dibandingkan bulan-bulan sebelumnya. 
                Pada bulan September tahun 2022 inflasi IHK (yoy) di Indonesia mencapai 5,95%. Inflasi merupakan salah satu hal penting dalam menentukan 
                kondisi perekonomian, sehingga perlu mendapatkan perhatian serius dari berbagai kalangan khususnya 
                otoritas moneter yang bertanggung jawab mengendalikan inflasi.
                """)
        fig_inf = go.Figure()
        fig_inf.add_trace(go.Scatter(y=df_inf["Inflasi"], x=df_inf.index,
                                    mode='lines',
                                    name='lines'))
        fig_inf.update_layout(title=go.layout.Title(
                                        text="Inflasi IHK Indonesia per Bulan (yoy) <br><sup>Sumber: Bank Indonesia</sup>",
                                        xref="paper",
                                        x=0
                                    ),
                                xaxis_title='Bulan',
                                yaxis_title='Inflasi')
        fig_inf.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig_inf, use_container_width=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.header("Tingkat Pengangguran Terbuka")
        st.write("""
                Pengangguran adalah jumlah tenaga kerja dalam perekonomian yang secara aktif mencari pekerjaan tetapi 
                belum mendapatkannya. Besar kecilnya tingkat pengangguran berdasarkan persentase dari perbandingan 
                jumlah orang yang menganggur dengan jumlah angkatan kerja. Pengangguran terbuka adalah orang yang termasuk 
                angkatan kerja akan tetapi tidak bekerja dan tidak mencari pekerjaan.
                """)
        fig_tpt = go.Figure()
        fig_tpt.add_trace(go.Scatter(y=df_tpt["TPT"], x=df_tpt.index,
                                mode='lines+markers',
                                name='lines+markers'))
        fig_tpt.update_layout(title=go.layout.Title(
                                        text="Tingkat Pengangguran Terbuka di Indonesia per Tahun <br><sup>Sumber: Badan Pusat Statistik</sup>",
                                        xref="paper",
                                        x=0
                                    ),
                            xaxis_title='Tahun',
                            yaxis_title='Tingkat Pengangguran Terbuka')
        fig_tpt.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig_tpt, use_container_width=True)
        

