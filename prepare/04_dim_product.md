# **Dimensão Produto (dim_product)**

### ✔ O que ela representa?

A **dim_product** guarda informações **descritivas e estáveis** sobre cada produto.
Ela não armazena fatos (quantidades, valores), apenas **atributos do produto**.

### **Atributos que pertencem ao produto:**

| Atributo         | Descrição           | Vai para a dimensão? |
| ---------------- | ------------------- | -------------------- |
| **Product ID**   | Identificador único | ✔                    |
| **Product Name** | Nome do produto     | ✔                    |
| **Category**     | Categoria           | ✔                    |
| **Sub-Category** | Subcategoria        | ✔                    |

---

# **1. Criar tabela `dim_product`**

```sql
CREATE TABLE IF NOT EXISTS dim_product (
    product_key     INT AUTO_INCREMENT PRIMARY KEY,
    product_id      VARCHAR(50),
    product_name    VARCHAR(255),
    category        VARCHAR(100),
    sub_category    VARCHAR(100)
);
```

---

# **2. Popular a Dimensão Produto**

## ✔ Opção 1 — Método simples: **DISTINCT**

Usar quando não há divergências entre registros do mesmo produto.

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

# **Opção 2 — Método robusto: tratar inconsistências**

Se houver produtos com **nomes diferentes para o mesmo ID**, usamos `ROW_NUMBER()`.

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
           ROW_NUMBER() OVER (
               PARTITION BY `Product ID`
               ORDER BY `Product Name`
           ) AS rn
    FROM superstore
) t
WHERE t.rn = 1;
```

---

# **3. Verificar quantos produtos únicos existem**

### No dataset original

```sql
SELECT COUNT(DISTINCT `Product ID`) 
FROM superstore;
```

### Na dimensão populada

```sql
SELECT COUNT(*) 
FROM dim_product;
```
