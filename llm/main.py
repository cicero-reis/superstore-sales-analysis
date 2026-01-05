import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage

from database import get_db
from template.insights_analysis_prompt import insights_analysis_prompt
from template.rentabilidade_critica_por_categoria import insights_rentabilidade_critica_por_categoria
from config import GOOGLE_API_KEY, DEFAULT_MODEL
from query import (
    query_rentabilidade_critica_por_categoria,
    query_distribuicao_mensal_de_vendas,
    query_media,
    query_mediana,
    query_moda,
    query_quartiles,
    query_min_and_max,    
    query_amplitude,
    query_desvio_padrao,
    query_variancia
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

@app.get("/analysis/health")
def health_check(db: Session = Depends(get_db)):
    query_distribuicao_mensal_de_vendas_result = db.execute(query_distribuicao_mensal_de_vendas, {"year": 2017}).fetchall()
    query_media_result = db.execute(query_media, {"year": 2017}).fetchall()
    query_mediana_result = db.execute(query_mediana, {"year": 2017}).fetchall()
    query_moda_result = db.execute(query_moda, {"year": 2017}).fetchall()
    query_quartiles_result = db.execute(query_quartiles, {"year": 2017}).fetchall()
    query_min_and_max_result = db.execute(query_min_and_max, {"year": 2017}).fetchall()
    query_amplitude_result = db.execute(query_amplitude, {"year": 2017}).fetchall()
    query_desvio_padrao_result = db.execute(query_desvio_padrao, {"year": 2017}).fetchall()
    query_variancia_result = db.execute(query_variancia, {"year": 2017}).fetchall()

    result = {
        "distribuicao_mensal_de_vendas": [dict(row) for row in query_distribuicao_mensal_de_vendas_result[:]],
        "media": [dict(row) for row in query_media_result[:]],
        "mediana": [dict(row) for row in query_mediana_result[:]],
        "moda": [dict(row) for row in query_moda_result[:]],
        "quartis": [dict(row) for row in query_quartiles_result[:]],
        "min_max": [dict(row) for row in query_min_and_max_result[:]],
        "amplitude": [dict(row) for row in query_amplitude_result[:]],
        "desvio_padrao": [dict(row) for row in query_desvio_padrao_result[:]],
        "variancia": [dict(row) for row in query_variancia_result[:]]
    }

    prompt = insights_analysis_prompt.format_prompt(
        data=result
    ).to_string()

    # Chama o LLM
    response = llm.invoke(prompt)

    # Extrai apenas o texto
    text_response = extract_text(response)

    return {"insights": text_response}

@app.get("/analysis/rentabilidade-critica-por-categoria")
def router_rentabilidade_critica_por_categoria(db: Session = Depends(get_db)):

    rentabilidade_critica_por_categoria_result = db.execute(query_rentabilidade_critica_por_categoria, {"year": 2017}).fetchall()

    result = {
        "rentabilidade_critica_por_categoria": [dict(row) for row in rentabilidade_critica_por_categoria_result[:]]
    }

    prompt = insights_rentabilidade_critica_por_categoria.format_prompt(
        data=result
    ).to_string()

    # Chama o LLM
    response = llm.invoke(prompt)

    # Extrai apenas o texto
    text_response = extract_text(response)

    return {"insights": text_response}