# Média das Vendas Mensais — 2017

## Objetivo da Análise

Calcular a **média de vendas mensais** no ano de 2017 para entender o **nível médio de volume vendido por mês**.

Esta métrica responde à pergunta:

> “Em média, quantas unidades a empresa vende por mês em 2017?”

---

## Base de Dados

- **Tabela fato:** `fact_sales`
- **Tabela dimensão:** `dim_date`
- **Métrica:** Quantidade vendida (`quantity`)
- **Período analisado:** Ano de 2017

---

## Cálculo da Média Mensal

### Consulta SQL

```sql
SET @varYear = 2017;

WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd 
        ON dd.date_key = fs.date_key
    WHERE dd.year = @varYear
    GROUP BY dd.year, dd.month
)
SELECT 
    ROUND(AVG(total_quantity_month), 2) AS avg_monthly_quantity
FROM monthly_quantity;
````

---

## Resultado

| Média mensal de vendas |
| ---------------------- |
| **1.039,67 unidades**  |

---

## Interpretação do Resultado

Em 2017, a empresa vendeu, em média, **aproximadamente 1.040 unidades por mês**.

Este valor representa um **indicador geral de volume**, útil para:

* Ter uma visão agregada do desempenho anual
* Comparar com outros anos
* Definir metas médias iniciais

---

## Observação Importante

A média é uma medida **sensível a valores extremos**.
Ela **não indica** se as vendas mensais foram estáveis ou concentradas em poucos meses com volumes muito altos.

Análises complementares (mediana, moda e dispersão) são necessárias para entender a **variabilidade** do comportamento mensal, mas **não fazem parte deste arquivo**.

---

## Conclusão

✔ A média mensal de vendas em 2017 foi **1.039,67 unidades**
✔ O valor fornece uma **visão geral**, mas não descreve a distribuição completa
✔ Serve como ponto de partida para análises mais profundas
