# **Limpeza e Padronização de Valores Numéricos (Sales, Discount, Profit)**

As colunas originais armazenam valores como **VARCHAR** com vírgula decimal, o que impede cálculos e análises.
O processo abaixo converte esses valores para **DECIMAL(10,2)**.

---

## **1. Criar novas colunas para valores decimais limpos**

```sql
ALTER TABLE superstore
ADD COLUMN sales_clean DECIMAL(10,2),
ADD COLUMN discount_clean DECIMAL(10,2),
ADD COLUMN profit_clean DECIMAL(10,2);
```

---

## **2. Converter valores `VARCHAR` → `DECIMAL`**

Substituir vírgulas por pontos e aplicar a conversão para decimal.

```sql
UPDATE superstore
SET 
    sales_clean    = CAST(REPLACE(Sales, ',', '.') AS DECIMAL(10,2)),
    discount_clean = CAST(REPLACE(Discount, ',', '.') AS DECIMAL(10,2)),
    profit_clean   = CAST(REPLACE(Profit, ',', '.') AS DECIMAL(10,2))
WHERE 
    REPLACE(Profit, ',', '.') REGEXP '^-?[0-9]+(\\.[0-9]+)?$'
    AND REPLACE(Sales, ',', '.') REGEXP '^-?[0-9]+(\\.[0-9]+)?$'
    AND REPLACE(Discount, ',', '.') REGEXP '^-?[0-9]+(\\.[0-9]+)?$';
```

---

## **3. (Opcional) Remover as colunas originais**

Execute apenas após verificar que todas as conversões ocorreram corretamente.

```sql
ALTER TABLE superstore
DROP COLUMN Sales,
DROP COLUMN Discount,
DROP COLUMN Profit;
```