import streamlit as st
import plotly.express as px
from utils.formatting import abbreviate_number

def render_quantidade_total_por_vendida_por_categoria_markdown():
    st.info(""" 🧠
    A categoria **Office Supplies** lidera em quantidade vendida, sendo responsável pela maior parte do volume operacional. 
    **Furniture** e **Technology** apresentam volumes semelhantes, porém muito inferiores ao líder.
    """)

def render_quantidade_total_por_vendida_por_categoria_chart(df_kpi):

    rank_colors = ["#1f77b4", "#2ca02c", "#d62728"]

    # Ordena por volume
    df_volume = df_kpi.sort_values("total_quantity", ascending=False).reset_index(drop=True)
    df_volume["color"] = rank_colors[:len(df_volume)]

    fig_volume = px.bar(
        df_volume,
        x="category",
        y="total_quantity",
        text_auto=True,
        labels={
            "category": "Categoria",
            "total_quantity": "Quantidade Vendida"
        },
        color="category",
        color_discrete_map=df_volume.set_index("category")["color"].to_dict(),
        title="Quantidade Total Vendida por Categoria — 2017"
    )

    fig_volume.update_layout(
        xaxis_title=None,
        title_x=0.5,
        uniformtext_minsize=10,
        uniformtext_mode="hide"
    )

    st.plotly_chart(fig_volume, use_container_width=True)