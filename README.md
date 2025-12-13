# 📊 Superstore Sales Analysis

**Projeto de Análise de Dados**

---

## 🔹 **Descrição do Projeto**

Este projeto utiliza o dataset **Superstore Sales** (Tableau) para estudar conceitos essenciais de análise de dados: limpeza, preparação, criação de perguntas, definição de objetivos SMART e organização dos dados em um modelo dimensional (*Star Schema*).

O foco principal é entender:

* Como preparar dados reais para análise
* Como transformar dados brutos em informações úteis
* Como construir perguntas de negócio simples e objetivas
* Como documentar bem o processo (Ask → Prepare → SOW → SMART)

---

## 🔹 **Perguntas de Negócio (Ask)**

1. **Como estão as vendas atualmente?**
2. **Quais produtos vendem mais?**
3. **A empresa está tendo lucro?**
4. **Quem são nossos principais clientes?**
5. **Onde vendemos mais?**
6. **O desconto está ajudando ou atrapalhando?**

---

## 🔹 **SMART**

* **S (Específico):** Identificar níveis atuais de vendas, lucro e produtos mais vendidos.
* **M (Mensurável):** Medir quantidade vendida, total de vendas, total de lucro e impacto dos descontos.
* **A (Alcançável):** Utilizar apenas SQL e dados da Superstore.
* **R (Relevante):** Informações essenciais para entender o desempenho básico da loja.
* **T (Temporal):** Concluir a análise inicial até o final do estudo do módulo *Prepare*.

---

## 🔹 **Tecnologias Utilizadas**

* **MySQL 8** — limpeza, normalização e criação das tabelas dimensionais
* **SQL** — consultas, CTEs e window functions
* **Git / GitHub** — versionamento e portfólio
* **(Opcional futuramente)** Tableau para visualização

> Por enquanto, o projeto está focado nas fases **Ask** e **Prepare**.

---

## 🔹 **Estrutura do Repositório**

```
Superstore-Sales-Analysis/
│
├── README.md
│
├── data/
│   ├── superstore.csv
│   ├── superstore.xls
├── docker/
│   ├── docker-compose.yml
│   ├── mysql-init.sql
│── docs/
│   ├── Ask.md
│   ├── SMART.md
│   ├── Prepare.md
│   └── SOW.md
├── sql/
│   ├── 01_prepare_dates.sql
│   ├── 02_prepare_numbers.sql
│   ├── 03_dim_customer.sql
│   ├── 04_dim_product.sql
│   ├── 05_dim_order.sql
│   ├── 06_dim_date.sql
│   └── 07_fact_sales.sql
│   
```

## 🔹 **Star Schema**

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

---

## 🔹 **Entregáveis**

* Tabela original corrigida
* Tabelas dimensionais (dim_customer, dim_product, dim_order, dim_date)
* Tabela fato (fact_sales)
* Documentação clara (Ask, SMART, Prepare, SOW)
* README estruturado para portfólio

---

## 🔹 **Autor**

**Cicero Reis**
Analista de Dados em desenvolvimento
