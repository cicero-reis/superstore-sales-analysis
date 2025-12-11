# ✅ **1. Criar a tabela `fact_sales`**

```sql
CREATE TABLE fact_sales (
    fact_id INT AUTO_INCREMENT PRIMARY KEY,

    -- Foreign Keys
    date_key INT NOT NULL,
    order_key   INT NOT NULL,
    product_key INT NOT NULL,
    customer_key INT NOT NULL,

    -- Measures
    quantity INT NOT NULL,
    sales DECIMAL(10,2) NOT NULL,
    discount DECIMAL(10,2) NOT NULL,
    profit DECIMAL(10,2) NOT NULL,

    -- FK constraints
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (order_key) REFERENCES dim_order(order_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key)
);
```

---

# ✅ **2. Popular a fato com base na tabela original**

```sql
INSERT INTO fact_sales (
	date_key,
    order_key,
    product_key,
    customer_key,    
    quantity,
    sales,
    discount,
    profit
)
SELECT
    DATE_FORMAT(s.order_date_clean, '%Y%m%d') AS date_key,
    o.order_key,
    p.product_key,
    c.customer_key,    
    s.Quantity,
    s.sales_clean,
    s.discount_clean,
    s.profit_clean
FROM superstore s
JOIN dim_order o
    ON s.`Order ID` = o.order_id
JOIN dim_product p
    ON s.`Product ID` = p.product_id
JOIN dim_customer c
    ON s.`Customer ID` = c.customer_id;
```

---

✅ 1. Verificar
```sql

SELECT
(SELECT COUNT(*) FROM superstore) as total_superstore,
(SELECT COUNT(*) FROM fact_sales) as total_fact_sales

SELECT
(
    SELECT 
        COUNT(*) 
    FROM superstore s 
    where s.`Order ID` = 'CA-2014-115812'
) as 'total_superstore',
(
    SELECT 
	    COUNT(*)
    FROM fact_sales f 
    JOIN dim_order d ON d.order_key = f.order_key
    WHERE d.order_id = 'CA-2014-115812'
) as 'total_fact_sales';

SELECT 
	s.`Order ID`, s.Quantity, s.order_date_clean, s.`Customer Name`
FROM superstore s 
WHERE s.`Order ID` = 'CA-2014-115812';

SELECT 
	d.order_id, f.quantity, d.order_date, d2.customer_name
FROM fact_sales f 
JOIN dim_order d ON d.order_key = f.order_key
JOIN dim_customer d2 ON d2.customer_key = f.customer_key
WHERE d.order_id = 'CA-2014-115812';
```
---

# ✅ 2. Verificar se todas as chaves estrangeiras foram resolvidas corretamente

## **2.1. Ver linhas com dimensões faltando (deveria retornar 0)**

```sql
SELECT *
FROM fact_sales
WHERE order_key IS NULL
   OR product_key IS NULL
   OR customer_key IS NULL;
```

Se retornar **0**, está OK.
---

# ✅ 3. Verificar se os valores numéricos foram importados corretamente

---

# 🧪 **3.1. Soma de Sales**

### Soma da tabela original:

```sql
SELECT SUM(REPLACE(Sales, ',', '.') + 0) AS total_sales_superstore
FROM superstore;
```

### Soma da tabela fato:

```sql
SELECT SUM(sales) AS total_sales_fact
FROM fact_sales;
```

✔ **Os valores devem ser iguais (ou diferir apenas por arredondamento pequeno).**

---

# 🧪 **3.2. Soma de Quantity**

```sql
SELECT SUM(Quantity) FROM superstore;
SELECT SUM(quantity) FROM fact_sales;
```

➡ Devem bater exatamente.

---

# 🧪 **3.3. Soma de Discount**

```sql
SELECT SUM(REPLACE(Discount, ',', '.') + 0) FROM superstore;
SELECT SUM(discount) FROM fact_sales;
```

---

# 🧪 **3.4. Soma de Profit**

```sql
SELECT SUM(REPLACE(Profit, ',', '.') + 0) FROM superstore;
SELECT SUM(profit) FROM fact_sales;
```

---

# ✅ 4. Conferir se cada ID de dimensão corresponde exatamente ao da tabela original

### Conferir Order ID

```sql
SELECT COUNT(*) AS diferencas
FROM superstore s
LEFT JOIN dim_order d
    ON s.`Order ID` = d.order_id
WHERE d.order_key IS NULL;
```

### Conferir Product ID

```sql
SELECT COUNT(*) AS diferencas
FROM superstore s
LEFT JOIN dim_product p
    ON s.`Product ID` = p.product_id
WHERE p.product_key IS NULL;
```

### Conferir Customer ID

```sql
SELECT COUNT(*) AS diferencas
FROM superstore s
LEFT JOIN dim_customer c
    ON s.`Customer ID` = c.customer_id
WHERE c.customer_key IS NULL;
```

➡ **Se todos retornarem 0, está tudo perfeito.**

---

# ✅ 5. Conferir agregações por grupo

Exemplo: total de vendas por estado.

Superstore:

```sql
SELECT State, SUM(REPLACE(Sales, ',', '.') + 0)
FROM superstore
GROUP BY State;
```

Fato + Dimensão:

```sql
SELECT d.state, SUM(f.sales)
FROM fact_sales f
JOIN dim_customer d ON f.customer_key = d.customer_key
GROUP BY d.state;
```

➡ Esses valores devem ser iguais.

---

# 🎯 Resumo das validações essenciais

| Validação                  | Objetivo                                              |
| -------------------------- | ----------------------------------------------------- |
| Count de linhas            | Verificar se nenhuma linha ficou de fora              |
| Soma das métricas          | Garantir que os valores foram importados corretamente |
| FK sem NULL                | Validar integridade com dimensões                     |
| Conferir IDs nas dimensões | Garantir que todas as dimensões estão completas       |
| Conferências por grupo     | Ver um exemplo prático de análise batendo             |

---
