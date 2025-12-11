1. Criar as novas colunas para decimal

```sql
ALTER TABLE superstore
ADD COLUMN sales_clean DECIMAL(10,2),
ADD COLUMN discount_clean DECIMAL(10,2),
ADD COLUMN profit_clean DECIMAL(10,2);
```

2. Converter valores VARCHAR → DECIMAL

```sql
UPDATE superstore
SET 
    sales_clean = CAST(REPLACE(Sales, ',', '.') AS DECIMAL(10,2)),
    discount_clean = CAST(REPLACE(Discount, ',', '.') AS DECIMAL(10,2)),
    profit_clean = CAST(REPLACE(Profit, ',', '.') AS DECIMAL(10,2))
WHERE 
    REPLACE(Profit, ',', '.') REGEXP '^-?[0-9]+(\\.[0-9]+)?$'
    AND REPLACE(Sales, ',', '.') REGEXP '^-?[0-9]+(\\.[0-9]+)?$'
    AND REPLACE(Discount, ',', '.') REGEXP '^-?[0-9]+(\\.[0-9]+)?$';
```

3. Remover as colunas originais (opcional)
 ```sql
ALTER TABLE superstore
DROP COLUMN Sales,
DROP COLUMN Discount,
DROP COLUMN Profit;
```