1. Criar as novas colunas de data

```sql
ALTER TABLE superstore
ADD COLUMN order_date_clean DATE,
ADD COLUMN ship_date_clean DATE;
```

2. Popular as novas colunas convertendo VARCHAR → DATE

```sql
UPDATE superstore
SET 
    order_date_clean = STR_TO_DATE(`Order Date`, '%m/%d/%Y'),
    ship_date_clean = STR_TO_DATE(`Ship Date`, '%m/%d/%Y');
```

3. Verificar se a conversão

```sql
SELECT 
    `Order Date`, order_date_clean,
    `Ship Date`, ship_date_clean
FROM superstore
LIMIT 20;
```

4. (Opcional) Remover as colunas antigas

```sql
ALTER TABLE superstore
DROP COLUMN `Order Date`,
DROP COLUMN `Ship Date`;
```

5. Criar as novas colunas para decimal

```sql
ALTER TABLE superstore
ADD COLUMN sales_clean DECIMAL(10,2),
ADD COLUMN discount_clean DECIMAL(10,2),
ADD COLUMN profit_clean DECIMAL(10,2);
```

6. Converter valores VARCHAR → DECIMAL

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

7. Remover as colunas originais (opcional)
 ```sql
ALTER TABLE superstore
DROP COLUMN Sales,
DROP COLUMN Discount,
DROP COLUMN Profit;
```