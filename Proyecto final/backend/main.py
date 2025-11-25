import os
import joblib
import psycopg
import pandas as pd
from psycopg.rows import dict_row
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal, Dict, Any

from google import genai
from google.genai import types

# GEMINI HELPER FUNCTIONS

import asyncio
import os
import sys
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")
model = joblib.load("crime_impact_model.joblib")

async def get_columns():
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT column_name
                              FROM information_schema.columns
                              WHERE table_name = 'datacrimes'
                              ORDER BY ordinal_position;""")
            results = [x["column_name"] for x in await cur.fetchall()]
    return results

async def get_primary_types():
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT DISTINCT primary_type 
                              FROM datacrimes 
                              ORDER BY primary_type;""")
            results = [x["primary_type"] for x in await cur.fetchall()]
    return results

async def get_existing_wards():
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT DISTINCT ward 
                              FROM datacrimes 
                              ORDER BY ward;""")
            results = [x["ward"] for x in await cur.fetchall()]
    return results

async def get_districts():
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT DISTINCT district 
                              FROM datacrimes 
                              ORDER BY district;""")
            results = [x["district"] for x in await cur.fetchall()]
    return results

async def get_community_areas():
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT DISTINCT community_area 
                              FROM datacrimes 
                              ORDER BY community_area;""")
            results = [x["community_area"] for x in await cur.fetchall()]
    return results

async def search_crimes_by_primary_type(primary_type: str):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT *
                              FROM datacrimes 
                              WHERE primary_type = %s
                              ORDER BY date DESC
                              LIMIT 100;""", (primary_type,))
            results = await cur.fetchall()
    return results

async def count_crimes_by_primary_type(primary_type: str):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT COUNT(*) AS count
                              FROM datacrimes 
                              WHERE primary_type = %s;""", (primary_type,))
            result = await cur.fetchone()
    return result["count"]

async def count_crimes_by_year(year: int):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT COUNT(*) AS count
                              FROM datacrimes 
                              WHERE EXTRACT(YEAR FROM date) = %s;""", (year,))
            result = await cur.fetchone()
    return result["count"]

async def count_crimes_by_ward(ward: int):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT COUNT(*) AS count
                              FROM datacrimes 
                              WHERE ward = %s;""", (ward,))
            result = await cur.fetchone()
    return result["count"]

async def crime_trend_over_years(primary_type: str):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT EXTRACT(YEAR FROM date) AS year, COUNT(*) AS count
                              FROM datacrimes 
                              WHERE primary_type = %s
                              GROUP BY year
                              ORDER BY year;""", (primary_type,))
            results = await cur.fetchall()
    return results

async def latest_crimes(limit: int = 10):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT *
                              FROM datacrimes 
                              ORDER BY date DESC
                              LIMIT %s;""", (limit,))
            results = await cur.fetchall()
    return results

async def latest_crimes_by_ward(ward: int):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT *
                              FROM datacrimes 
                              WHERE ward = %s
                              ORDER BY date DESC
                              LIMIT 10;""", (ward,))
            results = await cur.fetchall()
    return results

async def crimes_near_location(latitude: float, longitude: float, radius_km: float, limit: int = 50):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            # Haversine calc inside query
            await cur.execute("""
                SELECT id, date, primary_type, description, latitude, longitude,
                    (6371 * acos(
                        cos(radians(%s)) * cos(radians(latitude)) *
                        cos(radians(longitude) - radians(%s)) +
                        sin(radians(%s)) * sin(radians(latitude))
                    )) AS distance_km
                FROM datacrimes
                WHERE latitude IS NOT NULL AND longitude IS NOT NULL
                HAVING (6371 * acos(
                        cos(radians(%s)) * cos(radians(latitude)) *
                        cos(radians(longitude) - radians(%s)) +
                        sin(radians(%s)) * sin(radians(latitude))
                    )) < %s
                ORDER BY distance_km
                LIMIT %s;
            """, (
                latitude, longitude, latitude,
                latitude, longitude, latitude,
                radius_km, limit
            ))
            rows = await cur.fetchall()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "date": r[1].isoformat() if r[1] else None,
            "primary_type": r[2],
            "description": r[3],
            "latitude": r[4],
            "longitude": r[5],
            "distance_km": r[6],
        })
    return result

async def predict_crime_impact(hour: int, month: str, day_of_week: str, ward: str):
    df = pd.DataFrame({
        "hour": [hour],
        "month": [month],
        "day_of_week": [day_of_week],
        "ward": [ward]
    })
    probabilities = model.predict_proba(df)
    return {
        "low_impact_probability": probabilities[0][0][1],
        "medium_impact_probability": probabilities[1][0][1],
        "high_impact_probability": probabilities[2][0][1],
    }

