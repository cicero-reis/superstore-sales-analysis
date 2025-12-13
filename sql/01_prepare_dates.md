# 📅 **Limpeza e Padronização das Datas (Order Date / Ship Date)**

A tabela original armazena as datas como **VARCHAR**, o que impede análise temporal.
O processo abaixo converte essas datas para o tipo **DATE**, criando novas colunas limpas.

---

## ✅ **1. Criar novas colunas para armazenar as datas limpas**

```sql
ALTER TABLE superstore
ADD COLUMN order_date_clean DATE,
ADD COLUMN ship_date_clean DATE;
```

---

## ✅ **2. Popular as novas colunas convertendo `VARCHAR` → `DATE`**

O formato original das datas é **MM/DD/YYYY**, por isso utilizamos `STR_TO_DATE`.

```sql
UPDATE superstore
SET 
    order_date_clean = STR_TO_DATE(`Order Date`, '%m/%d/%Y'),
    ship_date_clean = STR_TO_DATE(`Ship Date`, '%m/%d/%Y');
```

---

## ✅ **3. Validar se a conversão ocorreu corretamente**

```sql
SELECT 
    `Order Date`       AS original_order,
    order_date_clean   AS clean_order,
    `Ship Date`        AS original_ship,
    ship_date_clean    AS clean_ship
FROM superstore
LIMIT 20;
```

Você deve ver as datas limpas no formato **YYYY-MM-DD**.

---

## 🧹 **4. (Opcional) Remover as colunas antigas**

Somente execute quando tiver certeza de que todas as conversões estão corretas.

```sql
ALTER TABLE superstore
DROP COLUMN `Order Date`,
DROP COLUMN `Ship Date`;
```


