import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Painel Orçamentário", layout="wide")

st.title("📊 Painel Orçamentário Público - Siga Brasil")

# Dicionário com os caminhos dos arquivos consolidados
temas = {
    "DRU": "consolidados/dru_consolidado.csv",
    "FAT": "consolidados/fat_consolidado.csv",
    "CIDE": "consolidados/cide_consolidado.csv",
    "Receita da Seguridade": "consolidados/receita_seguridade_consolidado.csv"
}

# Tema selecionado
tema = st.selectbox("Escolha o tema", list(temas.keys()))

# Verifica se o arquivo existe
caminho = temas[tema]
if os.path.exists(caminho):
    df = pd.read_csv(caminho)
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]  # limpa nomes de colunas

    if "ano" in df.columns:
        anos = sorted(df["ano"].dropna().unique())
        ano_selecionado = st.selectbox("Selecione o ano", anos)
        df = df[df["ano"] == ano_selecionado]

    st.markdown("### 📄 Tabela de Dados")
    st.dataframe(df, use_container_width=True)

    st.markdown("### 📈 Gráfico")
    colunas_numericas = df.select_dtypes(include=["float", "int"]).columns.tolist()
    if colunas_numericas:
        st.line_chart(df[colunas_numericas])
    else:
        st.warning("Nenhuma coluna numérica disponível para gráfico.")

    st.download_button(
        label="📥 Baixar CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"{tema.lower()}_dados.csv",
        mime="text/csv"
    )
else:
    st.warning("⚠️ Ainda não há dados consolidados disponíveis para este tema.")
