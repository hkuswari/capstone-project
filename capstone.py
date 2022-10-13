from cgitb import text
import streamlit as st 
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide")

df_inf = pd.read_csv("inflasiyoy.csv", sep=";", parse_dates=['Bulan'], index_col=['Bulan'])
df_tpt = pd.read_csv("tpt.csv", sep=";", parse_dates=['Tahun'], index_col=['Tahun'])
df_inftahunan = pd.read_csv("yinf.csv", sep=";", parse_dates=['tahun'], index_col=['tahun'])
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
                indeks gini mendekati satu memiliki arti bahwa perekonomian semakin timpang. Pada tahun 2021 nilai Indeks Gini di Indonesia
                adalah 37,9% meningkat 0,3%
                dari tahun sebelumnya.
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
        st.header("Inflasi Bulanan")
        st.write("""
                Inflasi dapat diartikan sebagai kenaikan harga barang dan jasa secara umum dan terus menerus dalam jangka waktu tertentu.
                Saat ini Inflasi di Indonesia sedang mengalami peningkatan yang cukup tinggi dibandingkan bulan-bulan sebelumnya. 
                Pada bulan September tahun 2022 inflasi Indeks Harga Konsumen (IHK) di Indonesia mencapai 5,95%. 
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
                angkatan kerja akan tetapi tidak bekerja dan tidak mencari pekerjaan. TPT tahunan yang digunakan dalam project ini
                adalah TPT bulan Agustus setiap tahunnya. Sampai dengan Februari 2022, TPT di Indonesia adalah sebesar 5,83%.
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
    with col4:
        st.header("Inflasi Tahunan")
        st.write("""
                Inflasi Tahunan atau Inflasi Aktual merupakan data dari inflasi IHK yoy di akhir tahun. Inflasi merupakan salah satu hal penting dalam menentukan 
                kondisi perekonomian, sehingga perlu mendapatkan perhatian serius dari berbagai kalangan khususnya 
                otoritas moneter yang bertanggung jawab mengendalikan inflasi. Inflasi Indonesia sampai dengan September 2022 mencapai 5,95%
                sedangkan target inflasi di Indonesia tahun 2022 adalah 3% 
                dengan standar deviasi kurang lebih 1%.
                """)
        fig_infy = go.Figure()
        fig_infy.add_trace(go.Scatter(y=df_inftahunan["Inflasi"], x=df_inftahunan.index,
                                    mode='lines+markers',
                                    name='lines+markers'))
        fig_infy.update_layout(title=go.layout.Title(
                                        text="Inflasi Aktual Indonesia per Tahun <br><sup>Sumber: Bank Indonesia</sup>",
                                        xref="paper",
                                        x=0
                                    ),
                                xaxis_title='Tahun',
                                yaxis_title='Inflasi')
        fig_infy.update_xaxes(rangeslider_visible=True)
        st.plotly_chart(fig_infy, use_container_width=True)
        
with st.container():
    #data
    x_inf = df_inftahunan["Inflasi"][df_inftahunan.index.year<2022].to_numpy()
    x_tpt = df_tpt["TPT"][df_tpt.index.year<2022].to_numpy()
    x_gini = df_gini["IndeksGini"].to_numpy()
    tahun = df_inftahunan.index.year[df_inftahunan.index.year<2022].to_numpy()
    rinftpt = np.corrcoef(x_inf,x_tpt)
    rinfgini = np.corrcoef(x_inf,x_gini)
    st.header("Hubungan Indeks Gini, Inflasi, dan Tingkat Pengangguran Terbuka")
    st.write("""
             Hubungan antara tiga variabel kemiskinan di atas akan dilihat menggunakan scatter plot dan korelasi antar variabel. 
             Analisis digunakan untuk melihat apakah ada pengaruh linier antara variabel satu dan variabel lainnya. Hal ini dibutuhkan
             karena perolehan data dari variabel satu dan variabel lainnya berbeda. Variabel inflasi merupakan variabel yang datanya 
             bisa diperoleh lebih cepat. Sehingga kita bisa memprediksikan apabila inflasi mengalami kenaikan atau penurunan maka 
             variabel yang lain juga akan mengalami perubahan.
             """)
    col5, col6 = st.columns(2)
    with col5:
        st.subheader("Inflasi dan Tingkat Pengangguran Terbuka")
        st.markdown(f"""
             Hubungan antara inflasi dan tingkat pengangguran terbuka diilustrasikan dalam grafik disamping. Dua variabel tersebut cenderung
             memiliki hubungan yang positif, dapat dilihat dari nilai inflasi yang tinggi cenderung memiliki nilai TPT yang tinggi juga.
             Hal ini dapat dilihat juga dari nilai korelasi yang positif antara dua variabel tersebut yakni sebesar **{rinftpt[0,1]:.2f}**. 
             Walaupun tidak memiliki nilai korelasi yang kuat, korelasi antara inflasi dan tingkat pengangguran terbuka memiliki arah yang positif.
             """)
    with col6:
        fig_inftpt = px.scatter(x=x_inf, y=x_tpt)
        fig_inftpt.update_traces(customdata = tahun,
            hovertemplate='Inflasi: %{x} <br>TPT: %{y} <br>Tahun: %{customdata}')
        fig_inftpt.layout.yaxis.tickformat = ',.2%'
        fig_inftpt.layout.xaxis.tickformat = ',.2%'
        fig_inftpt.update_layout(title=go.layout.Title(
                                            text="Scatter Plot Inflasi dan TPT<br><sup>2001 - 2021</sup>",
                                            xref="paper",
                                            x=0
                                        ),
                                  xaxis_title = 'Inflasi', yaxis_title = 'Tingkat Pengangguran Terbuka')
        st.plotly_chart(fig_inftpt)
    col7, col8 = st.columns(2)
    with col7:
        st.subheader("Inflasi dan Indeks Gini")
        st.markdown(f"""
             Hubungan antara inflasi dan indeks gini diilustrasikan dalam scatter plot disamping. Dua variabel tersebut cenderung
             memiliki hubungan yang negatif, dapat dilihat dari nilai inflasi yang tinggi cenderung memiliki nilai indeks gini yang lebih rendah.
             Hal ini dapat dilihat juga dari nilai korelasi yang negatif antara dua variabel tersebut yakni sebesar **{rinfgini[0,1]:.2f}**. 
             """)
    with col8:
        fig_infgini = px.scatter(x=x_inf, y=x_gini)
        fig_infgini.update_traces(customdata = tahun,
            hovertemplate='Inflasi: %{x} <br>Indeks Gini: %{y} <br>Tahun: %{customdata}')
        fig_infgini.layout.yaxis.tickformat = ',.2%'
        fig_infgini.layout.xaxis.tickformat = ',.2%'
        fig_infgini.update_layout(title=go.layout.Title(
                                            text="Scatter Plot Inflasi dan Indeks Gini<br><sup>2001 - 2021</sup>",
                                            xref="paper",
                                            x=0
                                        ),
                                  xaxis_title = 'Inflasi', yaxis_title = 'Indeks Gini')
        st.plotly_chart(fig_infgini)
