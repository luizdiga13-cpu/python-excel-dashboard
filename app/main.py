import streamlit as st
import pandas as pd
from processador import processar_arquivo
from dashboard import mostrar_dashboard

st.set_page_config(
    page_title="Dashboard Excel",
    layout="wide"
)

st.image(
    "../assets/logo.png",
    width=180
)

st.title("📊 Automação de Relatórios Excel")

arquivo = st.file_uploader(
    "Envie sua planilha Excel",
    type=["xlsx"]
)

if arquivo:

    df = pd.read_excel(arquivo)
    df.columns = df.columns.str.strip()
    st.subheader("Prévia da Planilha")
    st.dataframe(df)

    processar_arquivo(df)

    mostrar_dashboard(df)