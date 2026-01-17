# Superstore Sales Analysis — Vendas por Categoria (2017)

**Análise de Dados com foco em Performance por Categoria**

---

## Visão Geral

Este projeto tem como objetivo analisar as **vendas do ano de 2017**, com foco no **desempenho por categoria de produto** e no **comportamento temporal das vendas**, fornecendo insights estratégicos para apoio à tomada de decisão executiva.

Categorias analisadas:

* **Office Supplies**
* **Furniture**
* **Technology**

A análise busca oferecer aos **stakeholders** uma visão clara sobre:

* Volume de vendas
* Distribuição mensal
* Variabilidade e estabilidade operacional
* Padrões estatísticos de comportamento ao longo do ano

---

## Pergunta Central de Negócio

> **Como foi o desempenho de vendas por categoria no ano de 2017 e quais categorias concentram maior volume e maior estabilidade operacional?**

---

## Objetivos da Análise

* Identificar quais categorias concentram maior volume de vendas em 2017
* Avaliar a distribuição mensal das vendas
* Entender o grau de variabilidade (estabilidade vs. volatilidade)
* Apoiar decisões de priorização operacional e estratégica

---

## Escopo da Análise

* **Período:** Ano de 2017
* **Métrica principal:** Quantidade vendida
* **Nível de análise:** Categoria de produto
* **Tipo de análise:** Estatística descritiva e análise exploratória

> **Limitação do projeto:**
> Este estudo **não avalia receita ou lucro**, focando exclusivamente no comportamento do **volume de vendas**. Análises financeiras ficam como etapa futura.

---

## Abordagem Analítica

A análise segue um processo estruturado inspirado no ciclo analítico:

**Ask → Prepare → Process → Analyze → Share → Act**

Foram aplicados conceitos práticos de **estatística descritiva diretamente em SQL**, garantindo rastreabilidade e clareza metodológica.

### Análise por Categoria

* Frequência absoluta e relativa
* Frequência acumulada
* Classificação Pareto (A, B, C)
* Comparação entre categorias

### Medidas de Tendência Central

* Média mensal
* Mediana mensal
* Moda (faixa de vendas mais frequente)

### Medidas de Dispersão e Variabilidade

* Quartis (Q1, Q2, Q3, Q4)
* Mínimo e Máximo
* Amplitude
* Variância
* Desvio padrão

Essas medidas permitem avaliar **não apenas quanto se vende**, mas **quão previsível e estável é cada categoria ao longo do tempo**.

---

## Principais Insights (Resumo Executivo)

* **Office Supplies**

  * Maior volume de vendas em 2017
  * Categoria Classe A no Pareto (≈62% do volume total)
  * Alta relevância operacional e previsibilidade

* **Furniture**

  * Volume intermediário
  * Alta variabilidade mensal
  * Presença de meses extremos (outliers), indicando instabilidade operacional

* **Technology**

  * Menor volume relativo
  * Contribuição concentrada em poucos períodos
  * Potencial para análises futuras por valor (receita e margem)

> A análise demonstra que **alto volume não implica necessariamente estabilidade**, reforçando a importância de olhar além da média.

---

## Uso de IA como Apoio Analítico

A IA generativa foi utilizada exclusivamente como ferramenta de apoio, após a realização das análises estatísticas e consultas SQL.

### Como a IA foi utilizada

* Apoiar a síntese de insights
* Melhorar a clareza da comunicação executiva
* Servir como revisão crítica do raciocínio analítico

### O que NÃO foi feito pela IA

* Nenhuma métrica estatística foi calculada pela IA
* Nenhuma consulta SQL foi gerada automaticamente
* Nenhuma decisão analítica foi tomada sem validação nos dados

Todas as análises estatísticas, consultas SQL e interpretações de negócio foram desenvolvidas **manualmente**, com a IA atuando apenas como **suporte cognitivo e revisão crítica**.

**Tecnologias de IA utilizadas:**

* **LangChain**
* **LLM Gemini**

> A abordagem reflete um uso responsável e profissional de IA, alinhado às práticas atuais do mercado.

---

## Tecnologias Utilizadas

* **MySQL 8**

  * Limpeza, modelagem e análise dos dados
  * CTEs e funções analíticas
* **SQL**

  * Estatística aplicada diretamente no banco
* **Docker**

  * Ambiente reprodutível
* **Git / GitHub**

  * Versionamento e portfólio

---

## Estrutura do Repositório

```
Superstore-Sales-Analysis/
│
├── README.md
│
├── llm/
│   ├── FastApi/langChain/LLM
│
├── dashboard/
│   ├── streamlit
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
│   └── Sow.md
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

## Modelo Dimensional (Star Schema)

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

## Entregáveis

* Análise de vendas por categoria (2017)
* Classificação Pareto
* Análise estatística descritiva completa
* Insights explicados com racional analítico
* Documentação orientada a negócio

---

## Demonstração

![Demo do projeto](assets/demo.gif)

---

## Autor

**Cicero Reis**
Analista de Dados em desenvolvimento
Foco em **SQL**, **Estatística Aplicada** e **Análise de Negócio**
