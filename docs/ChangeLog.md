```
Todas as mudanças relevantes realizadas neste projeto são documentadas neste arquivo.
O versionamento segue um formato simples, didático e incremental.
```

---

## v0.1.0 — Importação e Preparação Inicial dos Dados

**Fase:** Prepare

### Adicionado

* Importação do dataset **Superstore Sales** (Tableau) para MySQL 8.
* Criação da tabela original `superstore` contendo os dados brutos.

### Observações

* Os dados foram mantidos inicialmente no formato original para preservar a integridade da fonte.

---

## v0.2.0 — Limpeza e Padronização de Tipos de Dados

**Fase:** Prepare

### Adicionado

* Criação de colunas auxiliares para correção de tipos:

  * `order_date_clean`
  * `ship_date_clean`
  * `sales_clean`
  * `discount_clean`
  * `profit_clean`

### Alterado

* Conversão de datas de `VARCHAR` para `DATE`.
* Conversão de valores numéricos (Sales, Discount, Profit) de `VARCHAR` para `DECIMAL`.

### Corrigido

* Ajuste do separador decimal (`,` para `.`) para compatibilidade com MySQL.

---

## v0.3.0 — Modelagem Dimensional (Star Schema)

**Fase:** Prepare

### Adicionado

* Criação do modelo dimensional em **estrutura estrela (Star Schema)**.
* Tabelas de dimensão criadas:

  * `dim_customer`
  * `dim_product`
  * `dim_order`
  * `dim_date`

### Detalhes

* Remoção de duplicidades utilizando `DISTINCT` e `ROW_NUMBER()`.
* Padronização dos nomes de tabelas e colunas para inglês.

---

## v0.4.0 — Criação da Tabela Fato

**Fase:** Prepare

### Adicionado

* Criação da tabela fato `fact_sales`.
* Definição de chaves estrangeiras:

  * `order_key`
  * `product_key`
  * `customer_key`

### Métricas incluídas

* `quantity`
* `sales`
* `discount`
* `profit`

### Observações

* A tabela fato foi populada a partir da tabela `superstore` com joins nas dimensões.

---

## v0.5.0 — Consolidação da Etapa Prepare

**Fase:** Prepare (Concluída)

### Consolidado

* Dataset limpo e estruturado.
* Modelo dimensional pronto para consultas analíticas.
* Base preparada para análises exploratórias.

---

## v0.6.0 — Etapa Process: Limpeza, Consistência e Estruturação

**Fase:** Process (Concluída)

### Adicionado

* Documentação formal da etapa **Process** (`Process.md`).
* Validação da integridade dos dados após limpeza.
* Confirmação da consistência entre dimensões e tabela fato.

### Aplicado

* Tratamento de dados sujos (*dirty data*).
* Padronização de formatos e tipos.
* Remoção de duplicações lógicas.
* Estruturação final para análise analítica.

### Resultado

* Dados confiáveis, consistentes e prontos para a etapa **Analyze**.
