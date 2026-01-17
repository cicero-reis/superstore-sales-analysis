import streamlit as st
import plotly.express as px
from utils.formatting import abbreviate_number

def render_lucro_total_por_categoria_markdown():
    st.info("""
    Apesar de apresentar um volume de vendas semelhante às outras categorias, **Furniture** gerou lucro significativamente inferior, 
    representando apenas uma pequena fração do lucro total da empresa. 
    Em contraste, **Technology** e **Office Supplies** concentram a maior parte da rentabilidade.
    """)

def render_lucro_total_por_categoria_chart(df_kpi):

    rank_colors = ["#1f77b4", "#2ca02c", "#d62728"]

    df_profit = df_kpi.sort_values("total_profit", ascending=False).reset_index(drop=True)
    df_profit["color"] = rank_colors[:len(df_profit)]

    fig_profit = px.bar(
        df_profit,
        x="category",
        y="total_profit",
        text_auto=".2s",
        labels={
            "category": "Categoria",
            "total_profit": "Lucro Total"
        },
        color="category",
        color_discrete_map=df_profit.set_index("category")["color"].to_dict(),
        title="Lucro Total por Categoria — 2017"
    )

    fig_profit.update_layout(
        yaxis_tickprefix="$",
        xaxis_title=None,
        title_x=0.5,
        uniformtext_minsize=10,
        uniformtext_mode="hide"
    )

    st.plotly_chart(fig_profit, use_container_width=True)
    