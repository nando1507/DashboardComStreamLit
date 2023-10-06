import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(    
    page_title="DashVendas",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })

st.title("DashVendas")
df = pd.read_csv(
            "supermarket_sales.csv",
            sep=";",
            decimal=","            
        )
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by='Date')
# df=df.sort_values(df["Date"])
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month).zfill(2))
month = st.sidebar.selectbox("Mês", df["Month"].unique())
df_filtered = df[df["Month"]==month]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(
    df_filtered, 
    x="Date", 
    y="Total",
    color="City",
    title="Faturamento por dia"
)
col1.plotly_chart(fig_date,use_container_width=True)

fig_prod = px.bar(
    df_filtered, 
    x="Date", 
    y="Product line",
    color="City",
    title="Faturamento por tipo de Produto",
    orientation="h"
)
col2.plotly_chart(fig_prod,use_container_width=True)

df_city = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_City = px.bar(
    df_city, 
    x="City", 
    y="Total",
    title="Faturamento por Cidade",
    # orientation="h"
)
fig_City.update_traces(marker_color='#8E44AD')
col3.plotly_chart(fig_City,use_container_width=True)

fig_pay = px.pie(
    df_filtered, 
    values="Total",
    names="Payment",
    title="Faturamento por tipo de pagamento"
)
col4.plotly_chart(fig_pay,use_container_width=True)


df_rat = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_City = px.bar(
    df_rat, 
    x="City", 
    y="Rating",
    title="Avaliação",
    # orientation="h"
    
)
fig_City.update_traces(marker_color='#C0392B')
col5.plotly_chart(fig_City,use_container_width=True)

df_filtered