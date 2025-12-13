# 💼 **Dimensão Cliente (dim_customer)**

A dimensão cliente armazena todas as informações relacionadas aos clientes do dataset **Superstore**.

---

## 1️⃣ **Colunas do dataset que pertencem ao cliente**

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

## 2️⃣ **Criar a tabela no MySQL**

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

## 3️⃣ **Identificar clientes duplicados na tabela original**

```sql
SELECT 
    `Customer ID`,
    COUNT(*) AS total
FROM superstore
GROUP BY `Customer ID`
HAVING total > 1;
```

---

## 4️⃣ **Popular a dimensão removendo duplicados com ROW_NUMBER**

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

## 5️⃣ **Conferir duplicados na dimensão criada**

```sql
SELECT 
    dc.customer_id,
    COUNT(*) AS total
FROM dim_customer dc
GROUP BY dc.customer_id
HAVING total > 1;
```

---

## 6️⃣ **Verificar quantidade de clientes únicos**

```sql
-- Na tabela original
SELECT COUNT(DISTINCT `Customer ID`) 
FROM superstore;

-- Na dimensão criada
SELECT COUNT(*) 
FROM dim_customer;
