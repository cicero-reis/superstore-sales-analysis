# Mínimo e Máximo das Vendas Mensais — 2017

## Objetivo da Análise

Identificar os **extremos de vendas mensais** no ano de 2017 para responder:

- Qual foi o **pior mês** em volume de vendas?
- Qual foi o **melhor mês** em volume de vendas?
- Qual a **distância entre os extremos**?

Essa análise ajuda a entender **limites reais de desempenho**, não médias.

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
    MIN(total_quantity_month) AS min_quantity,    
    MAX(total_quantity_month) AS max_quantity
FROM monthly_quantity;
````

---

## Resultado

| Métrica           | Quantidade |
| ----------------- | ---------- |
| **Mínimo mensal** | 363        |
| **Máximo mensal** | 1840       |

---

## Interpretação de Negócio

### Mínimo (363 unidades)

* Representa o **pior desempenho mensal** em 2017
* Está localizado no **1º quartil (Q1)**
* Indica:

  * Período de baixa demanda
  * Possível sazonalidade negativa
  * Mês crítico para planejamento operacional

---

### Máximo (1840 unidades)

* Representa o **melhor desempenho mensal** do ano
* Está localizado no **4º quartil (Q4)**
* Classificado como **evento excepcional**
* Provavelmente associado a:

  * Sazonalidade positiva
  * Datas promocionais
  * Alta concentração de pedidos

---

## Conexão com Quartis e Medidas Centrais

| Medida  | Valor    | Contexto                  |
| ------- | -------- | ------------------------- |
| Mínimo  | 363      | Q1 — meses fracos         |
| Mediana | 886      | Q2 — comportamento normal |
| Moda    | 801–1000 | Faixa mais frequente      |
| Média   | 1.039,67 | Elevada pelo Q4           |
| Máximo  | 1.840    | Q4 — outlier positivo     |

A grande distância entre mínimo e máximo **confirma alta variabilidade** ao longo do ano.

---

## Conclusão Estatística

✔ Mínimo e máximo **não representam o comportamento típico**
✔ Devem ser usados para:

* Definir **limites operacionais**
* Avaliar **cenários extremos**
* Apoiar análise de risco

Não devem ser usados isoladamente para:

* Previsão
* Metas padrão
* Avaliação média de desempenho