import streamlit as st
from services.kpi_service import get_kpis_by_category
from services.database import engine
from charts.render_overview_page import render_overview_page

# --------------------------------------------------
# Configuração geral da página
# --------------------------------------------------
st.set_page_config(
    page_title="Superstore Sales Analysis | 2017",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Sidebar — Contexto do Projeto
# --------------------------------------------------
st.sidebar.title("📊 Superstore Analysis")
st.sidebar.markdown(
    """
    **Ano analisado:** 2017  
    **Foco:** Vendas por categoria  
    **Objetivo:** Apoiar decisões estratégicas
    """
)

st.sidebar.divider()

# Navegação
page = st.sidebar.radio(
    "Navegação",
    [
        "📌 Visão Geral",
        "📦 Análise por Categoria",
        "📈 Análise Temporal",
        "📊 Análise Estatística"
    ]
)

st.sidebar.divider()
st.sidebar.markdown(
    """
    **Autor:** Cicero Reis  
    Analista de Dados em desenvolvimento
    """
)

# --------------------------------------------------
# Página: Visão Geral
# --------------------------------------------------
if page == "📌 Visão Geral":

    df_kpi = get_kpis_by_category(engine, year=2017)
    render_overview_page(df_kpi)

# --------------------------------------------------
# Página: Análise por Categoria
# --------------------------------------------------
elif page == "📦 Análise por Categoria":
    st.title("📦 Análise por Categoria")

    st.markdown(
        """
        Avaliação do desempenho de cada categoria considerando:
        - Volume de vendas
        - Lucro
        - Margem
        """
    )

    st.warning("Gráficos por categoria serão carregados aqui.")

# --------------------------------------------------
# Página: Análise Temporal
# --------------------------------------------------
elif page == "📈 Análise Temporal":
    st.title("📈 Análise Temporal — 2017")

    st.markdown(
        """
        Análise do comportamento das vendas ao longo dos meses.
        Identificação de sazonalidade e picos de demanda.
        """
    )

    st.warning("Distribuição mensal e sazonalidade serão exibidas aqui.")

# --------------------------------------------------
# Página: Análise Estatística
# --------------------------------------------------
elif page == "📊 Análise Estatística":
    st.title("📊 Análise Estatística")

    st.markdown(
        """
        Aplicação de medidas estatísticas para avaliar estabilidade e dispersão:
        - Média
        - Mediana
        - Moda
        - Quartis
        - Desvio padrão
        """
    )

    st.success(
        "📌 A mediana representa melhor o comportamento típico mensal do que a média."
    )

    st.warning("Boxplot e indicadores estatísticos serão exibidos aqui.")
