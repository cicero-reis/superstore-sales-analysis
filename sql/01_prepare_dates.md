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
