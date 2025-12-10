# 📊 Superstore Sales Analysis

**Projeto de Análise de Dados — Portfólio Analista de Dados (Iniciante)**

---

## 🔹 **Descrição do Projeto**

Este projeto utiliza o dataset **Superstore Sales** (Tableau/Kaggle) para realizar uma análise completa de vendas, lucros, descontos e performance por região e categoria.
O objetivo é identificar padrões, oportunidades de melhoria e gerar insights acionáveis para otimização de vendas e lucratividade.

O projeto segue o ciclo **DAA (Data Analysis Approach)**:

1. **Perguntar (Ask)** — Definir perguntas e objetivos SMART
2. **Preparar (Prepare)** — Limpeza e padronização dos dados no MySQL 8
3. **Processar (Process)** — Transformações, agregações e cálculos avançados
4. **Analisar (Analyze)** — Extração de insights, rankings e tendências
5. **Compartilhar (Share)** — Visualizações, gráficos e relatórios
6. **Agir (Act)** — Recomendações de negócio baseadas na análise

---

## 🔹 **Objetivos SMART**

* Identificar os produtos que mais geram prejuízo
* Avaliar performance de vendas e lucro por região
* Analisar o impacto de descontos na lucratividade

> Todos os objetivos possuem métricas mensuráveis e prazo de entrega de análise.

---

## 🔹 **Tecnologias Utilizadas**

* **Banco de dados:** MySQL 8
* **Linguagem de Análise:** SQL, Python (Jupyter Notebooks)
* **Visualização:** Matplotlib / Seaborn / Tableau
* **Controle de versão:** Git / GitHub

---

## 🔹 **Estrutura do Repositório**

```
Superstore-Sales-Analysis/
│
├── README.md
├── data/
│   ├── superstore.csv
│   └── superstore_clean.csv
├── sql/
│   ├── 01_import_prepare.sql
│   ├── 02_cte_window_functions.sql
│   └── 03_aggregations.sql
├── notebooks/
│   ├── EDA_Superstore.ipynb
│   └── Insights_Analysis.ipynb
├── docs/
│   ├── Ask.md
│   ├── Prepare.md
│   ├── Process.md
│   ├── Analyze.md
│   ├── Share.md
│   ├── Act.md
│   ├── SMART.md
│   └── SOW.md
└── visuals/
    ├── sales_trends.png
    ├── profit_by_category.png
    └── region_ranking.png
```

---

## 🔹 **Como Usar**

1. Clonar o repositório:

```bash
git clone https://github.com/seu-usuario/Superstore-Sales-Analysis.git
```

2. Importar o dataset para o MySQL:

```sql
LOAD DATA INFILE '/caminho/para/superstore.csv' INTO TABLE superloja
FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
```

3. Executar scripts SQL na ordem:

```text
01_import_prepare.sql → 03_aggregations.sql → 02_cte_window_functions.sql
```

4. Abrir notebooks Jupyter para análise visual e insights.

---

## 🔹 **Entregáveis do Projeto**

* Dados limpos e estruturados (MySQL)
* Notebooks com análises e gráficos
* Relatório analítico detalhado (PDF/Markdown)
* Visualizações: tendências, rankings, KPIs

---

## 🔹 **Autor**

**Cicero Reis** — Analista de Dados em desenvolvimento
📧 Email: [cicero@email.com](mailto:cicero@email.com)
🌐 GitHub: [github.com/seu-usuario](https://github.com/seu-usuario)

---

