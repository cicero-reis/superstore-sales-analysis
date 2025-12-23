import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage

from database import get_db
from json_cache import JSONCache
from template.insights_sales_prompt import insights_sales_prompt
from config import GOOGLE_API_KEY, DEFAULT_MODEL
from query import (
    query_desempenho_de_vendas,
    query_rentabilidade_critica_da_categoria_furniture,
    query_crescimento_nao_lucrativo_da_categoria_furniture
)
from resource import (
    get_sales_performance,
    get_rentabilidade_critica_da_categoria_furniture,
    get_crescimento_nao_lucrativo_da_categoria_furniture
)

app = FastAPI()

llm = ChatGoogleGenerativeAI(
    model=DEFAULT_MODEL,
    google_api_key=GOOGLE_API_KEY
)

def extract_text(response) -> str:
    if isinstance(response, AIMessage):
        return response.content
    elif isinstance(response, list):
        return " ".join(
            msg.content for msg in response if hasattr(msg, "content")
        )
    return str(response)


@app.get("/analysis/desempenho_de_vendas")
def desempenho_de_vendas(db: Session = Depends(get_db)):

    result = db.execute(query_desempenho_de_vendas, {"year": 2017}).fetchall()

    data = get_sales_performance(result)

    prompt = insights_sales_prompt.format_prompt(
        data=data
    ).to_string()

    lm_string = f"{llm.model}"

    # Verifica cache
    cache = JSONCache()
    cached = cache.lookup(prompt, lm_string)
    if cached is not None:
        return cached

    # Chama o LLM
    response = llm.invoke(prompt)

    # Extrai apenas o texto
    text_response = extract_text(response)

    return {"insights": text_response}

@app.get("/analysis/rentabilidade-critica-da-categoria-furniture")
def rentabilidade_critica_da_categoria_furniture(db: Session = Depends(get_db)):

    result = db.execute(query_rentabilidade_critica_da_categoria_furniture, {"year": 2017}).fetchall()

    data = get_rentabilidade_critica_da_categoria_furniture(result)

    prompt = insights_sales_prompt.format_prompt(
        data=data
    ).to_string()

    lm_string = f"{llm.model}"

    # Verifica cache
    cache = JSONCache()
    cached = cache.lookup(prompt, lm_string)
    if cached is not None:
        return cached

    # Chama o LLM
    response = llm.invoke(prompt)

    # Extrai apenas o texto
    text_response = extract_text(response)

    return {"insights": text_response}


@app.get("/analysis/crescimento-nao-lucrativo-da-categoria-furniture")
def crescimento_nao_lucrativo_da_categoria_furniture(db: Session = Depends(get_db)):

    result = db.execute(query_crescimento_nao_lucrativo_da_categoria_furniture, {"category": "Furniture"}).fetchall()

    data = get_crescimento_nao_lucrativo_da_categoria_furniture(result)

    prompt = insights_sales_prompt.format_prompt(
        data=data
    ).to_string()

    lm_string = f"{llm.model}"

    # Verifica cache
    cache = JSONCache()
    cached = cache.lookup(prompt, lm_string)
    if cached is not None:
        return cached

    # Chama o LLM
    response = llm.invoke(prompt)

    # Extrai apenas o texto
    text_response = extract_text(response)

    return {"insights": text_response}
