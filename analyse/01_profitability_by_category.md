# Rentabilidade Crítica por Categoria (2017)

## Objetivo da Análise
Avaliar a performance das categorias de produto sob a ótica de:
- Volume vendido
- Receita
- Lucro
- Rentabilidade (lucro por unidade e margem)

Essa análise responde à pergunta:
> **Quais categorias geram valor real para o negócio, além de volume?**

---

## Métricas Utilizadas
- Quantidade total vendida
- Receita total
- Lucro total
- Lucro por unidade
- Margem de lucro

---

## Query SQL Utilizada
```sql
SET @varYear = 2017;

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
WHERE q.`year` = @varYear;
```

## 🔍 Resultado

|year|category|total_quantity|total_sales|total_profit|profit_per_unit|profit_margin|
|----|--------|--------------|-----------|------------|---------------|-------------|
2017|Technology     |          2363|  271730.82|    50684.64|          21.45|         0.19|
2017|Office Supplies|          7676|  246097.09|    39736.69|           5.18|         0.16|
2017|Furniture      |          2437|  215387.28|     3018.44|           1.24|         0.01|


## Interpretação

- A categoria **Technology** apresenta o maior valor agregado ao negócio, combinando alto faturamento com excelente margem (19%) e lucro por unidade elevado.
- **Office Supplies** lidera em volume, mas com rentabilidade inferior, indicando possível foco em eficiência operacional.
- **Furniture** apresenta um claro desequilíbrio entre volume, receita e lucro, sugerindo problemas de precificação, custos ou mix de produtos.
