# 📊 Quartis das Vendas Mensais — 2017

## 🎯 Objetivo da Análise

Dividir as vendas mensais de 2017 em **quatro partes iguais (quartis)** para entender:

- A **distribuição dos meses**
- Quais valores representam comportamento **normal**
- Quais meses são **excepcionais (picos ou quedas)**

Esta análise responde à pergunta:

> “Como as vendas mensais se distribuem ao longo do ano?”

---

## 🗂️ Base de Dados

- **Tabela fato:** `fact_sales`
- **Tabela dimensão:** `dim_date`
- **Métrica:** Quantidade vendida (`quantity`)
- **Período:** 2017
- **Granularidade:** Mensal

---

## 🧮 Conceito de Quartis

| Quartil | Interpretação |
|------|--------------|
| Q1 | 25% dos meses com menores vendas |
| Q2 | 50% dos meses (mediana) |
| Q3 | 75% dos meses |
| Q4 | 25% dos meses com maiores vendas |

---

## 🔍 Consulta SQL Utilizada

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
ordered AS (
    SELECT
        total_quantity_month,
        NTILE(4) OVER (ORDER BY total_quantity_month) AS quartil
    FROM monthly_quantity
)
SELECT
    quartil,
    MIN(total_quantity_month) AS min_value,
    MAX(total_quantity_month) AS max_value
FROM ordered
GROUP BY quartil
ORDER BY quartil;
````

---

## 📊 Resultado dos Quartis

| Quartil | Mínimo | Máximo |
| ------- | ------ | ------ |
| Q1      | 363    | 733    |
| Q2      | 840    | 885    |
| Q3      | 887    | 1133   |
| Q4      | 1660   | 1840   |

---

## 🧠 Interpretação de Negócio

### 🔹 Q1 — Meses de Baixa Performance

* Intervalo: **363 a 733**
* Representa os **25% piores meses**
* Possíveis causas:

  * Sazonalidade negativa
  * Menor demanda
  * Períodos de baixa operação

---

### 🔹 Q2 — Comportamento Normal (Mediana)

* Intervalo: **840 a 885**
* Contém a **mediana (886)** ou muito próxima
* Representa o **padrão típico de vendas mensais**
* Base sólida para planejamento

---

### 🔹 Q3 — Meses Acima do Padrão

* Intervalo: **887 a 1133**
* Meses com desempenho **acima da normalidade**
* Possível impacto de:

  * Campanhas
  * Datas promocionais
  * Crescimento pontual

---

### 🔹 Q4 — Meses Excepcionais

* Intervalo: **1660 a 1840**
* Forte distanciamento dos quartis anteriores
* Indica **outliers positivos**
* Alta probabilidade de:

  * Eventos sazonais fortes
  * Datas comerciais (ex: fim de ano)

---

## 📌 Relação com Outras Medidas Estatísticas

| Medida       | Valor    | Onde se Encaixa      |
| ------------ | -------- | -------------------- |
| Mediana      | 886      | Dentro do Q2         |
| Moda (faixa) | 801–1000 | Entre Q2 e Q3        |
| Média        | 1.039,67 | Influenciada pelo Q4 |

📍 O **Q4 distorce a média**, confirmando que a mediana é mais representativa do comportamento normal.

---

## ⚠️ Conclusão Estatística

✔ A maioria dos meses está concentrada entre **Q2 e Q3**
✔ **Q4 representa meses excepcionais**, não recorrentes
✔ **Planejamento operacional** deve se basear em Q2/Q3
✔ **Metas agressivas** podem considerar Q4 como referência superior