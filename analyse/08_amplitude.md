# Amplitude das Vendas Mensais — 2017

## Objetivo da Análise

Medir a **amplitude das vendas mensais** no ano de 2017, respondendo à pergunta:

> Qual é a **diferença entre o melhor e o pior mês** em volume de vendas?

A amplitude mostra o **intervalo total de variação** dos dados.

---

## Base de Dados

- **Tabela fato:** `fact_sales`
- **Dimensão de tempo:** `dim_date`
- **Métrica:** Quantidade vendida (`quantity`)
- **Período:** Ano de 2017
- **Granularidade:** Mensal

---

## Consulta SQL Utilizada

```sql
SET @varYear = 2017;

WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd ON dd.date_key = fs.date_key
    WHERE dd.year = @varYear
    GROUP BY dd.year, dd.month
)
SELECT
    MAX(total_quantity_month) - MIN(total_quantity_month) AS amplitude
FROM monthly_quantity;
````

---

## Resultado

| Métrica       | Valor              |
| ------------- | ------------------ |
| **Amplitude** | **1.477 unidades** |

---

## Interpretação de Negócio

* O pior mês de 2017 teve **363 unidades vendidas**
* O melhor mês de 2017 teve **1.840 unidades vendidas**
* A diferença entre esses extremos foi de **1.477 unidades**

Isso indica que o desempenho mensal **variou drasticamente** ao longo do ano.

---

## 🔗 Conexão com Análises Anteriores

| Medida    | Valor    |
| --------- | -------- |
| Mínimo    | 363      |
| Máximo    | 1.840    |
| Amplitude | 1.477    |
| Mediana   | 886      |
| Moda      | 801–1000 |
| Média     | 1.039,67 |

* A **amplitude é maior que a mediana**
* A **média está deslocada para cima**, influenciada pelos meses de pico
* Confirma a presença de **valores extremos (Q4)**

---

## Limitações da Amplitude

✔ Fácil de interpretar
✔ Mostra rapidamente o intervalo total

Não informa:

* Frequência dos extremos
* Distribuição interna
* Comportamento típico

Por isso, a amplitude **não deve ser usada sozinha** para análise de desempenho.

---

## Conclusão

A amplitude de **1.477 unidades** confirma que as vendas mensais em 2017 apresentaram **alta volatilidade**, reforçando a necessidade de:

* Medidas de dispersão mais robustas
* Análise de sazonalidade
* Uso combinado com **desvio padrão e variância**
