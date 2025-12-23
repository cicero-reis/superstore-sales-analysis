from sqlalchemy import text

query_desempenho_de_vendas = text("""
WITH vendas_em_2017 AS (
    SELECT 
        dd.year,
        dd.month,
        SUM(f.sales) AS total_sales
    FROM fact_sales f
    JOIN dim_date dd ON dd.date_key = f.date_key
    WHERE dd.year = :year
    GROUP BY dd.year, dd.month
)
SELECT *
FROM vendas_em_2017
ORDER BY total_sales DESC;
""")

query_rentabilidade_critica_da_categoria_furniture = text("""
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

query_crescimento_nao_lucrativo_da_categoria_furniture = text("""
WITH comparacao_temporal_margem_de_lucro_da_caategoria_furniture AS (
	SELECT 
		dd.`year`,
		dp.category,
		SUM(f.quantity) as total_quantity, 
		ROUND(SUM(f.sales), 2) as total_sales,
		ROUND(SUM(f.profit), 2) as total_profit,
		ROUND(SUM(f.profit) / SUM(f.sales), 3) AS profit_margin
	FROM fact_sales f 
	INNER JOIN dim_product dp ON f.product_key = dp.product_key
	INNER JOIN dim_date dd ON f.date_key = dd.date_key 	
	WHERE dp.category = :category
	GROUP BY dd.`year`, dp.category
	ORDER BY dd.`year`
)
SELECT * FROM comparacao_temporal_margem_de_lucro_da_caategoria_furniture;
""")