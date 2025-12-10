# ✅ **1. Estrutura da Dimensão Cliente (DimCliente)**

A partir dos dados do Superstore, o que pertence ao cliente?

| Coluna no dataset | Pertence ao cliente?  | Vai para a dimensão? |
| ----------------- | --------------------- | -------------------- |
| Customer ID       | ✔ Identificador único | ✔                    |
| Customer Name     | ✔ Nome                | ✔                    |
| Segment           | ✔ Tipo de cliente     | ✔                    |
| Country           | ✔ País                | ✔                    |
| City              | ✔ Cidade              | ✔                    |
| State             | ✔ Estado              | ✔                    |
| Postal Code       | ✔ CEP                 | ✔                    |

---

# ✅ **2. Criar a tabela no MySQL**

```sql
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_key     INT AUTO_INCREMENT PRIMARY KEY,
    customer_id      VARCHAR(50),
    customer_name    VARCHAR(100),
    segment          VARCHAR(50),
    country          VARCHAR(50),
    state            VARCHAR(50),
    city             VARCHAR(50),
    postal_code      INT
);
```
---

# ✅ **3. Popular a DimCliente a partir da tabela original e conferir duplicados**

```sql
SELECT 
    `Customer ID`,
    COUNT(*) AS total
FROM superstore
GROUP BY `Customer ID`
HAVING total > 1;
```

```sql
INSERT INTO dim_customer (
    customer_id, customer_name, segment, country, state, city, postal_code
)
SELECT 
    t.`Customer ID`,
    t.`Customer Name`,
    t.Segment,
    t.Country,
    t.State,
    t.City,
    t.`Postal Code`
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY `Customer ID` ORDER BY `Customer ID`) AS rn
    FROM superstore
) t
WHERE t.rn = 1;
```

---

# ✅ **4. Conferir duplicados da tabela Dimensão**

```sql
SELECT 
    dc.customer_id,
    COUNT(*) AS total
FROM dim_customer dc
GROUP BY dc.customer_id
HAVING total > 1;
```
---

# 🔍 **3. Conferir quantos produtos únicos existem**

```sql
SELECT COUNT(DISTINCT `Customer ID`) 
FROM superstore;
```

E depois:

```sql
SELECT COUNT(*) FROM dim_client;
```
