import streamlit as st
import plotly.express as px
from utils.formatting import abbreviate_number

def render_receita_total_por_categoria_markdown():
    st.info(""" 🧠
    Em **2017**, as três categorias apresentaram volumes de receita relativamente próximos, com destaque para **Technology**, 
    seguida por **Office Supplies** e **Furniture**. 
    Isso indica que Furniture não é uma categoria irrelevante em faturamento, pois gera quase o mesmo nível de vendas que as demais.
    """)

def render_receita_total_por_categoria_chart(df_kpi):

    rank_colors = ["#1f77b4", "#2ca02c", "#d62728"]

    df_sales = df_kpi.sort_values("total_profit", ascending=False).reset_index(drop=True)
    df_sales["color"] = rank_colors[:len(df_sales)]

    fig_sales = px.bar(
        df_sales,
        x="category",
        y="total_sales",
        text=df_sales["total_sales"].apply(lambda x: f"${abbreviate_number(x)}"),  # aqui usamos abbreviate_number
        labels={
            "category": "Categoria",
            "total_sales": "Receita Total"
        },
        color="category",
        color_discrete_sequence=df_sales["color"],
        title="Receita Total por Categoria — 2017"
    )


    fig_sales.update_layout(
        xaxis_title=None,
        title_x=0.5,
        uniformtext_minsize=10,
        uniformtext_mode="hide"
    )

    st.plotly_chart(fig_sales, use_container_width=True)