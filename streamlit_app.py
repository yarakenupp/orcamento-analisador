import streamlit as st
from scripts.consulta_anexos import obter_anexos

st.set_page_config(page_title="Consulta Anexos Tesouro", layout="wide")

st.title("📊 Anexos de Demonstrativos - Tesouro Nacional")

try:
    df = obter_anexos()
    st.success("✅ Dados carregados com sucesso!")
    st.dataframe(df)
except Exception as e:
    st.error(f"Erro ao buscar dados: {e}")
