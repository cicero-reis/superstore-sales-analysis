import pandas as pd

from services.query import (
    query_rentabilidade_critica_por_categoria,
    query_distribuicao_mensal_de_vendas,
    query_media,
    query_mediana,
    query_amplitude,
    query_desvio_padrao,
    query_min_and_max,
    query_moda,
    query_quartiles,
    query_variancia

)

def get_rentabilidade_critica_por_categoria(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_rentabilidade_critica_por_categoria,
            con=conn,
            params={"year": year}
        )
    return df

def get_distribuicao_mensal_de_vendas(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_distribuicao_mensal_de_vendas,
            con=conn,
            params={"year": year}
        )
    return df

def get_media(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_media,
            con=conn,
            params={"year": year}
        )
    return df

def get_median(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_mediana,
            con=conn,
            params={"year": year}
        )
    return df

def get_quartiles(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_quartiles,
            con=conn,
            params={"year": year}
        )
    return df

def get_variance(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_variancia,
            con=conn,
            params={"year": year}
        )
    return df

def get_min_max(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_min_and_max,
            con=conn,
            params={"year": year}
        )
    return df

def get_moda(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_moda,
            con=conn,
            params={"year": year}
        )
    return df

def get_amplitude(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_amplitude,
            con=conn,
            params={"year": year}
        )
    return df

def get_desvio_padrao(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_desvio_padrao,
            con=conn,
            params={"year": year}
        )
    return df
