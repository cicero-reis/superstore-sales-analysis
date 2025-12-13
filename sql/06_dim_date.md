# 📅 **Dimensão de Datas (dim_date)**

A **dim_date** é fundamental em qualquer modelo estrela.
Ela permite análises por **ano, trimestre, mês, semana, dia**, além de facilitar cálculos como comparações históricas.

---

# 🧭 **1. Descobrir o intervalo completo de datas**

Antes de gerar a dimensão, identifique o período que seu dataset cobre:

```sql
SELECT 
    MIN(order_date_clean) AS min_order,
    MAX(order_date_clean) AS max_order,
    MIN(ship_date_clean)  AS min_ship,
    MAX(ship_date_clean)  AS max_ship
FROM superstore;
```

📌 **Resultado típico:**

| min_order  | max_order  | min_ship   | max_ship   |
| ---------- | ---------- | ---------- | ---------- |
| 2014-01-03 | 2017-12-30 | 2014-01-07 | 2018-01-05 |

---

# 🗂️ **2. Criar a tabela `dim_date`**

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

### 🔑 Por que `date_key` é inteiro?

✔ Facilita joins
✔ Ocupa menos espaço
✔ É padrão em modelos estrela
✔ Formato AAAAMMDD permite filtros rápidos

---

# 🔄 **3. Gerar o calendário completo**

Usamos uma CTE recursiva para criar todas as datas do intervalo:

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
    WEEK(dt, 3) AS week,   -- semana ISO
    DAY(dt) AS day,
    DAYNAME(dt) AS day_name
FROM date_range;
```

📌 **Isso gera 1464 linhas — uma por dia do intervalo.**

---

# 🛠️ **4. Erro de profundidade recursiva?**

Use:

```sql
SET cte_max_recursion_depth = 5000;
```

---

# 🔗 **5. Como ligar a `fact_sales` com a `dim_date`**

Quando for montar a tabela fato:

```sql
SELECT date_key
FROM dim_date
WHERE full_date = s.order_date_clean;
```
