from langchain.prompts import PromptTemplate

INSIGHT_TEMPLATE = """
Você é um analista de dados.
Com base nos dados abaixo, gere um insight de negócio no formato:
- Fato
- Impacto
- Ação sugerida

{data}
"""

insights_sales_prompt = PromptTemplate(
    input_variables=["data"],
    template=INSIGHT_TEMPLATE,
)