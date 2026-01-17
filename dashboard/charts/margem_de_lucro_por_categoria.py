import streamlit as st
import plotly.express as px
from utils.formatting import abbreviate_number

def render_margem_de_lucro_por_categoria_markdown():
    st.info("""
    A margem de lucro da categoria **Furniture** foi de apenas 1%, enquanto **Technology** e **Office Supplies** 
    operaram com margens saudáveis (19% e 16%, respectivamente). 
    Essa diferença revela uma ineficiência estrutural na categoria **Furniture**.
    """)

def render_margem_de_lucro_por_categoria_chart(df_kpi):

    rank_colors = ["#1f77b4", "#2ca02c", "#d62728"]

    df_margin = df_kpi.sort_values("profit_margin", ascending=False).reset_index(drop=True)
    df_margin["color"] = rank_colors[:len(df_margin)]

    fig_margin = px.bar(
        df_margin,
        x="category",
        y="profit_margin",
        text=df_margin["profit_margin"].apply(lambda x: f"{x:.0%}"),
        labels={
            "category": "Categoria",
            "profit_margin": "Margem de Lucro"
        },
        color="category",
        color_discrete_map=df_margin.set_index("category")["color"].to_dict(),
        title="Margem de Lucro por Categoria — 2017"
    )

    fig_margin.update_layout(
        yaxis_tickformat=".0%",
        xaxis_title=None,
        title_x=0.5,
        uniformtext_minsize=10,
        uniformtext_mode="hide"
    )

    st.plotly_chart(fig_margin, use_container_width=True)
    