DB_FUNCTIONS: Dict[str, Any] = {
    "get_columns": get_columns,
    "get_primary_types": get_primary_types,
    "get_existing_wards": get_existing_wards,
    "get_districts": get_districts,
    "get_community_areas": get_community_areas,
    "search_crimes_by_primary_type": search_crimes_by_primary_type,
    "count_crimes_by_primary_type": count_crimes_by_primary_type,
    "count_crimes_by_year": count_crimes_by_year,
    "count_crimes_by_ward": count_crimes_by_ward,
    "crime_trend_over_years": crime_trend_over_years,
    "latest_crimes": latest_crimes,
    "latest_crimes_by_ward": latest_crimes_by_ward,
    "crimes_near_location": crimes_near_location,
    "predict_crime_impact": predict_crime_impact,
}

# Gemini tool declaration

crime_tools = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="get_columns",
            description="Get the list of columns in the datacrimes table.",
            parameters=None
        ),
        types.FunctionDeclaration(
            name="get_primary_types",
            description="Get the list of distinct primary types of crimes.",
            parameters=None
        ),
        types.FunctionDeclaration(
            name="get_existing_wards",
            description="Get the list of distinct wards where crimes have been reported.",
            parameters=None
        ),
        types.FunctionDeclaration(
            name="get_districts",
            description="Get the list of distinct districts where crimes have been reported.",
            parameters=None
        ),
        types.FunctionDeclaration(
            name="get_community_areas",
            description="Get the list of distinct community areas where crimes have been reported.",
            parameters=None
        ),
        types.FunctionDeclaration(
            name="search_crimes_by_primary_type",
            description="Search crimes by their primary type.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "primary_type": types.Schema(type=types.Type.STRING, description="Primary type of the crime"),
                    "limit": types.Schema(type=types.Type.INTEGER, description="Number of results to return")
                },
                required=["primary_type"]
            )
        ),
        types.FunctionDeclaration(
            name="count_crimes_by_primary_type",
            description="Count the number of crimes for a given primary type.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "primary_type": types.Schema(type=types.Type.STRING, description="Primary type of the crime")
                },
                required=["primary_type"]
            )
        ),
        types.FunctionDeclaration(
            name="count_crimes_by_year",
            description="Count the number of crimes that occurred in a given year.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "year": types.Schema(type=types.Type.INTEGER, description="Year of the crimes")
                },
                required=["year"]
            )
        ),
        types.FunctionDeclaration(
            name="count_crimes_by_ward",
            description="Count the number of crimes that occurred in a given ward.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "ward": types.Schema(type=types.Type.INTEGER, description="Ward number")
                },
                required=["ward"]
            )
        ),
        types.FunctionDeclaration(
            name="crime_trend_over_years",
            description="Get the trend of crimes over the years for a given primary type.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "primary_type": types.Schema(type=types.Type.STRING, description="Primary type of the crime")
                },
                required=["primary_type"]
            )
        ),
        types.FunctionDeclaration(
            name="latest_crimes",
            description="Get the latest crimes reported.",
            parameters=None
        ),
        types.FunctionDeclaration(
            name="latest_crimes_by_ward",
            description="Get the latest crimes reported in a specific ward.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "ward": types.Schema(type=types.Type.INTEGER, description="Ward number")
                },
                required=["ward"]
            )
        ),
        types.FunctionDeclaration(
            name="crimes_near_location",
            description="Get crimes near a specific geographic location within a certain radius.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "latitude": types.Schema(type=types.Type.NUMBER, description="Latitude of the location"),
                    "longitude": types.Schema(type=types.Type.NUMBER, description="Longitude of the location"),
                    "radius_km": types.Schema(type=types.Type.NUMBER, description="Radius in kilometers"),
                    "limit": types.Schema(type=types.Type.INTEGER, description="Number of results to return")
                },
                required=["latitude", "longitude", "radius_km"]
            )
        ),
        types.FunctionDeclaration(
            name="predict_crime_impact",
            description="Predict the impact level of a crime based on its features.",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "hour": types.Schema(type=types.Type.INTEGER, description="Hour of the day (0-23)"),
                    "month": types.Schema(type=types.Type.STRING, description="Month of the year (e.g., 'January')"),
                    "day_of_week": types.Schema(type=types.Type.STRING, description="Day of the week (e.g., 'Monday')"),
                    "ward": types.Schema(type=types.Type.STRING, description="Ward number as a string (e.g., 'Ward_1')")
                },
                required=["hour", "month", "day_of_week", "ward"]
            )
        ),
    ]
)
    
# FASTAPI APPLICATION


