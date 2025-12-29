# 📌 Executive Summary

**Análise de Vendas por Categoria — Superstore | Ano 2017**

## Visão Geral

Esta análise avaliou o desempenho de vendas da Superstore em 2017, com foco em **volume vendido, rentabilidade e comportamento temporal**, utilizando dados consolidados em modelo dimensional (*Star Schema*). O objetivo foi identificar **o que está acontecendo**, **por que isso importa** e **onde agir para gerar valor**.

---

## 🔑 Principais Descobertas

### 1️⃣ Crescimento de Vendas Não Significa Crescimento de Lucro

* A categoria **Furniture** apresentou **alto volume de vendas ($215 mil)**, porém **rentabilidade crítica**, com:

  * Margem de lucro de apenas **1%**
  * Lucro total de **$3.018**
  * Lucro por unidade de **$1,24**

➡️ Em contraste:

* **Technology**: margem de **19%**
* **Office Supplies**: margem de **16%**

📌 **Conclusão:** Furniture consome recursos relevantes, mas gera retorno financeiro mínimo, reduzindo a lucratividade global do negócio.

---

### 2️⃣ Forte Dependência Operacional de Office Supplies

* **Office Supplies** respondeu por **62% do volume total vendido** em 2017 (Classe A no Pareto).
* Furniture e Technology juntas somam apenas 39% do volume.

📌 **Conclusão:** O negócio possui **alta dependência operacional** de uma única categoria em termos de volume, o que aumenta o risco operacional e exige eficiência máxima nessa área.

---

### 3️⃣ Vendas Extremamente Concentradas no Final do Ano

* **60% das vendas anuais ocorreram entre setembro e dezembro**
* Média mensal: **1.039 unidades**
* Mediana: **886 unidades**
* Desvio padrão: **445 unidades** (alta variabilidade)

📌 **Conclusão:** Existe **sazonalidade acentuada**, com picos no final do ano e meses iniciais com desempenho significativamente inferior.

---

## 📉 Implicações para o Negócio

* **Financeiras**

  * Furniture atua como um *diluidor de margem*
  * O crescimento de vendas não está convertido em lucro proporcional

* **Operacionais**

  * Risco de excesso de estoque em meses de baixa
  * Risco de ruptura e pressão logística no Q4

* **Estratégicas**

  * Recursos podem estar sendo alocados para categorias de baixo retorno
  * Falta de balanceamento entre volume e valor

---

## 🎯 Recomendações Estratégicas

### Curto Prazo

* Auditar custos e precificação da categoria **Furniture**
* Identificar e descontinuar produtos de margem próxima de zero
* Reforçar planejamento de estoque e logística para o Q4

### Médio Prazo

* Reavaliar o papel estratégico da categoria Furniture no portfólio
* Realocar investimentos para categorias mais rentáveis (Technology)
* Criar campanhas para estimular vendas nos meses de menor volume
* Desenvolver estratégias para reduzir a dependência excessiva de Office Supplies

---

## ✅ Conclusão Final

A Superstore apresenta **bom desempenho em volume**, porém enfrenta **ineficiências claras na conversão de vendas em lucro**, especialmente na categoria Furniture e na gestão da sazonalidade. A aplicação de ajustes estratégicos focados em **rentabilidade, mix de produtos e planejamento temporal** pode gerar ganhos financeiros significativos sem necessidade imediata de aumento de volume.

---

Se quiser, no próximo passo posso:

* adaptar esse resumo para **apresentação executiva (1 slide)**
* reduzir para um **one-pager**
* ou alinhar o texto ao padrão de **relatório corporativo / consultoria**

Você está fazendo **análise de dados de verdade**, não só rodando SQL.
