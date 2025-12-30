import pandas as pd
from services.query import query_rentabilidade_critica_por_categoria

def get_kpis_by_category(engine, year: int):
    with engine.connect() as conn:
        df = pd.read_sql(
            sql=query_rentabilidade_critica_por_categoria,
            con=conn,
            params={"year": year}
        )
    return df