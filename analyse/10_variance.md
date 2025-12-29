# 📊 Variância das Vendas Mensais — 2017

## 🎯 Objetivo da Análise

Calcular a **variância das vendas mensais** no ano de 2017 para responder à pergunta:

> Qual é o grau de dispersão das vendas mensais em relação à média, em termos quadráticos?

A variância é uma medida estatística que **quantifica a variabilidade dos dados**, sendo a base para o cálculo do desvio padrão.

---

## 🗂️ Base de Dados

- **Tabela fato:** `fact_sales`
- **Dimensão de tempo:** `dim_date`
- **Métrica:** Quantidade vendida (`quantity`)
- **Período:** Ano de 2017
- **Granularidade:** Mensal

---

## 🔍 Consulta SQL Utilizada

```sql
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
    ROUND(VARIANCE(total_quantity_month)) AS variance_quantity    
FROM monthly_quantity;
````

---

## 📊 Resultado

| Métrica       | Valor       |
| ------------- | ----------- |
| **Variância** | **197.668** |

---

## 🧠 Interpretação Estatística

A variância mede o **desvio médio quadrático** em relação à média.

* Uma variância de **197.668** indica que:

  * Os valores mensais estão **fortemente dispersos**
  * Existe grande distância entre meses fracos e meses de pico

📌 Como a variância está em **unidades ao quadrado**, sua interpretação direta é menos intuitiva do que a do desvio padrão.

---

## 🔗 Relação com o Desvio Padrão

A variância e o desvio padrão estão diretamente ligados:

[
\sqrt{197.668} \approx 445
]

| Medida        | Valor   |
| ------------- | ------- |
| Variância     | 197.668 |
| Desvio padrão | 445     |

📌 Isso confirma a **consistência matemática** da análise.

---

## 📈 Interpretação de Negócio

* A alta variância confirma que as vendas mensais **não seguem um padrão estável**
* O negócio apresenta:

  * Meses de alta concentração de vendas (ex: Q4)
  * Meses com desempenho significativamente inferior

📌 Estratégias baseadas apenas em médias mensais **não refletem a realidade operacional**.

---

## ⚠️ Limitações da Variância

✔ Essencial para análises estatísticas
✔ Base para modelos analíticos mais avançados

❌ Pouco intuitiva para stakeholders
❌ Amplifica o impacto de valores extremos

📌 Deve ser usada como **apoio técnico**, enquanto o desvio padrão e quartis comunicam melhor o cenário.

---

## ✅ Conclusão

A variância de **197.668** reforça que as vendas mensais em 2017 apresentam **alta volatilidade**, exigindo:

* Planejamento sazonal
* Análises segmentadas por período
* Uso de métricas robustas (mediana, quartis)

---

## 🔜 Próximo Passo

Encerrar o bloco estatístico com:
👉 **Resumo executivo das medidas estatísticas**
