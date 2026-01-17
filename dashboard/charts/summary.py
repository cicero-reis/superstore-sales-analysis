import streamlit as st
import plotly.express as px
from utils.formatting import abbreviate_number

def render_summary_page(df_kpi):

    st.title(" Superstore — Análise Executiva 2017")
    st.markdown("""
    Esta análise avaliou o desempenho de vendas da Superstore em 2017, com foco em volume vendido, rentabilidade e comportamento temporal, utilizando dados consolidados. O objetivo foi identificar o que está acontecendo, por que isso importa e onde agir para gerar valor.
    """)

    st.subheader("Resumo Executivo")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
    ** Contexto**  
    Este resumo apresenta os principais indicadores financeiros do ano, permitindo uma visão rápida da saúde do negócio.
    """)

    with col2:
        c1, c2, c3 = st.columns(3)
        c1.metric("Receita Total", f"${abbreviate_number(df_kpi.total_sales.sum())}")
        c2.metric("Lucro Total", f"${abbreviate_number(df_kpi.total_profit.sum())}")
        c3.metric("Margem Média", f"{df_kpi.profit_margin.mean():.1%}")
