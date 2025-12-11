# ✅ **Passo 1 — Enteder o intervalo completo de datas do dataset**

```sql
SELECT 
    MIN(order_date_clean) AS min_order,
    MAX(order_date_clean) AS max_order,
    MIN(ship_date_clean)  AS min_ship,
    MAX(ship_date_clean)  AS max_ship
FROM superstore;
```
```
min_order |max_order |min_ship  |max_ship  |
----------+----------+----------+----------+
2014-01-03|2017-12-30|2014-01-07|2018-01-05|
```

# ✅ **Passo 2 — Criar a tabela `dim_date`**

```sql
CREATE TABLE IF NOT EXISTS dim_date (
    date_key      INT PRIMARY KEY,   -- formato YYYYMMDD
    full_date     DATE NOT NULL,
    year          INT NOT NULL,
    quarter       INT NOT NULL,
    month         INT NOT NULL,
    month_name    VARCHAR(20),
    week          INT NOT NULL,
    day           INT NOT NULL,
    day_name      VARCHAR(20)
);
```

---

# ✅ **Passo 3 — Gerar as datas **

```sql
SET SESSION cte_max_recursion_depth = 5000;

INSERT INTO dim_date (
    date_key, full_date, year, quarter, month, month_name, week, day, day_name
)
WITH RECURSIVE date_range AS (
    SELECT DATE('2014-01-03') AS dt
    UNION ALL
    SELECT DATE_ADD(dt, INTERVAL 1 DAY)
    FROM date_range
    WHERE dt < '2018-01-05'
)
SELECT 
    DATE_FORMAT(dt, '%Y%m%d') + 0 AS date_key,
    dt AS full_date,
    YEAR(dt) AS year,
    QUARTER(dt) AS quarter,
    MONTH(dt) AS month,
    MONTHNAME(dt) AS month_name,
    WEEK(dt, 3) AS week,   -- ISO week (mode 3)
    DAY(dt) AS day,
    DAYNAME(dt) AS day_name
FROM date_range;
```

🔍 **Isso cria 1464 dias de dados (intervalo total)**.

---

# ❗ Caso o MySQL retorne erro de recursão

Altere temporariamente:

```sql
SET cte_max_recursion_depth = 5000;
```

---

# ⚡ Quer relacionar `fact_sales.order_date` e `fact_sales.ship_date` com essa dimensão?

Quando for criar o fact, usaremos:

```sql
SELECT date_key 
FROM dim_date 
WHERE full_date = s.order_date_clean;
```

---

Se quiser, posso gerar o script **completo do início ao fim**:

* criar tabela
* popular
* validar
* criar chaves estrangeiras na fact

Deseja isso?
