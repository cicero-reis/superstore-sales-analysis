from sqlalchemy import text

query_rentabilidade_critica_por_categoria = text("""
WITH category_quantity_sales_profit AS (
	SELECT 
		dd.`year`,
		dp.category,
		SUM(f.quantity) AS total_quantity, 
		SUM(f.sales) AS total_sales,
		SUM(f.profit) AS total_profit,
		ROUND(SUM(f.profit) / SUM(f.quantity), 2) AS profit_per_unit,
		ROUND(SUM(f.profit) / SUM(f.sales), 2) AS profit_margin
	FROM fact_sales f 
	INNER JOIN dim_product dp ON f.product_key = dp.product_key
	INNER JOIN dim_date dd ON f.date_key = dd.date_key 	
	GROUP BY dd.`year`, dp.category
	ORDER BY total_sales DESC
)
SELECT 
    * 
FROM category_quantity_sales_profit q 
WHERE q.`year` = :year;
""")

query_distribuicao_mensal_de_vendas = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    INNER JOIN dim_date dd 
        ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
)
SELECT * 
FROM monthly_quantity
ORDER BY month;
""")

query_media = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd 
        ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
)
SELECT 
    ROUND(AVG(total_quantity_month), 2) AS avg_monthly_quantity
FROM monthly_quantity;
""")

query_mediana = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd 
        ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
),
ordered_months AS (
    SELECT
        total_quantity_month,
        ROW_NUMBER() OVER (ORDER BY total_quantity_month) AS rn,
        COUNT(*) OVER () AS total_rows
    FROM monthly_quantity
)
SELECT 
    ROUND(AVG(total_quantity_month), 2) AS median_quantity
FROM ordered_months
WHERE rn IN (
    FLOOR((total_rows + 1) / 2),
    CEIL((total_rows + 1) / 2)
);
""")

query_moda = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd 
        ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.month
),
buckets AS (
    SELECT
        CASE
            WHEN total_quantity_month <= 800 THEN 'Até 800'
            WHEN total_quantity_month <= 1000 THEN '801–1000'
            WHEN total_quantity_month <= 1200 THEN '1001–1200'
            ELSE 'Acima de 1200'
        END AS faixa_venda
    FROM monthly_quantity
)
SELECT
    faixa_venda,
    COUNT(*) AS frequencia
FROM buckets
GROUP BY faixa_venda
ORDER BY frequencia DESC;
""")

query_quartiles = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd 
        ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
),
ordered AS (
    SELECT
        total_quantity_month,
        NTILE(4) OVER (ORDER BY total_quantity_month) AS quartil
    FROM monthly_quantity
)
SELECT
    quartil,
    MIN(total_quantity_month) AS min_value,
    MAX(total_quantity_month) AS max_value
FROM ordered
GROUP BY quartil
ORDER BY quartil;
""")

query_min_and_max = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
)
SELECT
    MIN(total_quantity_month) AS min_quantity,    
    MAX(total_quantity_month) AS max_quantity
FROM monthly_quantity;
""")

query_amplitude = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
)
SELECT
    MAX(total_quantity_month) - MIN(total_quantity_month) AS amplitude
FROM monthly_quantity;
""")

query_desvio_padrao = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
)
SELECT
    ROUND(STDDEV(total_quantity_month)) AS stddev_quantity
FROM monthly_quantity;
""")

query_variancia = text("""
WITH monthly_quantity AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd ON dd.date_key = fs.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
)
SELECT
    ROUND(VARIANCE(total_quantity_month)) AS variance_quantity    
FROM monthly_quantity;
""")