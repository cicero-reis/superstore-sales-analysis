# **Tabela Fato — `fact_sales`**

A **fact_sales** armazena todas as métricas que serão analisadas e conecta as dimensões através de chaves estrangeiras.

Ela responde perguntas como:

✔ Total de vendas
✔ Total de lucro
✔ Vendas por cliente, produto, estado
✔ Descontos aplicados
✔ Quantidade vendida

---

# **1. Criar a tabela `fact_sales`**

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

# **2. Popular a tabela fato**

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

# **3. Validações essenciais**

---

## **3.1. Conferir número total de linhas**

```sql
SELECT
(SELECT COUNT(*) FROM superstore) AS total_superstore,
(SELECT COUNT(*) FROM fact_sales) AS total_fact_sales;
```

→ **Os valores devem ser iguais.**

---

# **Resumo das validações**

| Validação                  | Resultado esperado |
| -------------------------- | ------------------ |
| Mesma quantidade de linhas | ✔                  |
| Métricas iguais            | ✔                  |
| FKs sem NULL               | ✔                  |
| IDs íntegros nas dimensões | ✔                  |
| Agregações equivalentes    | ✔                  |
