# ✅ **1. Criar a tabela `fact_sales`**

```sql
CREATE TABLE fact_sales (
    fact_id INT AUTO_INCREMENT PRIMARY KEY,

    -- Foreign Keys
    order_key   INT NOT NULL,
    product_key INT NOT NULL,
    customer_key INT NOT NULL,

    -- Measures
    quantity INT NOT NULL,
    sales DECIMAL(10,2) NOT NULL,
    discount DECIMAL(10,2) NOT NULL,
    profit DECIMAL(10,2) NOT NULL,

    -- FK constraints
    FOREIGN KEY (order_key) REFERENCES dim_order(order_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key)
);
```

---

# ✅ **2. Popular a fato com base na tabela original**

```sql
INSERT INTO fact_sales (
    order_key,
    product_key,
    customer_key,
    quantity,
    sales,
    discount,
    profit
)
SELECT
    o.order_key,
    p.product_key,
    c.customer_key,
    s.Quantity,
    REPLACE(s.Sales, ',', '.') + 0,
    REPLACE(s.Discount, ',', '.') + 0,
    REPLACE(s.Profit, ',', '.') + 0
FROM superstore s
JOIN dim_order o
    ON s.`Order ID` = o.order_id
JOIN dim_product p
    ON s.`Product ID` = p.product_id
JOIN dim_customer c
    ON s.`Customer ID` = c.customer_id;
```

---

# 📌 **3. Quantas linhas devem aparecer na fact_sales?**

A tabela original tem **9994 linhas**.
A fact table deve ter **exatamente 9994 linhas**, pois cada linha representa **um item do pedido**.

---

# 📌 **4. Próximo passo**

Após criar a tabela fato, podemos:

* Criar **views** de análise
* Criar queries para responder as perguntas:

  * produtos mais vendidos
  * total de vendas
  * lucratividade
  * impacto do desconto
  * clientes mais valiosos

Se quiser, posso gerar um **arquivo SQL completo**, ou criar as **primeiras queries de análise**. Quer que eu gere?
