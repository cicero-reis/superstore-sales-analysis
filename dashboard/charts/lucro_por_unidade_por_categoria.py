import streamlit as st
import plotly.express as px
from utils.formatting import abbreviate_number

def render_lucro_por_unidade_por_categoria_markdown():
    st.info(""" 🧠
    O lucro por unidade vendida na categoria **Furniture** foi extremamente baixo quando comparado às demais. 
    **Technology** gera alto valor por item vendido, enquanto **Office Supplies** mantém uma rentabilidade intermediária, 
    mesmo com alto volume.
    """)

def render_lucro_por_unidade_por_categoria_chart(df_kpi):

    rank_colors = ["#1f77b4", "#2ca02c", "#d62728"]

    df_unit_profit = df_kpi.sort_values("profit_per_unit", ascending=False).reset_index(drop=True)
    df_unit_profit["color"] = rank_colors[:len(df_unit_profit)]

    fig_unit_profit = px.bar(
        df_unit_profit,
        x="category",
        y="profit_per_unit",
        text=df_unit_profit["profit_per_unit"].apply(lambda x: f"${x:,.2f}"),
        labels={
            "category": "Categoria",
            "profit_per_unit": "Lucro por Unidade"
        },
        color="category",
        color_discrete_map=df_unit_profit.set_index("category")["color"].to_dict(),
        title="Lucro por Unidade por Categoria — 2017"
    )

    fig_unit_profit.update_layout(
        xaxis_title=None,
        title_x=0.5,
        uniformtext_minsize=10,
        uniformtext_mode="hide"
    )

    st.plotly_chart(fig_unit_profit, use_container_width=True)
