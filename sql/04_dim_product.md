# 🎯 **Objetivo da dimensão Produto**

A **dim_product** deve conter atributos que **descrevem o produto** e não mudam com frequência:

* Product ID
* Product Name
* Category
* Sub-Category

---

# ✅ **1. Criar tabela dim_product**

```sql
CREATE TABLE IF NOT EXISTS dim_product (
    produto_key     INT AUTO_INCREMENT PRIMARY KEY,
    product_id      VARCHAR(50),
    product_name    VARCHAR(255),
    category        VARCHAR(100),
    sub_category    VARCHAR(100)
);
```

---

# ✅ **2. Popular tabela com dados limpos**

Usaremos `DISTINCT` (ou `ROW_NUMBER()` se houver inconsistência entre atributos).

### ✔ Primeira opção (mais comum): DISTINCT

```sql
INSERT INTO dim_product (
    product_id, product_name, category, sub_category
)
SELECT DISTINCT
    `Product ID`,
    `Product Name`,
    Category,
    `Sub-Category`
FROM superstore;
```
---

# ⚠️ **E se existir inconsistência no cadastro?**

```sql
INSERT INTO dim_product (
    product_id, product_name, category, sub_category
)
SELECT 
    t.`Product ID`,
    t.`Product Name`,
    t.Category,
    t.`Sub-Category`
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY `Product ID` ORDER BY `Product Name`) AS rn
    FROM superstore
) t
WHERE t.rn = 1;
```

---

# 🔍 **3. Conferir quantos produtos únicos existem**

```sql
SELECT COUNT(DISTINCT `Product ID`) 
FROM superstore;
```

E depois:

```sql
SELECT COUNT(*) FROM dim_product;
```
---
