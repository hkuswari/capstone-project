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
x_inf = df_inftahunan["Inflasi"][df_inftahunan.index.year<2022].to_numpy()
x_tpt = df_tpt["TPT"][df_tpt.index.year<2022].to_numpy()
x_gini = df_gini["IndeksGini"].to_numpy()
tahun = df_inftahunan.index.year[df_inftahunan.index.year<2022].to_numpy()
rinftpt = np.corrcoef(x_inf,x_tpt)
rinfgini = np.corrcoef(x_inf,x_gini)
rtptgini = np.corrcoef(x_tpt,x_gini)

st.title("Hubungan Indeks Gini, Inflasi dan Tingkat Pengangguran Terbuka di Indonesia") 
st.caption("Oleh Herdina Kuswari")
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
        st.markdown("""
                **Indeks Gini** menurut *World Bank* merupakan suatu ukuran ketimpangan dari distribusi pendapatan atau pengeluaran konsumsi
                antar individu atau rumah tangga dalam suatu perekonomian. Indeksi Gini bernilai antara 0 sampai dengan 1. Nilai
                indeks gini mendekati 1 memiliki arti bahwa perekonomian semakin timpang. 
                Dari tahun 2001 sampai dengan 2021, nilai indeks gini tertinggi terjadi di tahun **2013** dengan indeks gini sebesar **40,8%**. 
                Sedangkan indeks gini terendah terjadi pada tahun 2001. Pada tahun 2021 Indeks Gini di Indonesia 
                mencapai **37,9%** meningkat 0,3% 
                dari tahun sebelumnya.
            """)
        fig_gini = go.Figure()
        fig_gini.add_trace(go.Scatter(y=df_gini["IndeksGini"], x=df_gini.index.year,
                                mode='lines+markers',
                                name='lines+markers'))
        fig_gini.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2012.5, y0=0.403,
                            x1=2013.5, y1=0.413,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_gini.add_annotation(x=2013, y=0.417,
                            text="40,8%",
                            showarrow=False)
        fig_gini.update_layout(title=go.layout.Title(
                                        text="Indeks Gini Indonesia per Tahun (2001 - 2021) <br><sup>Sumber: WDI</sup>",
                                        xref="paper",
                                        x=0
                                    ),
                            xaxis_title='Tahun',
                            yaxis_title='Indeks Gini')
        fig_gini.layout.yaxis.tickformat = ',.2%'
        st.plotly_chart(fig_gini, use_container_width=True)

    with col2:
        st.header("Inflasi Bulanan")
        st.markdown("""
                **Inflasi** dapat diartikan sebagai kenaikan harga barang dan jasa secara umum dan terus menerus dalam jangka waktu tertentu.
                Saat ini Inflasi di Indonesia sedang mengalami peningkatan yang cukup tinggi dibandingkan bulan-bulan sebelumnya. 
                Selama 21 tahun, inflasi di Indonesia cukup fluktuatif. Di bulan November 2005 inflasi di Indonesia mencapai **18,38%**, tercatat
                sebagai nilai inflasi tertinggi dari tahun 2001 - 2022. Selain November 2005, inflasi di Indonesia naik cukup signifikan di bulan
                **Mei 2008** dan puncaknya terjadi di bulan **September 2008** dengan nilai inflasi sebesar **12,4%**. Krisis ekonomi global tahun 2008
                merupakan salah satu pemicu terjadinya inflasi di tahun 2008. Tercatat Pemerintah menaikkan harga BBM pada Mei 2008 yakni 33% 
                untuk premium dan 28% 
                untuk solar. Selain di tahun 2005 dan 2008, inflasi di Indonesia meningkat di sekitar tahun 2010 - 2011 dan naik kembali di tahun 2013 - 2014.
                Sejak Maret 2016, inflasi di Indonesia mencapai nilai tertinggi pada bulan Juli 2022 dengan inflasi IHK (yoy) sebesar 4,94%
                dan naik kembali di September 2022 menjadi sebesar **5,95%**.
                
                """)
        fig_inf = go.Figure()
        fig_inf.add_trace(go.Scatter(y=df_inf["Inflasi"], x=df_inf.index,
                                    mode='lines',
                                    name='lines'))
        fig_inf.add_shape(type="circle",
                            xref="x", yref="y",
                            x0="2005-05-01", y0=0.12,
                            x1="2007-05-01", y1=0.20,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_inf.add_shape(type="circle",
                            xref="x", yref="y",
                            x0="2008-01-01", y0=0.08,
                            x1="2009-05-01", y1=0.14,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_inf.add_shape(type="circle",
                            xref="x", yref="y",
                            x0="2010-01-01", y0=0.05,
                            x1="2012-01-01", y1=0.075,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_inf.add_shape(type="circle",
                            xref="x", yref="y",
                            x0="2013-04-01", y0=0.06,
                            x1="2016-03-01", y1=0.10,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_inf.update_layout(title=go.layout.Title(
                                        text="Inflasi IHK Indonesia per Bulan (2003 - 2022)<br><sup>Sumber: Bank Indonesia</sup>",
                                        xref="paper",
                                        x=0
                                    ),
                                xaxis_title='Bulan',
                                yaxis_title='Inflasi')
        fig_inf.layout.yaxis.tickformat = ',.2%'
        st.plotly_chart(fig_inf, use_container_width=True)
        
    col3, col4 = st.columns(2)
    with col3:
        st.header("Tingkat Pengangguran Terbuka")
        st.markdown("""
                **Pengangguran** adalah jumlah tenaga kerja dalam perekonomian yang secara aktif mencari pekerjaan tetapi 
                belum mendapatkannya. Besar kecilnya tingkat pengangguran berdasarkan persentase dari perbandingan 
                jumlah orang yang menganggur dengan jumlah angkatan kerja. Pengangguran terbuka adalah orang yang termasuk 
                angkatan kerja akan tetapi tidak bekerja dan tidak mencari pekerjaan. Data Tingkat Pengangguran Terbuka (TPT) 
                tahunan yang digunakan dalam project ini adalah TPT bulan Agustus setiap tahunnya.
                """)
        st.markdown("""
                Grafik TPT di Indonesia disajikan dalam gambar di bawah ini. Selama 22 tahun terakhir, TPT di Indonesia mengalami nilai tertinggi
                pada tahun **2005** dengan tingkat pengangguran terbuka sebesar **11,24%** meningkat 1,38% 
                dibandingkan tahun sebelumnya. Sedangkan kenaikan tingkat pengangguran terbuka lainnya terjadi di tahun 2011, 2013, 2015 dan 2020 dengan
                kenaikan tertinggi terjadi di tahun **2020** dari tahun 2019 dengan kenaikan sebesar **1,83%**.
                Sampai dengan Semester 1 2022, tingkat pengangguran terbuka di Indonesia mencapai 5,83% turun 0,66% 
                dari tahun 2021.
                """)
        fig_tpt = go.Figure()
        fig_tpt.add_trace(go.Scatter(y=df_tpt["TPT"], x=df_tpt.index.year,
                                mode='lines+markers',
                                name='lines+markers'))
        fig_tpt.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2004.5, y0=0.11,
                            x1=2005.5, y1=0.115,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_tpt.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2010.5, y0=0.0728,
                            x1=2011.5, y1=0.0778,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_tpt.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2014.5, y0=0.0593,
                            x1=2015.5, y1=0.0643,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_tpt.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2019.5, y0=0.0682,
                            x1=2020.5, y1=0.0732,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_tpt.add_annotation(x=2005, y=0.117,
                            text="11,24%",
                            showarrow=False)
        fig_tpt.add_annotation(x=2011, y=0.08,
                            text="7,48%",
                            showarrow=False)
        fig_tpt.add_annotation(x=2015, y=0.067,
                            text="6,18%",
                            showarrow=False)
        fig_tpt.add_annotation(x=2020, y=0.075,
                            text="7,07%",
                            showarrow=False)
        fig_tpt.add_annotation(x=2022.2, y=0.0563,
                            text="5,83%",
                            showarrow=False)
        fig_tpt.update_layout(title=go.layout.Title(
                                        text="Tingkat Pengangguran Terbuka di Indonesia per Tahun (2001 - 2022) <br><sup>Sumber: Badan Pusat Statistik</sup>",
                                        xref="paper",
                                        x=0
                                    ),
                            xaxis_title='Tahun',
                            yaxis_title='Tingkat Pengangguran Terbuka')
        fig_tpt.layout.yaxis.tickformat = ',.2%'
        st.plotly_chart(fig_tpt, use_container_width=True)
    with col4:
        st.header("Inflasi Tahunan")
        st.write("""
                Inflasi Tahunan atau Inflasi Aktual merupakan data dari inflasi IHK yoy di akhir tahun. Inflasi merupakan salah satu hal penting dalam menentukan 
                kondisi perekonomian, sehingga perlu mendapatkan perhatian serius dari berbagai kalangan khususnya 
                otoritas moneter yang bertanggung jawab mengendalikan inflasi. 
                Sesuai dengan data inflasi bulanan, inflasi pada tahun 2005, 2008, 2010, 2013 dan 2014 merupakan tahun-tahun dengan
                nilai inflasi yang cukup tinggi dibandingkan tahun lainnya. 
                Inflasi Indonesia sampai dengan September 2022 mencapai 5,95%
                sedangkan target inflasi di Indonesia tahun 2022 adalah 3% 
                dengan standar deviasi kurang lebih 1%. Apabila inflasi di Indonesia sampai akhir tahun terus meningkat maka inflasi
                aktual pada tahun 2002 akan melebihi target inflasi di Indonesia. Sehingga diharapkan para pemangku kebijakan dapat 
                mengendalikan inflasi yang terjadi beberapa bulan terakhir ini.
                """)
        st.write("""
                
                """)
        fig_infy = go.Figure()
        fig_infy.add_trace(go.Scatter(y=df_inftahunan["Inflasi"], x=df_inftahunan.index.year,
                                    mode='lines+markers',
                                    name='lines+markers'))
        fig_infy.update_layout(title=go.layout.Title(
                                        text="Inflasi Aktual Indonesia per Tahun (2001-2021) <br><sup>Sumber: Bank Indonesia</sup>",
                                        xref="paper",
                                        x=0
                                    ),
                                xaxis_title='Tahun',
                                yaxis_title='Inflasi')
        fig_infy.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2004.5, y0=0.165,
                            x1=2005.5, y1=0.175,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_infy.add_annotation(x=2005, y=0.18,
                            text="17,11%",
                            showarrow=False)
        fig_infy.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2007.5, y0=0.1061,
                            x1=2008.5, y1=0.1141,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_infy.add_annotation(x=2008, y=0.12,
                            text="11,06%",
                            showarrow=False)
        fig_infy.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2009.5, y0=0.065,
                            x1=2010.5, y1=0.075,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_infy.add_annotation(x=2010, y=0.08,
                            text="6,96%",
                            showarrow=False)
        fig_infy.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2012.65, y0=0.08,
                            x1=2013.35, y1=0.09,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_infy.add_annotation(x=2013, y=0.084,
                            text="8,38%",
                            showarrow=False, yshift = 15)
        fig_infy.add_shape(type="circle",
                            xref="x", yref="y",
                            x0=2013.65, y0=0.08,
                            x1=2014.35, y1=0.09,
                            opacity=0.5,
                            line_color="red",
                        )
        fig_infy.add_annotation(x=2015.5, y=0.085,
                            text="8,36%",
                            showarrow=False)
        fig_infy.layout.yaxis.tickformat = ',.2%'
        st.plotly_chart(fig_infy, use_container_width=True)
        
with st.container():
    st.header("Hubungan Antar Variabel")
    st.markdown("""
             Hubungan antara tiga variabel kemiskinan di atas akan dilihat menggunakan *scatter plot* dan korelasi antar variabel. 
             Analisis digunakan untuk melihat apakah ada pengaruh linier antara variabel satu dan variabel lainnya. Hal ini dibutuhkan
             karena perolehan data dari variabel satu dan variabel lainnya berbeda. Data yang digunakan dalam analisis korelasi ini 
             adalah data tahunan setiap variabel dari tahun 2001 sampai dengan 2021. 
             """)
    col5, col6 = st.columns(2)
    with col5:
        st.subheader("Inflasi dan Tingkat Pengangguran Terbuka")
        st.markdown(f"""
             Hubungan antara inflasi dan tingkat pengangguran terbuka diilustrasikan dalam grafik disamping. Dua variabel tersebut cenderung
             memiliki hubungan yang positif, dapat dilihat dari nilai inflasi yang tinggi cenderung memiliki nilai TPT yang tinggi juga.
             Hal ini dapat dilihat juga dari nilai korelasi yang positif yang cukup kuat antara dua variabel tersebut yakni sebesar **{rinftpt[0,1]:.2f}**.
             """)
        st.markdown(f"""
             Hasil korelasi ini tidak sesuai dengan Teori Kurva Philips. **A.W. Phillips** menggambarkan sebaran hubungan antara inflasi dengan 
             tingkat pengangguran didasarkan pada asumsi bahwa inflasi merupakan cerminan dari adanya kenaikan permintaan agregat. Dengan 
             naiknya permintaan agregat, maka sesuai dengan teori permintaan, jika permintaan naik maka harga akan naik. Dengan tingginya 
             harga (inflasi) maka untuk memenuhi permintaan tersebut produsen meningkatkan kapasitas produksinya dengan menambah tenaga kerja 
             (asumsinya tenaga kerja merupakan satu-satunya input yang dapat meningkatkan output). Akibat dari peningkatan permintaan tenaga kerja 
             maka dengan naiknya harga-harga (inflasi), pengangguran berkurang. 
             """) 
        st.markdown(f"""
             Sedangkan beberapa penelitian di Indonesia seperti Mulyati (2009) tentang Analisis Hubungan Inflasi dan Pengangguran Indonesia 
             periode 1985-2008: Pendekatan Kurva Phillips , Qomariyah (2012) entang Pengaruh Tingkat Inflasi dan Pertumbuhan Ekonomi terhadap 
             Tingkat Pengangguran di Jawa Timur menyatakan bahwa tidak ada hubungan kausalitas dan inflasi berpengaruh tidak signifikan terhadap pengangguran.
             Silaban & Siagian (2021) dalam penelitiannya tentang Pengaruh Inflasi Dan Investasi Terhadap Tingkat Pengangguran Terbuka Di Indonesia Periode 2002-2019 
             menyatakan bahwa secara parsial disimpulkan variabel Inflasi berpengaruh Positif dan signifikan terhadap Pengangguran di Indonesia.
             """) 
    with col6:
        fig_inftpt = px.scatter(x=x_inf, y=x_tpt, trendline = "ols", trendline_color_override="red")
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
        st.info("""
            Hasil korelasi ini sejalan dengan beberapa penelitian yang sudah disebutkan, sehingga terdapat kemungkinan bahwa inflasi dan tingkat pengangguran
            terbuka memiliki hubungan dengan arah yang positif. Akan tetapi, karena nilai korelasi yang tidak cukup kuat maka diperlukan penelitian
            lebih lanjut untuk menyatakan bahwa inflasi dan tingkat pengangguran terbuka memiliki hubungan yang positif dan signifikan.
            """, icon="ℹ️")
    col7, col8 = st.columns(2)
    with col7:
        st.subheader("Inflasi dan Indeks Gini")
        st.markdown(f"""
             Hubungan antara inflasi dan indeks gini diilustrasikan dalam *scatter plot* disamping. Dua variabel tersebut cenderung
             memiliki hubungan yang negatif, dapat dilihat dari nilai inflasi yang tinggi cenderung memiliki nilai indeks gini yang lebih rendah.
             Hal ini dapat dilihat juga dari nilai korelasi yang negatif antara dua variabel tersebut yakni sebesar **{rinfgini[0,1]:.2f}**. 
             """)
    with col8:
        fig_infgini = px.scatter(x=x_inf, y=x_gini, trendline = "ols", trendline_color_override="red")
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
        
    col9, col10 = st.columns(2)
    with col9:
        st.subheader("Tingkat Pengangguran Terbuka dan Indeks Gini")
        st.markdown(f"""
            Tingkat Pengangguran Terbuka dan Indeks Gini memiliki arah hubungan yang negatif. Hal ini terlihat dari *scatter plot*
            disamping, nilai Indeks Gini yang tinggi cenderung memiliki nilai TPT yang rendah. Selain itu, nilai korelasi
            antara TPT dan Indeks Gini juga menunjukkan arah negatif dan nilai yang cukup kuat yakni sebesar **{rtptgini[0,1]:.2f}**. 
             """)
    with col10:
        fig_tptgini = px.scatter(x=x_tpt, y=x_gini, trendline = "ols", trendline_color_override="red")
        fig_tptgini.update_traces(customdata = tahun,
            hovertemplate='TPT: %{x} <br>Indeks Gini: %{y} <br>Tahun: %{customdata}')
        fig_tptgini.layout.yaxis.tickformat = ',.2%'
        fig_tptgini.layout.xaxis.tickformat = ',.2%'
        fig_tptgini.update_layout(title=go.layout.Title(
                                            text="Scatter Plot TPT dan Indeks Gini<br><sup>2001 - 2021</sup>",
                                            xref="paper",
                                            x=0
                                        ),
                                  xaxis_title = 'Tingkat Pengangguran Terbuka', yaxis_title = 'Indeks Gini')
        st.plotly_chart(fig_tptgini)

with st.container():
    st.header("Kesimpulan")
    st.markdown(f"""
             Inflasi, Indeks Gini dan Tingkat Pengangguran Terbuka merupakan beberapa dari banyak variabel yang dapat menunjukkan
             keadaan kemiskinan di Indonesia. Kombinasi dua dari tiga variabel tersebut yang memiliki hubungan linear terkuat
             adalah variabel TPT dan Indeks Gini, dengan nilai korelasi mencapai **{rtptgini[0,1]:.2f}**. 
             Dua variabel yang memiliki arah hubungan positif adalah variabel Inflasi dan TPT dengan nilai korelasi
             sebesar **{rinftpt[0,1]:.2f}**. Sedangkan berdasarkan nilai korelasi hubungan antara inflasi dan indeks gini cenderung negatif dengan nilai 
             korelasi sebesar **{rinfgini[0,1]:.2f}**.
             Untuk mengonfirmasi hubungan antar variabel dari tiga variabel ini diperlukan analis lebih lanjut karena analisis korelasi hanya
             menjelaskan hubungan linier antar variabel. Ada kemungkinan bahwa hubungan antar variabel yang sudah disajikan di atas bukan hubungan
             non linier. 
             """)
with st.container():
    st.header("Referensi")
    st.caption("Astuti, I. Y., Istiyani, N., & Yuliati, L. (2019). Pengaruh Pertumbuhan Ekonomi, Tingkat Inflasi, Dan Pertumbuhan Penduduk Terhadap Tingkat Pengangguran Terbuka Di Indonesia. Jurnal Ekonomi Akuntansi Dan Manajemen, 18(1), 52-62.")
    st.caption("Lipton, M., & Ravallion, M. (1995). Chapter 41 poverty and policy. Handbook of Development Economics, 3, 2551–2657.")
    st.caption("Meo, M. S., Khan, V. J., Ibrahim, T. O., Khan, S., Ali, S., & Noor, K. (2018). Asymmetric impact of inflation and unemployment on poverty in Pakistan: new evidence from asymmetric ARDL cointegration. Asia Pacific Journal of Social Work and Development, 28(4), 295-310.")
    st.caption("Mulyati, S. (2009). Analisis Hubungan Inflasi dan Pengangguran di Indonesia periode 1985-2008. Skripsi. Bogor: IPB.")
    st.caption("Qomariyah, I. (2012). Pengaruh Tingkat Inflasi dan Pertumbuhan Ekonomi terhadap Tingkat Pengangguran di Jawa Timur. Jurnal Ekonomi : Universitas Negeri Surabaya.")
    st.caption("Silaban, P. S. M., & Siagian, S. J. (2021). Pengaruh Inflasi Dan Investasi Terhadap Tingkat Pengangguran Terbuka Di Indonesia Periode 2002-2019. Niagawan, 10(2), 109-119.")
