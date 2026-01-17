# Mediana das Vendas Mensais — 2017

## Objetivo da Análise

Calcular a **mediana das vendas mensais** no ano de 2017 para identificar o **valor central da distribuição**, reduzindo a influência de meses com vendas extremamente altas ou baixas.

Esta métrica responde à pergunta:

> “Qual é o volume de vendas mensal que representa o ponto central do ano de 2017?”

---

## Base de Dados

- **Tabela fato:** `fact_sales`
- **Tabela dimensão:** `dim_date`
- **Métrica:** Quantidade vendida (`quantity`)
- **Período analisado:** Ano de 2017
- **Unidade de análise:** Vendas agregadas por mês

---

## Cálculo da Mediana Mensal

Como o MySQL não possui uma função nativa de mediana, foi utilizada uma abordagem baseada em:

- Ordenação dos valores mensais
- Numeração sequencial das linhas
- Seleção do(s) valor(es) central(is)

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
),
ordered_months AS (
    SELECT
        total_quantity_month,
        ROW_NUMBER() OVER (ORDER BY total_quantity_month) AS rn,
        COUNT(*) OVER () AS total_rows
    FROM monthly_quantity
)
SELECT 
    ROUND(AVG(total_quantity_month), 2) AS median_quantity
FROM ordered_months
WHERE rn IN (
    FLOOR((total_rows + 1) / 2),
    CEIL((total_rows + 1) / 2)
);
````

---

## Resultado

| Mediana mensal de vendas |
| ------------------------ |
| **886 unidades**         |

---

## Interpretação do Resultado

A mediana indica que:

* **50% dos meses** de 2017 tiveram vendas **iguais ou inferiores a 886 unidades**
* **50% dos meses** tiveram vendas **iguais ou superiores a 886 unidades**

Diferente da média, a mediana **não é influenciada por meses com picos elevados**, como novembro e dezembro.

---

## Comparação Conceitual (sem cálculo)

* **Média:** ~1.040 unidades
* **Mediana:** 886 unidades

A média ser maior que a mediana indica uma **distribuição assimétrica à direita**, puxada por meses com vendas muito altas no fim do ano.

---

## Observação Importante

A mediana é especialmente útil quando:

* Há **outliers**
* As vendas não são uniformes ao longo do tempo
* Deseja-se um valor central mais representativo do comportamento típico

Esta análise complementa — mas não substitui — a média.

---

## Conclusão

✔ A mediana mensal de vendas em 2017 foi **886 unidades**
✔ Representa melhor o comportamento típico mensal
✔ Confirma a presença de meses com vendas excepcionalmente altas
