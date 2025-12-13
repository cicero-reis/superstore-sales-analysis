## 📊 **Projeto: Análise de Vendas — Superstore Sales (MySQL 8)**

### 🎯 **Objetivo da Etapa**

Preparar o dataset **Superstore Sales** para análise no **MySQL 8**, garantindo:

* Estrutura organizada
* Dados limpos e consistentes
* Tipos corretos
* Criação de campos derivados
* Base pronta para dashboards e análises exploratórias

---

## 📂 **Sobre o Dataset**

* **Fonte:** Tableau — Sample Superstore
* **Formato original:** CSV
* **Tamanho:** 9.994 linhas • 21 colunas
* **Objetivo do tratamento:** transformar dados brutos em um conjunto confiável para análise de vendas, lucro e comportamento do cliente.

### 📌 **Colunas do Dataset após limpeza**

| Tipo                             | Colunas                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Identificação**                | `Row ID`, `Order ID`, `Product ID`, `Customer ID`                                                                         |
| **Datas limpas**                 | `order_date_clean`, `ship_date_clean`                                                                                     |
| **Texto / Categoria**            | `Ship Mode`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Region`, `Category`, `Sub-Category`, `Product Name` |
| **Numéricos tratados (DECIMAL)** | `sales_clean`, `discount_clean`, `profit_clean`, `Quantity`, `Postal Code`                                                |

