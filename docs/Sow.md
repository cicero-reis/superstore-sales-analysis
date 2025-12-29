Perfeito.
O **SOW (Statement of Work)** é onde você mostra **maturidade profissional**: deixa claro *o que será feito, como, por quem, quando e com quais limites*. Pouquíssimos projetos de portfólio têm isso — e isso te diferencia muito.

Abaixo está um **SOW.md completo**, alinhado ao seu projeto, ao foco em **Categorias em 2017**, e ao framework **Google Data Analytics**.

---

# 📄 SOW — Statement of Work

**Projeto:** Superstore Sales Analysis — Categorias (2017)

---

## 🔹 1. Visão Geral do Projeto

Este projeto tem como objetivo analisar o desempenho das **categorias de produtos** da empresa Superstore no **ano de 2017**, utilizando dados históricos de vendas.

O trabalho segue um processo estruturado de análise de dados, aplicando conceitos de limpeza, modelagem, estatística descritiva e interpretação de resultados para apoiar **decisões de negócio baseadas em dados**.

---

## 🔹 2. Objetivo do Trabalho

Fornecer aos stakeholders uma **visão clara, confiável e orientada ao negócio** sobre:

* Como as vendas se distribuíram entre as categorias em 2017
* Quais categorias concentram volume operacional
* Quais categorias geram mais valor financeiro
* O nível de estabilidade e variabilidade das vendas ao longo do ano

---

## 🔹 3. Escopo do Projeto

### ✅ Incluído no Escopo

* Importação do dataset **Superstore Sales**
* Limpeza e padronização de dados (datas e valores numéricos)
* Modelagem dimensional (*Star Schema*)
* Criação de tabelas:

  * `dim_customer`
  * `dim_product`
  * `dim_order`
  * `dim_date`
  * `fact_sales`
* Análise estatística descritiva:

  * Frequência absoluta e relativa
  * Pareto (ABC)
  * Média, mediana e moda
  * Quartis
  * Amplitude, variância e desvio padrão
* Análise focada nas **categorias de produtos em 2017**
* Documentação completa do processo

---

### ❌ Fora do Escopo

* Previsões de vendas (forecasting)
* Modelos de machine learning
* Análises em tempo real
* Dados externos ao dataset Superstore
* Recomendações estratégicas finais (fase Act)

---

## 🔹 4. Stakeholders

| Papel             | Interesse                                  |
| ----------------- | ------------------------------------------ |
| Gestão Comercial  | Entender desempenho por categoria          |
| Planejamento      | Avaliar estabilidade e variabilidade       |
| Operações         | Dimensionar volume e capacidade            |
| Analista de Dados | Garantir qualidade e interpretação correta |

---

## 🔹 5. Metodologia

O projeto segue as etapas do **Processo de Análise de Dados**:

1. **Ask** — Definição das perguntas de negócio
2. **Prepare** — Limpeza, padronização e modelagem dos dados
3. **Process** — Validação, consistência e transformação
4. **Analyze** — Exploração estatística e geração de insights
5. **Share** — Comunicação dos resultados *(planejado)*
6. **Act** — Ações baseadas nos insights *(fora do escopo atual)*

---

## 🔹 6. Entregáveis

* Dataset limpo e estruturado
* Modelo dimensional documentado
* Consultas SQL versionadas
* Documentos:

  * Ask.md
  * Smart.md
  * Prepare.md
  * Process.md
  * Analyze.md
  * SOW.md
* README.md com visão executiva do projeto

---

## 🔹 7. Cronograma (Estimado)

| Etapa   | Status         |
| ------- | -------------- |
| Ask     | Concluído      |
| Prepare | Concluído      |
| Process | Concluído      |
| Analyze | Concluído      |
| Share   | Planejado      |
| Act     | Fora do escopo |

---

## 🔹 8. Premissas e Restrições

### Premissas

* Os dados representam corretamente as vendas de 2017
* Não há atualização contínua do dataset
* O foco é análise exploratória e descritiva

### Restrições

* Análise limitada ao dataset fornecido
* Resultados dependem da qualidade dos dados originais
* Não há validação externa de mercado

---

## 🔹 9. Critérios de Sucesso

O projeto será considerado bem-sucedido se:

* Os dados estiverem limpos e organizados
* As análises forem reproduzíveis em SQL
* Os insights forem compreensíveis para stakeholders não técnicos
* A documentação permitir continuidade do projeto

---

## 🔹 10. Responsável

**Cicero Reis**
Analista de Dados em desenvolvimento
