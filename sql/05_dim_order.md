A **dim_order** conterá atributos relacionados ao pedido que **não mudam por transação**, mas descrevem o pedido como entidade:

📌 *Order ID*
📌 *Order Date (clean)*
📌 *Ship Date (clean)*
📌 *Ship Mode*
📌 *State / City / Country / Region*
📌 *Postal Code*
📌 *(Opcional) Shipping Delay*

---

# ✅ **1. Criar a tabela `dim_order`**

Campo mais importante: `order_id`.

```sql
CREATE TABLE IF NOT EXISTS dim_order (
    order_key       INT AUTO_INCREMENT PRIMARY KEY,
    order_id        VARCHAR(50),
    order_date      DATE,
    ship_date       DATE,
    ship_mode       VARCHAR(50),
    country         VARCHAR(50),
    state           VARCHAR(50),
    city            VARCHAR(50),
    postal_code     INT,
    region          VARCHAR(50),
    shipping_delay  INT  -- opcional, dias entre pedido e envio
);
```

# 🔍 **2. Verificar duplicações de Order ID**

Antes de prosseguir:

```sql
SELECT `Order ID`, COUNT(*)
FROM superstore
GROUP BY `Order ID`
HAVING COUNT(*) > 1;
```
---

# 🧼 **3. Usar as colunas de datas já limpas**

Assumindo que você já criou:

* `order_date_clean`
* `ship_date_clean`

---

# 🚀 **4. Inserir dados na dimensão**

Usaremos **DISTINCT**:

```sql
INSERT INTO dim_order (
    order_id,
    order_date,
    ship_date,
    ship_mode,
    country,
    state,
    city,
    postal_code,
    region,
    shipping_delay
)
SELECT
    t.order_id,
    t.order_date_clean,
    t.ship_date_clean,
    t.ship_mode,
    t.country,
    t.state,
    t.city,
    t.postal_code,
    t.region,
    DATEDIFF(t.ship_date_clean, t.order_date_clean) AS shipping_delay
FROM (
    SELECT 
        `Order ID` AS order_id,
        order_date_clean,
        ship_date_clean,
        `Ship Mode` AS ship_mode,
        Country AS country,
        State AS state,
        City AS city,
        `Postal Code` AS postal_code,
        Region AS region,
        ROW_NUMBER() OVER (PARTITION BY `Order ID` ORDER BY `Order ID`) AS rn
    FROM superstore
) AS t
WHERE t.rn = 1;

```

---
