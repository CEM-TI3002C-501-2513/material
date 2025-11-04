import os
import joblib
import psycopg
import pandas as pd
from psycopg.rows import dict_row
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal

class CrimeData(BaseModel):
    hour: int
    month: Literal["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    day_of_week: Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ward: str

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")

app = FastAPI()

@app.get("/top_primary_types")
async def get_top_primary_types():
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT primary_type, count(*) AS count
                              FROM datacrimes 
                              GROUP BY primary_type
                              ORDER BY count DESC
                              LIMIT 5;""")
            results = await cur.fetchall()
    return results

@app.post("/predict_impact")
async def post_predict_impact(crime_data: CrimeData):
    model = joblib.load("crime_impact_model.joblib")
    df = pd.DataFrame({
        "hour": [crime_data.hour],
        "month": [crime_data.month],
        "day_of_week": [crime_data.day_of_week],
        "ward": [crime_data.ward]
    })
    probabilities = model.predict_proba(df)
    return {
        "low_impact_probability": probabilities[0][0][1],
        "medium_impact_probability": probabilities[1][0][1],
        "high_impact_probability": probabilities[2][0][1],
    }
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)