class CrimeData(BaseModel):
    hour: int
    month: Literal["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    day_of_week: Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    ward: str
    
class GeminiQueryRequest(BaseModel):
    prompt: str

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

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

@app.get("/wards")
async def get_wards():
    results = await get_existing_wards()
    return results

@app.get("/recent_crimes/{ward}")
async def get_recent_crimes(ward: int):
    crime_impact_map = {
        "HOMICIDE": "high_impact",
        "CRIM SEXUAL ASSAULT": "high_impact",
        "CRIMINAL SEXUAL ASSAULT": "high_impact",
        "HUMAN TRAFFICKING": "high_impact",
        "KIDNAPPING": "high_impact",
        "ARSON": "high_impact",
        "ROBBERY": "high_impact",
        "WEAPONS VIOLATION": "high_impact",
        "BATTERY": "high_impact",
        "ASSAULT": "high_impact",

        "BURGLARY": "medium_impact",
        "CRIMINAL DAMAGE": "medium_impact",
        "THEFT": "medium_impact",
        "MOTOR VEHICLE THEFT": "medium_impact",
        "NARCOTICS": "medium_impact",
        "OTHER NARCOTIC VIOLATION": "medium_impact",
        "INTERFERENCE WITH PUBLIC OFFICER": "medium_impact",
        "INTIMIDATION": "medium_impact",
        "STALKING": "medium_impact",
        "OFFENSE INVOLVING CHILDREN": "medium_impact",
        "SEX OFFENSE": "medium_impact",

        "OTHER OFFENSE": "low_impact",
        "DECEPTIVE PRACTICE": "low_impact",
        "OBSCENITY": "low_impact",
        "CRIMINAL TRESPASS": "low_impact",
        "LIQUOR LAW VIOLATION": "low_impact",
        "PUBLIC PEACE VIOLATION": "low_impact",
        "PROSTITUTION": "low_impact",
        "PUBLIC INDECENCY": "low_impact",
        "GAMBLING": "low_impact",
        "CONCEALED CARRY LICENSE VIOLATION": "low_impact",
        "NON-CRIMINAL": "low_impact",
        "RITUALISM": "low_impact"
    }
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT date, primary_type, description FROM datacrimes WHERE ward = %s ORDER BY date DESC LIMIT 5;""", (ward,))
            results = await cur.fetchall()
            for record in results:
                primary_type = record["primary_type"]
                record["impact_level"] = crime_impact_map.get(primary_type, "low_impact")
    return results

@app.get("/highest_count_crime/{ward}")
async def get_highest_count_crime(ward: int):
    async with await psycopg.AsyncConnection.connect(POSTGRES_URL, row_factory=dict_row) as conn:
        async with conn.cursor() as cur:
            await cur.execute("""SELECT primary_type, COUNT(*) AS count
                              FROM datacrimes
                              WHERE ward = %s
                              GROUP BY primary_type
                              ORDER BY count DESC
                              LIMIT 1;""", (ward,))
            top_crime = await cur.fetchone()
            
            await cur.execute("""SELECT COUNT(*) AS total_count
                              FROM datacrimes
                              WHERE ward = %s;""", (ward,))
            total_count_result = await cur.fetchone()
            total_count = total_count_result["total_count"]
            
    if total_count == 0:
        ratio = 0.0
    else:
        ratio = top_crime["count"]  / total_count
    
    return {
        "primary_type": top_crime["primary_type"],
        "count": top_crime["count"],
        "ratio": ratio
    }

@app.post("/predict_impact")
async def post_predict_impact(crime_data: CrimeData):
    result = await predict_crime_impact(
        hour=crime_data.hour,
        month=crime_data.month,
        day_of_week=crime_data.day_of_week,
        ward=crime_data.ward
    )
    return result

@app.post("/gemini_query")
async def post_gemini_query(request: GeminiQueryRequest):
    async with genai.Client(api_key=GENAI_API_KEY).aio as aclient:
        contents = [
            types.Content(
                role="user",
                parts=[types.Part(text=request.prompt)]
            )
        ]
        system_instruction = """
Eres un analista de datos experto con acceso a una base de datos de crímenes. 
Utiliza las herramientas proporcionadas para responder a las consultas de los usuarios sobre datos de crímenes de manera precisa y eficiente. 
Si se realiza una llamada a una herramienta, ejecútala y usa los resultados para formular tu respuesta final. 
Siempre busca proporcionar respuestas claras y concisas basadas en los datos disponibles.
        """
        response = await aclient.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.prompt,
            config=types.GenerateContentConfig(
                tools=[crime_tools],
                system_instruction=system_instruction)
        )
        if response.candidates[0].content.parts[0].function_call:
            tool_call = response.candidates[0].content.parts[0].function_call
            if tool_call.name in DB_FUNCTIONS:
                func = DB_FUNCTIONS[tool_call.name]
                if tool_call.args:
                    args = tool_call.args
                    result = await func(**args)
                else:
                    result = await func()
                function_response_part = types.Part.from_function_response(
                    name=tool_call.name,
                    response={"result": result}
                )
                contents.append(response.candidates[0].content)
                contents.append(types.Content(role="user", parts=[function_response_part]))
                
                final_response = await aclient.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction
                    )
                )
                return {"response": final_response.candidates[0].content.parts[0].text}
            return {"error": f"Function {tool_call.name} not recognized."}
        else:
            return {"response": response.candidates[0].content.parts[0].text}
    return {"error": "Could not process the request."}
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)