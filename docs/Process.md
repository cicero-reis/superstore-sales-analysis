# Process — Data Cleaning & Transformation (Superstore Sales)

## Objetivo da Etapa

A etapa **Process** tem como objetivo transformar dados brutos e inconsistentes em dados **limpos, padronizados e confiáveis**, prontos para análise. Nesta fase, foi aplicado técnicas práticas de limpeza de dados utilizando **MySQL 8**, seguindo boas práticas de Análise de Dados.

---

## Dataset Utilizado

**Fonte:** Superstore Sales (Tableau)
**Formato original:** CSV importado para MySQL
**Tabela base:** `superstore`

Principais problemas identificados no dataset original:

* Datas armazenadas como `varchar`
* Valores numéricos (`Sales`, `Discount`, `Profit`) armazenados como texto
* Separador decimal inconsistente (`,` em vez de `.`)
* Registros duplicados de pedidos (`Order ID`)
* Estrutura inadequada para análise (tabela única)

---

## Verificação da Qualidade dos Dados (Data Integrity)

A primeira etapa consistiu em entender a estrutura dos dados e identificar problemas de qualidade.

Ações realizadas:

* Inspeção dos tipos de dados
* Verificação de valores nulos
* Identificação de duplicidades em `Order ID`
* Análise de campos numéricos e datas inconsistentes

---

## Correção de Tipos de Dados

Para evitar perda de informação, a estratégia adotada foi **criar novas colunas corrigidas**, mantendo as colunas originais temporariamente.

### Datas

* Conversão de `Order Date` e `Ship Date` de `varchar` para `DATE`
* Criação das colunas:

  * `order_date_clean`
  * `ship_date_clean`

### Valores Numéricos

* Conversão de `Sales`, `Discount` e `Profit` para `DECIMAL`
* Tratamento do separador decimal

Exemplo de abordagem:

* Substituição de `,` por `.`
* Conversão explícita para tipo numérico

---

## Tratamento de Dados Duplicados

Foram identificados múltiplos registros para o mesmo `Order ID`, o que é esperado em nível de itens, mas não em nível de pedido.

Ações realizadas:

* Uso de `ROW_NUMBER()` para identificar duplicatas
* Criação da dimensão `dim_order` com um registro único por pedido

Isso garantiu consistência na modelagem e evitou duplicidade lógica de pedidos.

---

## Padronização e Consistência

Para garantir consistência ao longo do projeto:

* Todos os nomes de tabelas e colunas foram padronizados em **inglês**
* Tipos de dados foram uniformizados (`DATE`, `DECIMAL`, `INT`)
* Criação de **chaves substitutas (surrogate keys)** nas dimensões

---

## Estruturação dos Dados (Modelagem Dimensional)

Os dados foram reorganizados utilizando **Star Schema**, facilitando análises futuras e escalabilidade.

### 📐 Dimensões criadas:

* `dim_customer`
* `dim_product`
* `dim_order`
* `dim_date`

### Tabela Fato:

* `fact_sales`

A tabela fato armazena métricas de vendas e se relaciona com as dimensões por meio de chaves estrangeiras.

---

## Criação da Dimensão de Datas (`dim_date`)

Foi criada uma tabela de datas contendo um intervalo completo entre:

* **2014-01-03** e **2018-01-05**

A dimensão de datas inclui atributos como:

* Ano
* Trimestre
* Mês
* Nome do mês
* Semana
* Dia
* Nome do dia da semana

Essa estrutura permite análises temporais mais eficientes.

---

## Validação Final dos Dados

Após o processamento, foram realizadas validações para garantir:

* Correspondência correta entre dimensões e fato
* Ausência de valores inválidos
* Integridade referencial entre tabelas

---

## Resultado da Etapa Process

Ao final desta etapa, os dados estão:

* Limpos
* Padronizados
* Sem duplicações lógicas
* Estruturados para análise
