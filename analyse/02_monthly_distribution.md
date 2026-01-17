# Distribuição Mensal de Vendas — 2017

## Objetivo da Análise

Analisar como o **volume de vendas (quantidade)** se distribuiu ao longo dos meses de **2017**, identificando:

- Meses de maior e menor volume
- Padrões de crescimento ou sazonalidade
- Picos e vales operacionais ao longo do ano

Esta análise ajuda stakeholders a entender **quando a operação é mais exigida** e **quando há retração nas vendas**.

---

## Base de Dados

- **Tabela fato:** `fact_sales`
- **Tabela de data:** `dim_date`
- **Métrica analisada:** Quantidade total vendida (`quantity`)
- **Período:** Ano de 2017

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
    INNER JOIN dim_date dd 
        ON dd.date_key = fs.date_key
    WHERE dd.year = @varYear
    GROUP BY dd.year, dd.month
)
SELECT * 
FROM monthly_quantity
ORDER BY month;
````

---

## 📊 Resultado da Consulta

| Ano  | Mês | Quantidade Vendida |
| ---- | --- | ------------------ |
| 2017 | 1   | 597                |
| 2017 | 2   | 363                |
| 2017 | 3   | 885                |
| 2017 | 4   | 733                |
| 2017 | 5   | 887                |
| 2017 | 6   | 931                |
| 2017 | 7   | 840                |
| 2017 | 8   | 884                |
| 2017 | 9   | 1660               |
| 2017 | 10  | 1133               |
| 2017 | 11  | 1840               |
| 2017 | 12  | 1723               |

---

## Análise dos Resultados

### Meses de Menor Volume

* **Fevereiro (363)** foi o mês com **menor quantidade vendida**
* Janeiro e abril também apresentam volumes relativamente baixos

Indica um início de ano mais fraco em termos de vendas.

---

### Meses de Maior Volume

* **Novembro (1.840)** foi o pico de vendas do ano
* Dezembro (1.723) e setembro (1.660) também se destacam

Forte concentração de vendas no **último trimestre**, sugerindo sazonalidade.

---

### Comportamento ao Longo do Ano

* Crescimento gradual a partir de março
* Estabilidade moderada entre março e agosto
* **Aceleração significativa a partir de setembro**
* Pico operacional no final do ano

---

## Insight de Negócio

### **Fato**

Em 2017, as vendas apresentaram forte **concentração no último trimestre**, com destaque para novembro e dezembro, enquanto os primeiros meses do ano tiveram volumes significativamente menores.

### **Impacto**

Essa distribuição indica **sazonalidade clara**, impactando diretamente planejamento de estoque, logística e capacidade operacional. A empresa precisa estar preparada para picos intensos no final do ano e possível ociosidade no início.

### **Ação Sugerida**

* Planejar estoque e logística com foco no **Q4**
* Avaliar campanhas comerciais para fortalecer vendas no **Q1 e Q2**
* Utilizar esses dados como base para análises estatísticas (média, mediana, dispersão)
