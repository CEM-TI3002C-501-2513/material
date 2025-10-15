import os
import io
import pandas as pd
import psycopg
from sodapy import Socrata
from dotenv import load_dotenv

load_dotenv()

chicago_api_token = os.getenv("CHICAGO_API_KEY")
client = Socrata("data.cityofchicago.org", chicago_api_token)

# Consulta SoQL de delitos recientes
query = """
SELECT *
WHERE date >= '2015-01-01'
LIMIT 3000000
"""

# El resultado de la consulta se almacena en un dataframe
results = client.get("ijzp-q8t2", query=query)
df = pd.DataFrame.from_records(results)
# Filtrar puntos válidos
df.dropna(subset=["latitude", "longitude"], inplace=True)
# remover columnas innecesarias
df.drop(['location'], axis=1, inplace=True)
# convertir a tipos de datos
df['year'] = df['year'].astype(int)
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)
df['date'] = pd.to_datetime(df['date'], errors='coerce', format="mixed")
df['updated_on'] = pd.to_datetime(df['updated_on'], errors='coerce', format="mixed")
df.dropna(subset=['date', 'updated_on'], inplace=True)
df.reset_index(drop=True, inplace=True)
df.columns = df.columns.str.upper()

POSTGRESQL_URL = os.getenv("POSTGRESQL_URL")
buffer = io.StringIO()
df.to_csv(buffer, index=False, header=False)
buffer.seek(0)

# Ejemplo de POSQTGRESQL_URL: postgres://usuario:contraseña@localhost:5432/mi_basedatos
with psycopg.connect(POSTGRESQL_URL) as conn:
    with conn.cursor() as cur:
        with cur.copy(f"COPY datacrimes ({','.join(df.columns)}) FROM STDIN WITH (FORMAT CSV)") as copy:
            copy.write(buffer.getvalue())