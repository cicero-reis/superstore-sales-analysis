# 📊 Superstore Sales Analysis — Vendas por Categoria (2017)

**Análise de Dados com foco em Performance por Categoria**

---

## 🔹 Visão Geral

Este projeto tem como objetivo analisar as vendas do ano de 2017,
com foco em desempenho por categoria e comportamento temporal,
fornecendo insights estratégicos para tomada de decisão executiva:

* Office Supplies
* Furniture
* Technology

O objetivo é oferecer aos **stakeholders** uma visão clara sobre **volume de vendas**, **distribuição**, **variabilidade** e **padrões de comportamento** entre as categorias ao longo do ano.

---

## 🔹 Pergunta Central de Negócio

> **Como foi o desempenho de vendas por categoria no ano de 2017 e quais categorias concentram maior volume e estabilidade operacional?**

---

## 🔹 Objetivos da Análise

* Identificar quais categorias concentram maior volume de vendas em 2017
* Avaliar a distribuição mensal de vendas por categoria
* Entender o grau de variabilidade (estabilidade vs. volatilidade)
* Apoiar decisões de priorização operacional e estratégica

---

## 🔹 Escopo da Análise

* **Período:** Ano de 2017
* **Métrica principal:** Quantidade vendida
* **Nível de análise:** Categoria de produto
* **Tipo de análise:** Estatística descritiva e análise exploratória

> ⚠️ Este projeto **não avalia receita ou lucro**, apenas comportamento de volume, deixando explícita essa limitação para decisões futuras.

---

## 🔹 Abordagem Analítica

A análise segue um processo estruturado:

**Ask → Prepare → Process → Analyze → Share → Act**

Com aplicação prática de:

### 📌 Análise por Categoria

* Frequência absoluta e relativa
* Pareto (Classificação A, B e C)
* Comparação entre categorias

### 📌 Tendência Central

* Média mensal
* Mediana mensal
* Moda (faixa de vendas mais frequente)

### 📌 Dispersão e Variabilidade

* Quartis (Q1, Q2, Q3, Q4)
* Mínimo e Máximo
* Amplitude
* Variância
* Desvio padrão

Essas medidas permitem avaliar **não apenas quanto se vende**, mas **quão previsível e estável é cada categoria**.

---

## 🔹 Principais Insights (Resumo Executivo)

* **Office Supplies**

  * Maior volume de vendas em 2017
  * Categoria Classe A no Pareto (≈62% do volume)
  * Alta relevância operacional

* **Furniture**

  * Volume intermediário
  * Maior variabilidade mensal
  * Presença de meses extremos (outliers)

* **Technology**

  * Menor volume relativo
  * Contribuição concentrada
  * Potencial de análise futura por valor (receita/margem)

> 🔎 A análise mostra que **volume não implica necessariamente estabilidade**, reforçando a importância de olhar além da média.

---

## 🔹 Tecnologias Utilizadas

* **MySQL 8**

  * Limpeza e modelagem dos dados
  * CTEs e funções analíticas
* **SQL**

  * Análises estatísticas diretamente no banco
* **Docker**

  * Ambiente reprodutível
* **Git / GitHub**

  * Versionamento e portfólio

---

## 🔹 Estrutura do Repositório

```
Superstore-Sales-Analysis/
│
├── README.md
│
├── database/
│   ├── superstore.csv
│   ├── superstore.xls
│
├── docs/
│   ├── Act.md
│   ├── Analyze.md
│   ├── Ask.md
│   ├── ChangeLog.md
│   ├── Prepare.md
│   ├── Process.md
│   ├── Share.md
│   ├── Smart.md
│   ├── Sow.md
│   └── Summary.md
│
├── prepare/
│   ├── 01_prepare_dates.md
│   ├── 02_prepare_numbers.md
│   ├── 03_dim_customer.md
│   ├── 04_dim_product.md
│   ├── 05_dim_order.md
│   ├── 06_dim_date.md
│   └── 07_fact_sales.md
│
├── analyse/   
│   ├── 01_profitability_by_category.md
│   ├── 02_monthly_distribution.md
│   ├── 03_media.md
│   ├── 04_median.md
│   ├── 05_moda.md
│   ├── 06_quartiles.md
│   ├── 07_min_max.md
│   ├── 08_amplitude.md
│   ├── 09_standard_deviation.md
│   └── 10_variance.md
```

---

## 🔹 Modelo Dimensional (Star Schema)

```
                 dim_customer
                       ▲
                       │
                 ┌─────┼─────┐
                 │     │     │
           dim_product │  dim_order
                 ▲     │     ▲
                 │     │     │
                 └─────┼─────┘
                       │
                  fact_sales
                       │
                       ▼
                  dim_date
```

---

## 🔹 Entregáveis

* Análise de vendas por categoria (2017)
* Classificação Pareto
* Análise estatística completa
* Insights explicados com racional analítico
* Documentação orientada a negócio

---

## 🔹 Autor

**Cicero Reis**
Analista de Dados em desenvolvimento
Foco em SQL, Estatística Aplicada e Análise de Negócio
