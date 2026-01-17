# Moda das Vendas Mensais — 2017

## Objetivo da Análise

Identificar a **moda das vendas mensais** no ano de 2017, ou seja, o **intervalo de valores que ocorre com maior frequência**.

Como os valores mensais de vendas são **contínuos** (cada mês tende a ter um valor único), a moda direta não é estatisticamente adequada.  
Por isso, utilizo **faixas de valores (buckets)** para identificar padrões recorrentes.

Esta análise responde à pergunta:

> “Em qual faixa de vendas os meses de 2017 se concentram com mais frequência?”

---

## Base de Dados

- **Tabela fato:** `fact_sales`
- **Tabela dimensão:** `dim_date`
- **Métrica:** Quantidade vendida (`quantity`)
- **Período analisado:** Ano de 2017
- **Unidade de análise:** Vendas agregadas por mês

---

## Observação Estatística Importante

A **moda tradicional** só faz sentido quando:
- Existem valores repetidos
- Ou os dados são categóricos

Como cada mês possui um valor único de vendas, apliquei a **moda por classes (faixas)**, técnica comum em análises exploratórias e relatórios executivos.

---

## Definição das Faixas de Venda

| Faixa | Critério |
|-----|---------|
| Até 800 | ≤ 800 |
| 801–1000 | 801 a 1000 |
| 1001–1200 | 1001 a 1200 |
| Acima de 1200 | > 1200 |

---

## Consulta SQL

```sql
SET @varYear = 2017;

WITH monthly_quantity AS (
    SELECT 
        dd.month,
        SUM(fs.quantity) AS total_quantity_month
    FROM fact_sales fs
    JOIN dim_date dd 
        ON dd.date_key = fs.date_key
    WHERE dd.year = @varYear
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
````

---

## Resultado

| Faixa de Venda | Frequência  |
| -------------- | ----------- |
| **801–1000**   | **5 meses** |
| Até 800        | 3 meses     |
| Acima de 1200  | 3 meses     |
| 1001–1200      | 1 mês       |

---

## Interpretação do Resultado

* A **moda das vendas mensais** em 2017 está na faixa **801–1000 unidades**
* **5 de 12 meses** ficaram concentrados nesse intervalo
* Essa faixa representa o **comportamento mais comum** do ano

---

## Conexão com Média e Mediana

| Medida           | Valor        | Observação                                    |
| ---------------- | ------------ | --------------------------------------------- |
| Média            | 1.039,67     | Influenciada por meses com vendas muito altas |
| Mediana          | 886,00       | Valor central mais representativo             |
| **Moda (faixa)** | **801–1000** | Faixa mais frequente                          |

A mediana (886) **está contida na faixa modal**, reforçando que ela descreve melhor o padrão típico mensal do que a média.

---

## Limitação da Moda por Faixas

* O resultado depende da **definição das faixas**
* Faixas diferentes podem alterar a moda
* Deve ser usada como **complemento**, não como única métrica

---

## Conclusão

✔ A moda por faixa indica que a maioria dos meses de 2017 teve vendas entre **801 e 1000 unidades**
✔ Confirma que a **média está inflada por meses excepcionais**
✔ Reforça o uso da **mediana** como medida mais robusta para este cenário
