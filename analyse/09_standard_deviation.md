# Desvio Padrão das Vendas Mensais — 2017

## Objetivo da Análise

Medir o **desvio padrão das vendas mensais** no ano de 2017, respondendo à pergunta:

> O quanto as vendas mensais **se afastam da média** ao longo do ano?

O desvio padrão é uma medida fundamental de **variabilidade** e indica se os dados estão **concentrados** ou **dispersos** em torno da média.

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
    ROUND(STDDEV(total_quantity_month)) AS stddev_quantity
FROM monthly_quantity;
````

---

## Resultado

| Métrica           | Valor            |
| ----------------- | ---------------- |
| **Desvio padrão** | **445 unidades** |

---

## Interpretação Estatística

* A **média mensal** em 2017 foi de **1.039,67 unidades**
* O **desvio padrão** de **445 unidades** indica que, em média:

  * As vendas mensais variam **±445 unidades** em torno da média

Isso representa aproximadamente **43% da média**, o que caracteriza **alta dispersão**.

---

## 🔗 Conexão com Outras Medidas

| Medida        | Valor    |
| ------------- | -------- |
| Média         | 1.039,67 |
| Mediana       | 886      |
| Desvio padrão | 445      |
| Amplitude     | 1.477    |

* A grande distância entre **média e mediana** já indicava assimetria
* O alto desvio padrão **confirma a instabilidade mensal**
* A amplitude elevada reforça a presença de meses extremos

---

## Interpretação de Negócio

* As vendas **não são consistentes** ao longo do ano
* Existem meses com desempenho **muito acima** e **muito abaixo** do padrão
* Planejamento baseado apenas na média **é arriscado**

A mediana e os quartis representam melhor o comportamento típico do negócio.

---

## Limitações do Desvio Padrão

✔ Mede bem a variabilidade
✔ Essencial para detectar instabilidade

Sensível a:

* Outliers
* Meses de pico (ex: Q4)

Deve sempre ser analisado junto com mediana e quartis.

---

## Conclusão

O desvio padrão de **445 unidades** evidencia que as vendas mensais em 2017 apresentaram **alta variabilidade**, reforçando que:

* O desempenho mensal é irregular
* Há forte efeito de sazonalidade
* Estratégias precisam considerar meses fracos e picos