# SMART — Objetivos da Análise

## Objetivo Geral

Analisar o desempenho de vendas por categoria no ano de **2017**, com foco em **volume**, **participação relativa** e **estabilidade ao longo do tempo**, para apoiar decisões estratégicas de priorização comercial e operacional.

---

## Objetivos SMART

### 🔹 **S — Específico (Specific)**

Avaliar **como cada categoria de produto performou em 2017**, identificando:

* Volume total de vendas por categoria
* Participação percentual de cada categoria no total
* Distribuição mensal das vendas
* Estabilidade e variabilidade do volume ao longo do ano

> Escopo claramente definido: **Categorias + Ano de 2017 + Volume de vendas**

---

### 🔹 **M — Mensurável (Measurable)**

A análise será baseada em métricas quantitativas objetivas:

#### Métricas de Volume

* Quantidade total vendida
* Frequência absoluta
* Frequência relativa
* Frequência acumulada
* Classificação de Pareto (A, B, C)

#### Métricas Estatísticas

* Média mensal
* Mediana mensal
* Moda (faixa de maior frequência)
* Quartis (Q1, Q2, Q3, Q4)
* Mínimo e máximo
* Amplitude
* Variância
* Desvio padrão

Essas métricas permitem medir **nível**, **concentração** e **variabilidade** das vendas.

---

### 🔹 **A — Alcançável (Achievable)**

Os objetivos são alcançáveis porque:

* Os dados de vendas estão disponíveis no dataset Superstore
* O modelo dimensional (*Star Schema*) já foi implementado
* As análises serão realizadas exclusivamente com **SQL (MySQL 8)**
* Não há dependência de fontes externas ou ferramentas avançadas

---

### 🔹 **R — Relevante (Relevant)**

O objetivo é relevante para o negócio porque:

* Permite identificar categorias críticas em volume
* Apoia decisões de:

  * Planejamento de estoque
  * Priorização comercial
  * Alocação de recursos operacionais
* Evita decisões baseadas apenas em percepção ou médias gerais

Além disso, cria uma **base sólida** para análises futuras de:

* Receita
* Margem
* Rentabilidade
* Previsão de demanda

---

### 🔹 **T — Temporal (Time-bound)**

A análise está delimitada ao período de:

* **Ano de 2017**

E será concluída:

* Após a execução das análises estatísticas descritivas
* Com documentação completa das etapas **Ask → Prepare → Analyze**

---

## Critérios de Sucesso

A análise será considerada bem-sucedida se:

* For possível identificar claramente:

  * A categoria de maior volume
  * A concentração das vendas (Pareto)
  * Categorias mais estáveis vs. mais voláteis
* As conclusões forem suportadas por métricas estatísticas
* Os insights puderem ser compreendidos por stakeholders não técnicos

---

## Alinhamento com o Negócio

Este SMART garante que:

* Cada consulta SQL responde a uma pergunta específica
* Cada métrica tem um propósito claro
* A análise gera **valor prático**, não apenas números
