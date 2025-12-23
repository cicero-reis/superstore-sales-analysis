from typing import List, Tuple, Dict

def get_sales_performance(result: List[Tuple]) -> List[Dict]:
 
     return [
        {
            "region": row[0],
            "total_sales": float(row[1]),
            "total_profit": float(row[2]),
            "profit_margin": float(row[3])
        }
        for row in result
    ]

def get_rentabilidade_critica_da_categoria_furniture(result: List[Tuple]) -> List[Dict]:
 
     return [
        {
            "year": row[0],
            "category": row[1],
            "total_quantity": float(row[2]),
            "total_sales": float(row[3]),
            "total_profit": float(row[4]),
            "profit_per_unit": float(row[5]),
            "profit_margin": float(row[6])
        }
        for row in result
    ]

def get_crescimento_nao_lucrativo_da_categoria_furniture(result: List[Tuple]) -> List[Dict]:
 
     return [
        {
            "year": row[0],
            "category": row[1],
            "total_quantity": float(row[2]),
            "total_sales": float(row[3]),
            "total_profit": float(row[4]),
            "profit_margin": float(row[5])
        }
        for row in result
    ]