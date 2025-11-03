import os
import psycopg
from psycopg.rows import dict_row
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")

app = FastAPI()

@app.get("/top_primary_types")
async def get_top_primary_types():
    with psycopg.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT primary_type, count(*) AS count
                        FROM datacrimes 
                        GROUP BY primary_type
                        ORDER BY count DESC
                        LIMIT 5;""")
            results = cur.fetchall()
    return results
            

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)