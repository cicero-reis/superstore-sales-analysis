import streamlit as st
import plotly.express as px    

def render_monthly_distribution_page(df_monthly):

    st.title("Distribuição Mensal de Vendas — 2017")

    # Garantir ordem correta dos meses
    df_monthly = df_monthly.sort_values("month")

    fig = px.line(
        df_monthly,
        x="month",
        y="total_quantity_month",
        markers=True,
        title="Distribuição Mensal de Vendas — 2017"
    )

    fig.add_vrect(
        x0=9,
        x1=12,
        fillcolor="LightGrey",
        opacity=0.3,
        layer="below",
        line_width=0,
        annotation_text="Q4",
        annotation_position="top left"
    )

    fig.update_layout(
        xaxis=dict(
            tickmode="linear",
            tick0=1,
            dtick=1,
            title="Mês"
        ),
        yaxis=dict(
            title="Quantidade Vendida",
            range=[0, df_monthly["total_quantity_month"].max() * 1.1]
        ),
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        Em 2017, as vendas apresentaram forte concentração no último trimestre, 
        com destaque para novembro e dezembro, enquanto os primeiros meses do ano 
        tiveram volumes significativamente menores.        
        """
    )


