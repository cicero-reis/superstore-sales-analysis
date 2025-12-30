import streamlit as st
import plotly.express as px    

def render_overview_page(df_kpi):

    st.title("📌 Visão Geral")
    st.subheader("Análise de Rentabilidade por Categoria (2017)")

    st.markdown(
        """
        - **Technology** apresenta o maior valor agregado ao negócio, combinando alto faturamento,
        excelente margem (19%) e lucro por unidade elevado.
        - **Office Supplies** lidera em volume, mas com rentabilidade inferior,
        indicando necessidade de foco em eficiência operacional.
        - **Furniture** apresenta um claro desequilíbrio entre volume, receita e lucro,
        sugerindo problemas de precificação, custos ou mix de produtos.
        """
    )

    rank_colors = ["#1f77b4", "#2ca02c", "#d62728"]

    df_sales = df_kpi.sort_values("total_profit", ascending=False).reset_index(drop=True)
    df_sales["color"] = rank_colors[:len(df_sales)]

    fig_sales = px.bar(
        df_sales,
        x="category",
        y="total_sales",
        text=df_sales["total_sales"].apply(lambda x: f"${x:,.0f}"),
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


    # =========================
    # Lucro por Categoria
    # =========================

    st.subheader("💰 Lucro Total por Categoria (2017)")

    # Ordena para reforçar narrativa visual
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

    # =========================
    # Volume Vendido por Categoria
    # =========================

    st.subheader("📦 Volume Vendido por Categoria (2017)")

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

    # =========================
    # Margem de Lucro por Categoria
    # =========================

    st.subheader("📈 Margem de Lucro por Categoria (2017)")

    # Ordena por margem
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

    # =========================
    # Lucro por Unidade por Categoria
    # =========================

    st.subheader("💰 Lucro por Unidade por Categoria (2017)")

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

    st.markdown(
        """
        📌 Conclusão Executiva — 2017
        - Technology é a principal alavanca de valor do negócio.
        - Office Supplies sustenta escala com margem controlada.
        - Furniture requer revisão imediata de estratégia.
        """
    )