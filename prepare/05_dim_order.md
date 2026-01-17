# **Dimensão Pedido (dim_order)**

A **dim_order** descreve *características do pedido* que não mudam por transação.
Esses atributos ajudam a contextualizar vendas, fretes e prazos.

### **Atributos que pertencem ao pedido:**

| Atributo                            | Descrição                      | Vai para a dimensão? |
| ----------------------------------- | ------------------------------ | -------------------- |
| **Order ID**                        | Identificador do pedido        | ✔                    |
| **Order Date (clean)**              | Data corrigida do pedido       | ✔                    |
| **Ship Date (clean)**               | Data de envio                  | ✔                    |
| **Ship Mode**                       | Tipo de envio                  | ✔                    |
| **Country / State / City / Region** | Localização do pedido          | ✔                    |
| **Postal Code**                     | CEP                            | ✔                    |
| **Shipping Delay (opcional)**       | Diferença entre envio e pedido | ✔                    |

---

# **1. Criar a tabela `dim_order`**

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
    shipping_delay  INT   -- (opcional) dias entre pedido e envio
);
```

---

# **2. Verificar duplicações de Order ID**

Antes de alimentar a dimensão:

```sql
SELECT `Order ID`, COUNT(*)
FROM superstore
GROUP BY `Order ID`
HAVING COUNT(*) > 1;
```

---

# **3. Usar colunas de datas já limpas**

Assumindo que você já criou e populou:

* `order_date_clean`
* `ship_date_clean`

---

# **4. Inserir dados na dimensão**

Usar `ROW_NUMBER()` para garantir **um único registro por Order ID**, mesmo que o dataset tenha múltiplas linhas por pedido.

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
        ROW_NUMBER() OVER (
            PARTITION BY `Order ID`
            ORDER BY `Order ID`
        ) AS rn
    FROM superstore
) AS t
WHERE t.rn = 1;
