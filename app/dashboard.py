import streamlit as st
import plotly.express as px


def mostrar_dashboard(df):

    st.subheader("📈 Dashboard")

    total = df["Vendas"].sum()

    media = df["Vendas"].mean()

    col1, col2 = st.columns(2)

    col1.metric("Total de Vendas", total)

    col2.metric("Média de Vendas", round(media, 2))

    grafico = px.bar(
        df,
        x="Produtos",
        y="Vendas",
        title="Vendas por Produto"
    )

    st.plotly_chart(grafico, use_container_width=True)