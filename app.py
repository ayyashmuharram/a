import pandas as pd #pip install pandas openpyxl
import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit

st.set_page_config(page_title="Production Dashboard",
                   page_icon="blackpink.png",
                   layout="wide")

#Main Page
st.title(":girl: Production Dashboard")
st.markdown("##")

#df = pd.read_csv(
#    io='produksi_minyak_mentah.csv',
#    engine='openpyxl',
#    sheet_name='produksi_minyak_mentah',
#    skiprows=3,
#    usecols='B:R',
#    nrows=1000,
#)

df = pd.read_csv('produksi_minyak_mentah.csv' ) 

#sidebar
st.sidebar.header("Please Filter Here:" )
negara = st.sidebar.multiselect(
    "Pilih Negara:",
    options=df["kode_negara"].unique(),
    default=df["kode_negara"].unique()
)

tahun = st.sidebar.multiselect(
    "Pilih Tahun:",
    options=df["tahun"].unique(),
    default=df["tahun"].unique()
)

df_selection = df.query(
    "kode_negara == @negara & tahun == @tahun"
)

#st.dataframe(df_selection)

#TOP KPI's
total_produksi = int(df_selection["produksi"].sum())
#average_rating = round(df_selection["Rating"].mean(),1)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Produksi")
    st.subheader(f" {total_produksi:,}")

st.markdown("---")

#Production by country (Bar Chart)
produksi_berdasarkan_negara = (
    df_selection.groupby(by=["kode_negara"]).sum()[["produksi"]].sort_values(by="produksi")     
)
fig_produksi_minyak = px.bar(
    produksi_berdasarkan_negara,
    x="produksi",
    y=produksi_berdasarkan_negara.index,
    orientation="h",
    title="<b>Produksi Minyak berdasarkan Negara</b>",
    color_discrete_sequence=["#0083B8"] * len(produksi_berdasarkan_negara),
    template="plotly_white",
)

st.plotly_chart(fig_produksi_minyak)




 


