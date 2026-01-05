import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from services.kpi_service import (
    get_receita_total_por_categoria,
    get_distribuicao_mensal_de_vendas,
    get_media,
    get_median,
    get_quartiles,
    get_variance,
    get_min_max,
    get_moda,
    get_amplitude,
    get_desvio_padrao
)
from services.database import engine
# Charts
from charts.receita_total_por_categoria import (
    render_receita_total_por_categoria_markdown,
    render_receita_total_por_categoria_chart
)
from charts.lucro_total_por_categoria import (
    render_lucro_total_por_categoria_markdown,
    render_lucro_total_por_categoria_chart
)
from charts.quantidade_total_por_vendida_por_categoria import (
    render_quantidade_total_por_vendida_por_categoria_markdown,
    render_quantidade_total_por_vendida_por_categoria_chart
)
from charts.margem_de_lucro_por_categoria import (
    render_margem_de_lucro_por_categoria_markdown,
    render_margem_de_lucro_por_categoria_chart
)
from charts.lucro_por_unidade_por_categoria import (
    render_lucro_por_unidade_por_categoria_markdown,
    render_lucro_por_unidade_por_categoria_chart
)
from charts.summary import render_summary_page

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
st.sidebar.markdown("""
**Ano analisado:** 2017  
**Foco:** Vendas por categoria  
**Objetivo:** Apoiar decisões estratégicas
""")
st.sidebar.divider()
st.sidebar.markdown("""
**Autor:** Cicero Reis  
Analista de Dados em desenvolvimento
""")

# --------------------------------------------------
# Carregar dados
# --------------------------------------------------
df_receita_total_por_categoria = get_receita_total_por_categoria(engine, year=2017)
df_distribuicao_mensal_de_vendas = get_distribuicao_mensal_de_vendas(engine, year=2017)
df_media = get_media(engine, year=2017)
df_median = get_median(engine, year=2017)
df_quartiles = get_quartiles(engine, year=2017)
df_variance = get_variance(engine, year=2017)
df_min_max = get_min_max(engine, year=2017)
df_moda = get_moda(engine, year=2017)
df_amplitude = get_amplitude(engine, year=2017)
df_desvio_padrao = get_desvio_padrao(engine, year=2017)

# --------------------------------------------------
# Bloco 1 — Resumo Executivo
# --------------------------------------------------
render_summary_page(df_receita_total_por_categoria)
st.markdown("---")

# ---------------------------
# Bloco 2 — Receita Total por Categoria
# ---------------------------
col1, col2 = st.columns([1, 2])
with col1:
    render_receita_total_por_categoria_markdown()
with col2:
    render_receita_total_por_categoria_chart(df_receita_total_por_categoria)
st.markdown("---")

col1, col2 = st.columns([2, 1])
with col1:
    render_lucro_total_por_categoria_chart(df_receita_total_por_categoria)
with col2:
    render_lucro_total_por_categoria_markdown()
st.markdown("---")

col1, col2 = st.columns([1, 2])
with col1:
    render_quantidade_total_por_vendida_por_categoria_markdown()
with col2:
    render_quantidade_total_por_vendida_por_categoria_chart(df_receita_total_por_categoria)
st.markdown("---")

col1, col2 = st.columns([2, 1])
with col1:
    render_margem_de_lucro_por_categoria_chart(df_receita_total_por_categoria)
with col2:
    render_margem_de_lucro_por_categoria_markdown()
st.markdown("---")

col1, col2 = st.columns([1, 2])
with col1:
    render_lucro_por_unidade_por_categoria_markdown()
with col2:
    render_lucro_por_unidade_por_categoria_chart(df_receita_total_por_categoria)
st.markdown("---")

# --- Dados ---
df_faixa = pd.DataFrame({
    "faixa_venda": df_moda["faixa_venda"],
    "frequencia": df_moda["frequencia"]
})

# --- Layout premium ---

col1, col2 = st.columns([1,2])

with col1:
    st.markdown(f"""
    **💡 Dados Estatísticos**  
    - Média mensal: {df_media.avg_monthly_quantity.mean():.0f} unidades  
    - Mediana: {df_median.median_quantity.mean():.0f} unidades  
    - Mínimo: {df_min_max.min_quantity.min():.0f} unidades  
    - Máximo: {df_min_max.max_quantity.max():.0f} unidades  
    - Amplitude: {df_amplitude.amplitude.mean():.0f} unidades 
    - Desvio padrão: {df_desvio_padrao.stddev_quantity.mean():.0f} unidades
    """)
    st.info(""" 🧠 As vendas mensais mostraram alta variabilidade com desvio padrão de 445 unidades.""")
    st.info(""" 🧠 Amplitude de 1477 unidades, variando de 363 (fevereiro) a 1840 (novembro) """)
    st.info(""" 🧠 Concentração significativa das vendas no último trimestre (setembro a dezembro).""")
    st.info(""" 🧠 A média (1040) é superior à mediana (886), indicando que picos de fim de ano elevam a média.""")

with col2:
    # --- Histograma de frequência por faixa ---
    fig_hist = px.bar(
        df_faixa,
        x="faixa_venda",
        y="frequencia",
        text=df_faixa["frequencia"],
        labels={"faixa_venda":"Faixa de Venda", "frequencia":"Número de Produtos"},
        title="Frequência de Produtos por Faixa de Quantidade"
    )
    
    # --- Boxplot dos quartis ---
    fig_box = go.Figure()
    fig_box.add_trace(go.Box(
        y=[df_quartiles["min_value"], df_quartiles["max_value"]],  # min, max e quartis
        boxpoints="all",
        jitter=0.5,
        pointpos=-1.8,
        name="Quantidade de Vendas",
        marker_color="lightblue"
    ))
    fig_box.update_layout(title="Distribuição de Quartis (Min, Q1, Mediana, Q3, Max)")

    # Mostrar os dois gráficos lado a lado
    st.plotly_chart(fig_hist, use_container_width=True)
    st.plotly_chart(fig_box, use_container_width=True)

# ---------------------------
# Bloco 6 — Conclusão Executiva
# ---------------------------
st.subheader("📌 Conclusão")

st.markdown("""
    A análise de 2017 revelou insights cruciais para a Superstore:

    1. **Rentabilidade Crítica em Furniture:** Apesar do alto volume de vendas, a categoria Furniture apresentou margem de lucro de apenas 1%, impactando negativamente a lucratividade geral. Recomenda-se revisar estratégias de precificação e custos nessa categoria.

    2. **Dependência Operacional de Office Supplies:** Com 62% do volume total vindo de Office Supplies, há um risco operacional significativo. Diversificar o portfólio e melhorar a eficiência em outras categorias pode mitigar esse risco.

    3. **Sazonalidade Marcante no Q4:** O quarto trimestre concentrou a maior parte das vendas, exigindo planejamento cuidadoso de estoque e logística para atender à demanda sem incorrer em custos excessivos.

    📊 **Recomendações Estratégicas:**
    - Focar em aumentar a rentabilidade de Furniture através de otimização de custos e revisão do mix de produtos.
    - Diversificar esforços de marketing e vendas para reduzir a dependência de Office Supplies.
    - Planejar promoções e estoques com base na sazonalidade identificada, especialmente para o Q4.

    Implementar essas ações pode melhorar significativamente a saúde financeira e operacional da Superstore em anos futuros.

""")

st.success("Dashboard finalizado com foco em decisão estratégica.")
