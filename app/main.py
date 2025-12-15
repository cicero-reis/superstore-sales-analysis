import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()

query = '''
SELECT * FROM fact_sales LIMIT 10;
'''

@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    result = db.execute(query).fetchall()
    return {"database": "ok", "result": result}


def query_database():
    # Placeholder for database query logic
    return {"data": "Sample data from database"}

@app.get("/")
async def read_root():
    return query_database()



